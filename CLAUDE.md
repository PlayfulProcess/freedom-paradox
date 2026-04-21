NExt session:
1) in the books/research-compedium folder
a)search for the merald episode on fire and see if it can help us weave this story better 
b) Check direct quotes from Gottman's new research file
3) Organizw all researhc into one folder and old book files into one folder called Old and whatever else you think might be clearner

# CLAUDE.md — Instructions for Claude Code

## PRIVACY — CRITICAL RULE

**The author publishes under the name PlayfulProcess. Never use any real/personal names for the author anywhere in this repository — not in files, commit messages, comments, or metadata. This applies to all past, present, and future content. If you encounter a real name in existing files, replace it with PlayfulProcess.**

This is a safety and identity boundary. Do not ask about it or reference it further.

## COPYRIGHT — CRITICAL RULE

**The author does not want to infringe anyone's copyright at any point in this project.** This applies to books, articles, podcasts, YouTube transcripts, song lyrics, scripture translations, and any other third-party source.

Rules:
1. **No substantial verbatim passages from copyrighted works in any committed file.** This includes chapter drafts, research notes, outlines, plans, changelogs, and prompts. "Substantial" means anything longer than ~30 words, and any shorter passage that captures the heart of a work's expression.
2. **Brief fair-use quotations (≤30 words)** are permitted inside finished chapter files when they are directly engaged for commentary, criticism, or citation, and attributed with full source information.
3. **In research files, outlines, and plans:** paraphrase rather than quote. Record *what a passage says*, *where it appears* (page, chapter, timestamp), and *how it fits the argument* — not the passage itself.
4. **Podcast transcripts, YouTube transcripts, and similar materials** remain local-only per the existing "Podcast Transcript Research — LOCAL ONLY" rule below. Never commit transcript content, index files naming episodes, or queue files to the repository.
5. **When drafting a chapter:** prefer paraphrase over quotation wherever possible. Quote only when the exact wording is argumentatively necessary.
6. **On request or dispute:** any quoted passage can be replaced with paraphrase at any time without argument.
7. **Never fabricate quotes, page numbers, or citations** to fill a gap. Use `[QUOTE NEEDED]` or `[VERIFY: citation]` flags instead.

If a task seems to require violating any of the above, pause and ask the author.

## Working With the Author

When you need files moved, downloaded, or placed in specific folders — **ask the author to do it**. Don't spend time trying to extract content from browser panels or fighting clipboard access. The author is happy to drag-and-drop files where they need to go. Similarly, if you need something from a Claude.ai chat, ask the author to download the files and tell you where they put them.

## Guiding Principle: Knowledge Without Action Is a Burden

This is an explicit authorial principle the author has asked to apply across all her non-fiction writing.

**Every philosophical claim in a non-fiction section should point at an action somewhere** — either in the author's own life, or in an honest invitation to the reader's. If a claim cannot point at an action, one of two things is true:

1. The claim is wrong and should come out.
2. The action has not been done yet, in which case either the claim comes out or the action needs to be done before the work ships.

The acting is also part of *testing* the claim — the Linehan filter (useful / fits the data / compassionate) remains operative through the action, not despite it. If the experience of the knowledge-in-action changes what the author can see, the framework gets revised.

When editing non-fiction chapters: watch for claims that float without an action anchor, and either surface the anchor, flag it for the author's decision, or propose revising the claim. Action anchors that already exist in this repo or in the author's public commit histories (recursive-eco, recursive.eco-schemas) are especially valuable — they are verifiable and specific.

## Git Config

GitHub email privacy is enabled. Always use this noreply email for commits:
`17236172+PlayfulProcess@users.noreply.github.com`

## Domain Note

The author owns **jongu.org** but hasn't configured it yet. For now, all references to "Jongu" in the Grammars book should point to **recursive.eco** instead. When jongu.org is eventually set up, we'll do a find-and-replace across the repo.

## Project Context

This is a multi-book writing project by PlayfulProcess. The author is a former Goldman Sachs equity research analyst, current MSW student, and builder on open-source tools (Supabase, Vercel, Next.js).

