# Tapesearch UIDs — Coordination Problem book

Run on 2026-04-20. 26 podcast titles searched.

## Confirmed hits (available on tapesearch)

| Podcast | UID | Priority | Why |
|---|---|---|---|
| Bankless | 1499409058 | HIGH | Yudkowsky's 4-hour appearance + crypto-AI crossover |
| Dan Carlin's Hardcore History | 173001861 | HIGH | Nuclear episodes, Destroyer of Worlds |
| Dan Carlin's Hardcore History: Addendum | 1326393257 | MED | Extras |
| The Lawfare Podcast | 498897343 | HIGH | Treaty law, coordination, AI policy |
| Rational Security (Lawfare) | 956270301 | MED | National security framing |
| GZERO World with Ian Bremmer | 1294461271 | MED | Geopolitical AI framing |
| Conversations with Tyler | 983795625 | MED | Cowen is accelerationist — steelman |
| Rationally Speaking | 351953012 | MED | Julia Galef, rationalist-adjacent |
| Unconfuse Me with Bill Gates | 1695132549 | LOW | Some AI episodes |

## Not found on tapesearch (smaller AI-safety podcasts)

These likely need YouTube / direct-site scraping, not tapesearch:

- **AXRP** (Daniel Filan) — alignment researchers interview series
- **Doom Debates** (Liron Shapira) — the Yudkowsky-adjacent podcast
- **Future of Life Institute Podcast** — Tegmark org, has Bengio, Russell, etc.
- **The Cognitive Revolution** (Nathan Labenz) — founder perspective on frontier labs
- **Machine Learning Street Talk** (Tim Scarfe) — technical-rigorous safety debates
- **The Inside View** (Michaël Trazzi) — alignment research interviews
- **Hear This Idea** (Fin Moorhouse, Luca Righetti) — EA / longtermist
- **Clearer Thinking** (Spencer Greenberg) — meta-rationality + AI safety
- **Robinson's Podcast** (Robinson Erhardt) — 5-hour Yudkowsky conversation
- **Arms Control Wonk** (Jeffrey Lewis) — nuclear treaty expert
- **Press the Button** (Ploughshares) — nuclear policy
- **At the Brink** — nuclear history

Workaround: use YouTube Data API (already available in recursive-eco) to fetch captions for specific episodes. Priority YouTube pulls:

1. Yudkowsky × Bankless (4hr) — YouTube
2. Yudkowsky × Robinson Erhardt (5hr+) — YouTube
3. Soares × various — YouTube
4. Bengio × FLI — YouTube
5. Hinton × Geoffrey Hinton CBS 60 Minutes — YouTube
6. Leopold Aschenbrenner × Dwarkesh (have)
7. Carl Shulman × Dwarkesh
8. AXRP key episodes with Paul Christiano, Evan Hubinger, Ajeya Cotra

## Download plan (conservative — stay within 2000/day)

**Phase 1** (once, next session, ~1000 calls):
- Bankless full feed (~400 eps, but filter for AI-safety-relevant before bulk download)
- Dan Carlin Hardcore History (~70 eps total — just pull all)
- The Lawfare Podcast AI-specific episodes only (search by keyword in title)

**Phase 2** (different day):
- Conversations with Tyler — filter for AI guests (Demis Hassabis, Dario Amodei, Yudkowsky, Bengio if present)
- GZERO — filter for AI episodes
- Rationally Speaking — AI-safety-tagged episodes

**Phase 3** (YouTube, not tapesearch):
- Use `recursive-eco` YouTube tooling to pull captions for the 8 priority episodes above
- Store in `transcripts/Podcasts-library/youtube-safety/`

## Commands to run (when ready)

```bash
cd transcripts/Podcasts-library

# Phase 1
python tapesearch_download.py --list 1499409058   # Preview Bankless
python tapesearch_download.py --download 1499409058 bankless  # Bulk

python tapesearch_download.py --list 173001861    # Preview Hardcore History
python tapesearch_download.py --download 173001861 hardcore-history

python tapesearch_download.py --list 498897343    # Preview Lawfare (huge)
# Do NOT bulk Lawfare — filter first. Thousands of episodes.
```

## Notes

- Tapesearch searches matched some podcasts by partial/wrong title. Confirmed hits verified by author name.
- The small AI-safety podcasts are the ones whose content is most thesis-relevant. YouTube scraping is the real path for those.
- The search script cost 26 API calls (budget: 2000/day). Plenty of headroom for Phase 1 downloads.
