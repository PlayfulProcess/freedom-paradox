# Future Session Plan — April 13, 2026

Logged at the end of a marathon session. These are next-session tasks, not urgent.

---

## 1. NVC/Tantra Deck: Add Emergence Patterns + Plutchik's Wheel

**Grammar ID:** `bf0cba5b-2f6b-4d80-941b-27bb0333a873`
**Current state:** 50 items, all flat (no levels, no parent_ids). 20 needs, 10 met feelings, 10 unmet feelings, 5 bridges, 6 emergences.

**What to do:**
- Set levels: L3 for category groupings (Needs, Met Feelings, Unmet Feelings, Bridges), L2 for emergences, L1 for individual items
- Add `parent_id` linking feelings to their need: e.g., Joy → Connection, Fear → Safety
- Add `composite_of` to emergences: e.g., "Sacred Anger" = Anger (unmet) + Honesty (need) + Fierce Compassion (emergence)
- Weave in Plutchik's Wheel of Emotions — his 8 basic emotions (joy, trust, fear, surprise, sadness, disgust, anger, anticipation) map to the NVC feelings. His dyads (joy+trust=love, fear+surprise=awe) map to the emergences. Consider using the Plutchik wheel as the cover image or as a visual organizer.
- Consider: unmet need → unmet feeling → bridge (tantric practice) → met feeling → met need. This is the NVC process AS a grammar path.

**Can be done directly in Supabase** — update the JSONB document_data for this grammar ID.

---

## 2. Music Grammar Type in UI

**Problem:** The music grammar type exists in code (`grammar_type: 'music'` with section presets: Lyrics, Translation, Notes, Credits) but there's no way to SELECT it from the UI when creating a new grammar.

**What to build:**
- Add "music" to the grammar type selector in the Create/New Grammar flow
- The type selector is probably in `UnifiedGrammarPage.tsx` or the new grammar creation modal
- When music type is selected, preset the section templates to Lyrics, Translation, Notes, Credits
- Add YouTube video ID field to item editor for music items
- Show the MusicYouTubePlayer component in the reader for music-type grammars
- The Spotify paste import already works — just needs the type to be selectable

**Files likely involved:**
- `apps/flow/src/components/offer/universal-editor/UnifiedGrammarPage.tsx`
- Grammar type selector component (find where `grammar_type` options are defined)
- `apps/flow/src/components/MusicYouTubePlayer.tsx` (already exists)

---

## 3. Personal Decks in Oracle Selector

**Problem:** The tarot oracle deck selector only shows community decks (from `tools` table). Personal decks (in `user_documents`) like the tattva deck don't appear.

**What to fix:**
- In `OracleSelector.tsx` → the `fetchItems` config function needs to ALSO query `user_documents` for the current user's grammars with oracle/tarot type
- Merge personal decks into the selector list, probably with a "My Decks" section above community decks
- The `fetchDeckWithCards()` function in `custom-tarot.ts` already handles `user_documents` — it's just the selector that doesn't list them

---

## 4. Code Cleanup Opportunities (author is NOT sure about these — log but don't act)

**a. tools table vs user_documents separation**
- The CLAUDE.md says tools → user_documents migration is planned
- **Author prefers keeping them separate for now.** The deck fetch checks both tables, which works. Don't merge yet.

**b. CardDetailModal.tsx (~650 lines)**
- Could split flexible sections, Spotify/YouTube embeds, and standard tarot fields into subcomponents
- Not urgent — it works fine

**c. OracleSelector.tsx (~500 lines)**
- Configs for tarot, I Ching, astrology, stories all in one file
- Each config could be its own module
- Not urgent

**d. custom-tarot.ts section mapping**
- The hardcoded section name mapping (Summary, Interpretation, Meaning) is fragile
- The fix we applied (also mapping Essence, Practice, About) helps but the pattern is still brittle
- A better approach: pass ALL sections to the AI and let the prompt interpret them
- Partially done in this session but could be cleaner

**e. The `:1` suffix on deck API calls**
- Couldn't reproduce in code — might be browser extension or stale cache
- Monitor, don't fix yet

