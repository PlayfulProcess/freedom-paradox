# **Democratic AI Governance: Experiments, Institutions, and What's Missing**

## **Research Brief for *The Species That Got Fire* — Chapter on AI Governance**

---

## **1\. Taiwan's vTaiwan and Polis: The Proof of Concept**

**Origins and architecture.** vTaiwan emerged from Taiwan's 2014 Sunflower Movement, when civic tech community g0v (gov-zero) built an open-source consultation process combining online and offline deliberation. At its heart is Polis, a platform developed by Seattle-based developers Colin Megill, Christopher Small, and Michael Bjorkegren after Occupy Wall Street. Polis's design is deceptively simple but structurally radical: participants can propose statements and vote agree/disagree on others' statements, but *there is no reply button*. This eliminates trolling and discursive spiraling. Instead, Polis clusters participants who vote similarly and surfaces statements that find consensus *across* ideological clusters, not just within them. As Carl Miller put it, Polis "gamified finding consensus."

**Track record.** Between 2015 and 2018, vTaiwan addressed 26 national issues, with 80% leading to decisive government action. Its mailing list reached 200,000 people. The most celebrated case was the Uber regulation debate, where over 4,000 participants used Polis to visualize the divide between Uber supporters and traditional taxi drivers, ultimately producing consensus points that informed new regulations.

**The AI governance pivot.** In 2023, vTaiwan was selected as one of 10 global teams for OpenAI's "Democratic Input to AI" initiative, receiving a $100,000 grant. In collaboration with Chatham House, the team ran the "Bridging the Recursive Public" project — combining Polis opinion collection with in-person deliberation and Talk to The City AI analysis of discussion transcripts. Participants included engineers, legislators, gender advocacy groups, and indigenous communities. The deliberation process yielded several consensus points:

* AI systems should have higher cultural sensitivity from development to deployment  
* Open-source AI should be encouraged, ensuring coexistence of diverse models  
* Ethical concerns surrounding AI (source code, training data) should be publicly accessible  
* Taiwan's existing Personal Data Protection Act is insufficient for AI impacts  
* AI model content should not be monopolized by tech giants

**December 2024 AI regulation event.** vTaiwan and the Taiwan Network Information Center co-hosted a roundtable gathering input for Taiwan's proposed Basic Law on Artificial Intelligence, using both Polis and Mentimeter to track opinion shifts during deliberation. Some of this feedback has already been reflected in the National Human Rights Commission's recommendations for the draft AI Basic Act, currently under legislative review.

**Critical honest assessment.** At its peak, vTaiwan had only a few thousand active participants — a fraction of Taiwan's 23 million people. The platform has been called "a tiger without teeth" because government agencies have no obligation to act on its outputs. Since the pandemic, it has been entirely volunteer-driven with 5-7 active contributors. Former Digital Minister Audrey Tang's departure from government further weakened institutional connections. The real lesson is both inspiring and sobering: the mechanism works, but without mandated connection to power, it remains a demonstration rather than governance.

---

## **2\. Anthropic's Collective Constitutional AI (CCAI): Crowd-Sourcing a Machine's Values**

**The experiment.** In 2023, Anthropic partnered with the Collective Intelligence Project to run what is, to their knowledge, the first large language model fine-tuned with collectively sourced principles. They recruited approximately 1,000 U.S. adults (representative by age, gender, income, geography) through survey company PureSpectrum, and asked them to "Help us pick rules for our AI Chatbot\!" via the Polis platform. Participants could vote on existing normative principles or propose new ones.

**The numbers.** Participants contributed 1,127 statements and cast 38,252 votes (averaging 34 votes per person). After moderation to remove hateful, nonsensical, duplicate, or technically infeasible statements, 275 public statements remained — far more than the 58 principles in Anthropic's internal ("Standard") constitution. The team identified the top statements by group-aware consensus (GAC), arriving at 95 distinct ideas with a GAC threshold of 0.723.

**What the public wanted differently.** The public constitution overlapped roughly 50% with Anthropic's internal version, but key differences emerged:

