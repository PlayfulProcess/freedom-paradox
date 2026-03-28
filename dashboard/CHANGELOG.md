# Dashboard Changelog & Research Notes

## 2026-03-28 — Live Verification Pass (Web Search)

### Verification Results

Ran 3 parallel research agents + direct web searches to verify all [VERIFY] flags against live sources. **Major corrections found.**

#### Confirmed (correct as-is)
- Supabase $5B valuation (Series E, Oct 2025) — TechCrunch, Fortune
- Supabase $70M ARR (Sacra estimate mid-2025, likely higher now)
- Vercel $9.3B valuation (Series F, Sep 2025) — Vercel blog, GIC
- Anthropic $380B valuation (Series G, Feb 2026) — CNBC, Anthropic press
- Harvard/Linux Foundation $8.8T OSS demand-side value — HBS Working Paper 24-038
- Tidelift 60% quit or considered quitting — confirmed
- Android dominance in Global South — confirmed (Africa 85%, S. America 87%)

#### Corrected (wrong or outdated)

| Figure | Old Value | Corrected Value | Source |
|--------|-----------|-----------------|--------|
| Next.js weekly downloads | 200M | **~27M** (off by ~10x!) | npm registry |
| Anthropic ARR | $7B | **~$19B** (nearly 3x higher) | Bloomberg, Yahoo Finance |
| GitLab FY2025 revenue | $955M | **$759M** | GitLab IR |
| GitLab market cap | $8B | **~$3.5B** (stock dropped 61%) | CompaniesMarketCap |
| MongoDB FY2025 revenue | $1.9B | **$2.01B** | MongoDB IR |
| MongoDB market cap | $14B | **~$20B** | MacroTrends |
| Elastic FY2025 revenue | $1.3B | **$1.48B** (1.3B was FY2024) | Elastic IR |
| HashiCorp acquisition | $5.7B | **$6.4B** at $35/share | IBM press release |
| Big Tech AI capex 2025 | $285B | **$380B+** | CNBC (Oct 2025) |
| Tidelift unpaid % | 74% | **60%** unpaid hobbyists | Tidelift 2024 report |
| Tidelift harassment 46% | 46% | **NOT from Tidelift** — source unknown | [RESEARCH NEEDED] |
| Terrell et al. framing | 78.6% "when hidden" | 78.6% is **overall**, not "when hidden" | PeerJ CS 3:e111 |
| Supabase total funding | $226M | **$543M** | PitchBook |
| GPT-5 training cost | $500M | **$500M–$2.5B** range (HSBC) | HSBC, press |

#### Flagged (needs further research)

| Figure | Issue |
|--------|-------|
| Surveillance cost trajectory ($30B→$1B) | **NOT from Amodei essay** — essay discusses surveillance qualitatively but no dollar trajectory found. Source unknown. |
| Stack Overflow gender percentages | Interactive JS charts, not scrapable. Need to check CSV download. |
| 2023 SO survey | **Gender question was dropped entirely** — gap in trend line |
| Ghost $8M ARR | Not verified — couldn't find confirmation |
| Automattic $7.5B / $500M ARR | Not verified this pass |

#### New findings not in original data

| Finding | Source | Book Relevance |
|---------|--------|----------------|
| Anthropic total funding: $67.3B from 90 investors | Crunchbase | Ch. 1, 10 — scale of safety investment |
| Anthropic ARR trajectory: $1B (late 2024) → $10B (end 2025) → $19B (Mar 2026) | Bloomberg, SaaStr | Ch. 11 — proprietary AI can grow faster |
| Claude Code alone: ~$2.5B ARR | Anthropic press | Ch. 2 — AI-generated code economics |
| India overtook US as largest GitHub contributor base (Octoverse 2025) | GitHub Octoverse 2025 | Ch. 5, 8 — shifts the geography narrative |
| 180M+ total developers on GitHub | Octoverse 2025 | Scale context |
| Big Tech AI capex 2026 projection: ~$700B | CNBC, CreditSights | Compute barrier thesis |
| Amazon alone: $125B (2025) → $200B (2026) capex | CNBC | Compute concentration |
| GPT-5 released Aug 7, 2025; 400K context; $1.25/$10 per 1M tokens | OpenAI | Ch. 11 — pricing of "openness" |
| Anthropic preparing potential IPO (2026), hired Wilson Sonsini | TechCrunch | Epilogue — what happens when safety goes public? |

### Book Notes from Verification

