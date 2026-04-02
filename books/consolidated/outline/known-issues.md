# Known Issues and Future Work

**Status:** Pre-publication audit, April 2026

---

## Source Verification Needed

### Consolidated Book
- Ch16: Coan Social Baseline Theory (2006) — paraphrase accurate, direct quote not available
- Ch19: Gilligan *Violence* — "pathogen is an emotion" quote approximately p. 110, needs physical copy verification
- Ch19: Singer ReSource Project cortisol figure — cited as 51%, primary source says "up to" 51%
- Ch25: Margulis "Life did not take over the globe by combat, but by networking" — widely attributed, likely *Symbiotic Planet* (1998), exact page needed
- Ch32: Aboriginal bird origin story — CARE Principles require verification against documented Aboriginal sources and consultation with community representatives before publication

### Real Cost of Lunch (Appendix A)
- Ch01: 15 [VERIFY] flags for agricultural statistics (hectares, market share, spraying frequency, emissions percentages, water footprint, land use, child labor, food waste). All are commonly cited figures from FAO, IPCC, EPA, ILO — need current-year verification for accuracy.
- These are data-level verifications, not argument-level concerns. The claims are directionally correct; exact figures may have updated.

---

## Structural Tensions (Intentionally Unresolved)

These are not errors. They are the book's honest tensions. Documented here for reader and editor awareness.

1. **Axiom vs Truth (Ch26-27)** — The book holds both positions without resolving them. Ch26 says inherent value is an axiom (chosen). Ch27 presents Kashmir Shaivism's claim that it is truth (recognized). The Silverstein poem and three "it might not matter" versions are the closest the book comes to resolution. This is a design choice.

2. **Eclecticism critique vs eclectic book (Ch40)** — The book critiques the spiritual buffet while being one. The Campbell/new mythology response is in Ch40. The community-must-respond framing acknowledges this is unfinished work.

3. **Helper's innocence vs building recursive.eco (Ch39)** — The book names the trap of solving while building the platform. The light/shadow framing from the about page is now in Ch39. The book does not claim innocence.

4. **Book Two starts with philosophy, not practice (Ch27-31)** — Bridge paragraph added at Ch27 opening explaining why philosophy precedes practice. Some readers may still find this section too abstract.

---

## Missing Elements (for future revision)

1. **Ch19 (Polarization of the Polis)** — Still has PLACEHOLDER comment for opening case study. Needs a concrete narrative opening (Rwanda gacaca courts, Northern Ireland cross-community storytelling, or similar).

2. **Ch35 (Family as Grammar)** — Does not address when repair isn't safe (abuse, broken families, situations where the grammar cannot hold). Needs a paragraph acknowledging conditions for repair.

3. **Ch40** — "Valid ≠ adaptive" framework not fully applied to the book's own recommendations. What does fidelity look like for someone whose tradition was destroyed by colonialism? Flagged but not resolved.

4. **Bibliography** — The book lacks a consolidated bibliography. Source citations are in HTML comments throughout. Needs compilation before formal publication.

5. **509 anti-oppressive SW course essays** — Not yet uploaded to master. When available, expand the MSW lived experience section in Ch39.

6. **Appendix A (Real Cost of Lunch)** — 8 chapters (Ch06-10, Ch12-13, Ch17) have no podcast research coverage. These commodity-specific and grief chapters need different sources (supply chain data, environmental psychology).

---

## Chapter Title Suggestions (from audit)

| Current | Suggested | Reasoning |
|---|---|---|
| Ch39: The Grammar We Need | Ch39: Beyond Solving | Chapter is about what grammars can't do, not what they are |
| Ch41: The Species That Tells Stories | (keep) | Strong closing title |
| Book Two: Relational Responsibilities | Consider subtitle: "What to Do When the Dilemmas Don't Resolve" | Clarifies for new readers |

---

## EPUB

- `mdbook-epub` added to CI workflow but not tested. First deploy will reveal if the plugin works with the current mdbook version (0.4.44). The epub backend is commented out in `book.toml` for local builds (uncommented by CI via sed).
