# PlayfulProcess — Books

Four open-source books. One architecture.

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
**First draft complete** · 12 chapters

A practical manual for building the containers. For parents, teachers, therapists — anyone who tells stories to anyone else.

## How They Connect

**The Freedom Paradox** is the diagnosis. **Grammars of the Living World** is the framework. **The Species That Tells Stories** is the narrative heart. **Working Architecture** is the practical manual. Each works alone; together they form the full architecture.

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
```

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
