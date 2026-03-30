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
**Status: Complete first draft**
Open source — a forty-year freedom movement — confronts genuine civilizational risk when applied to AI. 16 chapters + epilogue, ~85K words. All research and drafting done.
- Path: `books/freedom-paradox/`

### Book 2: Grammars of the Living World
**Status: Final outline complete, research organized (42 files), drafting Phase 1**
Human civilization has been acquiring power faster than it can build the communal practices to wield it responsibly. Grammars — finite symbolic systems maintained through shared practice — are responsibility structures: the cultural technology through which communities constrain their own power, align with the direction life moves in, and maintain the ratio between capacity and obligation. 6 parts, 10 chapters, ~55K–65K words. CC BY-SA 4.0.
- Path: `books/grammars-of-the-living-world/`
- Final outline: `outline/book-outline-final-march-2026.md`
- Thesis breakthrough: `drafts/thesis-breakthrough-march-2026.md`
- 42 research files in `research/raw/` (research-01 through research-41 + 06a)
- HTML draft of old Part III exists in `drafts/` (will be adapted)
- Recursive.eco is framed as **responsibility infrastructure**, not a contemplative technology platform

### How the Two Books Connect
The Freedom Paradox is the diagnosis (power without responsibility in the open-source/AI context). Grammars of the Living World is the response (what responsibility structures are, where they came from, why we keep dismantling them, and whether we can build new ones fast enough). A shared preface will frame both books. Each works alone; together they form the full architecture.

## Repository Structure

```
books/
  freedom-paradox/
    chapters/          # Markdown chapter drafts
    research/raw/      # Deep research dumps
    research/synthesis/ # Processed research
    research/sources/  # Bibliography
    notes/             # Working notes
    prompts/           # Research session prompts
    outline/           # Book outline
    drafts/            # HTML reading drafts
  grammars-of-the-living-world/
    chapters/          # Markdown chapter drafts
    research/raw/      # 42 deep research files (research-01 through research-41 + 06a)
    research/synthesis/ # Processed research (TODO)
    research/sources/  # Bibliography (TODO)
    notes/             # Working notes + recommendations
    outline/           # Final outline (6 parts, 10 chapters — March 2026)
    drafts/            # Thesis breakthrough + HTML drafts (old Part III)
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

## Important Constraints

- Never fabricate quotes. Flag as `[QUOTE NEEDED: topic, likely source]`
- Financial figures must have sources. Flag as `[VERIFY: figure, context]`
- When in doubt, add `[RESEARCH NEEDED: question]`
- For Grammars book: respect CARE Principles for Indigenous Data (Collective Benefit, Authority, Responsibility, Ethics) when discussing Ifá, Indigenous systems, etc.
