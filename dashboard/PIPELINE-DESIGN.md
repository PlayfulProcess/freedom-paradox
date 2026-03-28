# Open Source Metrics Dashboard — Pipeline Design

## Purpose

Visual evidence for *The Freedom Paradox*: who builds open source, who profits, who uses it, and who's left out. Each lens maps to a book argument.

## Four Lenses

### Lens 1: Value Creation vs. Value Capture (Ch. 7–9, 13)

**Question:** How much economic value does open source create, and who captures it?

**Metrics:**
- Total package downloads (npm, PyPI, Docker Hub) as proxy for value created
- Company revenue/valuation for the firms built on those packages
- Ratio: downloads-per-dollar-of-revenue (how much free value per dollar captured)
- Business model taxonomy: open core, SaaS, dual-license, foundation-backed, nonprofit

**Data Sources:**
| Source | Access | Cost |
|--------|--------|------|
| npm registry API (download counts) | Public | Free |
| PyPI stats (BigQuery / pypistats.org) | Public | Free |
| Docker Hub API | Public | Free |
| Crunchbase (funding, valuations) | API key | Free tier limited |
| SEC EDGAR (10-K, S-1 filings) | Public | Free |
| DB-Engines rankings | Scraping | Free |
| BuiltWith | API | Paid ($295+/mo) |

**Key Charts:**
1. **The Value Gap** — Bar chart: total downloads vs. company valuation for top 20 open-source companies. Shows asymmetry between value created (community) and value captured (company).
2. **Business Model Landscape** — Treemap of open-source companies by valuation, colored by business model type. Shows which models "win."
3. **The Funnel** — Sankey diagram: community contributions → company product → revenue → VC returns → community reinvestment (or not).

---

### Lens 2: Who Builds (Ch. 5–6, 13)

**Question:** Are "community projects" actually community-built, or corporate projects with a community wrapper?

**Metrics:**
- Contributor concentration (Gini coefficient of commits per person)
- Corporate vs. independent contributors (by email domain / org membership)
- PR acceptance rate: employee vs. external contributor
- Time-to-merge: insider vs. outsider
- First-time contributor retention rate (% who make a second PR within 12 months)
- Bus factor (minimum contributors responsible for 50% of code)

**Data Sources:**
| Source | Access | Cost |
|--------|--------|------|
| GitHub REST/GraphQL API | Token | Free (5000 req/hr) |
| git log / git blame (cloned repos) | Local | Free |
| GH Archive (BigQuery) | Public | Free (1TB/mo) |
| CHAOSS/Augur project | Open source tool | Free |
| Linux Foundation surveys | Published reports | Free |

**Key Charts:**
1. **The Gini of Git** — Lorenz curve of commit concentration for major projects (Linux, Kubernetes, Next.js, React, Supabase). Shows how "community" the community actually is.
2. **The Insider Advantage** — Paired bar chart: median time-to-merge for employee PRs vs. external PRs, across 10–20 projects. Reveals "openness theater."
3. **The Retention Cliff** — Survival curve: % of first-time contributors still active at 3, 6, 12, 24 months. Shows the revolving door.
4. **Who Writes the Code** — Stacked area chart over time: % of commits from corporate employees vs. volunteers for major projects.

---

### Lens 3: Who Uses (Ch. 8, 15)

**Question:** Does open source actually democratize access, or does it primarily serve developers in wealthy countries?

**Metrics:**
- Download geography (where available)
- Mobile OS market share by country (Android = open source proxy)
- Stack Overflow developer survey respondent geography
- GitHub user locations (self-reported)
- Language distribution of READMEs and documentation

**Data Sources:**
| Source | Access | Cost |
|--------|--------|------|
| StatCounter GlobalStats (OS share by country) | Public | Free |
| GitHub Octoverse reports | Published | Free |
| Stack Overflow Annual Survey (raw data) | Public download | Free |
| World Bank development indicators | Public API | Free |
| npm download stats (no geo) | Public | Free |

**Key Charts:**
1. **The Android Map** — Choropleth: Android vs. iOS market share by country, overlaid with GDP per capita. Shows open source's role in bridging the digital divide.
2. **Developer Geography** — Bubble map of GitHub contributors by country, sized by commits, colored by GDP bracket. Shows where the builders are.
3. **The Language Barrier** — Bar chart: % of top-1000 GitHub repos with documentation in languages other than English. Measures actual accessibility.
4. **Consumption vs. Contribution** — Scatter plot: countries by download volume (consumption) vs. commit volume (contribution). Shows who's building vs. who's benefiting.

---

### Lens 4: Demographics & Power (Ch. 13–15)

**Question:** How inclusive is open source, really? Who governs, who's heard, who's excluded?

**Metrics:**
- Gender distribution of contributors (name inference, with caveats)
- Geographic diversity of project leadership / foundation boards
- Governance model distribution (BDFL, corporate, foundation, community)
- Corporate board/leadership composition of OS companies
- Maintainer compensation (paid vs. volunteer)

**Data Sources:**
| Source | Access | Cost |
|--------|--------|------|
| GitHub Octoverse (aggregate demographics) | Published | Free |
| Stack Overflow Survey (gender, ethnicity, geography) | Public | Free |
| Linux Foundation/CNCF/ASF board composition | Public websites | Free |
| Tidelift maintainer survey | Published reports | Free |
| Company leadership pages | Public | Free |
| Academic papers (Vasilescu et al., Terrell et al.) | Published | Free |

