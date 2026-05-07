"""
Embed Wallis blog posts into a Cloudflare R2 JSONL knowledge base.

For each markdown file in transcripts/wallis-corpus/blog/:
- Strip YAML frontmatter, keep title/date/url/tags as metadata
- Chunk by paragraph, target ~700 tokens per chunk, 150-token overlap
- Generate embedding with OpenAI text-embedding-3-small
- Upload as one line per chunk in wallis-blog-embeddings.jsonl on R2

Idempotent: chunks with unchanged content (by SHA) are skipped on re-embed.

Run: python embed.py
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import boto3
import tiktoken
from botocore.config import Config as BotoConfig
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ----------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIM = 1536
TARGET_CHUNK_TOKENS = 700
OVERLAP_TOKENS = 150

CORPUS_DIR = Path(__file__).resolve().parent.parent.parent / "transcripts" / "wallis-corpus" / "blog"
META_DIR = Path(__file__).resolve().parent.parent.parent / "transcripts" / "wallis-corpus" / "_metadata"
LOCAL_MANIFEST = META_DIR / "manifest.json"

EMBEDDINGS_KEY = "wallis-blog-embeddings.jsonl"
MANIFEST_KEY = "manifest.json"


def _r2_env():
    """Read R2 credentials from env. Raises a clear error if missing."""
    missing = [k for k in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY") if k not in os.environ]
    if missing:
        raise RuntimeError(f"missing env vars: {', '.join(missing)} (copy .env.example to .env and fill in)")
    return {
        "bucket": os.environ.get("R2_BUCKET_NAME", "wallis-corpus"),
        "account": os.environ["R2_ACCOUNT_ID"],
        "key": os.environ["R2_ACCESS_KEY_ID"],
        "secret": os.environ["R2_SECRET_ACCESS_KEY"],
        "endpoint": f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
    }

AUTHOR_SLUG = "wallis"
AUTHOR_NAME = "Christopher Hareesh Wallis"


# ----------------------------------------------------------------------
# Markdown parsing
# ----------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Strip YAML frontmatter and return (metadata, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    metadata = {}
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        # Strip surrounding quotes
        if v.startswith("'") and v.endswith("'"):
            v = v[1:-1]
        elif v.startswith('"') and v.endswith('"'):
            v = v[1:-1]
        # Tags array
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            if inner:
                v = [s.strip().strip('"').strip("'") for s in inner.split(",")]
            else:
                v = []
        metadata[k.strip()] = v
    return metadata, body


# ----------------------------------------------------------------------
# Chunking
# ----------------------------------------------------------------------

ENCODER = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    return len(ENCODER.encode(text))


def chunk_paragraphs(text: str, target: int = TARGET_CHUNK_TOKENS, overlap: int = OVERLAP_TOKENS) -> list[str]:
    """Split text into chunks of ~target tokens with overlap.

    Splits primarily on paragraph boundaries (\n\n), accumulates until target
    is reached, then carries the last `overlap` tokens forward.
    """
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0
    for p in paragraphs:
        p_tokens = count_tokens(p)
        if current_tokens + p_tokens > target and current:
            chunks.append("\n\n".join(current))
            # Build overlap from the tail of the current chunk
            tail_text = "\n\n".join(current)
            tail_ids = ENCODER.encode(tail_text)
            tail_overlap = ENCODER.decode(tail_ids[-overlap:]) if len(tail_ids) > overlap else tail_text
            current = [tail_overlap]
            current_tokens = count_tokens(tail_overlap)
        current.append(p)
        current_tokens += p_tokens
    if current:
        chunks.append("\n\n".join(current))
    return chunks


# ----------------------------------------------------------------------
# R2 client
# ----------------------------------------------------------------------

def r2_client(env):
    return boto3.client(
        "s3",
        endpoint_url=env["endpoint"],
        aws_access_key_id=env["key"],
        aws_secret_access_key=env["secret"],
        config=BotoConfig(signature_version="s3v4"),
        region_name="auto",
    )


def load_existing_chunk_shas(r2, bucket) -> set[str]:
    """Read manifest.json from R2 to get already-embedded chunk SHAs."""
    try:
        resp = r2.get_object(Bucket=bucket, Key=MANIFEST_KEY)
        manifest = json.loads(resp["Body"].read().decode("utf-8"))
        return set(manifest.get("chunk_shas", []))
    except r2.exceptions.NoSuchKey:
        return set()
    except Exception as e:
        print(f"  [warn] could not load existing manifest: {e}", file=sys.stderr)
        return set()


def upload_jsonl(r2, bucket, jsonl_text: str):
    r2.put_object(Bucket=bucket, Key=EMBEDDINGS_KEY, Body=jsonl_text.encode("utf-8"), ContentType="application/x-ndjson")


def upload_manifest(r2, bucket, manifest: dict):
    r2.put_object(Bucket=bucket, Key=MANIFEST_KEY, Body=json.dumps(manifest, indent=2).encode("utf-8"), ContentType="application/json")


def download_existing_jsonl(r2, bucket) -> list[dict]:
    try:
        resp = r2.get_object(Bucket=bucket, Key=EMBEDDINGS_KEY)
        text = resp["Body"].read().decode("utf-8")
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    except r2.exceptions.NoSuchKey:
        return []


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def chunk_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def main():
    if not CORPUS_DIR.exists():
        print(f"Corpus directory not found: {CORPUS_DIR}")
        print("Run scrape.py first.")
        sys.exit(1)

    md_files = sorted(CORPUS_DIR.glob("*.md"))
    print(f"Found {len(md_files)} markdown files in {CORPUS_DIR}")

    if not md_files:
        print("Nothing to embed.")
        return

    print("Connecting to R2...")
    env = _r2_env()
    r2 = r2_client(env)
    bucket = env["bucket"]
    existing_shas = load_existing_chunk_shas(r2, bucket)
    existing_records = download_existing_jsonl(r2, bucket) if existing_shas else []
    print(f"  {len(existing_shas)} chunks already on R2 (bucket={bucket})")

    client = OpenAI()

    new_records = []
    skipped = 0
    new_chunk_count = 0

    for i, mdf in enumerate(md_files, 1):
        text = mdf.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        if not body.strip():
            continue

        chunks = chunk_paragraphs(body)
        for j, chunk_text in enumerate(chunks):
            sha = chunk_sha(chunk_text)
            if sha in existing_shas:
                skipped += 1
                continue

            # Embed
            try:
                resp = client.embeddings.create(model=EMBEDDING_MODEL, input=chunk_text)
                embedding = resp.data[0].embedding
            except Exception as e:
                print(f"  [error] embedding failed for {mdf.name} chunk {j}: {e}", file=sys.stderr)
                continue

            record = {
                "id": f"{mdf.stem}--{j:03d}--{sha}",
                "author_slug": AUTHOR_SLUG,
                "author_name": AUTHOR_NAME,
                "source_url": meta.get("url", ""),
                "post_title": meta.get("title", "(untitled)"),
                "post_date": meta.get("date", "unknown"),
                "tags": meta.get("tags", []),
                "chunk_index": j,
                "chunk_sha": sha,
                "text": chunk_text,
                "embedding": embedding,
                "embedding_model": EMBEDDING_MODEL,
            }
            new_records.append(record)
            new_chunk_count += 1
            existing_shas.add(sha)

        if i % 25 == 0:
            print(f"  [{i}/{len(md_files)}] {new_chunk_count} new chunks so far")

    print(f"\n  total new chunks: {new_chunk_count}")
    print(f"  total skipped (already embedded): {skipped}")

    if not new_records:
        print("Nothing new to upload.")
        return

    # Combine with existing and upload
    all_records = existing_records + new_records
    jsonl_text = "\n".join(json.dumps(r, ensure_ascii=False) for r in all_records) + "\n"
    print(f"\nUploading {len(all_records)} chunks ({len(jsonl_text) / 1024:.1f} KB) to R2...")
    upload_jsonl(r2, bucket, jsonl_text)

    manifest = {
        "author_slug": AUTHOR_SLUG,
        "author_name": AUTHOR_NAME,
        "embedding_model": EMBEDDING_MODEL,
        "embedding_dim": EMBEDDING_DIM,
        "total_chunks": len(all_records),
        "chunk_shas": sorted(existing_shas),
        "embeddings_key": EMBEDDINGS_KEY,
    }
    upload_manifest(r2, bucket, manifest)

    # Local copy for traceability
    META_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_MANIFEST.write_text(json.dumps({**manifest, "chunk_shas": "(omitted from local copy)"}, indent=2), encoding="utf-8")

    print(f"\nDone. Manifest at r2://{R2_BUCKET}/{MANIFEST_KEY}, embeddings at r2://{R2_BUCKET}/{EMBEDDINGS_KEY}")


if __name__ == "__main__":
    main()
