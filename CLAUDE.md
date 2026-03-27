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
**Status: Early draft + active research**
Contemplative and divinatory systems (I Ching, Ifá, Tarot, Kabbalah, astrology) as "grammars" — finite symbolic vocabularies that generate infinite meaning through combination and interpretation. Applies Kelty's recursive public framework to build a digital commons for these systems.
- Path: `books/grammars-of-the-living-world/`
- HTML draft of Part III (8 chapters) exists in `drafts/`
- Deep research ongoing (Akomolafe, Andreotti, decolonial theory, etc.)
- The platform described in this book IS recursive.eco (see Domain Note above)

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
    chapters/          # Markdown chapter drafts (TODO)
    research/raw/      # Deep research dumps
    research/synthesis/ # Processed research
    research/sources/  # Bibliography
    notes/             # Working notes
    outline/           # Book outline (TODO)
    drafts/            # HTML drafts (Part III exists)
```

## Writing Style

- Analytical but accessible. Think: a long-form New Yorker piece meets an equity research report.
- Concrete examples over abstractions. Name the companies, cite the numbers, tell the stories.
- Take all sides seriously before taking a position. The equity analyst instinct: who benefits from this narrative?
- Philosophical depth without jargon. Kelty, Ostrom, Akomolafe, Andreotti should be accessible to a reader who has never encountered them.
- Short paragraphs. No academic throat-clearing.
- **Grammars book specifically**: more contemplative, poetic register than Freedom Paradox. Think: the rigor of an equity analyst who learned to sit with mystery. CC BY-SA 4.0 licensed.

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