### Book 1: The Freedom Paradox
**Status: Complete first draft** · 16 chapters · ~85K words
Open source — a forty-year freedom movement — confronts genuine civilizational risk when applied to AI. The diagnosis: power without responsibility.
- Path: `books/freedom-paradox/`

### Book 2: Grammars of the Living World
**Status: First draft complete** · 10 chapters · ~21K words
What responsibility structures are, where they came from, and why we keep dismantling them. The theoretical response.
- Path: `books/grammars-of-the-living-world/`
- Final outline: `outline/book-outline-final-march-2026.md`
- Thesis breakthrough: `drafts/thesis-breakthrough-march-2026.md`
- 48 research files in `research/raw/` (research-01 through research-48 + 06a)
- Recursive.eco is framed as **responsibility infrastructure**, not a contemplative technology platform

### Book 3: The Species That Tells Stories
**Status: Draft in progress** · 3 of 7 chapters · ~20K words
We are the species that tells stories to its children. Love is the container. The container is disappearing. The narrative heart of the project.
- Path: `books/grammars-of-the-living-world/chapters/` (ch01-the-oldest-technology, ch02-the-darkness-is-the-medicine, ch03-what-the-old-stories-knew)
- Skeleton: `outline/new-skeleton-species-tells-stories-v1.md`

### Book 4: Working Architecture
**Status: First draft complete** · 12 chapters · ~20K words
A practical manual for building the containers. For parents, teachers, therapists — anyone who tells stories to anyone else.
- Path: `books/working-architecture/`
- Zero unresolved flags
- Five items need primary source page numbers (Ehrenreich, Somé, Gilligan, Margulis, Singer)

