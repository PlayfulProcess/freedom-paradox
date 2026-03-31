---
id: vibe-writing-102
title: "Vibe Writing 102: Write Open-Source Books with Claude Code"
description: "Use Claude Code Desktop to research, write, and publish an open-source book — autonomously. Claude navigates Chrome for deep research, writes chapters, builds the site, and pushes to GitHub. You direct. No coding experience required."
duration: 120
author: PlayfulProcess
date: 2026-03-30
---

# Vibe Writing 102: Write Open-Source Books with Claude Code

**In Vibe Writing 101, we created magic stories for our kids using Claude and ChatGPT. Now we go deeper: using Claude Code Desktop to research, write, and publish a book that belongs to the commons — forkable, improvable, and free forever.**

**What's different here:** Claude Code Desktop can open Chrome, navigate to sources, read web pages, search scholarly databases, and compile research — all autonomously. You don't copy-paste between tools. You tell Claude what to research, it opens Chrome, does the work, saves the findings, then writes the chapter. One conversation. One tool. One loop.

## What You'll Create Today

A published open-source book (or study, or story collection) that:
- Lives on GitHub under a Creative Commons license
- Was researched autonomously by Claude navigating Chrome for primary sources
- Was written by Claude Code following your voice and methodology
- Is published as a beautiful reading site via mdbook + GitHub Pages
- Can be forked, improved, and built upon by anyone
- Optionally imports into recursive.eco as a grammar for reading, printing, or sharing

### See it in action:

