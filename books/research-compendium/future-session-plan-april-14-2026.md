# Future Session Plan — April 14, 2026

Logged at end of multi-day session. Items identified but not addressed.

---

## recursive.eco Code

### 1. Shared viewer header JS module
- Tree viewer and grammar viewer now both have the same header buttons (Get a Reading, Explore More, GitHub, Copy, Report)
- Currently duplicated as inline HTML in each static file
- Should extract into a shared `viewer-header.js` that both pages include
- Files: `apps/landing/pages/tree-viewer.html`, `apps/landing/pages/grammar-viewer.html`

### 2. Grammar AI personality indicator in journal dropdown
- When a deck has `ai_personality_prompt`, the journal's "Review before sending" modal still shows "Default (Empathy Buddy)" in the dropdown
- The server-side priority works (grammar > template > default), but the user can't see which personality is active
- Suggestion: show a label below the dropdown: "🤖 Using [deck name] personality" when a grammar personality is active
- Or: auto-select the grammar personality in the dropdown when a deck with one is loaded

### 3. Simplify save paths in UnifiedGrammarPage
- Currently 4 separate save paths that all build the grammar object independently
- The stale closure bug (fixed with refs) wouldn't have happened with a single save function
- Consider extracting `buildGrammarForSave()` that all 4 paths call
- File: `apps/flow/src/components/offer/universal-editor/UnifiedGrammarPage.tsx`

### 4. Save confirmation UI
- No visual feedback when save succeeds — user doesn't know if it worked
- Add a brief toast/notification: "Saved ✓" that appears for 2 seconds after successful save
- Also: suppress the "unsaved changes" browser warning if the last save was < 5 seconds ago

### 5. Stale closure audit
- The `aiPersonalityPrompt` and `imageStylePrompt` had stale closure bugs in handleSave
- Other state variables might have the same issue (description, creatorName, etc.)
- Audit all state used in handleSave and convert to refs where needed
- Or: restructure handleSave to read state at call time instead of closure time

### 6. Music grammar type selector
- Music grammar type exists in code but can't be selected from the UI
- Either add "music" to the grammar type dropdown, or (better) make autoplay a per-grammar toggle instead of a type
- The autoplay toggle was ungated from music-only in this session, so the type may not be needed at all

### 7. SVG → PNG conversion at import time
- When importing a grammar with SVG images, the platform could convert them to PNG during R2 upload
- This would let the AI see all card images (it can't process SVGs)
- Requires adding `sharp` as a dependency to the upload pipeline
- May hit Vercel serverless function size limits

### 8. Spotify embed in Build card detail
- Spotify embeds show in the grammar reader but not in the Build card editor
- Console error: "Unsafe attempt to load URL" from chrome-error context
- May be a CORS/mixed-content issue specific to dev preview

### 9. Community deck ordering by stars then date
- The journal deck selector shows community decks in unspecified order
- Should sort by star count (descending) then creation date (descending)
- File: deck list API route or `custom-tarot.ts` fetch function

### 10. Lyrics from LRCLIB — test with music grammars
- The `/api/lyrics` route and "Fetch Lyrics" button were built but not fully tested
- Need to test with a music grammar that has artist + track metadata
- LRCLIB works for Brazilian music (confirmed with Novos Baianos)

### 11. Brazilian Portuguese grammar
- Untranslatable words as oracle cards: saudade, jeitinho, axé, mandinga, terreiro, malícia, gambiarra
- Discussed, not started. Future creative project.

### 12. Hareesh RAG system
- 307 transcripts (~1.44M words) in wallis-corpus
- Could embed in pgvector (Supabase), build search endpoint, integrate with Flow assistant
- Someday project. Start with option A (system prompt only — already done)

---

*Logged after a session that shipped: AI personality feature, stale closure fix, Spotify oEmbed import, LRCLIB lyrics, autoplay toggle, tree viewer header, Explore More fix, image hallucination fix, NVC deck restructuring, 52 PNG yantras, and two complete books.*
