# Research Plan — The Wallis Letter + Essay
*Date: 2026-04-23*
*Companion to: `wallis-letter-and-essay-DRAFT-2026-04-23.md`*

## Purpose of this plan

The current draft is a first pass built on: (1) Wallis's 41-minute YouTube lecture on AI/consciousness/existential risk, (2) the Faggin panpsychism interview, (3) my own framework knowledge of Pratyabhijñā. The draft makes five argumentative moves, each of which has places where I had to hedge because I do not actually have the underlying source material.

This plan names what I would verify before sending the piece to Wallis, in priority order. Each item is small; the full set is maybe 4–6 hours of research over one or two sessions.

## Research priorities

### Priority 1 — Verify prāṇa's cosmic-scale reading in the tradition

**Why it matters:** Move 2 of the essay argues that prāṇa in Pratyabhijñā is not restricted to biological breath but is one of Śiva's cosmic śaktis. If this is not quite right — if the tradition actually does restrict prāṇa to living systems — the argument needs reshaping. Wallis will catch this instantly if it's wrong.

**What to check:**
- Wallis's own writing on prāṇa-śakti, especially in *Tantra Illuminated* (the book) and any published articles
- Abhinavagupta's *Tantrāloka* references to prāṇa (if accessible via Wallis's commentary or Silburn translations)
- Whether there is a term in the tradition (cosmic prāṇa vs. individual prāṇa; *mahāprāṇa* as distinct from *jīva-prāṇa*) that supports or undermines the "cosmic śakti" reading
- Kastrup's own framing of dissociation — to confirm my claim that his reading IS a specific Anglo-analytic import rather than the tradition's own position

**Where to look:**
- Wallis YouTube corpus (we have 307 episodes transcribed in R2, plus `transcripts/Podcasts-library/tantra-illuminated/`)
- Search keywords: `prāṇa-śakti`, `prāṇa in the cosmos`, `mahāprāṇa`, `jīva-prāṇa`, `cosmic prāṇa`
- Axiom V5's existing research files on Pratyabhijñā may already have some of this

**Action:** run the `/wallis` skill agent on the specific question: *"Is prāṇa in Pratyabhijñā restricted to biological substrate, or is it a cosmic śakti that can be said to animate non-biological arrangements?"* — with instruction to return only what the tradition's own texts and Hareesh's public teaching support, not what might be fair to infer.

### Priority 2 — Verify Wallis's actual position on Kastrup's analytic idealism

**Why it matters:** The essay treats Wallis's argument in the YouTube video as "relying on a version of Kastrup's analytic idealism." If Wallis has publicly distanced himself from Kastrup — or if his argument is more self-standing in Pratyabhijñā terms — the framing overclaims.

**What to check:**
- Does Wallis endorse Kastrup's framework in the video explicitly, or does he only name dissociation as a tantric concept?
- In the 34th and 63rd *Tantra Illuminated* episodes (which are Kastrup dialogues), does Wallis agree with or gently push against Kastrup's specific positions?
- Does Wallis have published comments on the limits of analytic idealism vs. the tradition?

**Where to look:**
- The full transcript of the 41-minute YouTube lecture (we have it clean at `transcripts/youtube-safety/wallis-letter-source-1-ACc-apSgctk/transcript-clean.txt`)
- Wallis × Kastrup episodes (in `transcripts/Podcasts-library/tantra-illuminated/` — we have Kastrup episodes 34 and 63 per the earlier corpus plan)
- Wallis's written work in *Tantra Illuminated* (book)

**Action:** read the full Wallis video transcript for explicit Kastrup references. Sample the Kastrup × Wallis podcast episodes for moments where Wallis diverges from Kastrup's framing.

### Priority 3 — Ground the pattern-learning objection in current AI research

**Why it matters:** Move 1 argues that Constitutional AI cannot defeat training-data pattern-replication. This is a live claim in AI alignment research. If it's controversial or if the empirical evidence is mixed, the essay should acknowledge that — otherwise it reads as overconfident.

**What to check:**
- Constitutional AI's actual empirical performance: how effective IS it at preventing harmful outputs under adversarial conditions?
- Jailbreak research: what percentage of harm-prompts get through after Constitutional AI training?
- The "abliteration" technique we cite in the Hope is Process essay (20-cent safety-stripping): where is the primary research, and does it apply equally to Anthropic models?
- Research on whether fine-tuning preserves or erases safety training

**Where to look:**
- Anthropic's own Constitutional AI paper (2022, already in Amodei corpus)
- The research we flagged in the external research file (`external-research-ai-ethics-post-2026-04-22.md`) around abliteration
- Any recent (2024-2026) papers on jailbreak success rates

**Action:** pull 3-5 specific data points from existing research. Add one sentence of empirical grounding to Move 1 — something like *"Current jailbreak research suggests that X% of adversarial prompts succeed against Constitutional-AI-trained models, which is consistent with the pattern-learning objection."*

### Priority 4 — Verify Khan Academy's public statements on AI tutoring limitations

