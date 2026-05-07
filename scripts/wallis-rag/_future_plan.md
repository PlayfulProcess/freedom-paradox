# Wallis RAG — future plan

## YouTube + podcast parity

The current pipeline is **blog-only**. The same architecture extends naturally
to podcasts and YouTube talks. Plan when ready:

### Sources to add

- **Tantra Illuminated podcast** — hareesh.org/podcast/, also on Spotify/Apple
- **YouTube channel** — youtube.com/@HareeshWallis (talks, retreat sessions, dharma talks)
- **Mattamayura Institute** content — mattamayura.org

### Pipeline changes

1. **`scrape_youtube.py`** — new script using `yt-dlp` to download auto-captions:
   ```bash
   yt-dlp --write-auto-sub --sub-lang en --skip-download \
          --output 'transcripts/wallis-corpus/youtube/%(upload_date)s-%(id)s.%(ext)s' \
          https://www.youtube.com/@HareeshWallis
   ```
   Caption files (.vtt) parsed into markdown with `source_url` pointing at
   the video with timestamp anchor: `https://www.youtube.com/watch?v=ID&t=Ns`

2. **`scrape_podcast.py`** — RSS feed parser for the podcast feed; for episodes
   without auto-captions, use `faster-whisper large-v3` for transcription
   (or `whisperx` for diarization if multi-speaker episodes).

3. **`embed.py` update** — already author-aware via `AUTHOR_SLUG` and
   `AUTHOR_NAME`; needs only a `source_type` field added to each chunk record
   (`blog | youtube | podcast`) so retrieval can filter or label.

4. **`retrieve.py` update** — `format_for_claude()` should produce different
   citation strings per source type:
   - blog: "Read full post: URL"
   - youtube: "Watch from this point: URL&t=Ns"
   - podcast: "Listen to episode: URL"

### Storage estimate

- ~100 hours of YouTube/podcast at ~150 wpm = ~900K words = ~1.2M tokens
- Embedding cost: ~$0.05
- Storage: ~10 MB JSONL on R2 (negligible)
- Whisper transcription cost (if needed): ~$0.36/hour with API, or free with local Whisper + GPU
- Total for full multi-source corpus: well under $1 one-time

### Linking discipline

Per the user's note: "ideally I would like current data in R2 to also have
links to original youtube videos and be able to refer user to them, just like
we are doing with blog."

The `source_url` field is already present in every chunk record. For
YouTube, the URL includes a `&t=Ns` timestamp matching where the chunk's
text starts in the video. The system prompt already requires citation
with URL on every response — so this future plan extends naturally:
when a chunk comes from YouTube, the link the AI surfaces takes the user
to the right second of the right video.

## Multi-author corpora in the same R2 bucket

Eventually you may want a single recursive-rag bucket with multiple authors
(Wallis, Andreotti, others). The current schema already supports this via
the `author_slug` field on each chunk. The path forward:

1. Move from author-specific bucket (`wallis-corpus`) to shared
   (`recursive-rag-corpora`).
2. Keep one JSONL per author (`wallis/embeddings.jsonl`,
   `andreotti/embeddings.jsonl`) — easier to manage permissions and
   re-embeddings per author.
3. `retrieve.py` accepts `--authors wallis,andreotti` flag to filter.
4. System prompt selects the appropriate citation discipline per author
   (Wallis is comfortable with blog quoting; Andreotti requires permission
   first; etc.).

## Per-item AI prompt integration with recursive.eco

Once the RAG is live, the natural next step is wiring it into the recursive.eco
journal flow:

- When a user is journaling on a Wallis-flavored grammar (or directly asks
  the AI about a topic Hareesh has written about), `retrieve()` runs and
  the top-k chunks are injected into the system prompt as additional
  context.
- Pattern follows the existing `iching-ai-prompt.ts` shape — per-item /
  per-question system prompt construction.
- See `recursive.eco-schemas/plan/bus-passengers-grammar-plan.md` for the
  parallel architecture proposed for the Bus Passengers grammar.

## Permission and deprecation

Hareesh has been informed of the persona work via WhatsApp; offer-to-stop is
on record. If at any point he asks for the corpus to be taken down:

1. Delete `wallis-blog-embeddings.jsonl` and `manifest.json` from R2.
2. Delete `transcripts/wallis-corpus/` locally.
3. Remove any references in the recursive.eco grammar JSON.
4. Document the removal in `_metadata/permission-status.md`.

The pipeline is built to support that — there is no platform-side dependency
that would prevent clean removal.
