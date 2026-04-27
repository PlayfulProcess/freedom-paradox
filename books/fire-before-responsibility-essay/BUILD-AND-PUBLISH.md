# Fire Before Responsibility — Build & Publish (tomorrow's checklist)

The book is drafted. ~10,500 words across foreword + 8 chapters. This file is your run-script for tomorrow.

## Before building (10 min)

1. **Read once with fresh eyes.** Foreword + Ch 8 first (the bookends). Then Ch 4 (the wealth-effect chapter — newest, least cross-checked).
2. **Verify quotes.** The 28-word Amodei quote in Ch 3 is from the WEF January 2026 panel transcript at `transcripts/youtube-safety/02YLwsCKUww/hassabis-amodei-wef-2026-transcript.txt`. Confirm the exact wording matches; adjust if you find a sharper line.
3. **Decide on the signature.** Currently Ch 8 closes with "PlayfulProcess, recursive.eco" — change if you want.

## Build the EPUB

The book sits at `books/fire-before-responsibility-essay/`. Per CLAUDE.md, the EPUB pipeline expects `book.yaml` (already written) and chapters in `chapters/`. The build command is:

```bash
bash epub-build/build-single-epub.sh fire-before-responsibility-essay
```

This produces `epub-build/output/fire-before-responsibility-essay.epub`.

If `build-single-epub.sh` doesn't recognize the new slug, you may need to add it to the script. Per CLAUDE.md "When adding a new book or version" instructions:
- Add `mkdir -p` + `cp` lines to `build.sh`
- Add `mkdir -p` + `cp` lines to `.github/workflows/deploy-book.yml`
- Add entries to `src/SUMMARY.md`
- Update `docs/epubs/index.html` with Read Online + EPUB links
- `cp epub-build/output/fire-before-responsibility-essay.epub docs/epubs/`

## Publishing checklist

1. EPUB built and copied to `docs/epubs/`
2. mdbook site rebuilt: `bash build.sh`
3. Card added to `docs/epubs/index.html` for the new book
4. Git: add + commit + push (must include `books/`, `epub-build/output/`, `docs/epubs/`, `src/`)
5. GitHub Actions auto-deploys on push to master

## Submission flow

1. The Foreword IS the Dwarkesh Prize submission essay. ~990 words; under 1000 limit.
2. Submit Foreword as essay via Dwarkesh's submit form by May 10, 2026.
3. After submission, publish a Substack post with the Foreword text plus a link to the EPUB at the bottom: "If you want the long-form argument, the eight-chapter book is here: [books.recursive.eco link]."
4. Optionally email Dwarkesh directly with a link, attached as further reading.

## What the book is doing structurally

| Chapter | What it argues | Source files |
|---|---|---|
| Foreword | The 1000-word essay = Dwarkesh submission | New synthesis tonight |
| 1. The Smokescreen | Why "regulate AI like social media" is wrong | `kgm-section-230-design-defect`, `research-33-haidt`, `ANGLE-smokescreen-verification` |
| 2. Captive R&D | Labs cannot regulate themselves; investor control beneath captive structure | `dwarkesh-prize-Q2-captive-RnD-thesis` + tonight's investor-control sharpening |
| 3. Racers Have Said So | Public testimony from Hassabis/Amodei/Sharma/Aschenbrenner | Local Dwarkesh transcripts + WEF panel transcript |
| 4. The Wealth Effect | Bubble argument — political class can't slow because economy depends on AI valuations | Web research tonight on Mag-7, Schiller CAPE, Altman/Pichai/Dimon admissions |
| 5. Verification Before Treaty | OPCW model not IAEA; CWC vs BWC lesson; hardware-attestation feasibility | `nuclear-treaty-analogs-for-ai` |
| 6. What $180B Should Buy | Five allocations + five refusals | `ANGLE-smokescreen-verification` + Q3 drafts |
| 7. The Imperial Method | Why "save the Global South with AI" reproduces the colonial method; how to refuse without abandoning | Hao *Empire of AI*, Mhlambi, Hui, Lewis-Kite-Arista, Aneja, Q4 research file |
| 8. A Builder's Receipt | recursive.eco platform position; OpenAI removal; K.G.M. trigger | Axiom Ch10d, Author's Note, Somya letter |
| 9. The Hospicing | Roman/feudal historical parallel; Andreotti/Akomolafe close; Wonderwerk callback | Author's tonight messages on QE/COVID/state fragility |

## Open verification flags before submitting

Per CLAUDE.md privacy and accuracy rules:
- "Working Architecture" or "Fire and Intelligence" referenced as published — confirm framing
- "Stopped paying to acquire users" / "near-zero margins" / "clinician checkpoint" claims — these are NOT in the current book draft (the book uses your verifiable receipts instead: OpenAI removal commit, code-private-grammar-open commit, the K.G.M.-trigger commitment). The book is internally consistent on this front. Good.
- MSW completion — not claimed in the book.
- "Equity research analyst" — not claimed in the book; Ch 7 says "she runs a platform" without occupational pedigree. Good.
- Umbanda — not in this book (kept in the Q3 drafts where it serves; this book stays structural-economic).

## The book holds its own scope discipline

You asked tonight whether you were getting sidetracked. Answer: no. Every addition you made tonight (investor-control sharpening, wealth-effect, Roman/feudal frame) landed in a different chapter and tightened the argument. The book is converging, not sprawling.

The book does NOT include: Castaneda, AI mental-health-harms research, the Wallis material, the multi-narrator framing, the K.G.M. cross-book material at length. Those live in their respective books. This book is the urgent compressed version.
