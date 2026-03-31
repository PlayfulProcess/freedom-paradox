# CLAUDE.md — Instructions for Claude Code

## PRIVACY — CRITICAL RULE

**The author publishes under the name PlayfulProcess. Never use any real/personal names for the author anywhere in this repository — not in files, commit messages, comments, or metadata. This applies to all past, present, and future content. If you encounter a real name in existing files, replace it with PlayfulProcess.**

This is a safety and identity boundary. Do not ask about it or reference it further.

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

### Adding a new chapter
1. Write the chapter in `books/[book]/chapters/ch##-slug.md`
2. Add a line to `src/SUMMARY.md` pointing to the staged path
3. Add a `cp` line to `build.sh`
4. Run `bash build.sh`

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
- **Grammars book specifically**: more contemplative, poetic register than Freedom Paradox. Think: the rigor of an equity analyst who learned to sit with mystery. The book speaks — the author doesn't. No founder story, no personal brand. The argument stands on its own. CC BY-SA 4.0 licensed.
- **Key distinction**: good/bad are moral categories (weaponizable). Adaptive/non-adaptive are empirical (observable on a long enough timescale). The book uses the adaptive frame throughout.

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

## Research File Numbering

42 research files exist as of March 2026 (research-01 through research-43, including 06a). New research files continue the sequence. Each research file tags which chapters it serves. The outline's Research Coverage Map (`book-outline-final-march-2026.md`) is the authoritative mapping.

## Important Constraints

- Never fabricate quotes. Flag as `[QUOTE NEEDED: topic, likely source]`
- Financial figures must have sources. Flag as `[VERIFY: figure, context]`
- When in doubt, add `[RESEARCH NEEDED: question]`
- For Grammars book: respect CARE Principles for Indigenous Data (Collective Benefit, Authority, Responsibility, Ethics) when discussing Ifá, Indigenous systems, etc.
