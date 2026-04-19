# Deep-Research Pass — Scope, Sources, and Plan

**Date:** 2026-04-19
**Branch:** `claude/plan-retreat-insights-9lefO`
**Context:** v5 Ch03 §VII, Ch10 §VII, and Ch11 introduced (a) the Tristan Harris reversal beat, (b) the Ghost model as publishing-layer sibling, and (c) the Arjuna/Krishna + Dario framing. The chapters stand on repo content already. This pass adds the citation-grade research layer behind those chapters so the book can footnote and defend its claims.

---

## What PlayfulProcess asked for

Research material on:
1. **Tristan Harris** — his 2025–2026 public positions. The specific episode with Sam Harris if locatable.
2. **Jonathan Haidt** — *The Anxious Generation* (2024), its claims, the scholarly critique (Odgers, Przybylski, Etchells), and the recent legal wave (Meta lawsuits, KOSA-style prohibitions, state AG actions).
3. **Anna Lembke** — *Dopamine Nation* (2021), the pleasure-pain balance thesis, application to digital media, any DBT-adjacent claims.
4. **Peter Attia** — *Outlive* (2023), his public DBT journey (including the Paul Conti episodes), his episode with Sam Harris, and whatever material is available in his own voice.

Author note (mid-session correction): *"Travis Harris"* in the request was a typo for Tristan Harris. Confirmed.

---

## Source inventory — what is actually available in this session

### Local podcast transcripts (in `transcripts/`, gitignored, LOCAL-ONLY)

**Tristan Harris:**
- `transcripts/Podcasts-library/80000-hours/tristan-harris-changing-incentives-social-media.txt`

**Jonathan Haidt** (`guest-appearances/jonathan-haidt/`):
- `How Smartphones & Social Media Impact Mental Health & the Realistic Solutions | Dr. Jonathan Haidt` (Huberman Lab)
- `Jonathan Haidt - "The Anxious Generation" | The Daily Show`
- `The Anxious Generation with Jonathan Haidt | What Now? with Trevor Noah Podcast`
- `The Anxious Generation w/ Jonathan Haidt | The Psychology Podcast`
- `What Social Media Is Doing To Gen Alpha, with Jonathan Haidt`
- `Why We've Become The ANXIOUS Generation & How We Can Fix It | Dr. Jonathan Haidt`
- `'Our Kids Are the Least Flourishing Generation We Know Of' | The Ezra Klein Show`

**Anna Lembke** (`guest-appearances/anna-lembke/`):
- `Dopamine Expert: Doing This Once A Day Fixes Your Dopamine! What Alcohol Is Doing To Your Brain!`
- `Dopamine Expert: How TikTok Is Physically Rewiring Your Brain (Permanent Damage?)`
- `Dopamine Nation: Finding Balance in the Age of Indulgence with Anna Lembke`
- `Dr. Anna Lembke - Dopamine Nation and the Age of Digital Drugs | Prof G Conversations`
- `The Science of Self Control: Find Motivation, Increase Your Focus, and Hack Dopamine`
- `Understanding & Treating Addiction | Dr. Anna Lembke`

