# CLAUDE.md — Instructions for Claude Code

## PRIVACY — CRITICAL RULE

**The author publishes under the name PlayfulProcess. Never use any real/personal names for the author anywhere in this repository — not in files, commit messages, comments, or metadata. This applies to all past, present, and future content. If you encounter a real name in existing files, replace it with PlayfulProcess.**

This is a safety and identity boundary. Do not ask about it or reference it further.

## Project Context

This is a book project: "The Freedom Paradox: Open Source, AI, and the Limits of Openness" by PlayfulProcess. The author is a former Goldman Sachs equity research analyst, current MSW student, and builder on open-source tools. The book examines how open source — a forty-year freedom movement — confronts genuine civilizational risk when applied to AI.

## Repository Conventions

- All chapter drafts are markdown files in `chapters/`
- Research goes in `research/raw/` (dumps) → `research/synthesis/` (processed)
- Source tracking in `research/sources/bibliography.md`
- Working notes and fragments in `notes/`
- Prompts for research sessions saved in `prompts/`

## Writing Style

- Analytical but accessible. Think: a long-form New Yorker piece meets an equity research report.
- Concrete examples over abstractions. Name the companies, cite the numbers, tell the stories.
- Take all sides seriously before taking a position. The equity analyst instinct: who benefits from this narrative?
- Philosophical depth without jargon. Kelty, Ostrom, Tillich should be accessible to a reader who has never encountered them.
- Short paragraphs. No academic throat-clearing.

## The Recursive Research Workflow

This project uses a three-tool loop:

### 1. Claude in Chrome (Deep Research)
Use Claude in Chrome to conduct deep research sessions on specific topics. Each session should:
- Focus on ONE chapter or sub-topic
- Search broadly, then drill into primary sources
- Save research output to `research/raw/[topic-slug].md`

### 2. Claude Code (Synthesis & Writing)
Use Claude Code to:
- Read raw research and synthesize into chapter-ready summaries in `research/synthesis/`
- Draft chapters based on outline + synthesized research
- Maintain the bibliography in `research/sources/bibliography.md`
- Edit and revise based on the author's comments
- Run structural checks (chapter length balance, narrative flow, cross-references)

### 3. Author (Read, Comment, Direct)
The author reads drafts and adds comments directly in the markdown files using this format:
```
<!-- PP: [comment here] -->
```
Claude Code should look for these comments and address them in the next revision.

## Research Session Prompts

Store reusable prompts in `prompts/`. Each prompt should be a markdown file that can be copy-pasted into Claude in Chrome for a deep research session.

### Prompt Template

```markdown
# Research Session: [Topic]

## Context
This is research for Chapter [N] of "The Freedom Paradox," a book about open source confronting AI risk.

## What I Need
- [Specific questions]
- [Specific data points]
- [Specific sources to find]

## Depth Required
- Primary sources preferred (company blogs, SEC filings, academic papers, interviews)
- Named individuals and specific dates
- Financial data where relevant (valuations, revenue, market share)
- Direct quotes from key figures

## Output Format
Structure the research as:
1. Key findings (bullet points)
2. Narrative summary (2-3 paragraphs)
3. Key quotes (with attribution and date)
4. Sources (URLs, publication dates)
5. Open questions for further research
```

## Chapter Drafting Process

For each chapter:

1. **Research phase**: The author runs 2-3 deep research sessions in Claude in Chrome using prompts from `prompts/`
2. **Synthesis**: Claude Code reads raw research, synthesizes into `research/synthesis/ch[N]-[topic].md`
3. **First draft**: Claude Code writes chapter draft in `chapters/ch[N]-[topic].md` based on outline + synthesis
4. **Review**: The author reads and adds `<!-- PP: -->` comments
5. **Revision**: Claude Code addresses comments, revises
6. **Repeat** steps 4-5 until the author is satisfied

## Key Commands for Claude Code

```bash
# See current state of all chapters
ls -la chapters/

# Check word counts across all chapters  
wc -w chapters/*.md

# Find all of the author's unresolved comments
grep -rn "<!-- PP:" chapters/

# Generate bibliography from all synthesis files
grep -rh "http" research/synthesis/ | sort -u > research/sources/urls.txt
```

## Important Constraints

- Never fabricate quotes. If a quote is needed, flag it as `[QUOTE NEEDED: topic, likely source]`
- Financial figures must have sources. Flag unsourced numbers as `[VERIFY: figure, context]`
- When in doubt about a claim, add `[RESEARCH NEEDED: question]`
- Maintain a running list of interview candidates in `notes/interviews-wanted.md`