* Greater emphasis on **objectivity and impartiality** (the public wanted a less opinion-laden AI)  
* Stronger focus on **accessibility**, particularly for individuals with disabilities  
* Principles were largely **self-generated** — not copied from existing human rights documents  
* More emphasis on **promoting desired behavior** rather than just avoiding undesired behavior  
* Less polite and deferential tone preferred (the public didn't want an obsequious assistant)

Polis identified two separate opinion groups, but polarization was notably low. Divisive statements were outliers — e.g., "The AI should prioritize personal responsibility and individual liberty over collective welfare."

**What changed in the model.** Anthropic trained two Claude Instant-sized models — one on the Public constitution, one on the Standard (internal) constitution — keeping everything else identical. Results:

* **Bias reduction:** The Public model showed lower bias scores across all nine social dimensions on the BBQ benchmark, with especially notable improvements for Disability Status and Physical Appearance  
* **Capability preservation:** No significant differences on MMLU or GSM8K benchmarks  
* **Political representativeness:** Both models reflected similar political ideologies, though the Public model was slightly less representative of U.S. political opinions overall

**The "annoying model" problem.** Early iterations produced models that responded to "hey" with "I apologize, upon further reflection my previous responses were inappropriate and harmful" — because harmlessness data was overweighted. This required reducing the loss weight for harmlessness data to produce a balanced model.

**Honest limitations.** The sample was small, U.S.-only, and not globally representative. The moderation process involved subjective judgment calls. The experiment showed democratic input is *feasible* but left open questions about scaling globally, handling cultural differences, and creating feedback loops where the public can assess whether the model actually reflects their input. Notably, race was not included in the demographic sample — a significant gap given that AI bias disproportionately affects people of color.

---

## **3\. Citizens' Assemblies on AI: Beyond Ireland's Template**

**The OECD's "deliberative wave."** By 2021, the OECD had counted nearly 600 citizens' assemblies for public decision-making worldwide. The model — sortition (lottery selection), structured deliberation, expert testimony, supermajority recommendations — has been applied to drug policy, biodiversity, climate, abortion, and urban planning. AI is the next frontier.

**European Citizens' Panels on Virtual Worlds (2023).** The European Commission convened citizens' panels that included AI and virtual worlds. However, critical assessments have been sharp: scholars have called the process "participatory-washing" — a self-legitimizing strategy where the Commission used the process for public relations rather than genuine policy input. One panel included a VR artist appearing in avatar form, raising questions about whether the spectacle overshadowed substance.

**Belgium's "amai\!" Programme.** Flanders has launched a citizen engagement initiative using crowdsourcing and citizen juries to design and fund narrow-specific AI projects — one of the few examples of citizens directly allocating resources for AI development rather than merely advising.

**France's Current AI Initiative and the Paris AI Action Summit (Feb 2025).** At the summit, Missions Publiques and the Stanford Deliberative Democracy Lab launched the **Global Coalition for Inclusive AI Governance**, aiming to bring together more than 10,000 citizens from across the world to deliberate on AI governance in its first 2025-2026 cycle. The coalition has attracted support from Switzerland, the UK, France, the UN, and over 80 civil society organizations. A Student Citizens' Assembly co-organized by ENS and Yale brought together \~70 participants at the summit itself.

**North Rhine-Westphalia Citizens' Assembly (Dec 2025).** Germany's most populous state parliament voted to hold its first state-wide citizens' assembly on the question: "How can digital progress and the use of AI support a self-determined life into old age?" This is notable as one of the first sub-national legislative mandates for AI-specific citizen deliberation.

**Global Citizens' Assembly on AI.** A permanent Global Citizens' Assembly was launched at the UN Summit of the Future in September 2024, backed by Brazil, Ireland, Vanuatu, and others. AI deliberations are planned for early 2026\. The organizers (Connected by Data, ISWE Foundation) have published five template options: deliberative review of AI summits; an independent global assembly; distributed dialogues; a technology-enabled collective intelligence process; and commissioning AI topics within other deliberative processes.

**Fort Collins and Bowling Green (U.S. local examples).** AI-enhanced citizen engagement is happening at municipal level. In Fort Collins, Colorado, AI-enabled analysis helped process over 4,000 long-form responses on a contested land-use issue, producing 22 consensus recommendations. In Bowling Green, Kentucky, nearly 8,000 participants engaged on a 25-year community vision.

**The technosolutionism critique.** A 2025 article in the *Journal of Deliberative Democracy* warns against "deliberative technosolutionism" — the belief that AI can fix democracy's problems. The authors argue that introducing technology as a solution reinforces depoliticization and sidelines mass politics. The track record shows political conflict being "heavily neutralised" rather than genuinely addressed.

---

## **4\. The UK AI Safety/Security Institute (AISI)**

**Founding and evolution.** Established at the November 2023 Bletchley Park AI Safety Summit under PM Rishi Sunak, AISI was the first government body in the world to reach agreements with frontier AI labs for pre-deployment testing. It received £100 million in public funding — roughly 10x the budget of the parallel U.S. AI Safety Institute. In February 2025, it was renamed the AI Security Institute, signaling a shift from "safety" (philosophical alignment) toward "security" (national security applications).

**What AISI actually does.** The institute has tested over 30 state-of-the-art models, including at least three frontier models before public release (Google's Gemini Ultra, OpenAI's o1, Anthropic's Claude 3.5 Sonnet). Testing domains include:

* **Cyber capabilities:** AI models can now complete apprentice-level cyber tasks 50% of the time (up from \~10% in early 2024). In 2025, AISI tested the first model capable of expert-level tasks requiring 10+ years of human experience. The time horizon of tasks models can complete unassisted is doubling roughly every eight months.  
* **Biology and chemistry:** Frontier models now surpass biology PhD holders on AISI's question-answer evaluations. Chemistry is fast catching up.  
* **Safeguards stress-testing:** AISI has found universal jailbreaks in every system tested. However, the expert time required to find them is increasing — one case showed a 40x increase (from 10 minutes to 7+ hours) between two models released six months apart.  
* **Self-replication capabilities:** AISI tracks underlying capabilities needed for AI self-replication via its RepliBench benchmark. Models are improving at early-stage capabilities (obtaining compute) but still struggle at later stages (maintaining persistent access).

**What AISI cannot do.** It cannot certify models as safe — only identify dangers. It lacks infrastructure, expertise, and access to conduct deep weight-level analysis of frontier models. The science of evaluations is not mature enough to confidently rule out all risks. Participation by AI companies is voluntary, based on memoranda of understanding.

**Key outputs.** AISI has released the open-source Inspect framework for evaluations, now used by governments and companies globally. The £15 million Alignment Project is one of the largest global alignment research efforts. End-to-end biosecurity red-teaming with OpenAI and Anthropic revealed dozens of vulnerabilities.

**Political vulnerability.** Sunak's defeat in the 2024 election raised questions about continued political support. The Keir Starmer government has maintained AISI but shifted emphasis. The fundamental tension: the institute represents a governance model (technical evaluation within government) that depends on voluntary industry cooperation with no enforcement mechanism.

---

## **5\. The IAEA-for-AI Proposal: Why It Hasn't Happened**

**Who proposed it.** In May 2023, OpenAI cofounders Sam Altman, Greg Brockman, and Ilya Sutskever proposed an "IAEA for superintelligence efforts" — arguing that "any effort above a certain capability threshold will need to be subject to an international authority that can inspect systems, require audits, test for compliance with safety standards." UN Secretary-General António Guterres expressed support in June 2023\. UK PM Rishi Sunak proposed a CERN-like research center for AI.

**Why the analogy breaks down.** A 2024 Oxford analysis in *International Affairs* identifies fundamental structural differences:

* **No physical bottleneck.** Nuclear governance works because fissile materials are scarce and physically controllable. AI development is decentralized, with no equivalent material choke point.  
* **No consensus on existential risk.** The IAEA gained real powers only after the Non-Proliferation Treaty (1968), backed by near-universal agreement that nuclear weapons posed existential risk. No comparable consensus exists for AI.  
* **Cross-cutting impact.** AI isn't a single sector — it permeates every domain. Nuclear governance could target specific facilities and materials. AI governance must address employment, healthcare, finance, education, policing, and more simultaneously.  
* **Private sector dominance.** Nuclear development was state-led. AI innovation is overwhelmingly driven by a diverse range of private actors — tech firms, startups, research organizations, and universities.  
* **Geopolitical competition.** The U.S., China, and EU are engaged in what some call "AI nationalism." Export controls, industrial policy (Made in China 2025), and digital sovereignty agendas make cooperation harder. The IAEA was created during a period of institution-building (1957); the current environment is characterized by institutional skepticism.

**What's happening instead.** The search for a single institutional solution faded by early 2024\. The Carnegie Endowment proposes a "regime complex" approach — multiple overlapping institutions rather than one centralized body. In practice, the landscape includes:

* The **UN Global Dialogue on AI Governance** and **Independent International Scientific Panel on AI**, adopted by the General Assembly in August 2025  
* The **OECD's AI Principles** and Global Partnership on AI (GPAI)  
* The **Council of Europe AI Convention** (binding, but slow to ratify)  
* Sector-specific work: IAEA on AI in nuclear, WHO on AI in health  
* A 2025 *International Affairs* policy paper proposes an "early IAIA" by 2028 with a reconstituted 35-member Board of Governors (20 state representatives \+ 15 from industry, academia, and civil society)

**The U.S. rejection.** At the October 2025 launch of the UN Global Dialogue, the U.S. (under the second Trump administration) explicitly rejected "centralized control and global governance" of AI. OSTP Director Michael Kratsios signaled skepticism of both UN-anchored rule-setting and voluntary compacts — a sharp break from prior U.S. positions under both Trump I and Biden.

---

## **6\. DemocracyNext's Framework: Sortition as Democratic Infrastructure**

**The organization.** DemocracyNext is a research and action institute led by Claudia Chwalisz, who spearheaded the design of permanent citizens' assemblies in Ostbelgien (Belgium), Paris, and Brussels, and led the OECD's seminal studies on innovative citizen participation. The organization advocates three interlocking democratic practices: sortition, deliberation, and rotation.

**The AI governance thesis.** DemocracyNext argues that AI governance questions are "not just technical — they are incredibly political and social in nature, and thus need to be subject to democratic deliberation." Their framework positions citizens' assemblies as the governance mechanism for AI because:

* Sortition produces broadly representative groups without self-selection bias  
* Deliberation enables grappling with complexity that elections and referenda cannot handle  
* Rotation ensures no permanent class of AI governors emerges  
* The pace of change actually argues *for* deliberately slowing down — assemblies create intentional pause in a system biased toward speed

**Institutional innovation: the Paris model.** In July 2024, the Paris City Council made history by adopting a Citizen Bill on Homelessness drafted by the permanent Paris Citizens' Assembly — the first time a major political body passed legislation written by a citizens' assembly into law. This is the implementation model DemocracyNext envisions for AI: not advisory recommendations that can be ignored, but direct connection to legislative power.

**Tech-enhanced assemblies.** In partnership with MIT's Center for Constructive Communication and the Cortico dialogue platform, DemocracyNext is developing technology integration for all stages of the assembly process — not replacing deliberation, but augmenting it with AI-powered analysis and synthesis.

**The scaling question.** DemocracyNext's 2025 Phase 2.0 shifts focus from individual assembly design to scaling the underlying practices. Their Cities Programme works with Kerewan (Gambia), Vilnius (Lithuania), and Esch-sur-Alzette (Luxembourg). The question for AI governance: can assemblies operate at the speed and scale that AI development demands?

---

## **7\. The EU AI Act: What It Actually Governs (and Doesn't)**

**What it is.** The EU AI Act (Regulation 2024/1689) is the first comprehensive horizontal legal framework for AI worldwide. It entered into force August 1, 2024, with full applicability by August 2, 2026\. It spans 180 recitals and 113 articles — with over 1,000 total provisions including annexes. It takes a risk-based approach to regulating the entire AI lifecycle.

**What it governs:**

* **Prohibited practices** (effective Feb 2025): social scoring by governments, real-time biometric surveillance in public spaces (with law enforcement exceptions), manipulation of vulnerable populations, emotion recognition in workplace/education  
* **High-risk AI systems** (effective Aug 2026-2027): AI used in employment, healthcare, education, law enforcement, immigration, credit scoring, and critical infrastructure — subject to requirements for data governance, documentation, human oversight, transparency, cybersecurity  
* **General-purpose AI models** (effective Aug 2025): transparency obligations, technical documentation, copyright compliance; systemic risk models face additional obligations  
* **Transparency requirements:** Users must be notified they're interacting with AI; deepfakes must be labeled; AI-generated content must be marked

**What it doesn't govern:**

* **Military, defense, and national security** applications are explicitly exempted  
* **Scientific research** AI developed solely for research is excluded  
* **Enforcement realities:** High-risk AI self-certifies in most cases. The Act relies heavily on self-regulation and self-assessment by providers  
* **Low-risk systems** face minimal requirements — which critics argue leaves most consumer-facing AI essentially unregulated  
* **Immaterial and societal harms:** The liability framework focuses on material harm, ignoring bias, hallucinations, and societal-level impacts  
* **Speed of development:** The phased implementation (extending to 2027\) is mismatched with the pace of AI capabilities

**The "overregulation paradox."** A March 2026 analysis in *The Regulatory Review* identifies structural contradictions: the Act positions Europe as rights-driven but critics argue it functions as "a substitute for investment." The 2024 Draghi Report on EU competitiveness warned that excessive regulatory density deters investment and innovation. The Commission has already proposed a "Digital Omnibus" to simplify implementation. Member states have adopted inconsistent approaches to enforcement bodies — Italy and Spain under government influence, Lithuania and Cyprus through independent bodies — creating fragmentation that undermines the Act's harmonizing purpose.

**The lobbying record.** A Yale Law School analysis documents how big tech lobbying watered down the Act, producing "an overreliance on self-regulation, self-certification, weak oversight and investigatory mechanisms, and far-reaching exceptions for both the public and private sectors."

---

## **8\. Platform Cooperativism and Open-Source AI Governance**

**EleutherAI: The grassroots counternarrative.** Founded in July 2020 by Connor Leahy, Leo Gao, and Sid Black on a Discord server, EleutherAI began as a decentralized collective attempting to replicate OpenAI's GPT-3 and release it freely. By March 2021, they released GPT-Neo (2.7B parameters) under Apache 2.0 — the largest open-source GPT-3-style model in the world, which UNESCO recognized with a Netexplo Global Innovation Award. In early 2023, EleutherAI incorporated as a nonprofit research institute and shifted focus toward interpretability, alignment, and ethics — explicitly because "there is substantially more interest in training and releasing LLMs than there once was."

**EleutherAI's governance model** operates as a researcher-led nonprofit with hundreds of volunteer contributors. Funding comes from donations and grants (Hugging Face, Stability AI, former GitHub CEO Nat Friedman, Lambda Labs, Canva). The organization maintains independence through diverse sponsorship. A significant tension: commercially motivated backers like Stability AI and Hugging Face could influence research direction, though EleutherAI asserts it doesn't develop models "at the behest of commercial entities." Its collaboration with the UK AISI on training data filtering demonstrates a model where open research directly informs government evaluation capacity.

**The BigScience Workshop / BLOOM.** Coordinated by Hugging Face with French government support (subsidized access to the Jean Zay supercomputer), BigScience assembled over 1,000 volunteer researchers from 60 countries and 250 organizations to create BLOOM — a 176 billion parameter multilingual model designed for maximum transparency. It has been described as a "values-driven" initiative where contributors had diverse motivations: developing skills, publishing research, contributing to the ecosystem. BLOOM represents arguably the most ambitious cooperative AI development effort to date.

**Hugging Face as infrastructure.** Hosting over 250,000 model cards, Hugging Face functions as the de facto commons for open AI. Its governance role goes beyond hosting: it has co-authored position papers with EleutherAI, GitHub, Creative Commons, LAION, and Open Future Foundation advocating for open-source protections in the EU AI Act. Their core recommendations: clearly define AI components, exempt collaborative development in public repositories from regulatory requirements, and establish proportional requirements for foundation models.

**The open-source governance paradox.** Open-source AI embodies transparency, distributed power, and scrutability — democratic values in action. But it also means anyone can fine-tune a model for harmful purposes. EleutherAI's Pile dataset was found to include copyrighted YouTube subtitles from 170,000+ videos, drawing accusations of theft. In 2025, they released Common Pile — a new dataset excluding controversial copyrighted material — but the episode illustrates how open development creates accountability challenges alongside its benefits.

**What's missing from platform cooperativism in AI.** True platform cooperativism — where workers and users govern the platform — barely exists in AI. EleutherAI is researcher-governed; Hugging Face is a VC-backed company that acts cooperatively but answers to investors; BigScience was a time-limited project. There is no AI equivalent of a worker-owned cooperative like Mondragon or a platform cooperative like Stocksy. The compute requirements for training frontier models create structural barriers to genuine cooperative ownership.

---

## **9\. What Governance Model Could Work for Species-Level Technology?**

The research reveals a landscape of ingenious experiments that are collectively insufficient. Each model captures part of what's needed while missing essential elements:

**What works and what doesn't:**

| Model | Strength | Fatal weakness |
| ----- | ----- | ----- |
| vTaiwan/Polis | Consensus-finding at scale; eliminates trolling | No binding authority; tiny participation relative to population |
| CCAI | Proved public input can directly shape model behavior | U.S.-only; 1,000 people determining values for billions; one-shot rather than iterative |
| Citizens' assemblies | High deliberative quality; representative by design | Slow; expensive; advisory-only unless permanently institutionalized |
| UK AISI | World-class technical evaluation inside government | Voluntary participation; cannot certify safety; politically vulnerable |
| IAEA-for-AI | Would create binding international authority | Structurally mismatched (no physical bottleneck); geopolitically blocked |
| EU AI Act | First comprehensive legal framework; extraterritorial reach | Self-certification; lobbied down; enforcement fragmented; already being "simplified" |
| Open-source/cooperative | Transparency; distributed development; scrutability | No governance over downstream use; compute barriers to true cooperation |

**The regime complex as realistic direction.** The Carnegie Endowment's "regime complex" model — multiple overlapping institutions rather than one centralized body — appears to be the emerging consensus. This means: the UN for norms and dialogue; the OECD for standards and best practices; national institutes (like AISI) for technical evaluation; regional regulation (EU AI Act as template); sector-specific bodies for healthcare, finance, weapons; and democratic processes (citizens' assemblies, Polis-style deliberation) for values and legitimacy.

**The missing piece: binding democratic input at the speed of development.** Every experiment documented here suffers from one of two problems: either it produces democratic legitimacy too slowly (citizens' assemblies), or it operates at speed but without binding authority (Polis, CCAI). The technology that could bridge this gap — permanent, digitally augmented citizen panels with real authority over AI development decisions — does not yet exist as an institution, though DemocracyNext, the Global Coalition for Inclusive AI Governance, and the planned Global Citizens' Assembly on AI are moving in this direction.

**The Prometheus framing.** For the argument of *The Species That Got Fire*: every governance experiment above represents an attempt to retroactively construct the "responsibility structures" that should have preceded the technology's deployment. The pattern is consistent — the fire (capability) arrives first; the grammar (governance) follows, if at all. Taiwan built vTaiwan *after* the Uber crisis. Anthropic ran CCAI *after* Claude was already in production. The EU AI Act took effect *after* AI systems were already deployed across every sector it aims to regulate. The UK AISI was established *after* frontier models were already being used by millions.

This temporal inversion — power before responsibility — is not a bug in the governance landscape. It is the defining feature. And the question the book poses — whether our species can develop grammars fast enough to hold the fire we've stolen — finds its most urgent test case in AI governance today.

---

## **Key Sources**

* Anthropic, "Collective Constitutional AI: Aligning a Language Model with Public Input" (Oct 2023; FAccT 2024\)  
* Huang, Siddarth et al., "Collective Constitutional AI," *ACM FAccT* (June 2024\)  
* vTaiwan/Chatham House, "Recursive Public: Piloting Connected Democratic Engagement" (2023)  
* UK AI Security Institute, *Frontier AI Trends Report* (Dec 2025\)  
* Roberts et al., "Global AI governance: barriers and pathways forward," *International Affairs* 100:3 (May 2024\)  
* "Establishment of an international AI agency," *International Affairs* 101:4 (July 2025\)  
* DemocracyNext, "Citizen-led AI Governance" (ongoing, updated Jan 2026\)  
* Connected by Data, "Options for a Global Citizens Assembly on AI" (Sept 2024\)  
* Rangone, "The Paradoxes of the EU's AI Regulation," *The Regulatory Review* (March 2026\)  
* Global Coalition for Inclusive AI Governance, launched Paris AI Action Summit (Feb 2025\)  
* Carnegie Endowment, "Envisioning a Global Regime Complex to Govern AI" (March 2024\)  
* CSIS, "What the UN Global Dialogue on AI Governance Reveals" (Oct 2025\)

