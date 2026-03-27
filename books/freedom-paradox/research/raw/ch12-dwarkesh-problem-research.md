# Raw Research: Chapter 12 — The Dwarkesh Problem

## Research Date: March 27, 2026

---

## 1. Dwarkesh Patel's Article: "The most important question nobody's asking about AI"

**Published:** March 11, 2026 (approx)
**URL:** https://www.dwarkesh.com/p/dow-anthropic
**Also discussed:** LessWrong post at https://www.lesswrong.com/posts/PDWFed8JT9FitPkzQ/dwarkesh-patel-on-the-anthropic-dow-dispute

### Core Thesis
- The Department of War (renamed from Department of Defense) declared Anthropic a supply chain risk because Anthropic refused to remove redlines around the use of their models for mass surveillance and autonomous weapons.
- Patel's key question: Within 20 years, 99% of the workforce in the military, government, and private sector will be AIs — soldiers (robot armies), superhumanly intelligent advisors and engineers, police, etc. Our future civilization will run on AI labor.
- The most important question: Who will this future AI workforce be accountable and aligned to, and who gets to determine that? Who writes the "model constitution" that shapes the characters of the intelligent, powerful entities that will operate our civilization?
- A sub-question Patel raises: If AI really is that pervasive and powerful, then when forced to choose between their AI provider and a DoW contract (tiny fraction of revenue), wouldn't most tech companies drop the government, not the AI?

### Implications for Open Source
- If the question is about who controls AI alignment and values, open-source models represent an answer: everyone and no one simultaneously.
- Once models are released as open weights, the "who decides" question becomes moot — thousands of actors make their own decisions.
- The proliferation of derivatives means governance cannot be centralized.

---

## 2. The Anthropic-Pentagon Confrontation (Feb-March 2026)

### Timeline
- **January 2026:** Defense Secretary Pete Hegseth issued an AI strategy memorandum directing all DOD AI contracts to incorporate "any lawful use" language within 180 days.
- **February 2026:** Anthropic refused to remove its two redlines: no autonomous weapons, no mass domestic surveillance.
- **February 24, 2026:** Anthropic published RSP v3.0, removing hard pause commitment (covered in Ch10).
- **February 27, 2026:** Trump administration ordered military contractors and federal agencies to cease business with Anthropic. Trump posted on Truth Social. CNN reported: "Trump administration orders military contractors and federal agencies to cease business with Anthropic."
- **February 27, 2026:** OpenAI announced Pentagon deal same day Anthropic was banned (NPR).
- **March 5, 2026:** Pentagon supply chain risk label narrower than initially implied, per CNN.
- **March 6, 2026:** Pentagon labels Anthropic supply chain risk "effective immediately" (NPR).
- **March 9, 2026:** Anthropic sues the Trump administration (CNN).
- **March 11, 2026:** Dwarkesh publishes "The most important question nobody's asking about AI."
- **March 24-26, 2026:** Federal judge blocks Pentagon designation, ruling it "ran roughshod over constitutional rights." Judge pressed DOD on "pretty low bar." Fortune described it as "attempted corporate murder."

### Anthropic's Stated Reasons for Redlines
- "First, we do not believe that today's frontier AI models are reliable enough to be used in fully autonomous weapons. Allowing current models to be used in this way would endanger America's warfighters and civilians."
- "Second, we believe that mass domestic surveillance of Americans constitutes a violation of fundamental rights."

### Government Response
- The supply chain risk designation had previously been used only for companies connected to foreign adversaries.
- DOW records show designation was made because of Anthropic's "hostile manner through the press."
- All government agencies given 6 months to phase out Anthropic products.

### OpenAI's Position
- Sam Altman publicly stated OpenAI shares Anthropic's "red lines" (OPB, Feb 27, 2026).
- Same day, OpenAI announced Pentagon deal after Anthropic banned.
- OpenAI published "Our agreement with the Department of War" blog post.

---

## 3. Open-Source AI Proliferation Statistics

### Hugging Face Ecosystem (Spring 2026)
- 13 million users
- More than 2 million public models
- Over 500,000 public datasets
- 1,000-2,000 models uploaded per day

