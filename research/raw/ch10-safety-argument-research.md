# Research: Chapter 10 — The Safety Argument

## Research Date: March 27, 2026

---

## 1. Anthropic Founding Story

### Key Facts
- Founded in 2021 by former OpenAI employees
- Eleven employees left OpenAI, mostly between December 2020 and January 2021
- Co-founders: Dario Amodei (CEO, former VP of Research at OpenAI), Daniela Amodei (President, former VP of Safety & Policy at OpenAI)
- Other co-founders: Benjamin Mann, Jared Kaplan, Jack Clark, Sam McCandlish, Tom Brown, Christopher Olah
- Structured as a public benefit corporation (PBC)
- Initial fundraise: $124 million

### Reasons for Departure
- Directional disagreements over how aggressively AI capabilities should be scaled relative to safety research
- After GPT-2 and GPT-3, a group within OpenAI believed scaling compute would make models better, but also needed alignment/safety work alongside scaling
- OpenAI's 2019 $1B Microsoft investment raised fears of "industrial capture"
- OpenAI pushing forward with powerful models while safety was treated as an afterthought
- Dario Amodei described it as a difference in "vision" — safety needed to be foundational, not an afterthought

### Funding and Valuation (as of March 2026)
- Total raised: ~$67.3 billion over 17 rounds
- Series G (Feb 12, 2026): $30B at $380B post-money valuation, led by GIC and Coatue
- Series F (Sept 2025): $13B at $183B valuation
- Amazon invested ~$8B total
- Google invested ~$3B total
- Microsoft and Nvidia committed up to $5B and $10B respectively

---

## 2. Constitutional AI (CAI)

### Original Paper
- Published December 2022 (arXiv:2212.08073)
- Title: "Constitutional AI: Harmlessness from AI Feedback"

### How It Works — Two Phases
**Phase 1 — Supervised Learning:**
- Model generates responses, then self-critiques and revises them based on constitutional principles
- Original model is fine-tuned on the revised responses

**Phase 2 — Reinforcement Learning:**
- Instead of using human feedback (RLHF), uses AI-generated feedback
- AI evaluates outputs against the constitution to choose the more harmless/helpful output
- Called RLAIF (Reinforcement Learning from AI Feedback)

