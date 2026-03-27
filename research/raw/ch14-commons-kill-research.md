# Research: Chapter 14 — The Commons That Can Kill

## Context
This is research for Chapter 14 of "The Freedom Paradox," the opening chapter of Part V: The Question. The chapter applies Elinor Ostrom's Nobel Prize-winning commons governance framework to AI, testing whether the intellectual tools that solved the tragedy of the commons for fisheries and forests can work for a technology that, once released, cannot be recalled.

## Core Questions
1. What are Ostrom's 8 design principles for governing a commons?
2. How does each principle apply (or fail to apply) to AI?
3. Why does the rivalrous/non-rivalrous distinction matter so much?
4. What does the nuclear nonproliferation analogy teach us about AI governance?
5. Can a commons framework work for something whose harms are irreversible?

---

## Key Findings

### 1. Ostrom's 8 Design Principles

Elinor Ostrom (1933-2012) won the 2009 Nobel Prize in Economics for demonstrating that communities could successfully manage shared resources without either privatization or government regulation. Her 1990 book *Governing the Commons* challenged Garrett Hardin's influential 1968 "Tragedy of the Commons" argument that shared resources were doomed to overexploitation.

The eight design principles, derived from studying successful commons across cultures (Swiss alpine meadows, Japanese fisheries, Spanish irrigation systems, Philippine forests):

1. **Clearly defined boundaries** — Who has access rights and what are the resource limits
2. **Congruence between rules and local conditions** — Rules match the actual resource and community
3. **Collective-choice arrangements** — Those affected by rules can participate in modifying them
4. **Monitoring** — Active auditing of resource use and user behavior, accountable to community
5. **Graduated sanctions** — Escalating penalties for rule violations (warnings → fines → exclusion)
6. **Conflict resolution mechanisms** — Accessible, low-cost dispute resolution
7. **Minimal recognition of rights to organize** — External authorities recognize the community's self-governance
8. **Nested enterprises** — Governance organized in multiple layers for large-scale resources

### 2. Traditional Commons vs. AI — The Rivalrous Gap

**Traditional common pool resources (CPRs):**
- Fisheries: one fish caught is one fish gone. Rivalrous and depletable.
- Forests: one tree felled reduces the stock. Recovery takes decades.
- Irrigation water: one farmer's use reduces availability for others.
- The key feature: consumption by one user diminishes what's available to others.

**AI models as a "resource":**
- Non-rivalrous: copying a model does not diminish the original
- Non-depletable: downloading Llama does not reduce Meta's copy
- Zero marginal cost of reproduction (once trained)
- Open-source code (Linux, Apache) has functioned as a successful digital commons for decades precisely because of non-rivalry

**The critical distinction the chapter must make:**
- AI *models* are non-rivalrous — but AI *harms* are rivalrous
- Surveillance capacity: one actor's mass surveillance degrades everyone's privacy (shared trust resource)
- Deepfake generation: each convincing fake erodes the shared resource of epistemic trust
- Autonomous weapons: proliferation creates classic arms race dynamics (rivalrous security)
- Biosecurity: open biological AI models enable pathogen design that consumes shared safety
- The harms are rivalrous even though the technology is not

### 3. Where Ostrom's Principles Break for AI

**Principle 1 — Clearly defined boundaries:**
- Traditional: the fishing ground has physical boundaries; the user community is identifiable
- AI: once a model is released openly, the "boundary" of the commons is the entire internet. Users are anonymous, global, and ungovernable. There is no way to define who is "in" the commons
- Nuclear analogy: uranium enrichment requires identifiable facilities. AI training requires only GPUs and data, which are commercially available worldwide

**Principle 2 — Congruence with local conditions:**
- Traditional: Swiss farmers know their meadow. Rules match local ecology
- AI: there are no "local conditions" for a globally distributed model. A model trained in California can be fine-tuned for bioweapon design in any country