- **[books.recursive.eco](https://books.recursive.eco/)** — Five books + a research compendium built using this exact workflow
- [The Freedom Paradox repo](https://github.com/PlayfulProcess/freedom-paradox) — The repository powering the site above
- [The Campfire Stories](https://github.com/PlayfulProcess/campfire-stories) — Bedtime stories written in two prompts using this method

### By the end of this workshop, you'll have:

- A GitHub repository with your book's first chapter published
- A CLAUDE.md file that teaches AI your voice and methodology
- An autonomous research-and-writing workflow you can repeat for any project
- A published reading site at `your-username.github.io/your-book`

---

## Prerequisites (10m)

### Required

1. **GitHub account** — [github.com](https://github.com/) (free)
2. **Claude Code Desktop** — [Install guide](https://docs.anthropic.com/en/docs/claude-code/overview)
   - Must have **Claude in Chrome** MCP connected — this is how Claude opens and reads web pages
   - Verify: in Claude Code, the Chrome tools should appear (navigate, read_page, get_page_text, etc.)
3. **Git** — [git-scm.com](https://git-scm.com/)

### Optional

- **Node.js 18+** — Only needed for grammar.json generation
- **A topic you care about** — Come with a question, or we'll find one together

### Verify your setup

Open a terminal and check:

```bash
git --version     # Any recent version
claude --version  # Claude Code CLI
```

Then start Claude Code and ask:

> Can you open Chrome and navigate to google.com?

If Claude opens a Chrome tab and navigates, you're ready. If not, you need to connect the Claude in Chrome MCP server.

### Don't have Claude Code Desktop?

You can follow along using [claude.ai](https://claude.ai) in the browser. You won't get autonomous Chrome research or file creation, but you can generate all the content and manually create files. The course notes where the paths diverge.

---

## How It Works: The Autonomous Loop

This is the workflow that produced five books, 48 research files, and 41 chapters:

```
You: "Research [topic] for Chapter 1. Open Chrome, search for scholarly
      sources, read the papers, compile findings with citations."

Claude: [Opens Chrome tab]
        [Searches Google Scholar, JSTOR, specific author pages]
        [Reads each page, extracts key findings]
        [Saves to research/raw/ch01-research.md with full citations]

Claude: "Research complete. I found 12 sources. Key findings: ..."
        "Ready to write the chapter?"

You: "Yes. Follow CLAUDE.md voice. ~4,000 words. Open with a scene."

Claude: [Reads research file + CLAUDE.md]
        [Writes chapter to chapters/ch01-topic.md]
        [Flags [RESEARCH NEEDED] where evidence is thin]
        [Flags [QUOTE NEEDED] where attribution is missing]

You: "The opening is too abstract. The Coan study needs the sample size.
      Cut the Tronick section to just the key finding."

Claude: [Revises in place, preserves original in drafts/archive/]

You: "Good. Commit and push. Then start researching Chapter 2."

Claude: [Commits, pushes, opens Chrome for next research cycle]
```

**The key insight:** Claude does the research AND the writing in one continuous conversation. Your CLAUDE.md is the thread that holds everything together — it teaches Claude your voice, your methodology, and your rules across every chapter.

---

## Section 1: Explore an Existing Book Project (15m)

### Step 1: Read the example (5m)

Ask Claude Code:

> Open Chrome and navigate to books.recursive.eco. Take a screenshot so I can see it. Then navigate to github.com/PlayfulProcess/freedom-paradox and read the CLAUDE.md file for me.

Claude will open Chrome, show you the published books, then read the project's brain. Notice what CLAUDE.md contains:
- **Voice description** — how the writing should sound
- **Methodology** — the three-filter test for what goes in
- **Privacy rules** — author identity protection
- **Workflow** — the three-tool loop
- **Constraints** — never fabricate quotes, always flag uncertainty

### Step 2: Clone and explore (5m)

```bash
git clone https://github.com/PlayfulProcess/freedom-paradox.git
cd freedom-paradox
claude
```

Claude Code reads the CLAUDE.md automatically. Try:

> What is this project about? How many books are there and what's their status?

> Show me how Chapter 2 of The Species That Tells Stories uses the exposure therapy framework. What sources does it cite?

> How many [RESEARCH NEEDED] or [VERIFY] flags remain across all books?

### Step 3: Make a small contribution (5m)

> There's a [RESEARCH NEEDED] flag somewhere in the book. Find one, open Chrome, research it, and fill it in.

Watch Claude autonomously: find the flag → open Chrome → search → read sources → edit the file → resolve the flag. That's the whole workflow in miniature.

Commit:

```bash
git add .
git commit -m "Resolve research flag"
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
> - A CLAUDE.md with my voice, methodology, and research workflow instructions
> - A README.md with project description and CC-BY-SA-4.0 license
> - A chapters/ directory
> - A research/raw/ directory for deep research dumps
> - A .gitignore
> - Initialize git
> - A book skeleton (outline) based on my answers
>
> The CLAUDE.md should include instructions for how you (Claude) should research:
> "When researching a topic, open Chrome, search Google Scholar and general web for primary sources. Read each source page directly. Save all findings to research/raw/ with full citations (author, year, title, publication, specific page numbers or URLs). Flag anything you cannot verify as [RESEARCH NEEDED]. Never fabricate quotes."
>
> Don't write any content until you understand what I want. Start by asking question 1.

### Step 2: Answer Claude's questions (10m)

Claude Code will ask you each question in turn. Answer honestly.

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

Read the CLAUDE.md carefully:
- Does the voice description sound like you?
- Is the methodology clear enough that Claude could follow it chapter after chapter?
- Does the research workflow section tell Claude how to use Chrome for research?

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

Your book project is now live on the internet.

---

## Section 3: Research and Write Your First Chapter (30m)

### Step 1: Autonomous deep research (10m)

This is where Claude Code Desktop shines. Give it a single prompt:

> Research the topic for Chapter 1: [your chapter topic]. Open Chrome and do the following:
>
> 1. Search Google Scholar for peer-reviewed sources on [specific subtopics]
> 2. Search the general web for key thinkers, data points, and concrete examples
> 3. Read each source page directly — don't just use snippets
> 4. Look for the strongest counterargument to my thesis
> 5. Look for non-Western perspectives
> 6. Compile everything into research/raw/ch01-research.md with full citations
>
> I need author names, publication years, specific findings, and page numbers where possible. Flag anything you can't verify.

Claude will:
- Open a Chrome tab
- Navigate to Google Scholar
- Search your topic
- Click through to papers and articles
- Read the full text of each page
- Extract key findings, quotes, and data
- Save a structured research file with citations

**Watch it work.** You'll see Chrome tabs opening, pages loading, text being extracted. This is the autonomous research loop.

### Step 2: Write the first draft (15m)

> Read research/raw/ch01-research.md. Write a first draft of Chapter 1 following the voice and methodology in CLAUDE.md. Aim for [your target word count]. Save to chapters/ch01-[chapter-name].md. Flag any claim without a source as [RESEARCH NEEDED].

Then read the draft. This is where your judgment matters most.

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

> Paragraph 3 makes a claim without evidence. Open Chrome, find a source, and either back it up or remove it.

> The ending feels rushed. Expand the last section and close with a question rather than an answer.

Notice: you can ask Claude to **go back to Chrome mid-revision** to fill gaps. "Open Chrome and find the exact sample size for the Coan hand-holding study" — Claude will do it and update the chapter.

When you're satisfied:

```bash
git add .
git commit -m "First draft of Chapter 1"
git push
```

---

## Section 4: Publish as a Reading Site (15m)

### Step 1: Set up mdbook (5m)

> Set up mdbook for this project. I want a beautiful reading site with Substack-style typography deployed via GitHub Pages. Create the book.toml, src/SUMMARY.md, a custom CSS theme, a build script, and a GitHub Actions workflow that auto-deploys on every push to main.

Claude Code will create the entire publishing pipeline.

### Step 2: Build and preview (3m)

> Build the book and open it in Chrome so I can see how it looks.

Claude will run the build, then open the local HTML in Chrome for you to preview.

### Step 3: Deploy (3m)

```bash
git add .
git commit -m "Add mdbook publishing pipeline"
git push
```

The GitHub Actions workflow deploys automatically. Your book is live at `https://YOUR-USERNAME.github.io/my-book-project/`

### Step 4: (Optional) Create a grammar for recursive.eco (4m)

> Convert my book into a grammar.json for recursive.eco. Each chapter is an item. Use grammar_type "custom". Include _grammar_commons with CC-BY-SA-4.0 license. Save as grammar.json.

Import into [the Grammar Studio](https://flow.recursive.eco/create) and publish to the Library.

---

## The Power Moves

Once you have the basic loop working, here's what becomes possible:

### Parallel research agents

> Research Chapters 2, 3, and 4 simultaneously. Launch parallel agents — one per chapter. Save each to research/raw/.

Claude Code can spawn multiple research agents that open separate Chrome tabs and research different topics concurrently. Three chapters of research in the time it takes for one.

### Bulk flag resolution

> Find all [VERIFY] and [RESEARCH NEEDED] flags across all chapters. For each one, open Chrome, research it, and resolve it. Work through them systematically.

This is how we resolved ~70 flags across 16 chapters of The Freedom Paradox in one session.

### Cross-reference checking

> Read Chapter 3 and Chapter 7. Are there any contradictions between them? Any claims in Ch 7 that depend on evidence only cited in Ch 3? Flag any issues.

Claude reads both chapters, cross-references claims, and flags inconsistencies.

### Source verification

> Open Chrome and verify every citation in Chapter 1. For each source, navigate to it and confirm the author, date, title, and specific claim are accurate. Flag any that don't check out.

Claude will open each source URL, read the page, and verify or flag each citation.

---

## Troubleshooting

**Chrome doesn't open**
- Make sure Claude in Chrome MCP is connected. In Claude Code, check if Chrome tools are available.
- Try: "Can you open Chrome and navigate to google.com?" — if it fails, reconnect the MCP.

**Claude can't read a page**
- Some sites block automated reading. Try: "Take a screenshot of this page" or "Get the page text."
- For paywalled papers, ask Claude to search for open-access versions or preprints.

**Claude Code doesn't understand my voice**
- Be more specific in CLAUDE.md. Instead of "warm," try: "Short sentences. Concrete images. No jargon. Read everything aloud — if it stumbles, rewrite it."
- Paste an example paragraph you've written and say: "This is my voice. Match it."

**The research is too shallow**
- Be more specific: "Search Google Scholar, not just Google. I need peer-reviewed sources with author names, publication years, and specific findings."
- Ask for primary sources: "Don't summarize — navigate to the actual paper and read it."

**The writing sounds like AI, not me**
- Add to CLAUDE.md: "Never use: 'delve,' 'landscape,' 'tapestry,' 'multifaceted,' 'it's important to note.' Never start paragraphs with 'In the...' or 'When it comes to...'"
- After each draft: "Flag every sentence that sounds like AI wrote it. Rewrite those in a more natural voice."

**Git is confusing**
- You only need: `git add .`, `git commit -m "message"`, `git push`, `git pull`
- Or just ask Claude: "Commit everything and push to GitHub"

**mdbook won't build**
- Ask Claude: "The mdbook build failed. Read the error and fix it."

**GitHub Pages shows 404**
- Check Settings → Pages → set to "GitHub Actions" not "Deploy from branch"
- Wait 30 seconds after push

---

## What's Next?

Once you've published your first chapter:

- **Keep writing** — Use the autonomous loop for each chapter. "Research Ch 2 in Chrome, then write it."
- **Add visualizations** — "Write a Python script to generate charts from this data. Save PNGs to models/charts/."
- **Invite collaborators** — Others can fork your repo and submit pull requests.
- **Print it** — If on recursive.eco, use the Print viewer to make booklets.
- **Teach it** — Run this workshop for your own community. The course itself is open source.
- **Connect** — Share in the [Library](https://flow.recursive.eco/library).

The loop continues: research, write, share, repeat. Every book makes the commons richer.

---

## Weaving Stories and Songs

If you've taken [Vibe Writing 101: Magic Stories for Kids](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=magic-stories-for-kids), you can combine personal family stories with your open-source book:

- **Personal stories stay personal** — Magic Stories for Kids produces private family treasures
- **Commons stories go public** — Vibe Writing 102 produces open contributions
- **Both use the same methodology** — the three-filter test works for private bedtime stories and public book chapters alike

---

## Resources

- **[books.recursive.eco](https://books.recursive.eco/)** — The published books built with this workflow
- [Claude Code Desktop](https://docs.anthropic.com/en/docs/claude-code/overview) — Installation and usage
- [Claude in Chrome](https://chromewebstore.google.com/detail/claude/cjgbgcaaakmmnnkbaaaeecfkphcoefoo) — The Chrome extension that gives Claude eyes on the web
- [mdbook](https://rust-lang.github.io/mdBook/) — The static site generator for books
- [GitHub Pages](https://pages.github.com/) — Free website hosting from your repo
- [Recursive.eco schemas](https://github.com/PlayfulProcess/recursive.eco-schemas) — Grammar format for the library
- [Creative Commons CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/) — The license that makes the commons work
- [Vibe Writing 101](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=magic-stories-for-kids) — The personal stories course
- [Vibe Coding 101](/pages/courses/course-viewer.html?grammar_id=c0c00001-0000-4000-8000-000000c0c001&item=vibe-coding-101) — Build AI tools (no coding required)
