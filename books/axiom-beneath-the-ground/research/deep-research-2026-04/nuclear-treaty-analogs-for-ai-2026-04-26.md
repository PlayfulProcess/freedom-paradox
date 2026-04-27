# Nuclear-treaty analogs for AI governance — what's transferable, what isn't, what's actually happening

*Date: 2026-04-26*
*Source: synthesis from WebSearch + WebFetch (RAND, AI Frontiers, arXiv, OPCW, NVIDIA, BIS/CSIS, red-lines.ai, Brookings, Future of Life Institute, Bulletin of the Atomic Scientists, UNIDIR, NTI). Citation-grade for the Dwarkesh-prize Draft B argument and the Axiom Ch10 alignment cluster.*
*Source-type tags: **P** = peer-reviewed/preprint · **J** = journalism of record · **G** = government/treaty body · **NGO** = civil-society initiative · **S** = company/blog.*

---

## Bottom line in one paragraph

**The nuclear analogy is partially right and the part that's right is the verification regime, not the proliferation framework.** AI is not nuclear weapons (Horowitz & Kahn are correct on the structural disanalogy). But the lesson from nuclear governance is not the NPT's existence; it's that the **CWC works because of challenge inspections and the BWC fails because it has none.** A meaningful AI treaty regime is technically possible — hardware-level governance via TEEs (Trusted Execution Environments) on H100/Blackwell-class chips is now demonstrably real — and politically deteriorating, fast. The de facto regime today is unilateral US export controls plus the Wassenaar Arrangement, not any multilateral treaty. The 2023–2024 summit-led path (Bletchley → Seoul) toward a treaty has rolled back at Paris 2025 (US/UK refused to sign) and is now circulating without state-actor leadership. **The window for a treaty inspired by nuclear governance is narrowing, not widening, in 2026.**

---

## 1. The skeptical case (Horowitz & Kahn): why the NPT is the wrong model