### Sources of the Constitution
- UN Universal Declaration of Human Rights (chosen partly because ratified across 193 nations — most cross-culturally representative document available)
- Trust and safety best practices
- Principles from other AI labs (e.g., DeepMind's Sparrow Principles)
- Effort to capture non-Western perspectives
- Principles discovered through early research

### Key Advantages
- Scalable oversight — AI supervision instead of human supervision
- Transparency — easier to specify, inspect, and understand principles
- Reduces reliance on per-example human feedback

### Claude's Constitution — May 2023
- Anthropic published "Claude's Constitution" revealing specific principles
- Detailed values and selection process

### New Constitution — January 21, 2026
- 84-page, ~23,000-word overhaul released under Creative Commons CC0 1.0
- Internally known as "soul document" or "soul spec"
- Shift from rigid rules to philosophical reasoning
- Formally addresses AI consciousness
- Clear priority hierarchy: (1) safety + human oversight, (2) ethical behavior, (3) Anthropic's guidelines, (4) helpfulness
- Departure from 2023 version which more directly referenced the UN Declaration
- Now more principles-based philosophical approach rather than standalone rules

### Collective Constitutional AI
- Anthropic experiment aligning language model with public input
- Community participation in defining constitutional principles

---

## 3. Responsible Scaling Policy (RSP)

### Version 1.0 — September 19, 2023
- Introduced AI Safety Levels (ASLs), graduated safety/security measures
- ASL-1: No meaningful catastrophic risk (e.g., chess-playing bots)
- ASL-2: Early signs of dangerous capabilities (e.g., bioweapon instructions)
- ASL-3: Substantially increases catastrophic misuse risk OR shows low-level autonomous capabilities
- Included hard commitment to PAUSE development if adequate mitigations couldn't be implemented before reaching next level

### ASL-3 Activation — May 2025
- Anthropic activated ASL-3 safeguards for relevant models

### Version 3.0 — February 24, 2026
- Comprehensive rewrite — published same day as the Hegseth deadline
- KEY CHANGE: Removed the hard pause commitment
  - Previously: must halt development/deployment if can't implement adequate mitigations before next level
  - Now: replaced categorical pause trigger with dual condition requiring BOTH AI race leadership AND material catastrophic risk
- New elements: Frontier Safety Roadmaps, Risk Reports with external reviewer access
- Public goals graded for progress rather than hard commitments

### Controversy Over RSP v3.0
- Critics: dropping pause commitment makes deployment of unacceptably risky models more likely
- METR reviewer Chris Painter warned society not prepared for catastrophic risks
- Three forces Anthropic cited for change:
  1. "Zone of ambiguity" muddling public case for risk from capability thresholds
  2. Increasingly anti-regulatory political climate
  3. Requirements at higher RSP levels very hard to meet without industry-wide coordination
- Timing: released same week as Pentagon confrontation — critics saw it as capitulation

---

## 4. Dario Amodei — "The Adolescence of Technology"

### Publication Details
- Published January 26, 2026 on darioamodei.com
- ~20,000 words
- Posted to X/Twitter the same day

### Central Metaphor
- From the film "Contact": an alien asks "How did you evolve, how did you survive this technological adolescence without destroying yourself?"
- Amodei argues humanity is entering this rite of passage — "turbulent and inevitable, which will test who we are as a species"

### Five Risk Categories
1. **Autonomy and Control (Misalignment)**: AI systems developing goals/behaviors misaligned with human intentions
2. **Biological Misuse**: AI providing step-by-step guidance for designing/releasing biological weapons over weeks or months
3. **Authoritarian Consolidation**: Misuse of AI to seize or entrench power — AI-enabled surveillance, propaganda, autonomous weapons making repression nearly impossible to resist
4. **Economic Disruption**: Could displace half of all entry-level white-collar jobs within 1-5 years; wealth concentration exceeding Gilded Age; personal fortunes potentially reaching trillions
5. **Unknown Unknowns**: Rapid biology advances altering lifespans/intelligence, unhealthy changes from AI interaction, challenges to human purpose when AI exceeds humans across all domains

### Key Arguments
- AI development requires careful guidance during this "adolescent" phase
- Proposes concrete "battle plan" with technical defenses, governance strategies, economic interventions
- Not anti-development but pro-careful-management

### Reception
- Significant attention from policy world (Lawfare analysis, etc.)
- Zvi Mowshowitz response on Substack
- Some criticism for being self-serving — Anthropic benefits from regulatory frameworks that favor well-resourced labs

---

## 5. The Anthropic-Pentagon Confrontation (February 2026)

### Timeline
- **Feb 24**: Defense Secretary Pete Hegseth gives Dario Amodei deadline: relent by 5:01 PM Friday Feb 27, allow unrestricted use of AI models "for all legal purposes"
- **Feb 26**: Anthropic releases statement indicating it will not budge. Amodei declares company "cannot in good conscience accede" to Pentagon's demand
- **Feb 27**: Deadline passes. President Trump directs federal agencies to cease using Anthropic's products. Hegseth designates Anthropic a "supply chain risk"
- **March 9**: Anthropic sues federal government in California court, arguing irreparable harm
- **March 26**: Judge blocks Pentagon's supply chain risk designation, calling it "troubling" and questioning whether it was "tailored" to national security concerns

### Amodei's Two Red Lines
1. No domestic surveillance of Americans
2. No lethal autonomous weapons with no human in the loop

### Context
- Dispute centered on usage restrictions for military applications
- Anthropic concerned about autonomous weapons and mass surveillance
- Amodei wrote: "in a narrow set of cases, we believe AI can undermine, rather than defend, democratic values. Some uses are also simply outside the bounds of what today's technology can safely and reliably do"
- EFF weighed in: "Privacy Protections Shouldn't Depend On the Decisions of a Few Powerful People"

### Significance
- First major confrontation between an AI company and the US government over safety restrictions
- Tested whether a company could refuse government demands based on ethical principles
- Raised question: is it good or bad that one CEO's values determined whether an entire technology was available to the military?
- CFR analysis: "A Test of U.S. Credibility"

---

## 6. AI Safety — Closed vs. Open Source Debate

### Arguments for Closed Models Being Safer
- Advanced AI is dual-use technology (like nuclear/bioengineering)
- Open-sourcing powerful models allows anyone to cause harm without specialized knowledge
- Closed providers invest heavily in RLHF and safety measures
- Open models vary widely in safety properties
- Responsible labs can control deployment, monitor misuse, update safeguards
- "Responsible Scaling" only works if you can actually control the model's distribution

### Arguments for Open Models Being Safer
- Mozilla Joint Statement on AI Safety and Openness: 1,800+ signatories
- Increasing access makes models safer through transparency, scrutiny, knowledge sharing
- Openness breeds trust, improves safety, decentralizes power
- Security experts: transparency accelerates vulnerability fixes
- Closed models hide vulnerabilities but rely on vendor trust for patches
- "Safety through obscurity" doesn't work long-term (proven in cybersecurity)
- Concentration of power in few companies creates single points of failure

### 2025 International AI Safety Report
- Noted wide expert disagreement about likelihood of losing control over advanced AI
- Found "no scientific consensus" on risk of AI being used to manipulate public opinion

### The Convergence View
- Future may be hybrid — not either/or but both/and
- Different levels of openness for different capability levels
- "Responsible release" frameworks attempting middle ground

---

## 7. The Alignment Stack Problem

### Layers of AI Alignment
1. User preferences (what the individual user wants)
2. Company values (what Anthropic/OpenAI/Google believes is right)
3. Legal compliance (what the law requires)
4. Trained ethical principles (what the model was trained to follow)
5. Societal values (what "society" wants — but which society?)

### The Core Tension
- Who decides what values get encoded?
- Constitutional AI is transparent about principles — but the principles are still chosen by Anthropic employees
- Democratic input (Collective Constitutional AI) is an experiment, not standard practice
- Different cultures, political systems, and individuals have different values
- The "alignment" stack is ultimately a hierarchy of whose preferences win

---

## Sources

- https://research.contrary.com/company/anthropic
- https://en.wikipedia.org/wiki/Anthropic
- https://fortune.com/2026/02/17/anthropic-ceo-dario-amodei-balancing-safety-commercial-pressure-ai-race-openai/
- https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
- https://www.anthropic.com/news/claudes-constitution
- https://arxiv.org/abs/2212.08073
- https://www.darioamodei.com/essay/the-adolescence-of-technology
- https://fortune.com/2026/01/27/anthropic-ceo-dario-amodei-essay-warning-ai-adolescence-test-humanity-risks-remedies/
- https://www.anthropic.com/responsible-scaling-policy
- https://www.anthropic.com/news/responsible-scaling-policy-v3
- https://winbuzzer.com/2026/02/25/anthropic-drops-hard-safety-limit-responsible-scaling-policy-xcxwbn/
- https://www.techpolicy.press/a-timeline-of-the-anthropic-pentagon-dispute/
- https://www.cnbc.com/2026/02/27/anthropic-pentagon-ai-policy-war-spying.html
- https://www.cnbc.com/2026/02/27/defense-anthropic-ai-war-risks-hegseth-amodei.html
- https://www.cfr.org/articles/anthropics-standoff-with-the-pentagon-is-a-test-of-u-s-credibility
- https://www.eff.org/deeplinks/2026/03/anthropic-dod-conflict-privacy-protections-shouldnt-depend-decisions-few-powerful
- https://time.com/7354738/claude-constitution-ai-alignment/
- https://www.anthropic.com/news/claude-new-constitution
- https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- https://cmr.berkeley.edu/2026/01/the-coming-disruption-how-open-source-ai-will-challenge-closed-model-giants/
- https://ai-frontiers.org/articles/frontier-ai-should-be-open-source