**Key Charts:**
1. **The Governance Spectrum** — Horizontal bar chart of major projects by governance type, showing concentration of power.
2. **Who Sits at the Table** — Foundation board composition: geography, corporate affiliation, gender (where available). Shows who governs the "commons."
3. **The Unpaid Majority** — Stacked bar: % of maintainers who are paid vs. volunteer, by project size tier. (Tidelift/GitHub survey data.)
4. **The Stack Overflow Mirror** — Demographics over time from SO surveys: gender, geography, education level. Shows movement (or stasis) in who participates.

---

## Implementation Plan

### Phase 1: Static Dataset + Charts (Now)
Build a curated dataset from published sources (SO surveys, Octoverse reports, SEC filings, academic papers) and render charts with a simple HTML + D3.js or Chart.js dashboard. No API calls needed — just structured data from existing research.

**Deliverable:** Single HTML file with interactive charts, suitable for the book's website or appendix.

### Phase 2: GitHub API Pipeline (Next)
Python scripts that pull live data from GitHub API for a curated list of 20–30 projects (the ones discussed in the book). Calculates contributor concentration, PR acceptance disparities, corporate contribution %, etc.

**Deliverable:** Repeatable data pipeline + updated charts.

### Phase 3: Cross-referencing (Later)
Combine business data (valuations, revenue) with contributor data (who builds) and adoption data (who uses) to create composite visualizations that tell the full story.

**Deliverable:** The Sankey diagram of value flow through open source.

---

## Curated Project List (Maps to Book Chapters)

| Project | Chapter | Why It Matters |
|---------|---------|----------------|
| Linux kernel | Ch. 3–5 | The original recursive public |
| Supabase | Ch. 7 | Open core, $5B valuation |
| Vercel/Next.js | Ch. 7 | 200M downloads/week, $9.3B |
| Ghost | Ch. 7, 15 | Nonprofit counterpoint |
| GitLab | Ch. 7 | Public company, open core |
| Chromium | Ch. 8 | Google's platform play |
| Android (AOSP) | Ch. 8 | 3.9B devices |
| Llama (Meta) | Ch. 9, 12 | "Open" AI, 140K derivatives |
| Kubernetes | Ch. 5 | Corporate-born community project |
| React | Ch. 8 | Meta's ecosystem play |
| HashiCorp/OpenTofu | Ch. 6 | License war case study |
| Elasticsearch/OpenSearch | Ch. 6 | AWS fork case study |
| MongoDB | Ch. 7 | Public company, SSPL license |
| Redis | Ch. 6 | License change controversy |
| WordPress | Ch. 15 | Automattic/community tension |
| Python | Ch. 5 | Foundation-governed language |
| Rust | Ch. 5 | Mozilla → Foundation transition |
| PostgreSQL | Ch. 7 | Pure community, no company |
| SQLite | Ch. 15 | Public domain, billions of deployments |
| Hugging Face models | Ch. 12 | AI model distribution |

---

## Methodological Notes

### On Gender Inference
Name-based gender inference (Namsor, genderize.io) is used in published CS research (Vasilescu et al. 2015, Terrell et al. 2017) but carries serious limitations:
- Binary classification only
- Western-name bias (lower accuracy for Chinese, Korean, Indian names)
- ~70-85% accuracy depending on name origin
- **We should flag this explicitly in any visualization** and supplement with survey data where available

### On "Inclusivity"
This is not a single number. We operationalize it as a composite of:
- Geographic diversity (entropy of contributor countries)
- Contributor concentration (inverse Gini — more distributed = more inclusive)
- Governance representation (who decides)
- Barrier to entry (time-to-first-PR-merge for newcomers)
- Documentation accessibility (languages, readability score)

### On Causation
Open source doesn't "cause" inclusion or exclusion. The data shows *correlation* between open-source participation and existing global inequalities. The interesting question is whether open source *reproduces* those inequalities or *partially mitigates* them — and that requires comparing to proprietary software participation rates, which is harder to measure.

---

## Alternative Quantification Approaches

Beyond the four lenses above, other researchers have tried:

1. **Network analysis** — Map the dependency graph of packages. Who controls critical infrastructure? (See: Heartbleed, Log4j, xz-utils incidents.) Quantifies fragility.

2. **Economic multiplier models** — Harvard Business School (Hoffman et al. 2024) estimated open source's demand-side value at $8.8 trillion. The "value created" side of Lens 1.

3. **Labor economics approach** — Treat open-source contributions as unpaid labor. Calculate implicit wages, compare to VC returns. (Eghbal's framing in *Working in Public*.)

4. **Patent/IP analysis** — Compare patent filing rates in open-source-heavy sectors vs. proprietary. Does openness accelerate or decelerate innovation?

5. **Policy impact mapping** — Track government adoption of open source (EU's Cyber Resilience Act, US SBOM requirements). Quantifies institutional legitimacy.

6. **Sentiment analysis on governance decisions** — NLP on GitHub discussions, mailing lists during license changes (HashiCorp, Redis, Elastic). Quantifies community reaction to corporate control.

7. **Fork analysis** — When projects fork (OpenTofu, MariaDB, LibreOffice), compare trajectory of fork vs. original. Measures whether "exit" actually works as governance.