### Book 5: The Campfire Stories
**Status: Complete** · 5 books × 2 stories · ~9K words
Five-minute bedtime stories for ages 3–7, built from cross-cultural story arcs. Each book pairs two stories from different traditions around a shared theme.
- **Separate repo**: [github.com/PlayfulProcess/campfire-stories](https://github.com/PlayfulProcess/campfire-stories)
- Written in two prompts using the Vibe Writing 102 methodology
- Traditions: Akan (Anansi), Jātaka (Buddhist), Aboriginal Australian, Haudenosaunee, Japanese, 1001 Nights, European folk
- grammar.json ready for recursive.eco import
- CC BY-SA 4.0 licensed

### How the Books Connect
**The Freedom Paradox** is the diagnosis (power without responsibility). **Grammars of the Living World** is the framework (what responsibility structures are). **The Species That Tells Stories** is the narrative heart (how stories carry adaptive wisdom). **Working Architecture** is the practical manual (how to build containers Monday morning). **The Campfire Stories** is the proof of concept (stories built using the three-filter test, for actual children, in actual bedtimes). Each works alone; together they form the full architecture.

### Book 6: The Axiom Beneath the Ground
**Status: Complete** · 9 chapters · ~13K words
Tillich vs Christopher Wallis on whether inherent value is truth or axiom. The philosophical engine.
- Path: `books/axiom-beneath-the-ground/`

### Book 7: Fire Before Responsibility (formerly Fire and Intelligence)
**Status: Restructured to skeleton v3** · 9 chapters · ~18K words (target ~45-55K)
**THIS IS THE MAIN BOOK.** AI as fourth fire. "Do before you know" vs "know before you do." Absorbs content from Species That Tells Stories + Grammars of the Living World.
- Path: `books/fire-and-intelligence/`
- Skeleton: `books/fire-and-intelligence/outline/skeleton-v3.md`
- Content mapping: `books/fire-and-intelligence/outline/species-to-skeleton-mapping.md`
- 12-chapter draft archived: `books/fire-and-intelligence/drafts/12ch-draft-april-2026/`

### Book 8: The Real Cost of Lunch
**Status: Complete first draft** · 20 chapters
What your food actually costs — the nine hidden costs behind every plate.
- Path: `books/real-cost-of-lunch/`

### Book 9: The Repair Deck
**Status: Grammar imported, 6/22 chapters drafted** · ~50K words so far
A Major Arcana for mending. 22 archetypal repair patterns across intimate, communal, and civilizational scales. Gottman, Bowlby, Johnson, Linehan, Ostrom. 10 lenses per chapter.
- Path: `books/repair/`
- Source grammar: `research/grammar.json` from recursive.eco-schemas

### Book 10: The Wise Heart
**Status: Grammar imported, framework complete** · ~15K words (expandable to 50K)
DBT skills taught through world myths for ages 4-8. 29 story-skill pairs across 4 modules. Proof of concept #2 after Campfire Stories.
- Path: `books/dbt-wise-heart/`
- Source grammar: `research/grammar.json` from recursive.eco-schemas

### Book 11: Decolonization
**Status: Grammar imported, two source grammars** · ~50K words combined
Body, Mind, Spirit, Collective, Planet. The Tree of Coloniality (Andreotti). The decolonial companion to Grammars.
- Path: `books/decolonization/`
- Source grammars: `research/grammar-five-domains.json`, `research/grammar-gestures.json`, `research/grammar-decolonizing-childhood.json`

### Book 12: Social Working
**Status: Grammar imported** · ~15K words
The verb, not the profession. 76 cards deconstructing social work history. Erased voices, wicked history, more-than-human social working. The MSW companion.
- Path: `books/social-working/`
- Source grammar: `research/grammar.json` from recursive.eco-schemas

### How the Books Connect (Updated April 2026)
**Fire Before Responsibility** is THE book — the unified argument absorbing Species + Grammars content. **The Freedom Paradox** is the open-source history (separate, publishable now). **Working Architecture** is the practical manual (publishable now). **Axiom** is the philosophical engine (publishable now). **Real Cost of Lunch** applies it to food systems (needs 280 fact-checks). **The Wise Heart** is proof of concept (DBT through myths for children, card deck format). **Campfire Stories** is proof of concept #1 (separate repo). **Decolonization** and **Social Working** are recursive.eco grammars, not books. **The Repair Deck** is experimental format. **Consolidated** is retired.

### Publication Assessment
Full editorial audit: `books/PUBLICATION-ASSESSMENT-APRIL-2026.md`
- **PUBLISH:** Freedom Paradox, Working Architecture, Axiom
- **EDIT → PUBLISH:** Fire Before Responsibility (main project)
- **DRAFT:** Real Cost of Lunch (280 [VERIFY] flags), Repair Deck
- **SEED:** Decolonization, Social Working (platform grammars, not books)

### EPUB Pipeline
```bash
bash epub-build/build-single-epub.sh fire-and-intelligence  # Build one
bash epub-build/build-all-epubs.sh                           # Build all 13
# Output: epub-build/output/
# Metadata: epub-build/per-book-metadata/
```

## Publishing & Deployment

The books are published via **GitHub Pages** using **mdbook** (Rust-based static site generator).

### Build workflow
```bash
bash build.sh        # Syncs chapters from source dirs → src/, runs mdbook build
# Output: book/      # Pure static HTML site
```

### How it works
1. Source chapter files live in `books/*/chapters/*.md` (the source of truth)
2. `build.sh` copies them to `src/` subdirectories (staging area)
3. `mdbook build` generates the `book/` output from `src/SUMMARY.md`
4. GitHub Pages serves the `book/` directory

### Deployment
- **Live site**: [books.recursive.eco](https://books.recursive.eco/)
- **GitHub Pages**: deploy from `main` branch via GitHub Actions
- Custom CSS: `mdbook-theme/substack.css` (Newsreader serif, 19px, 680px max-width)
- Config: `book.toml`

### KDP Print-on-Demand Pipeline (Amazon paperback + Kindle)

Separate from the books.recursive.eco site. Produces Amazon-ready files.

**Build script:** `scripts/build-print.sh` (uses pandoc + typst, not LaTeX)

```bash
./scripts/build-print.sh freedom-paradox
./scripts/build-print.sh axiom-beneath-the-ground
./scripts/build-print.sh working-architecture
```

**Requires:**
- `pandoc` (already installed)
- `typst` — install once via `winget install Typst.Typst`
- One-time per book: create `books/<name>/book.yaml` with title/subtitle/author/description/source_url

**Per-book metadata (`books/<name>/book.yaml`):**
- `title:` — full title
- `subtitle:` — optional
- `author:` — defaults to "PlayfulProcess"
- `description:` — Amazon book description
- `source_url:` — GitHub link for attribution page
- `chapters_subpath:` — optional subfolder under chapters/ (e.g. `v5` for Axiom)

**Outputs:**
- `output/print/<name>-interior.pdf` — KDP paperback interior (6×9 trim, 0.625in inside gutter)
- `output/print/<name>.epub` — Kindle ebook

**Manual KDP upload steps (one-time per book, ~30 min each):**

**Before first upload — one-time account setup:**
1. Go to [kdp.amazon.com](https://kdp.amazon.com) → sign in with Amazon account (or create)
2. Complete tax interview (W-8BEN for non-US authors)
3. Add bank account for royalty deposits (required even at minimum royalty)

**Per book:**
1. KDP dashboard → **Create → Paperback**
2. **Language:** English
3. **Book Title:** copy from `book.yaml` `title`. Subtitle: copy from `subtitle`.
4. **Series/Edition:** leave blank
5. **Author:** PlayfulProcess (first name: PlayfulProcess, last name: leave blank, or Playful/Process)
6. **Description:** copy from `book.yaml` `description`
7. **Publishing rights:** "I own the copyright..."
8. **Keywords:** 7 max. For Axiom: tillich, wallis, consciousness, spiritual axiom, memoir, meditation, contemplative
9. **Categories:** pick 2 BISAC codes. For Axiom: "Religion/Spirituality" + "Biography & Autobiography/Personal Memoirs"
10. **Adult content:** No
11. **Next → Content:**
    - **Print ISBN:** "Get a free KDP ISBN" (start here; buy own ISBN only if you want IngramSpark later)
    - **Publication date:** leave blank (KDP assigns)
    - **Trim size:** 6 × 9 in
    - **Bleed:** No bleed
    - **Paper type:** White (default) or Cream — your call
    - **Cover finish:** Matte (looks classier) or Glossy
12. **Manuscript:** upload `output/print/<name>-interior.pdf`
13. **Cover:** use KDP Cover Creator (fastest — solid color + title + author). Or upload your own PDF if you have a cover design.
14. **Previewer:** review every page — fix errors back in the markdown + rebuild + re-upload
15. **Next → Pricing:**
    - **Territories:** All territories
    - **Primary marketplace:** Amazon.com (US)
    - **Royalty & Pricing:** 60% royalty. Set list price at **printing cost + $0.01** (KDP shows minimum; for a 311-page 6×9 it's typically $6.50–$8)
    - **KDP Select:** **DO NOT ENROLL** — requires Amazon exclusivity, incompatible with CC BY-SA
    - **Expanded distribution:** enable for libraries/bookstores (free, why not)
16. **Publish Your Paperback**

**Kindle ebook (after paperback is live):**
1. Back to dashboard → Create → **Kindle eBook**
2. Most fields copy from paperback (KDP will offer to clone)
3. **Manuscript:** upload `output/print/<name>.epub`
4. **Cover:** same cover from paperback (upload or Cover Creator)
5. **Pricing:** $2.99 minimum for 70% royalty tier (or $0.99 for 35% tier — books are CC BY-SA anyway so pricing is symbolic)
6. **DO NOT ENROLL in KDP Select** (same reason — exclusivity incompatible with CC)
7. Publish

**After upload:**
- Amazon review takes 24–72 hours for paperback, faster for Kindle
- Once approved, both formats appear on the book's Amazon page together
- Add the Amazon URL to `docs/epubs/index.html` card for that book

### Full Publishing Checklist (after any chapter edit)

When chapter content changes, ALL of these must be updated or the site will be stale:

1. **Edit the source file** in `books/[book]/chapters/` (the source of truth)
2. **Rebuild EPUB**: `bash epub-build/build-single-epub.sh [book-slug]`
3. **Copy EPUB to docs/epubs/**: `cp epub-build/output/[slug].epub docs/epubs/`
4. **Rebuild mdbook site**: `bash build.sh` (syncs chapters to `src/`, runs mdbook build)
5. **Git add + commit + push**: must include `books/`, `epub-build/output/`, `docs/epubs/`, `src/`
6. **GitHub Actions** auto-deploys on push to master (see `.github/workflows/deploy-book.yml`)

**Three places that must stay in sync:**
- `build.sh` — local build: copies chapters from `books/` to `src/`
- `.github/workflows/deploy-book.yml` — CI build: same copies, runs on GitHub Actions
- `src/SUMMARY.md` — mdbook table of contents: must list all chapters with correct paths

**Two landing pages:**
- `docs/epubs/index.html` — the main site landing page (books.recursive.eco), has Read Online + EPUB buttons. Gets copied to `book/index.html` during deploy.
- `epub-build/index.html` — the EPUB download page (legacy, less important)

**When adding a new book or version:**
1. Add `mkdir -p` + `cp` lines to BOTH `build.sh` AND `.github/workflows/deploy-book.yml`
2. Add entries to `src/SUMMARY.md`
3. Update `docs/epubs/index.html` with Read Online + EPUB links
4. Build the EPUB and copy to `docs/epubs/`

### Adding a new chapter
1. Write the chapter in `books/[book]/chapters/ch##-slug.md`
2. Add a line to `src/SUMMARY.md` pointing to the staged path
3. Add a `cp` line to `build.sh` AND `.github/workflows/deploy-book.yml`
4. Run `bash build.sh`
5. Rebuild EPUB: `bash epub-build/build-single-epub.sh [book-slug]`
6. Copy EPUB: `cp epub-build/output/[slug].epub docs/epubs/`

### Python emergence models
Computational models in `models/` support the books' arguments:
- `cultural_resilience_abm.py` — Agent-based cultural competition model
- `model_a_group_competition.py` — Tilman insurance hypothesis for cultures
- `model_a_insurance_test.py` — Clean insurance test
- `generate_charts.py` — Produces 6 matplotlib PNGs in `models/charts/`
- Charts are copied to `src/images/` during build

### Dashboard
Interactive Chart.js charts for Freedom Paradox data in `dashboard/`.

## Repository Structure

```
books/
  freedom-paradox/
    chapters/          # 16 markdown chapter drafts (source of truth)
    research/raw/      # Deep research dumps
    research/synthesis/ # Processed research
    research/sources/  # Bibliography
    notes/             # Working notes
    prompts/           # Research session prompts
    outline/           # Book outline
    drafts/            # HTML reading drafts
  grammars-of-the-living-world/
    chapters/          # 10 Grammars chapters + 3 Species chapters (source of truth)
    research/raw/      # 48 research files (research-01 through research-48 + 06a)
    research/synthesis/ # Processed research (TODO)
    research/sources/  # Bibliography (TODO)
    notes/             # Working notes + recommendations
    outline/           # Outlines + skeletons
    drafts/            # Thesis breakthrough + HTML drafts
  working-architecture/
    chapters/          # 12 markdown chapter drafts (source of truth)
    outline/           # Book outline
models/                # Python emergence models + generated charts
dashboard/             # Interactive Chart.js data visualizations
src/                   # mdbook staging area (generated by build.sh, gitignored except SUMMARY.md + index.md)
book/                  # mdbook output (gitignored, served by GitHub Pages)
mdbook-theme/          # Custom CSS for Substack-style typography
```

## Grammars Architecture (March 2026)

**Part I: The Body** — Ch 1 (Biological Hypothesis), Ch 2 (Why Stories)
**Part II: The Crisis** — Ch 3 (Stories Lose Homes), Ch 4 (Degradation of Hearth), Ch 5 (Polarization of Polis)
**Part III: The Grammars** — Ch 6 (Machines for Constructing Stories), Ch 7 (Survival and Capture)
**Part IV: The Fire** — Ch 8 (The Species That Got Fire) ← thesis chapter
**Part V: The Hinge** — Ch 9 (The Trap of Solving)
**Part VI: The Gesture** — Ch 10 (Grammars of the Living World)

**Epistemological posture (Linehan filter):** We cannot know if this is ultimately true. We know it is useful (testable predictions), it fits the data (neuroscience, ecology, cross-cultural research converge), and it is compassionate (doesn't require anyone to be wrong — just dysregulated in a dysregulating world).

## Writing Style

- Analytical but accessible. Think: a long-form New Yorker piece meets an equity research report.
- Concrete examples over abstractions. Name the companies, cite the numbers, tell the stories.
- Take all sides seriously before taking a position. The equity analyst instinct: who benefits from this narrative?
- Philosophical depth without jargon. Kelty, Ostrom, Akomolafe, Andreotti should be accessible to a reader who has never encountered them.
- Short paragraphs. No academic throat-clearing.
- **FOOTNOTE RULE (April 2026 reader feedback):** Academic infrastructure does NOT belong in body prose. Move the following to footnotes/endnotes every time:
  1. **Study details** — sample sizes, effect sizes (Cohen's d), replication dates, journal names, specific stats. The *finding* stays in prose; the *evidence apparatus* goes to a footnote.
  2. **Framework listings** — "Five frameworks walk into a tantric temple" pattern. When multiple scholars are listed in sequence to show the landscape of a debate, summarize the insight in prose and put the scholar-by-scholar breakdown in a footnote.
  3. **Epistemological disclaimers** — passages where the book pauses to caveat its own methodology ("The three-filter test governs this author's claims but not the traditions it examines..."). If the caveat is essential, keep ONE sentence; the full elaboration is a footnote.
  4. **Source attributions in prose** — "Ruth Feldman, who has spent decades measuring this at Bar-Ilan University" → prose just says "Ruth Feldman's research shows..." and the institutional/career context is a footnote.
  5. **Meta-commentary** — "This chapter will argue..." or "As established in Chapter 3..." — either cut entirely or condense to a single transitional phrase.
  The test: if a passage makes the reader feel like they're reading an academic paper instead of being carried by a story, it's a footnote.
- **Grammars book specifically**: more contemplative, poetic register than Freedom Paradox. Think: the rigor of an equity analyst who learned to sit with mystery. The book speaks — the author doesn't. No founder story, no personal brand. The argument stands on its own. CC BY-SA 4.0 licensed.
- **DEDUPLICATION RULE (April 2026 editorial audit):** Each piece of content has ONE owner book. Other books reference but never repeat. Owners:
  - Still-face experiment → Fire Ch1
  - Ostrom's eight principles → Fire Ch9
  - Sesame/Ghibli/Ghost models → Fire Ch9
  - Samudra Manthan retelling → Fire Ch1
  - San healing dance / Dagara grief → Working Architecture
  - Co-regulation as biological baseline (Feldman/Coan/Tronick) → Fire Ch1
  - Aboriginal firestick farming → Fire Ch1
  Other books say "as established in [Book Title]..." and move on. Never repeat a case study, experiment, or myth retelling across books.
- **Key distinction**: good/bad are moral categories (weaponizable). Adaptive/non-adaptive are empirical (observable on a long enough timescale). The book uses the adaptive frame throughout.
- **NO JUDGMENT ADJECTIVES FROM NARRATOR (April 2026 Kindle feedback):** The third-person narrator never evaluates. Remove: "compelling", "devastating", "brilliant", "extraordinary", "remarkable", "striking", "powerful", "profound", "radical" from narrator voice. These words are OK only in:
  - First-person Author's Note
  - Character's interior thoughts ("she found it compelling")
  - Direct quotes from named persons
  The narrator observes; the narrator does not evaluate. "Who says it's compelling? Let the reader decide."
- **NO ABSOLUTIST CLAIMS (April 2026 audit — 81 edits across 4 books):**
  - "the only" → "among the few" or scope to text ("the thinkers examined here")
  - "every tradition" → "the traditions examined in this book" or "tradition after tradition"
  - Unhedged superlatives → "arguably" or "among the most"
  - "nobody knows" → "we do not know"
  - Population claims ("many", "most", "few") → ground in text's own evidence or use generic singular
  - The "who counted?" test: if a reader would ask "how do you know it's many?", rewrite.
- **REALISTIC DOMESTIC DETAIL:** Bedtime at 8pm. Void/reflection arrives ~10pm. She wakes 6:30am, daughter 7-8am (meditation time before the day). No mother is routinely up at 2am. Ground times in real parenting rhythms.
- **THE AUTHOR'S BACKSTORY (for narrative chapters using "she"):**
  - Catholic upbringing, pro forma — parents attended out of cultural/community obligation, not faith. Grandfather attended for community standing. More cultural than spiritual.
  - The faith/ground question was never fully set aside. It took different forms: meditation, yoga, readings, drug use. The ONLY time it was truly incompatible was during years as investment banking analyst at Goldman Sachs. After leaving, the question returned.
  - The retreat was real. The tradition is real. But the book is not positioned as author's spiritual journey — let the character carry it.

## Pending Research Queue

There is a sequential research task file at `books/research-compendium/pending-research-tasks.md`. When starting a new session with available capacity, work through these tasks **one at a time, in order**. Each task is self-contained. Commit after each task. Work in small batches to avoid rate limits. The file contains 11 tasks across 4 tiers (thesis-critical → source refinement → cross-book integration).

## The Recursive Research Workflow

This project uses a three-tool loop:

### 1. Claude in Chrome (Deep Research)
- Focus on ONE chapter or sub-topic
- Search broadly, then drill into primary sources
- Save research output to `books/[book]/research/raw/[topic-slug].md`

### 2. Claude Code (Synthesis & Writing)
- Read raw research → synthesize into `research/synthesis/`
- Draft chapters in `chapters/`
- Maintain bibliography in `research/sources/bibliography.md`
- Edit and revise based on author's `<!-- PP: -->` comments

### 3. Author (Read, Comment, Direct)
```
<!-- PP: [comment here] -->
```

## Draft Preservation — CRITICAL RULE

**Never delete or overwrite existing content without preserving it first.**

- Before rewriting any chapter draft, copy the current version to `drafts/archive/` with a date suffix (e.g., `ch01-biological-hypothesis-2026-03-29.md`)
- Before restructuring the outline, copy the current version to `outline/` with a date suffix
- Before major edits to research files, preserve the original in the same directory with `-original` suffix
- **Only delete archived files when PlayfulProcess explicitly asks you to clean up**
- When in doubt, keep both versions. Disk is cheap; lost writing is not.
- The `drafts/archive/` directory is the "never touch without permission" zone

## Podcast Transcript Research — LOCAL ONLY

Podcast transcripts are copyrighted material used for research purposes. They follow strict local-only rules.

### What is NEVER committed
- The entire `transcripts/` directory (gitignored) — raw transcripts, indexes, queues, podcast lists, plans
- Any file containing substantial verbatim transcript text
- Any committed file referencing specific copyrighted episode content (no episode lists, no index files naming episodes)

### What IS committed
- Research output files: `books/[book]/research/raw/podcast-[slug].md` — these contain original analysis, synthesis, and brief attributed quotes only (under 15 words per quote)
- General workflow instructions in this CLAUDE.md (no episode-specific references)

### Storage
- All podcast material lives in `transcripts/Podcasts-library/[podcast-slug]/`
- Transcripts are downloaded via tapesearch.com subscription
- Each podcast gets its own subdirectory

### Three Processing Modes
1. **Additional Research** — supporting evidence, examples, and quotes that illuminate arguments in specific chapters
2. **Alternative Hypotheses** — genuinely different explanations for phenomena the books discuss
3. **Stress Testing** — strongest counterarguments to specific thesis statements

### Epistemological Posture for Processing
- Inclusive and compassionate — validate every human action as understandable
- Maintain a moral claim based on current knowledge of what is adaptive and what is not adaptive
- Not critical but understanding across all positions
- Apply the Linehan filter: useful, fits the data, compassionate
- Flag contradictions with `<!-- PP: PODCAST CONFLICT: [description] -->`

### Research Output Format
Research files follow the standard pattern with a `Serves:` header, source attribution, and sections organized by chapter relevance. Prefix: `podcast-[slug].md` to distinguish from numbered research files.

## Research File Numbering

42 research files exist as of March 2026 (research-01 through research-43, including 06a). New research files continue the sequence. Each research file tags which chapters it serves. The outline's Research Coverage Map (`book-outline-final-march-2026.md`) is the authoritative mapping.

## Important Constraints

- Never fabricate quotes. Flag as `[QUOTE NEEDED: topic, likely source]`
- Financial figures must have sources. Flag as `[VERIFY: figure, context]`
- When in doubt, add `[RESEARCH NEEDED: question]`
- For Grammars book: respect CARE Principles for Indigenous Data (Collective Benefit, Authority, Responsibility, Ethics) when discussing Ifá, Indigenous systems, etc.
