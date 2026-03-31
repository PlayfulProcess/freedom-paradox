# PlayfulProcess — Books

Five open-source books. One architecture.

**Read online: [books.recursive.eco](https://books.recursive.eco/)**

---

## The Books

### 1. The Freedom Paradox
**Complete first draft** · 16 chapters · ~85K words

Open source — a forty-year freedom movement — confronts genuine civilizational risk when applied to AI. The diagnosis: power without responsibility.

### 2. Grammars of the Living World
**First draft complete** · 10 chapters · ~21K words

What responsibility structures are, where they came from, and why we keep dismantling them. The theoretical response.

### 3. The Species That Tells Stories
**Draft in progress** · 3 of 7 chapters · ~20K words

We are the species that tells stories to its children. Love is the container. The container is disappearing.

### 4. Working Architecture
**First draft complete** · 12 chapters · ~20K words

A practical manual for building the containers. For parents, teachers, therapists — anyone who tells stories to anyone else.

### 5. The Campfire Stories
**Complete** · 5 books × 2 stories · ~9K words · [**Separate repo →**](https://github.com/PlayfulProcess/campfire-stories)

Five-minute bedtime stories for ages 3–7, built from cross-cultural story arcs. Each book pairs two stories from different traditions (Akan, Jātaka, Aboriginal Australian, Haudenosaunee, Japanese, 1001 Nights, European folk) around a shared developmental theme.

**How it was made:** The entire Campfire Stories book — 10 stories, CLAUDE.md, grammar.json, README — was written using [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) in **two prompts**. The first set up the project (voice, methodology, structure, first two stories). The second wrote the remaining eight stories. The methodology is described in [Vibe Writing 102](docs/vibe-writing-102.md). Fork the repo and try it yourself.

## How They Connect

**The Freedom Paradox** is the diagnosis. **Grammars of the Living World** is the framework. **The Species That Tells Stories** is the narrative heart. **Working Architecture** is the practical manual. **The Campfire Stories** is the proof of concept — stories built using the three-filter test, for actual children, in actual bedtimes. Each works alone; together they form the full architecture.

## Repository Structure

```
books/
  freedom-paradox/chapters/          # 16 chapters (source of truth)
  grammars-of-the-living-world/
    chapters/                         # 10 Grammars + 3 Species chapters
    research/raw/                     # 48 research files
    prompts/                          # Chrome deep research prompts
    outline/                          # Outlines + skeletons
  working-architecture/chapters/     # 12 chapters
models/                               # Python emergence models + charts
dashboard/                            # Interactive data visualizations
docs/                                 # Vibe Writing 102 course
```

*The Campfire Stories lives in its own repo: [PlayfulProcess/campfire-stories](https://github.com/PlayfulProcess/campfire-stories)*

## Publishing

The site at [books.recursive.eco](https://books.recursive.eco/) is built with [mdbook](https://rust-lang.github.io/mdBook/) and deployed via GitHub Pages.

```bash
bash build.sh    # Syncs chapters → builds static site
```

Every push to `master` automatically rebuilds and deploys via GitHub Actions.

## Writing Workflow

See `CLAUDE.md` for the full recursive research-and-writing workflow using Claude Code and Claude in Chrome.

## License

CC BY-SA 4.0

## Author

PlayfulProcess · [recursive.eco](https://recursive.eco)