---

## 5. Hareesh AI with RAG (someday project)

**What exists:**
- **307 podcast transcripts** in `book-repo/transcripts/Podcasts-library/wallis-corpus/` (~1.44M words, cleaned text)
- **Full system prompt** at `book-repo/transcripts/Podcasts-library/wallis-agent-prompt.md` (~9.5KB)
- **Claude Project** on claude.ai named "Christopher Wallis / Hareesh" (created this session, needs system prompt pasted + files uploaded)
- **`/wallis` slash command** in Claude Code (already configured)

**How a RAG system would work:**

1. **Embed the corpus:** Run all 307 transcripts through an embedding model (OpenAI's text-embedding-3-small or Anthropic's). Store the embeddings in a vector database (Supabase pgvector is free and already available in the project).

2. **Create a search function:** Given a query, embed it, find the top 5-10 most relevant transcript chunks, return them.

3. **Build the API route:** New endpoint (e.g., `/api/ai/wallis`) that:
   - Takes a user question
   - Searches the vector DB for relevant transcript chunks
   - Injects the system prompt + relevant chunks into the AI context
   - Returns the response in Wallis's voice

4. **Integrate with the Flow assistant:** Add Hareesh as an AI personality option in the journal. When selected, the system prompt changes and the RAG pipeline provides grounding.

5. **Connect to the tattva deck:** When a tattva card is cast, the Wallis RAG could provide tradition-specific interpretation grounded in his actual teachings — not hallucinated imagery.

**Cost estimate:** Embedding 1.44M words ≈ $0.02 with text-embedding-3-small. Storage in pgvector is free on Supabase. The ongoing cost is just the AI API calls for each query.

**The ethical question:** This was discussed in the session. The Wallis project (the AI persona) gave excellent editorial feedback. But deploying a public "Hareesh AI" raises the same extraction concern the Axiom book critiques — taking the teacher out of the container. The recommendation: build it for personal use, show it to him, let him decide if it should be public. "Do before you know, then show the teacher."

---

## 6. Oracle Philosophy Page for recursive.eco

**Already planned** at `recursive.eco-schemas/plan/oracle-philosophy-plan.md`

Key points:
- "The card is a mirror, not a map"
- Name the near enemy (conceptual bypassing)
- Connect casting to the three upāyas
- Applies to ALL oracle grammars, not just tattvas

---

## 7. Brazilian Portuguese Grammar (future)

Discussed but not started. Untranslatable words as oracle cards: saudade, jeitinho, axé, mandinga, terreiro, malícia, gambiarra. Each word is a card with a practice. "Which untranslatable word is presenting itself for recognition right now?"

---

## 8. Spotify Import: Only URLs, No Metadata

**Problem:** When importing from Spotify, only the track URLs get imported — no track name, artist, album, or cover art. The item name shows as `https://open.spotify.com/track/...` instead of "Artist - Song Title".

**Current state:** The `spotify-import.ts` parser handles Spotify Desktop paste format (Ctrl+A → Ctrl+C) and Exportify CSV. But if you just paste Spotify share links, it only captures the URL.

**What's needed:**
- When a Spotify URL is pasted, scrape the track metadata from the URL (Spotify's oEmbed endpoint is still public: `https://open.spotify.com/oembed?url=TRACK_URL` returns title, artist, thumbnail)
- Alternatively, use Spotify's public embed endpoint to extract metadata without API auth
- Fill in: item name = "Artist - Song", image_url = album art, metadata.spotify_url = the link
- The Spotify Web API requires OAuth — avoid this. The oEmbed endpoint is simpler and doesn't need auth.

**Files:** `apps/flow/src/lib/spotify-import.ts`, the import modal in the unified editor

---

*Logged by Claude Opus 4.6 after a 12+ hour session that produced: 2 books (60K+ words), 1 tattva deck (52 cards, 3 rounds of traditional review, 52 yantras), 13 EPUBs, a landing page, an epub pipeline, a dramatic dialogue, strategic platform advice, and the sentence "Maybe it is earth talking. Maybe we are learning the language."*