**Peter Attia:**
- `transcripts/Podcasts-library/sam-harris-corpus/health-longevity-a-conversation-with-peter-attia.txt` (Making Sense #328)

**Adjacent Sam Harris episodes (context for the social-media argument):**
- `sam-harris-corpus/making-sense-of-social-media-and-the-information-landscape.txt`
- `sam-harris-corpus/a-better-way-to-use-your-phone.txt`

### External web sources (use WebSearch / WebFetch)

For material not in local transcripts:
- Tristan Harris's 2025–2026 writing at `humanetech.com` and *Your Undivided Attention* show notes
- The specific Tristan Harris × Sam Harris episode (Sam Harris's Waking Up #71, 2017, *What Is Technology Doing to Us?*) — not in local corpus
- Scholarly critique of *The Anxious Generation*: Candice Odgers in *Nature*; Andrew Przybylski; Pete Etchells (*Guardian*, *Aeon*)
- Meta lawsuits: the multi-state AG suit filed October 2023, plus subsequent federal/state legal actions through 2025–2026; KOSA (Kids Online Safety Act) status as of early 2026
- *Outlive* (Peter Attia, 2023): publisher and key claims via publisher materials + Attia's public essays at `peterattiamd.com`
- Peter Attia's public DBT journey: his Paul Conti series on *The Drive*; his memoir-adjacent passages in *Outlive* Chapter 17

### Not available in this session

- Peter Attia Drive podcast transcripts (not locally downloaded)
- Your Undivided Attention podcast transcripts (not locally downloaded)
- Sam Harris Waking Up #71 (Tristan Harris, 2017 — predates the local archive)
- Any transcript behind a Tapesearch API key — `.env.local` with `TAPESEARCH_API_KEY` is not in the book-repo root; if PlayfulProcess drops the key, the `tapesearch_download.py` script at `transcripts/Podcasts-library/tapesearch_download.py` can pull the missing episodes in a follow-up pass

---

## Plan — what this pass produces

Per CLAUDE.md copyright and podcast-locality rules:
- Raw transcripts stay local and uncommitted.
- Research files contain original synthesis with `≤15` words per attributed quote.
- No fabricated page numbers, timestamps, or URLs. Flag `[VERIFY]` / `[RESEARCH NEEDED]` where uncertain.
- Privacy: author is PlayfulProcess throughout.

### Output files (will commit under `books/axiom-beneath-the-ground/research/`)

1. `podcast-tristan-harris-80k-hours.md` — synthesis of the local 80K Hours episode
2. `research-32-tristan-harris-public-positions.md` — composite: the 80K Hours synthesis + web-verified 2025–2026 public positions. Covers *Your Undivided Attention*, Center for Humane Technology writing, the "AI dilemma" arc, and the specific Sam Harris Waking Up #71 episode by reference (if locatable)
3. `podcast-haidt-composite.md` — synthesis across the seven local Haidt episodes
4. `research-33-haidt-anxious-generation-critique.md` — *Anxious Generation* claims + the scholarly pushback (Odgers, Przybylski, Etchells) + the Meta/KOSA legal layer
5. `podcast-lembke-composite.md` — synthesis across the six local Lembke episodes
6. `research-34-lembke-dopamine-nation.md` — *Dopamine Nation* thesis, where the neuroscience is solid and where it is clinical-philosophical, application to AI/LLM use
7. `podcast-peter-attia-sam-harris.md` — synthesis of Making Sense #328
8. `research-36-peter-attia-outlive-and-dbt.md` — *Outlive*'s Chapter 17 / emotional-health section + Attia's public DBT / Paul Conti arc + the Sam Harris episode summary

Rename note: `research-35` is reserved in the author's ordering for Substack; Meta-lawsuits material can either live inside `research-33` (Haidt composite) or as a sibling `research-37-meta-lawsuits-kosa.md`. Decision deferred to the author.

### What is NOT produced in this pass

- No Tristan Harris × Sam Harris episode synthesis (source not locally available)
- No Peter Attia Drive podcast synthesis (source not locally available)
- No full-corpus grep across all 5,000+ local transcript files — targeted extraction only
- No committed podcast transcripts of any kind

### Blocker for the fuller version

Drop `TAPESEARCH_API_KEY` into `book-repo/.env.local` and this session can:
- Download Peter Attia Drive's Paul Conti DBT series (estimated 4–6 episodes)
- Download *Your Undivided Attention* selected episodes
- Download Sam Harris Waking Up #71 if it is still in Tapesearch's index

Each episode is one API call to list + ~one API call per episode body. The script handles rate limiting (60-second backoff on HTTP 429).

---

## Execution order

1. **[this file]** Research plan — done
2. Tristan Harris composite — local transcript + WebSearch 2025–2026 positions
3. Haidt composite — local transcripts + WebSearch critique + Meta/KOSA legal layer
4. Lembke composite — local transcripts + WebSearch book claims and neuroscience sourcing
5. Peter Attia composite — local Sam Harris #328 + WebSearch *Outlive* + WebSearch DBT/Conti arc
6. CHANGELOG update + commit

Each composite research file will end with a working footnote draft, a "Notes for the book" section, and a list of `[RESEARCH NEEDED]` / `[VERIFY]` flags.