#### India Overtaking the US (NEW — Major)
> The Octoverse 2025 report delivers a finding that reframes the entire geographic narrative: **India has overtaken the United States as the largest open-source contributor base on GitHub**. India added 5.2 million developers in one year, accounting for 14% of all new accounts. This doesn't invalidate the contribution-vs-consumption gap — India remains underrepresented relative to its population share — but it changes the trajectory. The question is no longer "will the Global South participate?" but "on whose terms?"

#### Anthropic's Revenue Curve (NEW — Ch. 11)
> Anthropic's revenue trajectory is itself an argument about open source: $1B ARR in late 2024, $10B by end of 2025, $19B by March 2026. A company that chose *not* to open-source its models is growing faster than any open-source AI company. Claude Code alone generates ~$2.5B ARR — roughly what it would cost to retrain a frontier model. The proprietary path is not just viable; it's dominant. The question for the open-source movement: does this prove that safety requires closure, or that closure is simply more profitable?

#### The $380B Capex Correction (Strengthens Compute Thesis)
> The original $285B figure was wrong — the actual 2025 combined AI capex is $380B+, with 2026 projections approaching $700B. Amazon alone will spend $200B in 2026. This strengthens the compute barrier argument considerably: the gap between "hobbyist accessible" and "frontier competitive" is not narrowing — it's widening exponentially. When four companies spend more on AI infrastructure than the GDP of all but ~20 countries, "openness" becomes a question of physics, not philosophy.

---

## 2026-03-28 — Compute Economics Layer Added

### What Was Done