### Model Family Derivatives
- **Qwen (Alibaba):** 113,000+ derivative models; over 200,000 when including all tagged models. More derivatives than Google and Meta combined.
- **Llama (Meta):** 60,000+ derivatives (earlier figure; may be higher by March 2026). User briefing mentions 140,000+.
- **DeepSeek:** ~6,000 derivatives.
- By August 2025, Qwen derivatives were 40%+ of new HF language model derivatives; Llama had fallen to ~15%.
- Chinese open models accounted for 41% of HF downloads over the preceding year (Spring 2026 report).

### The Uncensored Model Trend
- "Abliteration": post-processing technique that identifies and neutralizes the refusal direction vector in the model's residual stream. Retains 100% intelligence, removes safety guardrails.
- Unmodified flagship models refuse 81.2% of "edgy" prompts; uncensored variants achieve 74%+ compliance on same prompts.
- Multiple "Top Uncensored Models" lists for 2026 openly catalog and rank these.
- Movement has transitioned from niche developer preference to "fundamental requirement."

### Fine-Tuning Safety Removal
- Researchers jailbroke GPT-3.5 Turbo's safety with only 10 adversarially designed examples, at cost of $0.20.
- Academic paper: "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!" (OpenReview/arXiv 2310.03693).
- Even benign fine-tuning datasets can inadvertently degrade safety alignment.
- "Shadow alignment" research examines ease of subverting safely-aligned models.

---

## 4. Surveillance and AI Governance

### Cost Curve
- AI law enforcement decreases cost and increases pervasiveness of government surveillance, overcoming traditional barriers to panoptic monitoring.
- Systems becoming easier to deploy at scale, reducing per-unit monitoring costs toward zero.

### Democracy Threat
- AI's promise of behavior prediction and control fuels a cycle of surveillance and abuse of power (Bulletin of the Atomic Scientists, Aug 2025).
- 2025 Democracy Index, Freedom House report, and V-Dem Democracy Report all show authoritarianism rising globally.
- AI increasingly used as tool of authoritarian control.

### Governance Gap
- Decision to release open-weight models rests solely on developer judgment, with no shared standards.
- No commonly adopted industry standard or universal framework for assessing when advanced AI should be released as open-weight.
- International AI Safety Report (Jan 2025, 30 countries) found consensus: future models highly likely to assist motivated users across threat domains.

---

## 5. Counter-Arguments: Open Source as Democratization

### Core Arguments
- Open-source alternatives rival proprietary systems, representing "the most significant democratization of technological power in human history."
- Open-source models decentralize AI capabilities, reducing monopoly risk.
- Decentralizing AI power comparable to anti-trust efforts as policy goal.
- Open protocols prevent Big Tech from using data lock-in to extend monopoly power.

### Geopolitical Dimension
- Trump administration's 2025 AI action plan framed open-source AI as strategic asset.
- Both US and China calculating that exporting open models aligns middle powers with their AI/hardware ecosystems.
- Chatham House (2024): Open source and democratization of AI analysis.

### Complexity
- Even as open-weight models proliferate, transparency is collapsing — downloads of opaque models outnumber those meeting basic open-source criteria.
- Open-weight is not the same as open-source (training data, methodology often withheld).

---

## 6. Key Sources

- Dwarkesh Patel, "The most important question nobody's asking about AI," dwarkesh.com, March 2026
- LessWrong discussion of Dwarkesh's essay, lesswrong.com
- CNN: Multiple articles on Anthropic-Pentagon confrontation (Feb-March 2026)
- NPR: "OpenAI announces Pentagon deal after Trump bans Anthropic" (Feb 27, 2026)
- Lawfare: "The Situation: Thinking About Anthropic's Red Lines"
- Hugging Face: "State of Open Source on Hugging Face: Spring 2026"
- arXiv 2310.03693: "Fine-tuning Aligned Language Models Compromises Safety"
- GitHub/LLM-Tuning-Safety: GPT-3.5 jailbreak with 10 examples
- Oxford study (Aug 2025): Filtered data and openly-available AI models
- Centre for Future Generations: "Can open-weight models ever be safe?" and "Beyond the binary"
- SSRN: "Open Technical Problems in Open-Weight AI Model Risk Management"
- Bulletin of the Atomic Scientists (Aug 2025): AI and surveillance capitalism
- NTIA: Open-weight AI model comments and policy approaches
- MIT Technology Review: "What's next for Chinese open-source AI" (Feb 2026)
- Red Hat: "State of open source AI models in 2025"
- Interconnects: "2025 Open Models Year in Review"
