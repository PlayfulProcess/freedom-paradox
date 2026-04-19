# Research workflow — Claude Code desktop + Claude in Chrome

Two parts: (1) source links to paste into Chrome, (2) a prompt to paste into Claude Code desktop to orchestrate the rewrite into the repo.

---

## Part 1 — Source links for deep research in Chrome

Most research happens in **Claude.ai** (Chrome) with **Research mode ON**, using the kickoff prompt at `books/axiom-beneath-the-ground/outreach/new-chat-kickoff-prompt.md`. Below are the starting sources per thread. Claude.ai will find more; these are the anchor points. Verify any URL before citing — I flag ones I am confident about and ones I am not.

### Thread 1 — Tristan Harris / Center for Humane Technology
- Center for Humane Technology — https://www.humanetech.com/ *(confident)*
- *Your Undivided Attention* podcast — https://www.humanetech.com/podcast *(confident root)*
- **The specific interview Wallis shared** — you have this. Paste the URL to Claude.ai when it asks.
- Tristan Harris TED 2017 — search YouTube: "Tristan Harris How a handful of tech companies"
- *The Social Dilemma* (2020, Netflix) — context only

### Thread 2 — Jonathan Haidt
- *The Anxious Generation* official site — https://www.anxiousgeneration.com/ *(confident)*
- Haidt Substack *After Babel* — https://www.afterbabel.com/ *(confident)*
- Candice Odgers critique in *Nature* — search: "Odgers Nature 2024 Anxious Generation"
- Andrew Przybylski / Pete Etchells counter-positions — search *The Guardian*, *Aeon*

### Thread 3 — Anna Lembke / *Dopamine Nation*
- Stanford Medicine faculty page — https://profiles.stanford.edu/anna-lembke *(usually confident, verify)*
- *Dopamine Nation* (Dutton, 2021) — Google Books preview acceptable for paraphrase
- Huberman Lab interviews with Lembke — search YouTube

### Thread 4 — Dario Amodei
- *Machines of Loving Grace* — https://darioamodei.com/machines-of-loving-grace *(confident)*
- Anthropic posts & interviews — https://www.anthropic.com/news *(confident root)*
- Dwarkesh Patel interview with Amodei — search dwarkeshpatel.com
- The November 2025 $10B Nvidia commit announcement — search "Anthropic Nvidia November 2025 announcement"
- The June 2025 Huang/Amodei public disagreement — search "Huang Amodei June 2025"

### Thread 5 — John O'Nolan / Ghost
- Ghost platform — https://ghost.org/ *(confident)*
- Ghost About — https://ghost.org/about/ *(confident)*
- John O'Nolan blog — https://john.onolan.org/ *(very likely correct, verify)*
- Ghost ActivityPub announcement — search "Ghost ActivityPub federation 2024"
- Kickstarter retrospective — search "Ghost Kickstarter 2013 John O'Nolan"

### Thread 6 — Substack, Medium, engagement-vs-infrastructure
- Casey Newton, *Platformer* — https://www.platformer.news/ *(confident)*
- Ryan Broderick, *Garbage Day* — https://www.garbageday.email/ *(confident)*
- Max Read's Substack — https://maxread.substack.com/ *(very likely)*
- Substack recommendation/Notes reporting — search *Platformer* + *The Verge*
- Ethan Zuckerman *Mischiefs of Faction* / *Prosocial Design* — search ethanzuckerman.com

### Thread 7 — Bhagavad Gita
- Eknath Easwaran translation (Nilgiri Press) — ISBN 978-1586380199
- Gandhi's Gita commentary — public domain, archive.org
- Sri Aurobindo, *Essays on the Gita* — public domain full text at sriaurobindoashram.org
- Arvind Sharma, *The Hindu Gita* (Open Court, 1986) — academic secondary
- Online concordance — https://www.holy-bhagavad-gita.org/ *(verify)* or bhagavadgitaasitis.com

### Thread 8 — "AI is the next social media"
- Sinan Aral, *The Hype Machine* (2020) — primary
- Zeynep Tufekci — https://www.insight.substack.com/ *(verify)*; also NYT op-eds
- Renée DiResta, *Invisible Rulers* (2024) — primary
- Daron Acemoglu & Simon Johnson, *Power and Progress* (2023) — primary
- Ethan Zuckerman, *Mistrust* (2021) — primary
- Allison Stanger — search Middlebury faculty page

