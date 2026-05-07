"""
Query the Wallis RAG knowledge base on R2.

Usage:
    python retrieve.py "what does Hareesh say about prajna?"
    python retrieve.py "your question" --top 8

Or import in another script:
    from retrieve import retrieve, format_for_claude
    chunks = retrieve("question text")
    context = format_for_claude(chunks)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import boto3
from botocore.config import Config as BotoConfig
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDINGS_KEY = "wallis-blog-embeddings.jsonl"


def _r2_env():
    missing = [k for k in ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY") if k not in os.environ]
    if missing:
        raise RuntimeError(f"missing env vars: {', '.join(missing)}")
    return {
        "bucket": os.environ.get("R2_BUCKET_NAME", "wallis-corpus"),
        "account": os.environ["R2_ACCOUNT_ID"],
        "key": os.environ["R2_ACCESS_KEY_ID"],
        "secret": os.environ["R2_SECRET_ACCESS_KEY"],
        "endpoint": f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
    }


# ----------------------------------------------------------------------
# Cached load — loads JSONL once per process
# ----------------------------------------------------------------------

_CACHED_RECORDS: list[dict] | None = None


def _r2_client(env):
    return boto3.client(
        "s3",
        endpoint_url=env["endpoint"],
        aws_access_key_id=env["key"],
        aws_secret_access_key=env["secret"],
        config=BotoConfig(signature_version="s3v4"),
        region_name="auto",
    )


def load_records() -> list[dict]:
    """Load all chunk records from R2 (cached after first call)."""
    global _CACHED_RECORDS
    if _CACHED_RECORDS is not None:
        return _CACHED_RECORDS
    env = _r2_env()
    r2 = _r2_client(env)
    resp = r2.get_object(Bucket=env["bucket"], Key=EMBEDDINGS_KEY)
    text = resp["Body"].read().decode("utf-8")
    records = [json.loads(line) for line in text.splitlines() if line.strip()]
    size_mb = len(text) / (1024 * 1024)
    if size_mb > 500:
        print(f"  [warn] embeddings file is {size_mb:.1f} MB — consider chunking by author", file=sys.stderr)
    _CACHED_RECORDS = records
    return records


# ----------------------------------------------------------------------
# Cosine similarity
# ----------------------------------------------------------------------

def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _norm(a):
    return sum(x * x for x in a) ** 0.5


def cosine(a, b):
    na, nb = _norm(a), _norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return _dot(a, b) / (na * nb)


# ----------------------------------------------------------------------
# Public API
# ----------------------------------------------------------------------

def retrieve(question: str, top_k: int = 5) -> list[dict]:
    """Embed the question and return the top_k most-similar chunks."""
    if not question.strip():
        return []
    client = OpenAI()
    resp = client.embeddings.create(model=EMBEDDING_MODEL, input=question)
    q_emb = resp.data[0].embedding

    records = load_records()
    scored = [
        {
            "text": r["text"],
            "source_url": r.get("source_url", ""),
            "post_title": r.get("post_title", "(untitled)"),
            "post_date": r.get("post_date", "unknown"),
            "tags": r.get("tags", []),
            "similarity_score": cosine(q_emb, r["embedding"]),
        }
        for r in records
    ]
    scored.sort(key=lambda x: x["similarity_score"], reverse=True)
    return scored[:top_k]


def format_for_claude(chunks: list[dict]) -> str:
    """Format retrieved chunks as a context string for a Claude system prompt."""
    blocks = []
    for c in chunks:
        block = (
            f"[Source: {c['post_title']} ({c['post_date']})]\n"
            f"{c['text']}\n"
            f"Read full post: {c['source_url']}"
        )
        blocks.append(block)
    return "\n\n---\n\n".join(blocks)


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Query the Wallis RAG.")
    parser.add_argument("question", help="The question to retrieve context for")
    parser.add_argument("--top", type=int, default=5, help="Number of chunks to return")
    parser.add_argument("--format", choices=["claude", "json", "plain"], default="claude")
    args = parser.parse_args()

    chunks = retrieve(args.question, top_k=args.top)

    if args.format == "json":
        print(json.dumps(chunks, indent=2, ensure_ascii=False))
    elif args.format == "plain":
        for i, c in enumerate(chunks, 1):
            print(f"\n=== Result {i} (similarity {c['similarity_score']:.3f}) ===")
            print(f"Title: {c['post_title']} ({c['post_date']})")
            print(f"URL:   {c['source_url']}")
            print(f"Text:  {c['text'][:400]}{'...' if len(c['text']) > 400 else ''}")
    else:  # claude
        print(format_for_claude(chunks))


if __name__ == "__main__":
    main()
