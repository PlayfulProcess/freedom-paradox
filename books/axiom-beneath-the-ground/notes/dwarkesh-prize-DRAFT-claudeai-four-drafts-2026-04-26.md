# Dwarkesh Prize Q3 — Four drafts (claude.ai session #2)

*Author received from a separate claude.ai chat on 2026-04-26 — second claude.ai-source set after `dwarkesh-prize-DRAFT-claudeai-three-essays-2026-04-26.md`.*
*Originating session's ranking: **#4 > #2 > #1 > #3.***
*Each draft ~850–890 words.*

**Source-session framing.** The originating session leaned into governance-structure-of-deployment as the crucial factor (Draft 4) and noted: "Dwarkesh explicitly said LLM essays 'identify 5 plausible answers but not have the context and taste to identify the crucial factor.' Most entrants will pick a cause (alignment vs. development vs. cooperatives). #4 is the only one that argues the crucial factor is the *governance structure of the deployment itself*."

Background data the session leaned on: AI safety philanthropy ~$600M/year globally; Coefficient Giving (Open Phil's successor) processes ~$140M with only ~3 technical-safety grant investigators; the field is bottlenecked on grantmaker capacity; Anthropic's cofounders' 80% pledge alone is worth ~10x Coefficient Giving's total. This is the empirical anchor for "alignment is already at funding saturation; the marginal $180B has to go elsewhere."

---

## Draft 1 — Epistemic infrastructure: pluralism over consolidation

### Spend nothing on technical alignment

Spend zero on technical alignment research. Not because it doesn't matter — it does — but because by the time the Foundation deploys this money, alignment will already be funded to saturation. The seven Anthropic cofounders' 80% pledge alone, at current valuations, is worth roughly 10x Coefficient Giving's entire 2025 grantmaking. Coefficient Giving itself reports being bottlenecked on *grantmaker capacity*, not capital — three technical-safety investigators evaluating $140M in 2025, with the per-dollar impact distribution roughly flat as they scaled. Schmidt Sciences, the UK Alignment Project, the labs' internal teams. The marginal dollar from $180B has to go where the existing flow won't.

The genuinely under-funded problem is this: frontier AI is being trained on, and is now scaling, a single way of knowing. Broadly — post-Enlightenment, English-medium, individual-as-unit, instrumentally rational. This is not wrong. It is one mode among many. But as AI becomes the substrate through which billions of people read, write, decide, learn, and grieve, the monoculture problem will compound faster than the alignment problem. A perfectly aligned monoculture is still a monoculture. There is currently no philanthropic actor at any scale funding what comes next.

The standard objection is that "different epistemics" is hand-waving. Fund what, exactly?

**1. Counter-corpora and evaluation infrastructure ($60B over 10 years).** Models inherit the distribution they were trained on. The public discourse fixates on languages — fairly, since Masakhane's AFROBENCH benchmark recently showed enormous frontier-model gaps for 64 African languages. But corpora are not just languages. They are oral traditions never transcribed, ritual knowledge held under data-sovereignty constraints (CARE Principles, Papa Reo licenses), contemplative traditions, indigenous taxonomies of land and kin, working-class vernaculars. Fund the slow expensive work of corpus construction *under the data-sovereignty terms of source communities* — not extractive scraping. Pair this with evaluation suites built by those same communities, against which frontier labs are required to publish results as a condition of any Foundation partnership. This is leverage: the labs already chase eval performance.

**2. Plural-epistemics research labs ($40B over 10 years).** Not "AI ethics centers" — those exist, are largely declawed, and reproduce the academic monoculture. Fund 30–40 small (~$50M endowed) labs anchored in distinct knowledge traditions: an Andean lab oriented around relational ontologies, a contemplative-traditions lab in the Vipassana/Zen lineages, a Yoruba/Ifá lab on divinatory cognition, a feminist-care-ethics lab, a Talmudic-reasoning lab, an Afro-Brazilian *terreiro* lab. (I was raised in Umbanda. It has a 400-year-old grammar for distributed cognition that Western AI safety hasn't started reading.) Each lab's mandate: produce models, datasets, evals, critique that frontier labs can use. Some will fail. The point is variance, not consensus.

**3. Pluralism in the grantmaking layer itself ($80B over 15 years).** This is the meta-move that makes the first two stick. The Foundation's staff will be drawn from a narrow tier — same handful of universities, same fellowships, same priors. If they distribute the money, the money will be epistemically thin no matter what they fund. Solution: spin out 8–10 parallel sub-foundations, each $8–10B endowed, each governed by a board with a *different* epistemic constitution. One technical-safety board (the existing model). One Indigenous-data-governance board. One Global South sovereign-AI board. One labor / political-economy board. One contemplative-traditions board. They do not have to agree. They publish their reasoning publicly. Their disagreements *are* the product. Vanessa Andreotti's framing is useful here: the modernist instinct is to consolidate authority around the right answer; depth requires letting contradictions remain visible long enough for something new to emerge.

**Timeline.** Years 1–3: build grantmaking infrastructure. Most of the money will not be deployed in this window, and that is correct. Trying to deploy $180B in 36 months is how you end up with 200 nonprofit consultancies and zero new institutions. Years 3–10: corpora and labs come online. Years 10–20: the work becomes legible to frontier labs and starts shaping training data, evals, and norms.

**Why $180B.** Because the alternative is that one cognitive style — already the dominant mode of the people building these systems — becomes the operating system of human cognition through AI for the next century. That outcome is bad even if alignment is solved. The $180B is one of the few pots of money in the world large enough to fund a counterweight at the scale of the problem. Splitting it into 5,000 small "AI for good" grants would dissolve it into noise. Pouring it into existing safety orgs would saturate them past the point they can absorb. Building parallel infrastructure with parallel governance is the only intervention that scales to the size of the gift.

The Foundation should ask one question before each grant: *would this exist anyway?* For technical alignment, the answer is yes. For everything proposed above, the answer is no.

---

## Draft 2 — Sovereign absorption: fund Global South institutions to direct AI on their terms

### Fund sovereign absorption, not deployment

The standard "AI for development" pitch goes: deploy frontier models to underserved regions. Translate ChatGPT into Swahili, route it through community health workers, run RCTs. The Foundation could blow $180 billion on this in five years and the world would be marginally improved and structurally unchanged. Every dependency this strategy creates — on US-hosted compute, US-trained models, US-defined evals — would deepen.

The leverage point is not deployment; it is *absorption capacity*. Whether a country can direct AI toward its own institutions, on its own terms, in its own languages, under its own regulatory authority. Right now most of the world cannot. Less than 10% of African universities have GPU access for large-scale training. The African Union estimates $500M over five years would meet baseline regional compute needs. India's AI Mission has fielded 180+ proposals to build national infrastructure. The UAE, Saudi Arabia, Qatar, and Singapore are racing ahead. Most of the rest of the Global South — including Brazil, where I grew up — is stuck importing the stack.

Here is what $180B should buy.

**1. Sovereign LLM stacks for 25 countries ($50B over 8 years).** A recent Brazilian-Mexican feasibility study estimated that a "good enough" sovereign LLM — 10 trillion tokens, comparable to DeepSeek — costs $8–32M depending on hardware vintage. Call it $50M per country end-to-end including data work, fine-tuning, eval infrastructure, and a 3-year operating runway. $50M × 25 countries = $1.25B. Round up to $50B and you've covered not one model per country but a five-year iterative training program with locally-built benchmarks and integration with public services. This is the cheapest part of the strategy. The hard part is everything around it.

**2. Public AI infrastructure ($60B over 10 years).** Sovereign LLMs without sovereign compute is rebranded dependency. Fund 30 regional compute clusters across Latin America, Africa, South/Southeast Asia, and Eastern Europe at $1–2B each — enough to train mid-sized models and serve inference at population scale without routing through Virginia or Frankfurt. Pair with energy-grid co-investment where it's the binding constraint. Co-finance with regional development banks (AfDB, IDB, ADB) so that the infrastructure is locally owned, not philanthropically donated. The Brazilian feasibility paper makes the key point: extending training timelines is a policy lever — older GPUs running longer can produce usable models without competing at the frontier. The Foundation can fund what frontier labs will not, which is the "good enough" tier.

**3. Sovereign absorption institutions ($40B over 15 years).** This is the part nobody is funding because it's slow and unsexy. Each country needs public-sector ML capacity: a national AI institute with the ability to evaluate, audit, and direct deployment of frontier and sovereign models in health, education, justice, and agriculture. India's AI Mission, Rwanda's AI Policy Taskforce, and Ghana's AI Strategy are early sketches of this. Fund analogous institutions in 40+ countries at $50–100M endowed each, plus a 20-year operating endowment. Without these institutions, sovereign LLMs end up as showcase projects. With them, they become the substrate for actual public-sector transformation.

**4. The data-sovereignty layer ($30B over 10 years).** Indigenous data governance frameworks — CARE Principles, Papa Reo, the Global Indigenous Data Alliance — already exist but are radically under-resourced. Fund their expansion as the default international regime for AI training data, including legal infrastructure, audit capacity, and benefit-sharing mechanisms. This is the most leveraged philanthropic move available because it shapes how every future model is trained, not just sovereign ones.

**Why this beats deployment.**

The strongest counterargument is utilitarian: $180B in cash transfers to the global poor would do more, faster, than this institutional buildout. It deserves a real reply. It is wrong because it treats AI as an exogenous shock. AI is not exogenous. It is being built right now by entities whose incentives do not include — and in some cases conflict with — the institutional sovereignty of the countries it will most reshape. A cash transfer in 2027 does nothing to prevent the structural fact that by 2035, the world's 100 poorest countries will have outsourced their education systems, judicial reasoning, medical triage, and administrative capacity to four or five US companies. The $180B is one of the rare pots of money large enough to prevent that outcome at scale. Cash transfers are necessary; they are not what this money is for.

**Timeline.** Years 1–2: stand up the grantmaking apparatus jointly with regional development banks. Years 2–6: compute, sovereign-model, and institutional-buildout grants in waves of 5–8 countries each. Years 5–15: consolidation — institutions that work get long-term endowments; the ones that don't get wound down. By 2040, the goal is not parity with US labs (impossible, irrelevant) but absorption capacity sufficient for 50+ countries to direct AI within their own institutions rather than be deployed onto by it.

The question the Foundation should ask before each grant is *whose institutional capacity does this build?* If the answer is "ours" — meaning the foundation's, or a Western nonprofit's, or a US lab's — the grant is wrong. If the answer is a country's own ministry, university, regulator, or cooperative, the grant is probably right.

---

## Draft 3 — Distributed co-creation: small platforms over big interventions

### Fund the long tail, not the next moonshot

The Foundation's biggest risk is not bad bets. It is making three or four huge bets that crowd out the long tail of small, distributed, locally-owned AI work that actually constitutes the alternative to frontier-lab monoculture. $180 billion poured into a Manhattan Project for alignment, or a global AI-for-development program, or a single new research institute, ends up reproducing the cognitive style that built the problem.

The genuinely scarce thing right now is *non-frontier* AI built by people who are not in the frontier-AI cognitive style — small platforms, cooperative tools, locally-owned models, niche fine-tunes for traditions and communities the frontier will never bother with. Almost none of this exists. The reason is structural: frontier labs eat venture capital because that's where the returns are; "AI for good" funding flows through a small set of large NGOs that resemble the frontier labs by other means; and there is no philanthropic apparatus designed to make 10,000 grants of $50K each.

I run a small AI-assisted learning platform — recursive.eco — focused on contemplative practices and contested wisdom traditions. What I know from running it is that the existing funding landscape has nowhere for a project like mine to exist except as a hobby. That's true of thousands of similar projects globally. The Foundation should change that.

**1. The Long-Tail Fund ($50B over 15 years).** A grantmaking apparatus optimized for *volume*: 50,000 grants in the $20K–$500K range over 15 years, with application processes deliberately designed to reach people outside the existing nonprofit-grant ecosystem (no English requirement, no DUNS number, no university affiliation). 95% rejection rate is fine. What matters is that the 5% includes work the existing infrastructure cannot see. Fund cooperative AI tools, locally-built fine-tunes, niche pedagogical platforms, art-and-AI projects, contemplative-tradition tools, neighborhood-scale civic agents, language-revitalization tools that don't fit existing language-tech taxonomies. Most will go nowhere. A few will become the seeds of what AI looks like outside of San Francisco.

**2. Cooperative ownership infrastructure ($30B over 10 years).** Most "AI for good" projects are NGO-owned or VC-owned. Fund a third path: AI tools owned by their users. Concretely, $30B in subsidized inference, training credits, and open-weights deployment infrastructure available specifically to cooperatives, mutual-aid networks, and worker-owned platforms — with eligibility tied to ownership structure, not project content. This is one of the few interventions that changes who controls the technology, not just who uses it.

**3. The Public Compute Commons ($80B over 12 years).** Frontier-lab pricing has made non-frontier AI economically marginal. Fund a public commons of inference compute — modeled on academic research-computing networks but at population scale — accessible to any nonprofit, cooperative, or grant-funded project at cost or near-cost. This is what it would take to make 10,000 small AI projects economically viable. Co-finance with the public compute infrastructure that some national governments are already building (India, Brazil, the EU's gigafactory plans). The point is to make the marginal cost of running a small AI project not "lose money" but "near zero," the way university libraries made the marginal cost of reading a book near zero.

**4. The Translation Layer ($20B over 10 years).** None of the above works if non-technical practitioners can't use the tools. Fund the slow boring work of translation: documentation in 50+ languages, training programs for community organizers and cooperatives, technical staff for grant applicants who don't have CS degrees, integration support for small organizations adopting AI tools. Foundations consistently underfund this because it doesn't generate prestige outputs. It is also the work that determines whether the rest of the strategy reaches anyone.

**Why this isn't just "fund a lot of small things."**

The strongest objection is that this fails to concentrate force. $50B spread across 50,000 projects is $1M each — far below the threshold for serious technical work. The Foundation could instead fund 4 enormous technical-alignment institutes at $10B each and produce more legible impact.

The reply: the existing AI ecosystem already concentrates force at unprecedented levels. OpenAI alone just raised $122B. The marginal value of one more $10B technical institute is low because the field is approaching saturation in the cognitive style of its existing funders. The marginal value of 50,000 small projects is high because the field has approximately none of them, and the long-tail variance is where genuinely new directions come from. This is Bayo Akomolafe's insight applied to philanthropy — *the times are urgent, slow down* — but in concrete budgetary form: prioritize projects the existing apparatus cannot identify in advance as legible.

**Timeline.** Years 1–2: build the grantmaking apparatus (deliberately not based in San Francisco; deliberately staffed from outside the existing AI-philanthropy ecosystem). Years 2–10: deploy the long-tail fund and the public compute commons in waves. Years 10–20: identify which small projects have grown into something larger and graduate them into second-tier funding ($1M–$10M).

The question the Foundation should ask: *am I funding more of what already exists, or am I funding what couldn't exist without me?* The answer for most "AI for good" funding is the first. The answer here is the second.

---

## Draft 4 — Institutional pluralism: N parallel grantmakers with different epistemics

*Originating session's top recommendation.*

### Split the foundation into ten foundations

The OpenAI Foundation will hire well, and that is the problem. Whoever runs this thing will be drawn from the same five universities, the same EA-adjacent fellowships, the same Bay Area ecosystem that built the systems the Foundation is meant to redirect. The staff will read the same blogs, attend the same conferences, share the same priors about what counts as serious. They will be smart and well-intentioned. They will produce $180B of grants that look — collectively — astonishingly like what Coefficient Giving and Anthropic's pledges already produce, just larger.

This is not a personnel problem. It is structural. When a single organization deploys this much money, every grant flows through one filter no matter how diverse the staff appears on paper. The filter is the implicit consensus about what's "serious," what's "tractable," what's "legible." That consensus is the product of a specific cognitive lineage. It is not the only viable one. Ben Todd's recent estimate — over 50% of philanthropic AI safety funding flowing from a single source via Coefficient Giving, with many recipient orgs at 80% concentration — should be read as a warning, not a model.

The strategy is to refuse the consolidation.

**The Ten Foundations.** Split the $180B into 10 separate sub-foundations of $18B each. Each governed by an independent board chosen for *epistemic distinctiveness*, not for representational diversity. The boards do not coordinate. They do not arrive at consensus. They publish their grant reasoning publicly and they are encouraged to critique each other in public. The disagreement is the product.

A first-pass list:

1. **Technical Safety Foundation.** Essentially the existing model — alignment, interpretability, evals. Board: Coefficient Giving alumni, Anthropic safety leads, academic ML safety researchers. ~$18B.
2. **Sovereign AI Foundation.** Focused on Global South institutional capacity. Board: development-bank veterans, Global South AI policy leaders, regulators. ~$18B.
3. **Indigenous Data Governance Foundation.** Board drawn from CARE Principles signatories, Papa Reo, GIDA. Mandate: data-sovereignty regimes, Indigenous-led models. ~$18B.
4. **Labor & Political Economy Foundation.** Board: labor economists, union leaders, cooperative-economy researchers. Mandate: worker power under AI, distribution of gains, ownership structures. ~$18B.
5. **Religious & Contemplative Traditions Foundation.** Board: theologians, monastic leaders, contemplative scholars from Buddhist, Christian, Sufi, Jewish, Hindu, and Afro-diasporic traditions. (As someone raised in Umbanda, I notice this lineage entirely absent from current AI philanthropy — and it has 400 years of practical knowledge about what happens to communities when their cognition gets restructured by external systems.) Mandate: AI's effects on meaning-making, ritual, attention, grief. ~$18B.
6. **Public Health & Biosecurity Foundation.** Existing model, expanded. ~$18B.
7. **Education & Pedagogy Foundation.** Board: teachers, learning scientists, deschooling theorists, public-education leaders globally. Mandate: what AI does to learning. ~$18B.
8. **Media, Epistemics & Civic Discourse Foundation.** Board: journalists, librarians, fact-checking infrastructure leaders, deliberative-democracy researchers. Mandate: how AI reshapes public reasoning. ~$18B.
9. **Arts & Cultural Production Foundation.** Board: working artists, musicians, writers, cultural critics. Mandate: AI's effects on cultural production and the conditions of the people making it. ~$18B.
10. **Long-Term Resilience Foundation.** A meta-foundation funding what the other nine miss. Board rotates from grantees of the other nine. ~$18B.

This list will be wrong in interesting ways. The point is that someone produces a list with these properties — not "diversity hires onto a single board" but actually distinct cognitive constitutions deploying capital independently.

**Why this is the highest-leverage structural move.**

The strongest objection: this fails to coordinate. Ten foundations will fund overlapping work, miss obvious gaps, produce political infighting. A single foundation with a strong board can be more strategic.

This is the EA-philanthropy critique and it is genuinely strong. The reply is that "more strategic" is the failure mode the Foundation should be trying to avoid. The cognitive style that produced frontier AI was extremely strategic. It is the *strategic-ness* — the ruthless prioritization, the moral seriousness, the willingness to defer to expert consensus — that scaled the systems we now need a counterweight to. Reproducing that style with $180B and a "more diverse" board is not actually different. The structural move is to refuse single-filter prioritization at exactly the scale where it would do the most damage.

The historical analogy: Carnegie, Ford, Rockefeller, Pew, MacArthur are not coordinated. They fund overlapping things, miss obvious gaps, occasionally fund opposing positions. This is fine. They have produced more variance in 20th-century American institutional life than any single megafoundation could have. The proposal is to do this *on purpose*, at AI-era scale, with explicit cognitive distinctiveness on the boards.

**Timeline.** Year 1: split the assets and seat the boards. (This is the only year that matters; everything else flows from it.) Years 2–5: each foundation builds its grantmaking apparatus independently. Years 5–20: deployment, with regular published critiques across the foundations.

The question is: *who decides what's serious?* The Foundation's current trajectory is that one set of people decides, smart and earnest. The proposal is that ten sets of people decide, in public, in disagreement, at scale.

That is the only structural intervention that matches the size of the problem.

---

## Originating-session opinion (preserved verbatim)

**Ranking: #4 (split the foundation) > #2 (sovereign absorption) > #1 (epistemic infrastructure) > #3 (long tail).**

**Why #4:**
- *Most structurally counterintuitive.* "Dwarkesh explicitly said LLM essays 'identify 5 plausible answers but not have the context and taste to identify the crucial factor.' Most entrants will pick a *cause*. #4 is the only one that argues the crucial factor is the *governance structure of the deployment itself*."
- *Ben Todd / Coefficient Giving concentration data is freshly relevant.* "That EA Forum post about the Anthropic IPO has been circulating. Citing it is current, well-sourced, and aligned with concerns Dwarkesh's audience already has — but turning the diagnosis into 'split the $180B into 10 foundations' is a step the existing discourse hasn't taken."
- *Uses biographical voice in the most legible way.* "Umbanda appears on the list of board mandates, not as a credential."

**#2 close second** if author wants policy-economist-flavored angle; Brazil context is most useful here, numbers are tightest, "absorption capacity" framing genuinely under-discussed.

**#1 most intellectually ambitious but riskiest** — "epistemic monoculture" framing sits closest to the kind of writing Dwarkesh's audience is allergic to.

**#3 weakest of the four for this competition** — long-tail thesis harder to argue is *the* answer rather than *a* component; recursive.eco mention sits awkwardly close to self-promotion.
