# Wallis RAG Pipeline

A complete pipeline for ingesting Christopher "Hareesh" Wallis's blog (hareesh.org)
into a Cloudflare R2 bucket as a RAG knowledge base, then querying it with
always-cite-the-source behavior.

## Pipeline overview

```
hareesh.org/blog          ┐
   ↓                      │
scrape.py  ──→  transcripts/wallis-corpus/blog/*.md  (LOCAL ONLY, gitignored)
                          │
                          ↓
embed.py  ──────────→  R2 bucket: wallis-corpus
                       wallis-blog-embeddings.jsonl
                       manifest.json
                          │
                          ↓
retrieve.py  ─────→  format_for_claude(top_k chunks)
                       always cites Hareesh + post title + URL
```

## Setup (one-time)

1. **Python 3.11+** (uses standard typing).

2. **Install deps:**
   ```bash
   cd book-repo/scripts/wallis-rag
   pip install -r requirements.txt
   ```

3. **R2 bucket** — `wallis-corpus` already exists in your Cloudflare account
   (verified via Cloudflare MCP, created 2026-04-15, ENAM region).

4. **Environment variables** — copy `.env.example` to `.env` and fill in:
   ```
   OPENAI_API_KEY=sk-...                    # for embeddings
   R2_ACCOUNT_ID=186ee77dc3cb07be2e88eb78137860c7
   R2_ACCESS_KEY_ID=...                     # from Cloudflare dashboard → R2 → Manage API tokens
   R2_SECRET_ACCESS_KEY=...
   R2_BUCKET_NAME=wallis-corpus
   ```
   The R2 credentials are likely already in `recursive-eco/apps/flow/.env.local`
   per the project's existing R2 setup — copy them over.

## Run order

```bash
# 1. Scrape (one-time, resumable; ~25 min for ~500 posts at 2s delay)
python scrape.py

# 2. Embed + upload (one-time, idempotent; ~5-10 min)
python embed.py

# 3. Query from anywhere (returns top-k chunks with citations)
python retrieve.py "what does Hareesh say about prajna?"
```

## What the scraper captures

For each blog post:
- URL, title, publication date, tags, full body text (clean)
- **Hareesh's own comment replies** (filtered by author name; third-party
  commenters excluded per author privacy and citation discipline)
- Saved as `transcripts/wallis-corpus/blog/YYYY-MM-DD-slug.md` with YAML
  frontmatter

**Resumable:** files that already exist are skipped on re-run. Useful for
periodic refresh.

## What the embedder does

- Reads all markdown files from `transcripts/wallis-corpus/blog/`
- Chunks by paragraph (target 600-800 tokens, 150 token overlap)
- Generates embeddings via OpenAI `text-embedding-3-small`
- Uploads to R2 as `wallis-blog-embeddings.jsonl` (one chunk per line)
- Writes `manifest.json` with stats and chunk SHA index for idempotency
- **Idempotent:** chunks with unchanged content (by SHA) are skipped on
  re-embed. Useful when adding new posts.

## What the query function returns

```python
from retrieve import retrieve, format_for_claude

chunks = retrieve("what does Hareesh say about prajna?", top_k=5)
context = format_for_claude(chunks)
# Each chunk in `context` is formatted as:
#
#   [Source: Title (YYYY-MM-DD)]
#   chunk text...
#   Read full post: https://hareesh.org/...
```

## System prompt

`system_prompt.md` contains the canonical system prompt for using these chunks
with Claude. The prompt:

- Frames the AI as **scaffolding**, not teacher or substitute for Hareesh's work
- ALWAYS cites by post title and source URL when drawing on his writing
- Reproduces no more than ~30 words verbatim from any source
- Redirects users to read original posts at hareesh.org for depth
- Refuses to perform AS Hareesh; positions the tool as "informed by his
  published teachings"
- Tone: thoughtful, slow, willing to redirect back to embodied practice

## Costs (estimated)

| Item | Time | Money | Storage |
|------|------|-------|---------|
| Scrape ~500 posts | ~25 min | $0 | ~10 MB local |
| Embed ~2,000 chunks | ~5-10 min | ~$0.02-0.05 (text-embedding-3-small) | ~5-15 MB on R2 |
| Per query | <2 sec | ~$0.000002 (1 embed) + Sonnet response | n/a |
| R2 storage ongoing | n/a | $0 (10 GB free, we use <0.1%) | n/a |

## Adding new author corpora later

The pipeline is parameterized by author. To add a second corpus
(e.g. Andreotti):

1. Set `AUTHOR_SLUG=andreotti` in `.env` (or pass `--author andreotti` to
   each script).
2. Adjust `scrape.py` `BASE_URL` and the comment-author filter for the new
   author.
3. Run scrape → embed → query in the same R2 bucket; chunks are tagged
   with `author_slug` so retrieve filters correctly.

## Future plan: YouTube + podcast parity

Logged as TODO in `_future_plan.md`. The current pipeline is blog-only.
The same architecture works for podcast/YouTube transcripts (yt-dlp +
faster-whisper for audio, then the same chunk → embed → retrieve flow,
with `source_url` pointing back to the YouTube video at the right
timestamp `&t=Ns`).

## Ethical guardrails

- **Never reproduce** more than ~30 words verbatim in any AI response
- **Always link** back to the original hareesh.org post
- **Tool is local + private** until Hareesh has been informed (he has, via
  WhatsApp; offer to stop is on record)
- **Respect robots.txt and rate limits** — 2 second delay between scraper
  requests, real User-Agent identifying the project
- **Comments filtering**: only Hareesh's own replies are captured;
  third-party commenters are excluded for author privacy and citation
  discipline

## Files in this directory

```
scrape.py                # Blog scraper
embed.py                 # Chunk + embed + R2 upload
retrieve.py              # Top-k cosine similarity query
system_prompt.md         # Canonical scaffolding-not-teacher prompt
requirements.txt         # Python deps (pinned)
.env.example             # Env var template
_future_plan.md          # YouTube/podcast parity, multi-author, etc.
tests/
  test_pipeline.py       # End-to-end test (3 posts, no upload)
README.md                # This file
```