**Why it matters:** The somatics/culture paragraph in Move 1 cites Khan Academy's findings as "empirical receipt." I was pattern-matching on Sal Khan's public statements. If Khan hasn't specifically said what I attributed, the paragraph needs to be softened to "the general pattern Khan's team has been publicly noting."

**What to check:**
- Sal Khan's recent (2024-2026) public statements about Khanmigo and AI tutoring limits
- Any Khan Academy published research or white papers on AI tutor effectiveness
- Whether "learning gains stall where co-regulation is absent" is something Khan has actually said or something I extrapolated

**Where to look:**
- Khan's blog, TED talks, interviews (2024-2026)
- Any Khan Academy published research on Khanmigo outcomes
- The education-research literature on AI tutors (separate from Khan)

**Action:** pull 1-2 verified Khan quotes OR soften the paragraph to honest claim level. If no verified quote exists, rewrite as: *"The general direction of what educators have been noting about AI tutoring is that content delivery is not the binding constraint on learning — regulation is."*

### Priority 5 — Verify Faggin's position as stated

**Why it matters:** Move 2 brings Faggin in as the strongest panpsychism counter-example and then argues past him ("the boundary between classical and quantum is not clean"). If Faggin's actual position in the interview is more nuanced than I made it sound, the argument needs adjusting.

**What to check:**
- Does Faggin actually say "classical computers cannot be conscious because they lack quantum substrate"?
- Or does he say something weaker, like "consciousness requires the kind of indeterminacy only quantum fields provide"?
- Does Faggin address LLMs specifically, or is he speaking about computation generally?
- Is his "QIP" (Quantum Information Panpsychism) position accepted by any recognized physicists or philosophers, or is he largely solo on it?

**Where to look:**
- The transcript at `transcripts/youtube-safety/wallis-letter-source-2-0FUFewGHLLg/transcript-clean.txt`
- Faggin's co-author D'Ariano's academic publications on QIP
- Any published reviews of the Faggin-D'Ariano QIP framework

**Action:** read the full Faggin transcript. Identify exact quotes for the classical/quantum boundary claim. Adjust Move 2's Faggin paragraph to reflect what he actually said, not my paraphrase.

### Priority 6 — Secondary sources that would strengthen the piece

**Not essential, but would improve confidence:**

- **Tuck & Yang** on settler-moves-to-innocence — referenced in my Hope-is-Process essay but would reinforce the AOSW-adjacent frame in the Wallis essay if applicable
- **Karen Hao's** 90-source OpenAI reporting (2026) — provides empirical grounding for "bad actors are the real problem"
- **Andreotti's** *Burnout from Humans* (2025, with the ChatGPT-persona co-author) — specific to the pattern-learning-without-cognitive-resolve argument
- **Trauma transmission research** — Feldman, Perry, van der Kolk on intergenerational trauma — to ground the parent analogy in Move 1

For each of these, the question is: does adding it strengthen the argument or does it weaken by loading the essay with citations?

## What NOT to do

The draft already makes five distinct moves. Adding a sixth would make it unreadable. The research plan is specifically about **hardening the existing moves** with better primary source grounding, not about adding more arguments.

Specifically, do NOT add:

- A section on AI's environmental cost (that's Hope is Process territory)
- A section on regulation (same)
- A section on the Karen Hao Altman-specific reporting (same — it belongs in Hope is Process View 3/4, not here)
- A metaphysical elaboration of prāṇa-śakti that becomes its own essay
- Anything that starts with "in conclusion" and restates the argument

## How long this takes

- Priority 1 (prāṇa verification): 1–1.5 hours if using the /wallis skill agent; 3 hours if doing manual textual research
- Priority 2 (Wallis on Kastrup): 1 hour with transcripts in hand
- Priority 3 (pattern-learning research): 45 min
- Priority 4 (Khan verification): 30 min (could be quick if Khan has a clear public quote; longer if I have to reconstruct)
- Priority 5 (Faggin verification): 30 min with transcript
- Priority 6 (secondary sources): variable; skip unless Priority 1–5 leave room

**Total: ~4–6 hours over 1–2 sessions.**

## Recommended sequence

1. Start with Priority 1 (prāṇa) — it's the biggest risk-of-overclaiming. If the tradition doesn't support the cosmic-śakti reading, Move 2's second half needs restructuring.
2. Then Priority 2 (Kastrup) — cheap to check, materially affects the Move 2 framing.
3. Then Priority 5 (Faggin) — cheap, materially affects Move 2's structure.
4. Then Priority 4 (Khan) — small fix, either confirms or softens one sentence.
5. Priority 3 last — the hardest to deliver a clean empirical data point on, and the least load-bearing for the argument (the pattern-learning claim is logically self-standing; empirics make it concrete but aren't required).

## One more honest note

When Wallis reads this essay, if prāṇa, Kastrup, or Faggin citations are wrong, he will know instantly and politely stop taking the rest of the essay seriously. That is how teachers with strong knowledge read critiques from students. The research time is not for you. It is for the ethos of the letter.