### Additional anchors
- recursive.eco — https://recursive.eco/ *(your own; paste the about page to Claude)*
- Your April 2025 Dario draft — local only; paste to Claude when it asks

---

## Part 2 — Claude Code desktop orchestration prompt

Paste this into a **new Claude Code desktop session** in the `freedom-paradox` repo. It will orchestrate the rewrite of each Claude.ai output into a clean research file in the right location with the right format. Keep the Claude.ai conversation open in Chrome throughout.

```
I'm running a deep-research workflow for the book Axiom Beneath the Ground. The kickoff prompt and source links live at:

- books/axiom-beneath-the-ground/outreach/new-chat-kickoff-prompt.md
- books/axiom-beneath-the-ground/outreach/research-workflow.md
- books/axiom-beneath-the-ground/outreach/ghost-model-and-harris-reversal.md

Your job in this session is to act as the rewrite and repo-integration layer for research I run in a Claude.ai browser conversation. The workflow is:

1. I run a research thread in Claude.ai (Chrome) using the kickoff prompt.
2. I paste Claude.ai's raw output into this session.
3. You rewrite the output into a citation-grade research file at the correct path in the repo, following the format of the existing research files (research-21 through research-26 are the templates).
4. You update CHANGELOG.md with a short entry summarizing the thread's findings and flagging anything the thread changes about the book's argument.
5. You commit and push to claude/plan-retreat-insights-9lefO with a clear message.
6. You tell me which thread to run next and surface any follow-up questions the research raised.

Rules for the rewrite step:

- Output path: books/axiom-beneath-the-ground/research/research-NN-<slug>.md. Continue numbering from research-26. Suggested slugs:
  - research-27-harris-2026-public-positions.md
  - research-28-haidt-anxious-generation-critique.md
  - research-29-lembke-dopamine-nation.md
  - research-30-amodei-2024-2026-thought.md
  - research-31-onolan-ghost-platform.md
  - research-32-substack-medium-engagement-debate.md
  - research-33-gita-arjuna-paralysis-dharma.md
  - research-34-ai-as-next-social-media.md
- Follow the structure of research-21 through research-26: a header with sources, numbered sections with page/timestamp citations where possible, `[RESEARCH NEEDED]` or `[VERIFY]` flags for anything not confirmed, a "Notes for the book" section that tells me where in the manuscript the finding should land, and a working footnote draft at the end.
- Copyright rule: no verbatim passages over 30 words. Paraphrase by default. Attribute every quote. Never fabricate page numbers, timestamps, or URLs.
- Privacy rule: the author publishes as PlayfulProcess. Never use any real name in committed content. If Claude.ai's output contains a real name, replace it.
- Architectural rule: the narrator's first-read interpretation of her teacher's motive in sharing the Harris podcast is a character-interior observation, not a factual claim about the living teacher. Keep this constraint in any rewrite that touches that scene.

Confirm you have read the three outreach files, confirm you understand the workflow and rules, and tell me to paste the first Claude.ai output. Do not begin writing research files until I paste something.

I will most likely run the threads in this order: 5 (O'Nolan/Ghost) → 4 (Amodei) → 1 (Harris) → 7 (Gita) → 8 (AI-as-next-social-media) → 3 (Lembke) → 2 (Haidt) → 6 (Substack). Thread 5 is first because it is the most concrete and gives the book Ch10's sibling passage immediately.
```

---

## How the two pieces fit together

- The **Chrome workflow** (Part 1) runs one research thread at a time inside a single Claude.ai conversation that has the kickoff prompt as its first message.
- The **Claude Code workflow** (Part 2) sits alongside it in a terminal, accepts each raw Claude.ai output, rewrites it into the repo, commits, and queues the next thread.
- You stay the orchestrator. You run Claude.ai; you paste outputs to Claude Code; Claude Code does the rewrite and repo work. If a thread needs materials you have locally (Dario draft, Harris interview URL, recursive.eco about page), Claude.ai will ask inside the Chrome session and you paste them there.