**New Dataset: `data/compute-economics.json`**
- Training costs for 11 AI models (GPT-2 through GPT-5, Llama family, DeepSeek-V3, Gemini Ultra)
- Inference costs: API pricing and self-hosting hardware requirements
- Big Tech AI capex ($285B combined in 2025)
- Surveillance cost trajectory (Amodei's estimates: $30B → $1B by 2030)
- The DeepSeek disruption: $5.6M training cost challenges the cost barrier narrative

**New Dashboard Section: Lens I-B (Compute Economics)**
- 4 new charts: Training Cost (log-scale bar), AI Capex (bar), Self-Hosting Ladder (log-scale), Surveillance Cost Curve (line)
- 4 stat cards: $285B capex, $500M GPT-5 estimate, $5.6M DeepSeek, $150K self-hosting minimum
- Insight boxes connecting each chart to specific book chapters

**Updated CHANGELOG.md** — Added this entry plus book incorporation notes for compute economics

---

## 2026-03-28 — Initial Build

### What Was Done

**Pipeline Design (`PIPELINE-DESIGN.md`)**
- Defined four-lens framework: Value Creation vs. Capture, Who Builds, Who Uses, Demographics & Power
- Mapped each lens to specific book chapters
- Catalogued data sources with access method and cost
- Listed 20 curated projects that map to book arguments
- Documented 7 alternative quantification approaches beyond the four lenses
- Wrote methodological caveats (gender inference limitations, survey bias, causation vs. correlation)

**Curated Datasets (`data/`)**
- `business-metrics.json` — 14 companies/projects with valuations, revenue, business models, governance type, license, key metrics. All mapped to book chapters.
- `contributor-demographics.json` — Aggregate data from Stack Overflow surveys (gender trend 2018–2024), GitHub Octoverse (geographic distribution), Tidelift (maintainer burnout/pay), Terrell et al. (gender bias in PR review), StatCounter (mobile OS by region).

**Interactive Dashboard (`index.html`)**
- Single-file HTML + Chart.js, dark theme, no build step
- 8 charts across 4 lenses:
  1. The Value Gap (company valuations, log scale)
  2. Business Model Landscape (doughnut: open core dominance)
  3. Paid vs. Unpaid Divide (stacked bar: Linux kernel vs. long-tail)
  4. Gender Bias in Code Review (Terrell et al. data)
  5. Digital Divide Map (Android vs. iOS by region)
  6. Contribution vs. Consumption (country contributor % vs. population %)
  7. Gender in Open Source Over Time (flat line at ~5%)
  8. Governance Spectrum (corporate → community scale)
- Summary stat cards with key numbers
- Insight boxes linking each chart to specific book arguments
- Methodology disclaimer section

---

### What's Still Needed

#### Data Gaps (Priority Order)

1. **Compute cost layer** — Training costs ($100M+ for frontier models), inference costs, infrastructure subsidies. This changes the economics of "free" fundamentally. Need: OpenAI/Anthropic/Meta training cost estimates, cloud GPU pricing curves, cost-to-retrain-Llama estimates.

2. **[VERIFY] flags** — Every major figure needs primary source confirmation:
   - Supabase $5B valuation, $70M ARR
   - Vercel $9.3B valuation, 200M weekly downloads
   - Anthropic $380B valuation (Feb 2026 Series G)
   - GitLab FY2025 revenue ($955M)
   - MongoDB FY2025 revenue ($1.9B)
   - All StatCounter regional percentages
   - Stack Overflow survey percentages per year
   - Tidelift 2024 exact figures (74% unpaid, 60% considered quitting, 46% harassment)

3. **Contributor concentration data (Gini of Git)** — Need to actually run git log analysis on 10–20 projects to calculate commit concentration. Planned for Phase 2 (GitHub API pipeline).

4. **PR acceptance disparities by project** — Time-to-merge for insiders vs. outsiders. Requires GitHub API queries. Phase 2.

5. **First-time contributor retention curves** — Survival analysis: what % of first-PR contributors return? Requires GitHub API. Phase 2.

6. **Foundation board composition** — Manual research: who sits on Linux Foundation, CNCF, ASF, Python Software Foundation, Rust Foundation boards? Corporate affiliation, geography, gender. This is hand-collected data.

7. **AI model ecosystem metrics** — Hugging Face download data, derivative model counts, who's fine-tuning Llama and where, the Qwen/DeepSeek story (41% of HF downloads from Alibaba variants).

8. **Fork trajectory analysis** — When projects fork (OpenTofu, MariaDB, LibreOffice, OpenSearch), compare metrics pre/post fork. Does "exit" actually work as governance?

9. **Labor economics framing** — Calculate implicit wages for unpaid OSS work. If maintainers spend 10 hrs/week unpaid, and there are X maintainers, what's the total labor subsidy to the tech industry?

10. **Language/accessibility audit** — What % of top repos have non-English documentation? Measures actual global accessibility vs. rhetoric.

#### Charts Still Needed

- **The Compute Barrier** — Line chart: cost to train frontier models over time. Shows the new barrier to "open" AI.
- **The Sankey of Value** — Flow diagram: community contributions → company product → revenue → VC returns → (how much flows back?). This is the killer chart.
- **The Gini of Git** — Lorenz curves of commit concentration for major projects.
- **The Insider Advantage** — Time-to-merge comparison.
- **The Retention Cliff** — Survival curves for first-time contributors.
- **The Dependency Graph** — Network visualization of critical infrastructure (who controls what everything depends on).
- **Fork Trajectories** — Before/after metrics for major forks.

#### Infrastructure Needed for Phase 2

- Python environment with `requests`, `pandas`, `matplotlib` or stick with Chart.js
- GitHub personal access token for API queries (5000 req/hr)
- BigQuery access for GH Archive (free tier: 1TB/mo) and PyPI stats
- Decision: keep everything in single HTML file or move to a proper Next.js/Vercel dashboard?

---

### Notes to Incorporate in the Book

#### For Chapter 7 (Open Core, Closed Profit)

> The dashboard data reveals a striking pattern: the seven open-core companies in our dataset have a combined valuation exceeding $50 billion, built on code that is nominally "free." PostgreSQL — the purest community project, with no corporate parent — has a valuation of zero, despite being the foundation on which Supabase ($5B), Neon, CrunchyData, and dozens of others are built. The value gap is not between open and closed source. It's between those who write the code and those who capture the distribution.

> Ghost, at $8M ARR with zero venture funding, proves an alternative model exists. But it also proves why VCs don't fund it: the nonprofit structure caps returns by design. The market selects for extraction, not sustainability.

#### For Chapter 8 (The Platform Play)

> Android's market share data tells a story the open-source movement rarely tells about itself: open source's greatest consumer-facing achievement is also its greatest corporate strategy. In Africa (84% Android) and South America (85%), open source literally provides mobile computing to billions priced out of proprietary alternatives. But the "open" in Android is AOSP — the bare operating system. Google Play Services, the layer that actually makes the phone useful, is proprietary. Google opened the commodity layer and closed the monetization layer. The farmers in Uttar Pradesh got smartphones. Google got their data.

> The geographic contribution data adds another dimension: the US produces 22.7% of open-source contributors but only 4.2% of the world's population — a 5.4x overrepresentation. Nigeria produces 1.2% of contributors and 2.8% of the population — underrepresented by more than half. Open source democratizes *consumption* far more effectively than it democratizes *production*. The Global South uses the software; the Global North builds it.

#### For Chapter 9 (Meta's Confession)

> Meta's Llama downloads (1.2 billion) and derivatives (140,000+ on Hugging Face) represent the largest-scale experiment in "open" AI. But compute costs reframe the entire picture. Llama 3 cost an estimated $30M+ to train. "Open weights" means anyone can *use* the model, but retraining or modifying it at scale requires Meta-level compute infrastructure. This is "free as in beer" where the beer requires a $10 million brewery. The freedom to fork is meaningless without the resources to run what you've forked.

> When Meta pivoted to proprietary "Avocado," it confirmed what the compute economics already implied: openness was strategy, not conviction. You open-source the previous generation to build ecosystem and talent pipeline. You close the current generation to capture revenue. The open/closed binary is a fiction; what matters is *which layer* is open and *who controls the compute*.

#### For Chapter 10 (The Safety Argument)

> **Compute cost note for safety framing:** Amodei's mass surveillance cost trajectory ($30B/year today → <$1B/year by 2030) should be placed alongside open-model proliferation data. If surveillance-capable models are open-weight AND compute costs drop, the "safety through scarcity" argument collapses. The dashboard should eventually model this intersection: when does the cost curve meet the capability curve for specific threat categories?

#### For Chapter 13 (Value Creation for Whom?)

> The Terrell et al. data on PR acceptance is perhaps the most precise quantification of open source's inclusion gap. Women's PRs are accepted at 78.6% when gender is hidden — *higher* than men's 74.6%. When gender is visible, women's acceptance drops to 62.5% while men's barely moves (73.8%). Open source is a meritocracy, but only when identity is invisible. The "just show me the code" ethos works — until the code comes attached to a name, a photo, a pronoun.

> The gender trend line (flat at ~5% women since 2020) suggests that the problem is not downstream (code review bias, though that exists) but upstream: who enters the pipeline, who stays, who has the unpaid time to contribute. The sociological question is not "is open source biased?" but "does open source reproduce or disrupt the demographic patterns of the tech industry that surrounds it?" The data says: reproduces.

#### For Chapter 14 (The Commons That Can Kill)

> Ostrom's principles for governing commons included boundaries, sanctions, and graduated conflict resolution. The governance spectrum chart shows that most major open-source projects have *none of these* — they are governed by corporate fiat (Llama, Android, React, Next.js) or by benevolent dictator (SQLite). The projects closest to genuine community governance (PostgreSQL, Rust) are the exceptions, not the norm. "The commons" in open source is mostly a metaphor, not a governance structure.

#### For the Epilogue

> **The Sankey question:** If we could trace one dollar of value from its creation (a developer writing open-source code on an evening) through its capture (a company hosting that code as a service) to its distribution (VC returns, employee compensation, community reinvestment), what would the flow look like? The dashboard data suggests the ratio is something like: for every $1 of value created by community contributors, $0.01 flows back to the community in any form. The other $0.99 flows to shareholders, employees of the capturing company, and VCs. This is not a bug in open source. It is the business model.

#### Cross-cutting: The Compute Economics Thesis

> **New argument thread:** The dashboard should eventually support a meta-argument that runs through the entire book: the economics of "free" depend entirely on what's scarce. When code was scarce (1970s–2000s), freeing code was revolutionary. When code became abundant but *distribution* was scarce (2000s–2020s), companies that controlled distribution captured the value. Now that AI can regenerate code from specifications (Ch. 2, O'Nolan's provocation), code itself may become worthless — but *compute* and *data* are the new scarcities. Open source freed the thing that was becoming commodity anyway. The question for the book's conclusion: can the open-source *ethos* adapt to govern compute and data, or was it always a philosophy of abundance applied to things that were already becoming abundant?

---

### Alternative Quantification Approaches Worth Exploring

1. **Network centrality analysis** — Which packages are most depended-upon? (npm dependency graph, PyPI). Maps fragility: when one maintainer controls a package used by 100,000 others, that's a governance crisis, not a technical one.

2. **License migration tracking** — Chart the movement from copyleft (GPL) → permissive (MIT/Apache) → restricted (BSL/SSPL) over time. The arc of open source bends toward... what?

3. **VC return analysis** — For the open-source companies that have exited (GitLab IPO, HashiCorp acquisition, Red Hat → IBM), calculate VC multiples vs. community contribution value. The equity analyst in you will want this.

4. **Hiring pipeline analysis** — Do open-source contributions function as unpaid job interviews? Track: contributors who later got hired by the company whose project they contributed to. This reframes "community" as "talent pipeline."

5. **Regulatory impact mapping** — EU Cyber Resilience Act, US SBOM requirements, ITAR for AI models. How do regulations reshape who can participate in open source?

6. **The O'Nolan Test** — Can AI regenerate each project from its specification? If so, what's the "moat" — the code or the community? Test this by having Claude Code attempt to rebuild small-to-medium OSS projects from README + test suite alone.
