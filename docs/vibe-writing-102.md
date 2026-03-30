---
id: vibe-writing-102
title: "Vibe Writing 102: Write Open-Source Books with Claude Code"
description: "Use Claude Code, Claude in Chrome, and GitHub to research, write, and publish an open-source book. From question to published commons contribution. No coding experience required — just a question you care about."
duration: 120
author: PlayfulProcess
date: 2026-03-30
---

# Vibe Writing 102: Write Open-Source Books with Claude Code

**In Vibe Writing 101, we created magic stories for our kids using Claude and ChatGPT. Now we go deeper: using Claude Code and GitHub to research, write, and publish a book that belongs to the commons — forkable, improvable, and free forever.**

## What You'll Create Today

A published open-source book (or study, or story collection) that:
- Lives on GitHub under a Creative Commons license
- Was researched using Claude in Chrome (deep research) and written with Claude Code
- Follows a methodology you define (your filter for what's true and good)
- Is published as a beautiful reading site via mdbook + GitHub Pages
- Can be forked, improved, and built upon by anyone
- Optionally imports into recursive.eco as a grammar for reading, printing, or sharing

### See it in action:

- **[books.recursive.eco](https://books.recursive.eco/)** — Four books built using this exact workflow, published via mdbook + GitHub Pages
- [The Freedom Paradox](https://github.com/PlayfulProcess/freedom-paradox) — The repository powering the site above
- [The Campfire Stories](https://github.com/PlayfulProcess/campfire-stories) — Five-minute bedtime stories built from cross-cultural story arcs

### By the end of this workshop, you'll have:

- A GitHub repository with your book's first chapter published
- A CLAUDE.md file that teaches AI your voice and methodology
- A three-tool research-and-writing workflow you can repeat for any project
- A published reading site at `your-username.github.io/your-book`
- Understanding of how Claude Code manages multi-step creative projects

---

## Prerequisites (10m)

### Required

1. **GitHub account** — [github.com](https://github.com/) (free)
2. **Claude Code** — [Install guide](https://docs.anthropic.com/en/docs/claude-code/overview)
   - The command-line version of Claude that reads/writes files and runs scripts
3. **Git** — [git-scm.com](https://git-scm.com/)

### Recommended

4. **Claude in Chrome** — The browser extension for deep research
   - This is your research engine. Claude Code writes; Claude in Chrome researches.

### Optional

- **Node.js 18+** — Only needed if you want to generate a grammar.json for recursive.eco
- **A topic you care about** — Come with a question, or we'll find one together

### Verify your setup

Open a terminal and check:

```bash
git --version     # Any recent version
claude --version  # Claude Code CLI
```

### Don't have Claude Code?

You can follow along using [claude.ai](https://claude.ai) in the browser. You won't get file creation and git integration, but you can generate all the content and manually create files. The course notes where the two paths diverge.

---

## The Three-Tool Loop

This is the workflow that produced four books and 41 chapters. It's simple:

### 1. Claude in Chrome → Deep Research
Open Chrome with the Claude extension. Focus on ONE chapter or sub-topic. Search broadly, then drill into primary sources. Save the research output to `research/raw/topic-slug.md`.

**Why Chrome and not Claude Code?** Claude in Chrome can browse the web deeply — following links, reading papers, cross-referencing sources. Claude Code can do web searches but is optimized for file operations and writing. Use the right tool for the right job.

**Example research prompt** (paste into Claude in Chrome):
```
Research the following for a book chapter on [your topic]:
- Key scholarly sources and their specific findings
- The strongest counterargument to the main claim
- Cross-cultural perspectives (not just Western/English-language)
- Concrete examples, data points, and named individuals
- Save everything with author names, dates, and specific quotes I can verify
```

### 2. Claude Code → Synthesis & Writing
Claude Code reads the raw research, synthesizes it, and drafts chapters. It follows the voice and methodology in your CLAUDE.md. It manages files, commits to git, and handles the technical plumbing.

### 3. You → Read, Comment, Direct
You read the drafts. You leave comments using `<!-- PP: your comment -->` markers. You make the creative decisions. You apply the methodology. Claude Code responds to your comments on the next pass.

**The loop repeats:** research a topic → write a chapter → review → revise → research the next topic → write the next chapter.

---

## Section 1: Explore an Existing Book Project (15m)

### Step 1: Read the example (5m)

Open [books.recursive.eco](https://books.recursive.eco/) in your browser. This is a four-book reading site built using the exact method you're about to learn.

Then look at the repo: [github.com/PlayfulProcess/freedom-paradox](https://github.com/PlayfulProcess/freedom-paradox)

Notice the structure:
- **CLAUDE.md** — The "brain" of the project. Voice, methodology, rules, workflow.
- **books/*/chapters/** — The actual chapters, written in markdown (source of truth).
- **src/SUMMARY.md** — The table of contents that mdbook uses for the sidebar.
- **models/** — Python computational models that generated charts for the books.
- **build.sh** — One command to rebuild the site.
- **.github/workflows/** — Automatic deployment on every push.

### Step 2: Clone and explore with Claude Code (5m)

```bash
git clone https://github.com/PlayfulProcess/freedom-paradox.git
cd freedom-paradox
claude
```

Claude Code reads the CLAUDE.md automatically. Try asking it:

> What is this project about? How many books are there?

> What's the three-filter test? How does it apply to the Grammars book?

> Show me how Chapter 1 of The Species That Tells Stories uses the exposure therapy framework.

Notice how Claude Code already "knows" the project because CLAUDE.md taught it. That file is the most important thing you'll create today.

### Step 3: Make a small contribution (5m)

Try asking Claude Code:

> The [RESEARCH NEEDED] flag in Chapter 2 of Species That Tells Stories needs a source for the Grimms' edition-by-edition changes. Search for "Zipes Brothers Grimm seven editions" and fill it in.

Or:

> Add a `<!-- PP: This section needs a concrete opening scene -->` comment to any chapter that starts too abstractly.

Commit your change:

```bash
git add .
git commit -m "Fill research gap in Ch 2"
```

You just made your first contribution to an open-source book.

---

## Section 2: Set Up Your Own Book Project (25m)

### Step 1: Start Claude Code with the setup prompt (5m)

Open a new terminal, create a directory, and start Claude Code:

```bash
mkdir my-book-project
cd my-book-project
claude
```

Paste this prompt:

> I want to set up an open-source writing project. Before you create anything, ask me these questions one at a time:
>
> 1. What's the book about? (1-2 sentences)
> 2. Who is it for? (audience)
> 3. What's my voice? (formal/casual, first person/third, any authors I want to sound like)
> 4. What methodology or filter do I use to decide what's true, good, or worth including?
> 5. Do I have any existing repos with research or source material you should read?
>
> After I answer, create:
> - A CLAUDE.md with my voice and methodology
> - A README.md with project description and CC-BY-SA-4.0 license
> - A chapters/ directory
> - A research/raw/ directory for deep research dumps
> - A prompts/ directory for research session prompts
> - A .gitignore
> - Initialize git
> - A book skeleton (outline) based on my answers
> - Research prompts for each chapter (saved to prompts/) — these are what I'll paste into Claude in Chrome for deep research
>
> Don't write any content until you understand what I want. Start by asking question 1.

### Step 2: Answer Claude's questions (10m)

Claude Code will ask you each question in turn. Answer honestly. Take your time. The quality of these answers determines the quality of everything that follows.

**If you don't have a topic yet, here are starter ideas:**

- "A parent's guide to bedtime stories from around the world"
- "What the research says about screen time — a 30-minute read for busy parents"
- "Five things I learned about [your profession] that I wish someone told me"
- "A collection of wisdom from my grandmother, organized by theme"
- "What my neighborhood's history tells us about how cities change"

**For the methodology question (#4), some options:**

- The Three-Filter Test: "Is it useful? Does it fit the data? Is it compassionate?"
- The Fred Rogers Test: "Does this make the reader feel loved, capable, and curious?"
- The Wikipedia Standard: "Is this verifiable, neutral, and well-sourced?"
- Your own: describe how you personally decide what's true and worth sharing

### Step 3: Review what Claude Code created (5m)

Claude Code will generate your CLAUDE.md, README, skeleton, and research prompts. Read them carefully.

**Check the CLAUDE.md:**
- Does the voice description sound like you?
- Is the methodology clear enough that a stranger (or an AI) could follow it?
- Are there any rules you want to add?

**Check the research prompts:**
- Does each prompt ask for the right sources and evidence?
- Are there perspectives missing? (Non-Western? Counter-arguments?)

Ask Claude Code to revise:

> The voice is too formal. Make it warmer, like I'm talking to a friend over coffee.

> Add a chapter between 2 and 3 about [topic]. Remove chapter 5, it's not essential.

> My methodology should also include: "Does this honor the source tradition without extracting from it?"

### Step 4: Push to GitHub (5m)

```bash
git add .
git commit -m "Initial project setup with CLAUDE.md and skeleton"
```

Create a new repository on GitHub:

1. Go to [github.com/new](https://github.com/new)
2. Name it (e.g., `my-book-project`)
3. Set to **Public**
4. Don't add a README (you already have one)
5. Follow the instructions to push:

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-book-project.git
git branch -M main
git push -u origin main
```

Your book project is now live on the internet. Open source. Forkable. Real.

---

## Section 3: Research and Write Your First Chapter (30m)

### Step 1: Deep research with Claude in Chrome (10m)

Open the research prompt for Chapter 1 (saved in `prompts/ch01-*.md`). Paste it into Claude in Chrome.

Claude in Chrome will search the web, follow links, read papers, and compile findings. When it's done, save the output:

> Save this research to a file. I'll paste it into my project.

Copy the output and ask Claude Code:

> Save this research to research/raw/ch01-research.md

**Tips for better research:**
- Be specific: "Find peer-reviewed sources, not blog posts. I need author names, publication years, and specific findings."
- Ask for counter-arguments: "What's the strongest case against my thesis?"
- Ask for diversity: "Are there non-Western perspectives on this?"
- Ask for data: "I need specific numbers, dates, and named individuals — not vague claims."

### Step 2: Write the first draft with Claude Code (15m)

> Read research/raw/ch01-research.md. Write a first draft of Chapter 1 based on this research. Follow the voice and methodology in CLAUDE.md. Aim for [your target word count — 2,000 words is a good start]. Save to chapters/ch01-[chapter-name].md.

Let Claude Code write. Then read the draft. This is where your judgment matters most.

**Questions to ask yourself:**
- Does this sound like me, or like AI?
- Does every claim pass my methodology filter?
- Would I read this aloud to my intended audience without cringing?
- Are the sources real? Can I verify them?

**Red flags to watch for:**
- Vague attributions ("studies show," "experts say") — demand specifics
- AI voice tics ("delve," "landscape," "tapestry," "multifaceted") — kill them
- Claims without sources — flag with `[RESEARCH NEEDED: question]`
- Fabricated quotes — flag with `[QUOTE NEEDED: topic, likely source]`

### Step 3: Revise with Claude Code (5m)

> The opening paragraph is too abstract. Start with a concrete scene or story instead.

> Paragraph 3 makes a claim without evidence. Either find a source or remove it.

> The ending feels rushed. Can you expand the last section and close with a question rather than an answer?

> Read the whole chapter aloud to yourself (silently). Flag any sentence that feels clunky when spoken.

Each revision, Claude Code updates the file in place. You can always see the diff:

```bash
git diff
```

When you're satisfied:

```bash
git add .
git commit -m "First draft of Chapter 1"
git push
```

---

## Section 4: Publish as a Reading Site (15m)

### Step 1: Set up mdbook (5m)

Ask Claude Code:

> Set up mdbook for this project. I want a beautiful reading site with Substack-style typography deployed via GitHub Pages. Create the book.toml, src/SUMMARY.md, a custom CSS theme, a build.sh script, and a GitHub Actions workflow that auto-deploys on every push to main. Follow the pattern used in github.com/PlayfulProcess/freedom-paradox.

Claude Code will create:
- `book.toml` — mdbook configuration
- `src/SUMMARY.md` — table of contents (sidebar navigation)
- `src/index.md` — landing page
- `mdbook-theme/substack.css` — custom typography
- `build.sh` — build script
- `.github/workflows/deploy-book.yml` — auto-deploy on push

### Step 2: Build and preview locally (3m)

```bash
bash build.sh
# Open book/index.html in your browser
```

You should see your book with:
- Sidebar navigation
- Dark mode toggle
- Full-text search (press `s`)
- Substack-style typography

### Step 3: Enable GitHub Pages (3m)

Push to GitHub and the Actions workflow will deploy automatically:

```bash
git add .
git commit -m "Add mdbook publishing pipeline"
git push
```

Your book is now readable at `https://YOUR-USERNAME.github.io/my-book-project/`

**Want a custom domain?** Add a `CNAME` file with your domain name and configure DNS.

### Step 4: (Optional) Create a grammar for recursive.eco (4m)

If you want your book on recursive.eco alongside tarot decks, I Ching translations, and kids' stories:

> Read the grammar format at https://github.com/PlayfulProcess/recursive.eco-schemas. Convert my book into a grammar.json where each chapter is an item. Use grammar_type "custom". Include _grammar_commons with CC-BY-SA-4.0 license and my name. Save as grammar.json.

You can then import this into [the Grammar Studio](https://flow.recursive.eco/create) and publish to the Library.

---

## The Full Session (What It Actually Looks Like)

Here's the real workflow that produced [books.recursive.eco](https://books.recursive.eco/):

```
# 1. Claude in Chrome: deep research
[Paste research prompt for Ch 1 into Claude in Chrome]
[Claude searches web, reads papers, compiles 5,000-word research dump]
[Save to research/raw/ch01-research.md]

# 2. Claude Code: synthesis and writing
You: Read the research in research/raw/ch01-research.md and write Chapter 1.
     Follow CLAUDE.md voice and methodology. ~6,000 words.

Claude Code: [Writes chapter, flags [RESEARCH NEEDED] where evidence is thin,
             flags [QUOTE NEEDED] where attribution is missing]

# 3. You: review and direct
You: The opening is too abstract. Start with the scene on the couch.
     The Coan study needs the exact sample size.
     The section on Tronick is too long — cut to the key finding.

Claude Code: [Revises, preserving original in drafts/archive/]

# 4. Repeat for next chapter
You: Now read the research prompt for Ch 2 — I'll go research it in Chrome.

# 5. When ready to publish
You: Set up mdbook and deploy to GitHub Pages.

Claude Code: [Creates build pipeline, commits, pushes, site goes live]
```

The key insight: **Claude in Chrome researches, Claude Code writes, you direct.** Each tool does what it's best at. The CLAUDE.md is the thread that holds them together.

---

## Troubleshooting

**Claude Code doesn't understand my voice**
- Be more specific in CLAUDE.md. Instead of "warm," try: "Short sentences. Concrete images. No jargon. Read everything aloud — if it stumbles, rewrite it."
- Paste an example paragraph you've written and say: "This is my voice. Match it."

**The research is too shallow**
- Use Claude in Chrome for deep research, not Claude Code's built-in web search
- Be more specific in your research prompts: "Find peer-reviewed sources, not blog posts. I need author names, publication years, and specific findings."
- Ask for primary sources: "Don't summarize — give me the actual data, the actual quotes, the actual study designs."

**The writing sounds like AI, not me**
- Add to CLAUDE.md: "Never use: 'delve,' 'landscape,' 'tapestry,' 'multifaceted,' 'it's important to note.' Never start paragraphs with 'In the...' or 'When it comes to...'"
- After each draft, ask: "Read this draft and flag every sentence that sounds like AI wrote it. Rewrite those sentences in a more natural voice."

**Git is confusing**
- You only need four commands: `git add .`, `git commit -m "message"`, `git push`, `git pull`
- If things get messy: `git stash` saves your changes, `git stash pop` brings them back
- Ask Claude Code: "Help me fix my git situation" — it can see the state and advise

**mdbook won't build**
- Check that `src/SUMMARY.md` points to files that actually exist
- Run `build.sh` and read the error — it's usually a missing file
- Ask Claude Code: "The mdbook build failed. Read the error and fix it."

**GitHub Pages shows 404**
- Check Settings → Pages → make sure it's set to "GitHub Actions" not "Deploy from branch"
- The workflow file must be on the `main` or `master` branch
- Wait 30 seconds after push — deployment takes a moment

**I don't know what to write about**
- Start with what you already know. What do people ask you about?
- Start with what you're curious about. What would you research if you had infinite time?
- Start with what your kids need. What story doesn't exist yet that should?

---

## What's Next?

Once you've published your first chapter:

- **Keep writing** — Use the three-tool loop for each chapter. Research in Chrome, write in Claude Code, review yourself.
- **Add visualizations** — If your book uses data, write Python scripts to generate charts. Store in `models/`, output PNGs that mdbook embeds.
- **Invite collaborators** — Others can fork your repo and submit pull requests with improvements.
- **Print it** — If on recursive.eco, use the Print viewer to make booklets, card sheets, or storyboards.
- **Teach it** — Run this workshop for your own community. The course itself is open source.
- **Connect** — Share in the [Library](https://flow.recursive.eco/library) so others can find your work.

The loop continues: research, write, share, repeat. Every book makes the commons richer.

---

## Weaving Stories and Songs

If you've taken [Vibe Writing 101: Magic Stories for Kids](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=magic-stories-for-kids), you can combine personal family stories with your open-source book:

- **Personal stories stay personal** — Magic Stories for Kids produces private family treasures
- **Commons stories go public** — Vibe Writing 102 produces open contributions
- **Both use the same methodology** — the three-filter test works for private bedtime stories and public book chapters alike

If you've taken [Meaningful Songs for Your Family](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=meaningful-songs-for-family), you can add Suno-generated songs as companion audio for your book chapters.

---

## Resources

- **[books.recursive.eco](https://books.recursive.eco/)** — The published books built with this workflow
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/overview) — Installation and usage
- [Claude in Chrome](https://chromewebstore.google.com/detail/claude/cjgbgcaaakmmnnkbaaaeecfkphcoefoo) — Deep research in the browser
- [mdbook](https://rust-lang.github.io/mdBook/) — The static site generator for books
- [GitHub Pages](https://pages.github.com/) — Free website hosting from your repo
- [Recursive.eco schemas](https://github.com/PlayfulProcess/recursive.eco-schemas) — Grammar format for publishing to the library
- [Creative Commons CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) — The license that makes the commons work
- [Vibe Writing 101: Magic Stories for Kids](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=magic-stories-for-kids) — The personal stories course
- [Vibe Coding 101](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=vibe-coding-101) — Build AI tools (no coding required)
- [Vibe Coding 102](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=vibe-coding-102) — Create audiobooks with Claude Code