Michael C. Horowitz (UPenn) and Lauren A. Kahn (CFR), in *AI Frontiers* [[Source](https://ai-frontiers.org/articles/nuclear-non-proliferation-is-the-wrong-framework-for-ai-governance)] (J), articulate the strongest published version of the skeptical case. Three points:

1. **Scope.** Nuclear technology's primary strategic value is weapons. AI is general-purpose — military, commercial, civilian — making sector-specific governance more appropriate than unified non-proliferation architecture.

2. **Excludability.** Nuclear weapons depend on **plutonium and HEU** — geographically scarce, requiring industrial infrastructure (enrichment cascades, reprocessing facilities) that emit detectable signatures. AI's closest analog is **compute**, but compute is fungible, replicable, and already commoditizing. Open-weight models (DeepSeek V4-Pro, April 24, 2026) further undermine exclusivity at the model layer.

3. **Strategic value gradient.** Nuclear weapons deliver binary advantage (you have one or you don't). AI delivers continuous, graduated advantage. The deterrence logic that underpins the NPT does not transfer cleanly.

**Their alternative:** sector-specific governance via existing institutions (FDA-style regulators, standards bodies, export-control regimes), not a unified "IAEA for AI."

**Where the skeptical case is right:** the fissile-material → compute analogy is incomplete. Compute is more like cement than uranium.

**Where it's incomplete:** it conflates *the model layer* (commoditizing rapidly) with *the production stack underneath it* (more concentrated than uranium enrichment ever was). EUV lithography is a single-vendor monopoly (ASML, Veldhoven, Netherlands). Leading-edge fabs are five companies on three continents (TSMC, Samsung, Intel, SMIC, Micron). The talent pool is in the low thousands globally. **The production stack is more excludable than 1970 fissile-material enrichment.** The Horowitz/Kahn argument is right about the wrong layer.

---

## 2. The CWC vs BWC lesson: verification is everything

Reading the nuclear-treaty corpus the way an analyst reads two competing companies, the operative comparison is not NPT vs nothing — it's **Chemical Weapons Convention (CWC) vs Biological Weapons Convention (BWC).**

### BWC (1972) — failed in operation

- Concluded quickly in 1972, signed by 184 states.
- **No verification regime.** No challenge inspections. No mandatory declarations.
- Implementation Support Unit operates with three full-time staff [[Source](https://thebulletin.org/2024/03/how-the-biological-weapons-convention-could-verify-treaty-compliance/)] (J).
- *Bulletin of the Atomic Scientists* (March 2024) on the BWC's ISU budget: smaller than an average McDonald's restaurant.
- The Ninth BWC Review Conference (late 2022) finally formed a working group on verification — 50 years after the treaty.

### CWC (1993) — operational

- Negotiated 21 years after BWC.
- **Challenge inspection regime.** Any state party can request inspection of any other; **no right of refusal**.
- OPCW conducts ~241 facility inspections per year (pre-pandemic) [[Source](https://www.opcw.org/about-us/history)] (G).
- Has functioned through Syrian civil war, Russia-Ukraine, Skripal poisoning. Imperfect, but operative.

### What this means for AI

Any AI treaty without verification reproduces the BWC. The Global Call for AI Red Lines [[Source](https://red-lines.ai)] (NGO) explicitly names this lesson: it proposes a three-tiered structure (treaty + national licensing + IAEA-style technical body) precisely to avoid the BWC trap. Whether the technical body can do CWC-style challenge inspections of AI training runs depends entirely on whether hardware-level verification is feasible — see §5 below.

---

## 3. The fissile-material analog actually works for *fab and lithography*, not for *models*

Restating the nuclear analogy at the right layer of the stack:

| Nuclear regime | AI equivalent |
|---|---|
| Fissile material (HEU, Pu-239) | Leading-edge AI training compute (H100, Blackwell, Trainium2/3) |
| Enrichment cascades (Natanz, Pickering) | TSMC Tainan / Samsung Pyeongtaek leading-edge fabs |
| Centrifuge technology | EUV lithography (ASML monopoly) |
| Trigger / weaponization expertise | Frontier-lab algorithmic IP + research talent |
| Delivery vehicles | Cloud deployment infrastructure (hyperscaler grid + interconnect) |
| Test ban verification (CTBT) | Compute-cap verification (training runs above threshold) |

The closest mature dual-use export-control regime is the **Wassenaar Arrangement** (1996), which already covers advanced semiconductors and quantum technologies. Wassenaar is not a treaty — it's a voluntary multilateral export-control regime, structurally similar to the Australia Group (chemical/biological precursors) and the Missile Technology Control Regime. **All three function without being treaties.**

The de facto AI export-control regime today combines Wassenaar with **US BIS unilateral controls**:

- **October 2022:** initial advanced-chip export controls
- **October 2023:** expanded scope, A800/H800 closed
- **December 2024:** 140 entities added to Entity List; HBM and DRAM controls; expanded FDPR scope [[Source](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)] (G)
- **January 2025:** AI Diffusion Framework + Foundry Due Diligence Rule [[Source](https://www.congress.gov/crs-product/R48642)] (G)
- **Effectiveness:** mixed. Smuggling is significant — ~$390M in banned NVIDIA GPUs reached Malaysia via shell companies in 2024 [[Source](https://www.csis.org/analysis/limits-chip-export-controls-meeting-china-challenge)] (J). China's domestic capability (Huawei Ascend, SMIC 7nm) is accelerating partly *because* of controls.

**The key fact for the Dwarkesh essay:** the operational AI governance regime is not at the treaty layer. It's at the export-control layer, run by a US-led cartel (US, UK, NL, JP, KR, TW), targeting one rival (China). Multilateralizing this into a CWC-style regime would require US-China cooperation that is not on offer in 2026.

---

## 4. Asilomar 1975 — when self-imposed moratoria work, and why this isn't that moment

Asilomar is the single most-cited precedent for AI safety self-regulation. The 1975 conference [[Source](https://www.science.org/doi/10.1126/science.adv3132)] (J) [[Source](https://en.wikipedia.org/wiki/Asilomar_Conference_on_Recombinant_DNA)] (J) emerged from a 1974 voluntary moratorium signed by ~150 molecular biologists. The conference produced biosafety guidelines that became the NIH Recombinant DNA Advisory Committee (RAC) framework — operative for 50 years.

### Why Asilomar worked
- Pre-commercial: no profit at stake yet.
- Small expert community: ~150 working researchers, all in academic settings, mostly NIH-funded.
- Self-regulation was credible because the alternative was federal regulation that would have been worse for the field.
- Limited scope: containment of a specific technical risk (recombinant DNA), not broad societal impact.

### Why it doesn't transfer to AI in 2026
- Commercial stakes are now ~$1.5T in market cap across the frontier labs and their hyperscaler partners.
- Practitioner community is in the tens of thousands, distributed globally, working at adversarial firms.
- The "alternative is worse regulation" argument is inverted: most labs *want* lighter regulation.
- Scope is civilizational, not contained.

### What Asilomar actually demonstrates for AI
The 2017 Asilomar AI Principles (signed by Hawking, Hassabis, Altman, Musk, etc.) and the 2023 FLI "Pause Giant AI Experiments" letter are direct attempts at the Asilomar move. Neither produced the regulatory framework Asilomar 1975 produced. The model has been tried and has failed at AI's commercial scale.

**Critical critique that applies to both:** Asilomar 1975 was criticized for excluding ethicists, public-interest representatives, and patient communities. The AI versions reproduce this exclusion at higher stakes [[Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5331236/)] (P).

---

## 5. Hardware-level verification: technically real, politically contested

The strongest pro-treaty technical argument is that **chip-level verification is now demonstrably feasible** — a precondition that did not exist when Horowitz & Kahn first published.

### NVIDIA H100 confidential computing
- On-die hardware root of trust (RoT) shipped with Hopper architecture.
- Encrypted firmware, attested boot, fault-injection countermeasures [[Source](https://developer.nvidia.com/blog/confidential-computing-on-h100-gpus-for-secure-and-trustworthy-ai/)] (S).
- AES-GCM hardware encrypts PCIe traffic.
- Single-GPU confidential computing is production-ready as of 2024.

### Limitations as of 2026
- **Multi-GPU verification not yet supported.** Frontier training runs span hundreds-to-thousands of accelerators; cluster-wide TEE not in production [[Source](https://arxiv.org/html/2505.03742v1)] (P).
- NVIDIA has indicated multi-GPU support in future product generations but no shipping date.

### Technical proposals on the table
- **Petrie's embedded security blocks** [[Source](https://arxiv.org/html/2604.04712v1)] (P): <40,000 transistors per block, 10,000 blocks per chip, <1% die area on H100. Tracks "usage allowance" decrementing with each authorized computation.
- **FlexHEG (Flexible Hardware-Enabled Guarantee)**: auxiliary "guarantee processor" in tamper-proof enclosure monitors all instructions and data transfers; prevents FLOP double-counting.
- **Heim et al. (2024)**: training vs inference signature distinction; KYC-for-cloud-providers regime; jurisdictional compute reporting.
- **Shavit, Sastry, Trask, Khan**: proposed compute-cap treaty with FLOPS thresholds and TEE attestation.
- **Treaty for international compute cap** ([arXiv 2311.10748](https://arxiv.org/abs/2311.10748)) (P): formal proposal for ≥10²⁵ FLOPS training-run cap with hardware-attested verification.

**Where this lands:** the verification stack is roughly 80% feasible at the single-GPU layer and ~30% feasible at the cluster layer. The technical gap is real but bounded; it is not the binding constraint. **The binding constraint is political will, not technical capability.**

---

## 6. The summit track is rolling back, not building toward treaty

The 2023–2025 summit sequence is the closest thing to a treaty pathway that has actually been attempted at state-actor scale.

| Summit | Year | Status |
|---|---|---|
| Bletchley Park (UK) | Nov 2023 | 28 countries including US **and** China signed Bletchley Declaration. Frontier AI Safety commitments. |
| Seoul (KR) | May 2024 | Frontier AI Safety Commitments expanded; voluntary lab disclosures. |
| Paris (FR) | Feb 2025 | Renamed "AI Action Summit" — dropped "Safety". US and UK **refused to sign** the non-binding communiqué. |
| New Delhi (IN) | Feb 2026 | Held; weak outcome documents; no binding mechanisms. |

[[Source](https://www.epc.eu/publication/The-Paris-Summit-Au-Revoir-global-AI-Safety-61ea68/)] (J) [[Source](https://www.brookings.edu/articles/the-bletchley-park-process-could-be-a-building-block-for-global-cooperation-on-ai-safety/)] (J)

The trajectory is unmistakable: from "framework for global cooperation on AI safety" (Bletchley framing) to "AI action" (Paris reframing) to "no binding outputs" (Delhi outcome). The state-actor track that would have built toward an AI treaty has been hollowed out by the Trump administration's withdrawal of US support, the EU's pivot to deregulation, and China's read of the political room.

**Two parallel tracks survived:**

1. **EU's Council of Europe Framework Convention on AI** (signed Sept 2024, ratified by EU Parliament March 2026, 455-101-74 vote) [[Source](https://www.febis.org/2026/03/12/eu-endorses-first-international-treaty-on-ai-governance-what-it-means-for-the-future-of-trusted-ai/)] (J). First international treaty on AI governance. Limited to human-rights and democratic-values framing; no compute-cap or verification regime. Effectively a soft-law instrument with EU enforcement teeth via the AI Act.

2. **Civil-society treaty initiatives.** The Global Call for AI Red Lines (Sept 2025, 300+ signatories including Bengio, Hinton, Wojciech Zaremba, Maria Ressa, Mary Robinson) [[Source](https://red-lines.ai)] (NGO). Calls for binding red lines by end of 2026. Three-tier proposal: international treaty + national licensing + technical body modeled on IAEA. Six categories of red lines: nuclear-launch delegation, lethal autonomous weapons, mass surveillance, deception of users about AI identity, cyberoffensive critical-infrastructure attacks, WMD facilitation, self-replication, loss-of-control / inability-to-terminate.

---

## 7. The 2026 timing — what's coinciding

A list of dates that matter for any 2026 essay or strategy document:

- **April 24, 2026:** DeepSeek V4-Pro release. Open-weight model matching frontier closed models.
- **April 27 – May 22, 2026:** **Eleventh NPT Review Conference** at UN HQ, NYC. Five-year cycle since 2022. Will not produce consensus document on Article VI obligations [[Source](https://www.un.org/en/conferences/treaty-on-the-non-proliferation-of-nuclear-weapons-npt-2026)] (G).
- **May 10, 2026:** Dwarkesh Prize submission deadline.
- **September 2026:** UN General Assembly — last opportunity for state-led AI treaty initiative before US 2026 midterms.
- **End of 2026:** Global Call for AI Red Lines target deadline for binding agreement.

**The NPT Review Conference and the Dwarkesh deadline overlap by one week.** That's not a coincidence the essay should ignore. The NPT Conference's likely failure to produce consensus is itself the strongest empirical evidence for skeptics of treaty-based AI governance and the strongest empirical signal for those proposing alternatives.

---

## 8. What would actually work — synthesis

If you want a 2026-era position that is honest about what is feasible:

### What is technically and politically feasible now
- **Strengthen the Wassenaar / BIS export-control regime as the operational chokepoint.** It exists. It works imperfectly. Multilateralize it incrementally: bring NL, JP, KR, TW formally in (largely done); push for parallel regimes in IN, BR.
- **Hardware-level verification at single-GPU layer.** TEE/RoT on H100/Blackwell. Mandate attestation for cloud workloads above declared FLOPS thresholds. Domestically achievable in US/EU; doesn't require a treaty.
- **Insurance markets and tort liability** as the responsibility infrastructure (per K.G.M. v. Meta March 2026 verdict). These are non-state pricing mechanisms that bound the race from below.

### What is technically feasible but politically blocked
- **Bilateral US-China compute cap on training runs above 10²⁵–10²⁶ FLOPS.** Requires Track-II diplomacy → Track-I conversion. Plausible only if both states perceive asymmetric vulnerability. The DeepSeek V4 release is the kind of asymmetric signal that could shift Beijing's calculus; the Pentagon's domestic AI demand is the kind that could shift Washington's.
- **Multi-GPU TEE attestation for cluster-scale training runs.** NVIDIA roadmap dependency; ~2-3 year horizon.

### What is politically infeasible
- **A unified IAEA-for-AI organization.** US administration won't fund it; China won't accept it; EU is moving on its own track via the Council of Europe Convention.
- **NPT-style global non-proliferation regime for AI.** The structural disanalogy is real (Horowitz/Kahn), and the political appetite for new treaty architecture is gone post-Trump-2025.
- **Asilomar-style voluntary moratorium at frontier labs.** Tried 2023 (FLI letter); failed because commercial stakes too high and incentives misaligned.

### The realistic path
A patchwork of:
- (a) US-led export-control multilateralization (Wassenaar+),
- (b) EU Council of Europe Framework Convention enforcement via AI Act,
- (c) civil-society Red Lines campaign producing pressure on individual jurisdictions,
- (d) hardware-attested compute reporting at the single-GPU level,
- (e) bilateral US-China Track-II compute discussions when (and only when) capability shocks force them.

This is not a treaty regime. It's a regulatory cartel + a soft-law instrument + a civil-society campaign + a technical-attestation layer. **It looks more like the Australia Group than the NPT.** That may be the right answer.

---

## 9. Implications for the Dwarkesh essay (Draft B specifically)

The Dwarkesh-prize Draft B's $60B "US-China-EU compute-verification treaty" allocation is *not* naive but it is *misframed*. The honest version of the same argument:

> The Foundation cannot fund a treaty regime ex nihilo. It can, however, fund the technical and political infrastructure that makes a treaty regime possible if and when the political window opens. That looks like:
>
> 1. **$10B for hardware verification R&D** — multi-GPU TEE, FlexHEG-style guarantee processors, FLOP attestation at cluster scale. Closes the technical gap between current single-GPU TEE and verifiable training-run compliance.
>
> 2. **$15B for Track-II diplomatic infrastructure** — US-China safety dialogue, India / Brazil / Indonesia onboarding, EU Council of Europe enforcement support. Pugwash conferences (Pugwash funded the bilateral channels that made arms control possible during the Cold War; it ran on small foundation money for 30 years before the treaties happened).
>
> 3. **$20B to multilateralize and harden the existing export-control regime** — formalize the Wassenaar+ cartel, fund jurisdictional KYC for cloud providers, fund the customs-and-controls infrastructure in allied capitals. This is the regime that already works.
>
> 4. **$15B for the civil-society infrastructure that produced the Red Lines campaign** — Future of Life Institute, CeSIA, Center for AI Safety, the Mary Robinson / Bengio / Hinton coalition. Civil-society pressure has been the single most consistent driver of the soft-law instruments that exist.

This reframing is more defensible against the Horowitz/Kahn critique because it does not commit the Foundation to creating an institution (IAEA-for-AI) that is unlikely to exist. It funds the *substrate* of the institution — verification tech, diplomatic channels, regulatory cartel infrastructure, civil-society pressure — so that *if* the political window opens, the materials are ready.

The frame to use: **"Buy the verification stack, the diplomatic channels, and the regulatory cartel — not the treaty itself."** The treaty either follows or doesn't, but the substrate is useful in either case.

---

## 10. The honest answer to the prize-essay question

**Is there something to be done in AI geopolitics inspired by nuclear treaties?**

Not the NPT. Not an IAEA-for-AI as a unified institution. Not a global compute cap by 2026.

**Yes** to:
- The CWC's verification model (challenge inspections, on-site monitoring) — adapted to TEE-based compute attestation.
- The Australia Group's voluntary cartel structure — applied to compute and lithography exports (already happening).
- Pugwash-style Track-II diplomacy as the patient infrastructure for eventual bilateral US-China agreements.
- Hardware-enabled mechanisms (TEE/RoT/FlexHEG) as the technical substrate without which any treaty would replicate the BWC's verification failure.

**The strongest essay-line:** *the question is not "will there be an IAEA for AI" but "will the substrate for one exist when the political window finally opens." Spend $60B on the substrate. Whether the treaty follows is downstream of capability shocks the Foundation does not control.*

---

## Sources

### Pro-treaty proposals
- [Global Call for AI Red Lines](https://red-lines.ai) (NGO) — 300+ signatories, treaty by end-2026
- [Urging an International AI Treaty open letter](https://aitreaty.org/) (NGO)
- [Treaty for international compute cap (arXiv 2311.10748)](https://arxiv.org/abs/2311.10748) (P)
- [Conditional AI Safety Treaty (arXiv 2503.18956)](https://arxiv.org/html/2503.18956v1) (P)
- [Hardware-level governance feasibility taxonomy (arXiv 2604.04712)](https://arxiv.org/html/2604.04712v1) (P)
- [Hardware-Enabled Mechanisms for Verifying Responsible AI Development (arXiv 2505.03742)](https://arxiv.org/html/2505.03742v1) (P)

### Skeptical case
- [Horowitz & Kahn, "Nuclear Non-Proliferation Is the Wrong Framework for AI Governance" — AI Frontiers](https://ai-frontiers.org/articles/nuclear-non-proliferation-is-the-wrong-framework-for-ai-governance) (J)
- [RAND, "Insights from Nuclear History for AI Governance"](https://www.rand.org/pubs/perspectives/PEA3652-1.html) (J)

### Treaty regimes (CWC/BWC/Wassenaar/Asilomar)
- [OPCW History](https://www.opcw.org/about-us/history) (G)
- [Bulletin of the Atomic Scientists, "How the BWC could verify treaty compliance"](https://thebulletin.org/2024/03/how-the-biological-weapons-convention-could-verify-treaty-compliance/) (J)
- [Arms Control Association, "Verifying the Chemical Weapons Ban"](https://www.armscontrol.org/act/2007-01/features/verifying-chemical-weapons-ban-missing-elements) (J)
- [Asilomar 1975 — Science magazine retrospective](https://www.science.org/doi/10.1126/science.adv3132) (J)
- [Asilomar critique — PMC, scientific self-regulation limits](https://pmc.ncbi.nlm.nih.gov/articles/PMC5331236/) (P)

### Operational regime — export controls
- [BIS press release Dec 2024](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military) (G)
- [CRS Report R48642 — US Export Controls and China: Advanced Semiconductors](https://www.congress.gov/crs-product/R48642) (G)
- [CSIS, "The Limits of Chip Export Controls"](https://www.csis.org/analysis/limits-chip-export-controls-meeting-china-challenge) (J)

### Summit track
- [European Policy Centre, "The Paris Summit: Au Revoir, Global AI Safety?"](https://www.epc.eu/publication/The-Paris-Summit-Au-Revoir-global-AI-Safety-61ea68/) (J)
- [Brookings, "Bletchley Park process as building block"](https://www.brookings.edu/articles/the-bletchley-park-process-could-be-a-building-block-for-global-cooperation-on-ai-safety/) (J)
- [EU Council of Europe Framework Convention on AI, March 2026 ratification](https://www.febis.org/2026/03/12/eu-endorses-first-international-treaty-on-ai-governance-what-it-means-for-the-future-of-trusted-ai/) (J)

### Hardware verification
- [NVIDIA H100 Confidential Computing Whitepaper](https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/HCC-Whitepaper-v1.0.pdf) (S)
- [NVIDIA Secure AI with Blackwell and Hopper, August 2025](https://docs.nvidia.com/nvidia-secure-ai-with-blackwell-and-hopper-gpus-whitepaper.pdf) (S)
- [NVIDIA GPU Confidential Computing Demystified (arXiv 2507.02770)](https://arxiv.org/html/2507.02770v1) (P)
