# PlayfulProcess — Books

Twelve open-source books. One argument. The species got fire before it had the grammars to hold it.

**Read online: [books.recursive.eco](https://books.recursive.eco/)**
**Download EPUBs: [Latest Release](https://github.com/PlayfulProcess/freedom-paradox/releases/latest)**

---

## Featured Books

### The Freedom Paradox
**Publication-ready** · 17 chapters · ~67K words

Open source — a forty-year freedom movement — confronts genuine civilizational risk when applied to AI. The diagnosis: power without responsibility.

### Working Architecture
**Publication-ready** · 12 chapters · ~20K words

A practical manual for building the containers. For parents, teachers, therapists — anyone who tells stories to anyone else.

### The Axiom Beneath the Ground
**Publication-ready (v3)** · 7 chapters + The Ceremony · ~31K words

Alternating narrative and philosophy in the style of Kundera. A woman in the void between faith and atheism encounters Tillich, Linehan, and nondual Shaiva Tantra. The construction is the recognition becoming visible to itself.

### Fire Before Responsibility
**Main project — in progress** · 9 chapters · ~18K words (target ~50K)

Intelligence, AI, and the wisdom we need. Absorbs *The Species That Tells Stories* and *Grammars of the Living World*.

### The Campfire Stories
**Complete** · 5 books x 2 stories · with audio · [Separate repo](https://github.com/PlayfulProcess/campfire-stories)

Five-minute bedtime stories for ages 3-7 from world traditions.

## All Books

| Book | Status | Chapters | Words |
|------|--------|----------|-------|
| The Freedom Paradox | Publication-ready | 17 | ~67K |
| Working Architecture | Publication-ready | 12 | ~20K |
| The Axiom Beneath the Ground (v3) | Publication-ready | 7 + Ceremony | ~31K |
| Fire Before Responsibility | In progress | 9 | ~18K |
| The Real Cost of Lunch | Draft | 20 | ~46K |
| The Wise Heart (DBT + myths) | Card deck format | 35 | ~15K |
| The Repair Deck | Experimental | 17 | ~50K |
| Decolonization | Platform grammar | 54 cards | — |
| Social Working | Platform grammar | 107 cards | — |
| The Campfire Stories | Complete | 10 stories | ~9K |

## How to Use This Repo

### Read the books
- **Online**: [books.recursive.eco](https://books.recursive.eco/)
- **EPUB (Kindle, Apple Books, etc.)**: [Download from Releases](https://github.com/PlayfulProcess/freedom-paradox/releases/latest)

### Build locally
```bash
# Prerequisites: pandoc, mdbook (or use the bundled .mdbook-bin/)

# Build the website
bash build.sh

# Build all EPUBs
bash epub-build/build-all-epubs.sh

# Full publish: rebuild everything + create GitHub Release + push
bash publish.sh "Your commit message"
```

### Fork and adapt
All books are CC BY-SA 4.0. Fork the repo, edit the markdown in `books/*/chapters/`, rebuild. The grammars are yours to practice.

## Repository Structure

```
books/
  axiom-beneath-the-ground/chapters/v3/   # Axiom v3 (Kundera-style)
  freedom-paradox/chapters/                # 17 chapters
  working-architecture/chapters/           # 12 chapters
  fire-and-intelligence/chapters/          # 9 chapters (main project)
  consolidated/chapters/                   # Omnibus (42 chapters)
  ...
epub-build/
  build-single-epub.sh                     # Build one EPUB
  build-all-epubs.sh                       # Build all EPUBs
  per-book-metadata/                       # YAML metadata per book
docs/epubs/
  index.html                               # Landing page (books.recursive.eco)
models/                                    # Python emergence models + charts
publish.sh                                 # One-command full publish
build.sh                                   # Build mdbook site
CLAUDE.md                                  # Writing instructions for AI sessions
```

## Publishing Pipeline

```
bash publish.sh "commit message"
```

This single command:
1. Rebuilds all 14 EPUBs via pandoc
2. Rebuilds the mdbook site
3. Commits and pushes source changes
4. Creates a GitHub Release with all EPUBs attached
5. GitHub Pages auto-deploys the site

EPUBs are served from [GitHub Releases](https://github.com/PlayfulProcess/freedom-paradox/releases) (not tracked in git) to keep the repo lean.

## License

CC BY-SA 4.0 — Fork them, argue with them, build on them.

## Author

PlayfulProcess · [recursive.eco](https://recursive.eco) · [Substack](https://www.playfulprocess.com/)
