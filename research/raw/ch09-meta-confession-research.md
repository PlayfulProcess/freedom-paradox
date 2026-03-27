# Chapter 9 Research: Meta's Confession

## Raw Research Notes — Compiled March 27, 2026

---

## 1. Zuckerberg's July 2024 Open Letter

**Source**: Mark Zuckerberg, "Open Source AI Is the Path Forward," July 23, 2024
- Published alongside Llama 3.1 release (405B parameter model)
- Key quote: "One of my formative experiences has been building our services constrained by what Apple will let us build on their platforms. Between the way they tax developers, the arbitrary rules they apply, and all the product innovations they block from shipping..."
- Called open-source AI "the path forward" — framed as philosophical commitment
- Explicitly named Apple as the reason he supports open ecosystems
- Extended the argument to AR/VR: "Meta and many other companies would be freed up to build much better services for people if we could build the best versions of our products and competitors were not able to constrain what we could build"
- **Sources**: [Entrepreneur](https://www.entrepreneur.com/business-news/mark-zuckerberg-calls-out-apple-outlines-meta-ai-strategy/477517), [TIME](https://time.com/7002563/mark-zuckerberg-ai-llama-meta-open-source/), [HackerNoon](https://hackernoon.com/should-ai-be-open-source-mark-zuckerbergs-open-letter-explained)

## 2. Llama Adoption Numbers

- **650 million downloads** by December 2024
- **1 billion downloads** by mid-March 2025 (Zuckerberg announcement)
- **1.2 billion downloads** by April 2025 (LlamaCon)
- Average of ~1 million downloads per day since February 2023 first release
- Enterprise adopters include Spotify, AT&T, DoorDash
- Meta AI reached ~600 million monthly active users, on track to 1 billion
- **LlamaCon** (April 29, 2025): First-ever conference dedicated to Llama models
  - Announced Llama API (customizable, no lock-in, OpenAI SDK compatible)
  - Partnerships with Cerebras and Groq for inference
  - Released Llama Guard 4, LlamaFirewall, Llama Prompt Guard 2
  - $1.5M+ in Llama Impact Grants (second round)
- **Sources**: [TechCrunch](https://techcrunch.com/2025/03/18/mark-zuckerberg-says-that-metas-llama-models-have-hit-1b-downloads/), [Tech Startups](https://techstartups.com/2025/04/29/metas-llama-ai-models-hit-1-2-billion-downloads-as-open-source-bet-starts-paying-off/), [Meta AI Blog](https://ai.meta.com/blog/llamacon-llama-news/)

## 3. The OSI Challenge — Is Llama Actually Open Source?

### OSI Position
- OSI published "The Open Source AI Definition" in October 2024
- Requires: open weights, open training code, sufficient training data detail for reproducibility
- OSI blog post (Feb 2025): "Meta is trying to redefine Open Source for their own benefit and at the expense of our freedom"
- On Llama 4 launch (April 2025): "Llama 4 is still not #opensource and Europeans are excluded"

### Specific License Restrictions
- Commercial use restricted for applications with 700M+ monthly users
- Acceptable use policy prohibits certain fields (regulated substances, critical infrastructure)
- Training data not disclosed — impossible to reproduce the model
- Geographical restrictions in Llama 4 (Europeans excluded from some uses)
- Free Software Foundation classified Llama 3.1's license as "nonfree" (January 2025)

### The "Open Weights" Distinction
- Open Weights: shares model parameters but NOT training data, training code, or full methodology
- Open Source (per OSI): weights + training code + training data description sufficient for reproduction
- Key insight: "Open Weights enable replication; Open Source enables advancement"
- Training data non-disclosure prevents independent auditing of bias, quality, diversity
- Legal complexity: datasets often include proprietary/licensed content

- **Sources**: [OSI Blog](https://opensource.org/blog/metas-llama-license-is-still-not-open-source), [SiliconANGLE](https://siliconangle.com/2024/10/28/osi-clarifies-makes-ai-systems-open-source-open-models-fall-short/), [IT Pro Today](https://www.itprotoday.com/it-operations/meta-s-llama-llms-spark-debate-over-open-source-ai)

## 4. Llama 4 Launch — The Benchmark Scandal (April 2025)

- Llama 4 released April 2025 with Scout and Maverick models
- Immediately accused of benchmark manipulation
- Allegations: submitted an "experimental" chat version of Maverick to LMArena leaderboard — different from the publicly released model
- Former Meta engineer reportedly posted on Chinese forum that post-training datasets were adjusted for better scores
- Meta initially denied (April 7, 2025 TechCrunch interview)
- Yann LeCun later acknowledged: "results were fudged a little bit" and team "used different models for different benchmarks"
- Zuckerberg "really upset and basically lost confidence in everyone who was involved"
- Result: Zuckerberg "sidelined the entire GenAI organisation"
- **Sources**: [TechCrunch](https://techcrunch.com/2025/04/07/meta-exec-denies-the-company-artificially-boosted-llama-4s-benchmark-scores/), [Slashdot](https://tech.slashdot.org/story/26/01/02/1449227/results-were-fudged-departing-meta-ai-chief-confirms-llama-4-benchmark-manipulation), [The Register](https://www.theregister.com/2025/04/08/meta_llama4_cheating/)

## 5. Llama 4 Behemoth — Shelved

- Behemoth: ~2 trillion parameter MoE model, Meta's largest ever
- Meta initially claimed it outperformed GPT-4.5, Claude Sonnet 3.7, Gemini 2.0 Pro on MATH-500 and GPQA Diamond
- Independent evaluations could NOT reproduce these claims
- Llama 4 significantly underperformed Llama 3 on coding benchmarks in third-party testing
- Release postponed from early summer to fall 2025 or later
- Never made generally available — remained in "limited preview"
- **Sources**: [SiliconANGLE](https://siliconangle.com/2025/05/15/meta-postpone-release-llama-4-behemoth-model-report-claims/), [Axios](https://www.axios.com/2025/05/15/meta-behemoth-llama-scaling-delays), [Rootly](https://rootly.com/blog/llama-4-underperforms-a-benchmark-against-coding-centric-models)

## 6. DeepSeek's Impact (January 2025)

- DeepSeek R1 launched January 2025
- Overtook ChatGPT as most-downloaded free app on Apple App Store in US
- Demonstrated comparable reasoning/math skills to leading proprietary models
- Built on open research including PyTorch and Llama from Meta
- Trained at reportedly fraction of cost of Western frontier models

### Yann LeCun's Response
- Framed it as vindication: "open source models are surpassing proprietary ones"
- "DeepSeek profited from open research and open source (e.g. PyTorch and Llama from Meta)"
- "They came up with new ideas and built them on top of other people's work. Because their work is published and open source, everyone can profit from it. That is the power of open research and open source."
- Meta stock rose ~2% on DeepSeek news

### The Double Edge
- Vindicated open-source philosophy (innovation through openness)
- BUT demonstrated competitive risk: Chinese startup replicated/exceeded Meta's architecture
- Spurred broader open-source momentum: OpenAI released first open model in six years in response
- **Sources**: [Yahoo/VentureBeat](https://www.yahoo.com/tech/metas-chief-ai-scientist-says-193729910.html), [CNBC](https://www.cnbc.com/2025/02/04/deepseek-breakthrough-emboldens-open-source-ai-models-like-meta-llama.html), [WEF](https://www.weforum.org/stories/2025/02/open-source-ai-innovation-deepseek/)

## 7. The Pivot — Avocado and Superintelligence Labs

### Scale AI Acquisition (June 2025)
- Meta invested $14.3 billion for 49% stake in Scale AI
- Alexandr Wang (Scale AI founder/CEO) became Meta's first Chief AI Officer
- Wang leads "Meta Superintelligence Labs" (MSL)
- Zuckerberg personally recruited ~50-person team at homes in Lake Tahoe and Palo Alto
- Scale AI valuation: $29+ billion
- **Sources**: [Fortune](https://fortune.com/2025/06/13/meta-scale-ai-alexandr-wang-superintelligence-team/), [TechCrunch](https://techcrunch.com/2025/06/10/report-meta-taps-scale-ais-alexandr-wang-to-join-new-superintelligence-lab/)

### Avocado Model
- New proprietary text LLM, codename "Avocado"
- Being built inside Meta Superintelligence Labs
- Originally targeted for Q1 2026, then postponed to May 2026+
- May NOT be open source — significant departure from Llama strategy
- Internal tests show Avocado lags behind Google, OpenAI, Anthropic
- Reports Meta even considered licensing Google's Gemini as fallback
- CNBC (Dec 2025): "From Llamas to Avocados: Meta's shifting AI strategy is causing internal confusion"
- **Sources**: [eWeek](https://www.eweek.com/news/meta-new-avocado-model/), [CNBC](https://www.cnbc.com/2025/12/09/meta-avocado-ai-strategy-issues.html), [Engadget](https://www.engadget.com/ai/meta-is-reportedly-working-on-a-new-ai-model-called-avocado-and-it-might-not-be-open-source-215426778.html), [Trending Topics](https://www.trendingtopics.eu/meta-delays-avocado-ai-model-again-might-even-license-gemini-from-google/)

### Capital Expenditure Escalation
- 2025 CapEx: $70-72 billion (~70% increase over 2024)
- 2026 CapEx guidance: $115-135 billion (CFO Susan Li: "notably larger")
- Long-term: $600 billion on US data centers/infrastructure by 2028
- **Sources**: [TechCrunch](https://techcrunch.com/2025/07/30/meta-to-spend-up-to-72b-on-ai-infrastructure-in-2025-as-compute-arms-race-escalates/), [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/meta-avocado-delay-puts-135-billion-dollar-ai-bet-under-scrutiny/)

## 8. Open Model Ecosystem (Context)

- Llama: 140,000+ derivatives on Hugging Face [VERIFY — number from task brief, not confirmed in search]
- Qwen (Alibaba): 160,000+ derivatives, became most-downloaded open model family by end of 2025 [VERIFY]
- Mistral: 38,000+ derivatives [VERIFY]
- DeepSeek models also widely forked
- OpenAI released first open model in 6 years in response to DeepSeek
- Hugging Face serves as central platform for open model ecosystem

## 9. Timeline Summary

| Date | Event |
|------|-------|
| Feb 2023 | Original Llama leaked/released |
| Jul 2023 | Llama 2 released with community license |
| Jul 2024 | Zuckerberg's "Open Source AI Is the Path Forward" letter + Llama 3.1 |
| Oct 2024 | OSI publishes Open Source AI Definition |
| Dec 2024 | Llama reaches 650M downloads |
| Jan 2025 | DeepSeek R1 launches, tops App Store; LeCun calls it open-source vindication |
| Jan 2025 | FSF classifies Llama 3.1 license as nonfree |
| Mar 2025 | Llama crosses 1B downloads |
| Apr 2025 | Llama 4 launch + benchmark manipulation scandal |
| Apr 2025 | LlamaCon; 1.2B downloads announced |
| May 2025 | Behemoth release postponed |
| Jun 2025 | Meta acquires 49% of Scale AI ($14.3B); Alexandr Wang becomes Chief AI Officer |
| Jun 2025 | Meta Superintelligence Labs established |
| Late 2025 | Avocado model development confirmed; may not be open source |
| Dec 2025 | CNBC reports internal confusion over strategy shift |
| Q1 2026 | Avocado delayed again; lags competitors in internal tests |
| Mar 2026 | Reports Meta considered licensing Google Gemini |

## Items Flagged for Verification

- [VERIFY] Exact derivative counts (140K Llama, 160K Qwen, 38K Mistral) — these appear in the task brief but weren't confirmed in search results
- [VERIFY] Whether Behemoth was formally "shelved" vs merely "delayed indefinitely"
- [VERIFY] Exact DeepSeek training cost claims (widely reported but disputed)
- [VERIFY] Whether Avocado has been formally confirmed as proprietary or if it's "may not be open source"
- [RESEARCH NEEDED] Meta's advertising revenue numbers to contextualize why open-sourcing models doesn't undercut their business model
- [RESEARCH NEEDED] Specific companies/governments that adopted Llama for sensitive applications