**Principle 3 — Collective-choice arrangements:**
- Traditional: fishers in a village can meet and set rules
- AI: who participates in setting the rules? The developers? The users? The people harmed by outputs? There is no "community" that maps onto Ostrom's village
- Current reality: AI governance decisions are made by corporations (OpenAI, Google, Meta, Anthropic) or by national governments (EU AI Act, US executive orders, China's regulations). Neither maps to Ostrom's bottom-up collective choice

**Principle 4 — Monitoring:**
- Traditional: monitors can observe who is fishing, how much they catch
- AI: once model weights are released, there is no way to monitor downstream use. The model runs locally. No telemetry, no audit trail, no fishing inspector
- Contrast with API-only models (Claude, GPT) where usage can be monitored

**Principle 5 — Graduated sanctions:**
- Traditional: first offense gets a warning, repeated offenses escalate
- AI: sanctions against whom? A model released under Apache 2.0 cannot be recalled. A user who fine-tunes for harmful purposes cannot be identified, much less sanctioned
- The time horizon problem: by the time harm is detected, the model has proliferated beyond any possibility of enforcement

**Principle 6 — Conflict resolution:**
- Traditional: village elders, community councils, courts
- AI: international conflicts over AI governance have no resolution mechanism. The US, EU, and China have fundamentally different approaches. No "village elder" for global AI

**Principle 7 — Minimal recognition of rights to organize:**
- Traditional: the government acknowledges the fishing cooperative's authority
- AI: governments are not recognizing commons self-governance — they are trying to impose top-down regulation. The EU AI Act, US executive orders, and China's regulations are all state-driven, not community-driven
- Open-source community self-governance (Apache Foundation, Linux Foundation) has worked for code but has not been tested against catastrophic risk

**Principle 8 — Nested enterprises:**
- Traditional: local → regional → national layers of governance
- AI: governance is fragmented. No coherent nesting. National regulations conflict. International coordination is minimal (no AI equivalent of IAEA, despite calls for one)

### 4. Nuclear Nonproliferation Analogy

**Why the analogy is popular:**
- Both technologies have dual-use potential (energy/weapons, productivity/harm)
- Both involve potentially catastrophic consequences
- Sam Altman and others have called for an "IAEA for AI"
- Bill Gates compared AI to nuclear technology: "both promising and dangerous"

**Why the analogy breaks:**
- Nuclear weapons require physical infrastructure: enrichment facilities, specific materials (uranium, plutonium), detectable supply chains
- AI requires only computation and data — both commercially available and globally distributed
- Nuclear technology has a clear civilian/military divide. AI does not — the same model that writes poetry can help design pathogens
- Nuclear materials cannot be copied. AI model weights can be copied infinitely at zero cost
- The NPT (Nuclear Non-Proliferation Treaty, 1968) works because enrichment is hard and detectable. AI "enrichment" (training) is getting cheaper and more distributed every year

**Where the analogy holds:**
- The fundamental question is the same: can a technology with catastrophic potential be governed through international cooperation?
- Both involve asymmetric power (nuclear haves vs. have-nots; frontier AI labs vs. everyone else)
- Both create tension between openness (for peaceful use) and restriction (for safety)
- Both involve the question of whether knowledge, once created, can be contained

**RAND Corporation research (2024):**
- Published "Insights from Nuclear History for AI Governance"
- Key finding: nuclear governance succeeded partly because the technology was inherently hard to develop. AI governance faces the opposite challenge — the technology is inherently easy to distribute
- The NPT bargain (access to peaceful nuclear tech in exchange for weapons restraint) has no AI equivalent because "peaceful" and "harmful" AI are the same artifact

**Georgetown CSET critique:**
- "Nuclear Non-Proliferation Is the Wrong Framework for AI Governance"
- AI is a general-purpose technology; nuclear weapons are a single-purpose technology
- Basing AI policy on the nuclear analogy "is conceptually flawed and risks inflating expectations about the international community's ability to control model proliferation"

### 5. The Code Commons vs. the AI Commons

**Where commons governance works for software:**
- Linux kernel: 30+ years of successful commons governance
- Apache web server: foundation model (literally) for commons governance
- Ostrom's principles map well: defined contributors (Principle 1), community norms (Principle 2), collective decision-making (Principle 3), code review as monitoring (Principle 4), graduated responses to bad actors (Principle 5)
- Key reason: software code is non-rivalrous AND non-harmful. Bad code can be identified and reverted. The worst outcome is a buggy kernel, not a bioweapon

**Why AI breaks the code commons model:**
- AI models are not just code — they are trained capabilities
- A malicious Linux patch can be caught in code review. A model's harmful capabilities cannot be easily audited
- The attack surface is the model's entire capability space, not discrete lines of code
- Open-source code governance assumes good faith + revertibility. AI harms are often irreversible

### 6. AI Governance Landscape (2024-2025)

**EU AI Act (2024):**
- Risk-based classification system
- Bans certain uses (social scoring, untargeted facial recognition)
- Requirements for high-risk AI systems
- Does not address open-source model release directly in a satisfying way

**US approach:**
- Biden executive order (Oct 2023) — focused on reporting requirements for frontier models
- Trump administration (2025) — rolled back requirements, emphasized innovation over safety
- Fragmented state-level regulation (California SB-1047 vetoed)

**China:**
- Regulations on generative AI (2023), deepfakes, recommendation algorithms
- State-directed approach: openness within government control

**International:**
- No binding international AI treaty
- AI Safety Summits (Bletchley Park 2023, Seoul 2024, Paris 2025) — declarations but no enforcement
- Calls for "IAEA for AI" have not materialized into institutional form

### 7. Biosecurity as the Sharpest Example

- Open-source biological AI models can be used to design pathogens
- DNA synthesis screening is currently voluntary and has known gaps
- Researchers demonstrated that AI protein-design tools could "paraphrase" toxic protein sequences to evade screening
- This is the clearest case where AI openness creates a rivalrous harm: one bad actor's use of a biological AI model can cause mass casualties
- The same model that designs cancer therapies can design bioweapons — dual use with no technical separator

### 8. Mozilla/Open Future Data Commons Work

- Mozilla and Open Future exploring "data commons" approaches (2024-2025)
- OSI + Open Future Paris workshop (Oct 2024) on data governance in open-source AI
- Proposed paradigm shifts: data commons governance, data trusts, cooperatives
- But these focus on training data governance, not on model capability governance
- The governance gap: even if you govern the data commons, the trained model, once released, is ungovernable

---

## Key Quotes

- Garrett Hardin (1968): "Ruin is the destination toward which all men rush, each pursuing his own best interest in a society that believes in the freedom of the commons" [from "The Tragedy of the Commons," Science]
- Georgetown CSET: AI differs "so fundamentally from nuclear technology that basing AI policy around the nuclear analogy is conceptually flawed"
- Bill Gates: AI and nuclear technology are both "promising and dangerous" — rare technologies requiring governance
- Bulletin of the Atomic Scientists (2024): "The sharp distinction between civil and military nuclear programs, which has no analogue for AI, makes nonproliferation efforts much easier"

---

## Sources

- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Hardin, G. (1968). "The Tragedy of the Commons." *Science*, 162(3859), 1243-1248.
- Georgetown CSET (2024). "Nuclear Non-Proliferation Is the Wrong Framework for AI Governance."
- Bulletin of the Atomic Scientists (2024). "AI and the A-bomb: What the analogy captures and misses."
- RAND Corporation (2024). "Insights from Nuclear History for AI Governance."
- Nature Reviews Physics (2025). "Why is the nuclear-AI analogy so popular?"
- Open Future / OSI (2025). "Data Governance in Open Source AI: Enabling Responsible and Systematic Access."
- Mozilla Foundation (2025). "Navigating the Future of Openness and AI Governance."
- Springer (2025). "In search of a global governance mechanism for Artificial Intelligence: a collective action perspective."
- Science (2024). "AI and biosecurity: The need for governance."

---

## Open Questions for Further Research

1. Has anyone formally mapped Ostrom's 8 principles to AI in a peer-reviewed paper? The Springer collective action paper comes closest.
2. What specific commons have historically failed despite Ostrom's principles? (Atmosphere/climate is the obvious one — and it may be the better analogy for AI than fisheries.)
3. The "digital commons" literature (Hess & Ostrom, 2007, *Understanding Knowledge as a Commons*) — does it address catastrophic risk?
4. Is there a meaningful distinction between "commons governance of AI code" (which works) and "commons governance of AI capabilities" (which may not)?
