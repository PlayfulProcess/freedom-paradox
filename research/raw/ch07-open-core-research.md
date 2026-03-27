# Chapter 7: Open Core, Closed Profit — Raw Research

## Supabase

### Founding & People
- Founded 2020 by Paul Copplestone (CEO) and Ant Wilson (CTO)
- Both moved to Singapore for Entrepreneur First accelerator; lived together for a year before co-founding
- Copplestone: born/raised on farm near Kaikoura, New Zealand; started coding at 18
- Origin story: Copplestone hit Firebase scaling problems in a previous startup, switched to Postgres, wrote a real-time engine on top of Postgres. Open-sourced that engine
- Key pivot: In May 2020, Copplestone changed the website tagline from "real-time Postgres" to "the open-source Firebase alternative." Within 3 days: 8 hosted databases → 800
- Quote (Copplestone): "I didn't build the startup for investors, I just built what I thought would be the best product for developers." [VERIFY: exact source]

### Financial Trajectory
- 2020: Founded
- 2021 (Oct): $30M Series A (~16 months after founding)
- 2024: $80M Series C
- 2025 (Apr): $200M at $2B valuation — "vibe coding" cited as growth driver
- 2025 (Oct): $100M Series E at $5B valuation — led by Accel and Peak XV, Figma Ventures joined
- Revenue: $70M ARR (up from $20M a year earlier) [VERIFY: exact timeline of $20M → $70M]
- Another source says $31M annual revenue by 2025 [VERIFY: reconcile with $70M ARR figure]

### Community & Usage Metrics
- 99.2K GitHub stars, 11.8K forks, 35K+ commits, 1,742 contributors
- 4 million developers (up from 1M to 4M in one year)
- 1M+ active databases; 2,500 new databases created daily
- Clients include: 1Password, PwC, Johnson & Johnson

### Technical Architecture — ALL Open Source
- PostgreSQL: the database itself (MIT-like license)
- PostgREST: auto-generated REST API from Postgres schema (MIT, Haskell)
- GoTrue: authentication service (MIT, Go)
- Realtime: real-time subscriptions via WebSockets (Apache 2.0, Elixir)
- Storage: file storage service (Apache 2.0, Node.js/TypeScript)
- Deno-based Edge Functions
- Every core component is open source; self-hosting is fully supported
- What's proprietary: managed hosting, cloud infrastructure orchestration, dashboard/UX polish

### Business Model
- "Open source Firebase alternative" — every component open source
- Revenue from managed hosting (Supabase Cloud)
- Self-hosting explicitly supported — no vendor lock-in
- Differentiation: convenience, managed infrastructure, support, integrations
- "Vibe coding" trend (AI-generated apps) driving massive database creation

---

## Vercel

### Founding & People
- Founded by Guillermo Rauch (Argentine, creator of Socket.IO, author of "Smashing Node.js")
- Created Next.js as open-source React framework
- Company originally called ZEIT, renamed to Vercel

### Financial Trajectory
- 2024 (May): $3.25B valuation
- 2024 (end): $144M ARR
- 2025 (May): $200M ARR — doubled from $100M in 15 months
- 2025 (Sep/Oct): $300M Series F at $9.3B valuation — led by Accel and GIC
- Near 3x valuation increase from $3.25B to $9.3B in ~18 months

### Next.js & Open Source Strategy
- Next.js: MIT-licensed React framework
- Downloaded 200 million times per week [VERIFY]
- Powers Walmart.com, TikTok web, major enterprise sites
- Rauch quote: open source is "a speedrun to product-market fit, because if people don't use it when it's free, when it's easy to consume, when the code is available, then you probably should be working on something else"
- Key insight: Rauch kept Next.js completely free without gating capabilities — no open-core feature restriction
- Business model: pay Vercel for best deployment experience — performance, reliability, serverless scale, global edge
- Rauch: "you could create open-source software targeted at engineers, while simultaneously building an enterprise business based on services and infrastructure"

### v0 (AI Product)
- AI code generation product, $20/month premium tier
- 3.5 million users
- Teams/Enterprise accounts = 50%+ of v0 revenue
- Dual revenue: v0 subscription fees + downstream infrastructure consumption on Vercel

### Business Model Details
- B2B SaaS: infrastructure reselling + developer tooling
- Usage-based pricing (compute, bandwidth, storage)
- Per-seat Pro ($20/month/seat) and Enterprise plans
- "Progressive disclosure of complexity" — approachable for beginners, powerful for enterprise

---

## Ghost

### Founding & People
- Founded April 2013 by John O'Nolan & Hannah Wolfe
- O'Nolan: former Deputy Head of the WordPress UI team
- Started with a Kickstarter campaign
- Set up as non-profit foundation (Ghost Foundation, HQ Singapore)

### Financial & Organizational
- Crossed $10M ARR (as of ~2025/2026) [VERIFY exact date]
- Earlier figure: $8.86M ARR, 28K customers [VERIFY: when was this figure from?]
- Indie publisher revenue earned with Ghost: ~$130M
- 0% transaction fees on creator revenue
- 34 full-time staff (as of Oct 2025)
- Bootstrapped — zero venture capital

### Business Model
- MIT License — fully open source
- Revenue from Ghost(Pro) managed hosting service
- Free core application, premium managed service
- Non-profit structure: no shareholders, no investors, mission-driven
- O'Nolan's philosophy: built for independent journalists and writers

### Significance
- Proves open-core model works without VC
- Non-profit structure eliminates the license-change incentive entirely
- No pressure to maximize shareholder returns → no "rug pull" risk
- Counterpoint to HashiCorp/MongoDB pattern

---

## HashiCorp

### License Change & Acquisition
- Aug 10, 2023: switched all products from MPL 2.0 to BSL (Business Source License)
- Products affected: Terraform, Vault, Consul, Nomad
- BSL: source-available, not open source; restricts offering as managed service
- Aug 15, 2023: OpenTF Manifesto published — 33K GitHub stars, 140 companies, 700 individuals
- Sep 20, 2023: Linux Foundation accepted OpenTofu fork
- Jan 2024: OpenTofu first stable release
- Feb 2025: IBM acquired HashiCorp for $6.4 billion [VERIFY: exact close date]
- IBM has not announced returning products to open source
- IBM also acquired Red Hat for $34B in 2019; maintained open source commitments there
- Irony: IBM engineers work on OpenTofu and OpenBao (Vault fork)

---

## GitLab

### Financial Performance
- Public company (NASDAQ: GTLB)
- FY2025: $759.2M revenue
- FY2026: $955.2M revenue (26% growth)
- Net loss: $56.0M (FY2026) vs $6.3M (FY2025) — wider loss but improving cash flow
- Operating cash flow margin: 24% (up from -8%)
- Gross margin: 87%
- 10,682+ base customers; 50%+ of Fortune 100

### Business Model
- Open-core: Community Edition (free) + Enterprise features (paid subscriptions)
- "Dual flywheel": R&D team + community contributions create virtuous cycle
- Almost all revenue from paid tier subscriptions

---

## Grafana Labs

### Financial Performance
- $400M+ ARR (as of Sep 2025)
- $270M ARR in June 2024 (69% YoY growth)
- $6B valuation (Aug 2024 Series D extension)
- 7,000+ customer organizations
- 20M total users; monetizing ~1% of them

### Business Model
- Hybrid open-source/commercial
- Grafana Cloud (SaaS) + Grafana Enterprise Stack (self-hosted)
- 80-90% gross margins via open-source-led growth
- Customers: Anthropic, NVIDIA, Salesforce, Microsoft
- 2025 Gartner Magic Quadrant Leader for Observability

---

## The PEXT Finding
- Research analyzing 44 open-source developer tools (2020-2025) [VERIFY: exact source, authors, publication]
- Key finding: "Control of distribution and operational infrastructure matters more than control of code"
- Business model predicts outcomes more reliably than community metrics
- Implication: GitHub stars, contributor counts matter less than who controls the deployment/hosting layer

---

## Open-Core Criticisms & Tensions

### The "Rug Pull" Pattern
- Companies use open source for distribution → build community → change license
- Examples: MongoDB (AGPL → SSPL, 2018), Elastic (Apache → SSPL/Elastic, 2021), HashiCorp (MPL → BSL, 2023), Redis (BSD → SSPL, 2024)
- Redis reversed course in 2025: added AGPL as option, citing forks had differentiated enough
- ScyllaDB, Fluent Assertions also moved to source-available in 2025

### AI Disruption of Open Source Economics
- Tailwind CSS: used by 617K+ websites, 75M downloads/month — but revenue dropped 80%
- Cause: AI tools generate Tailwind CSS directly, documentation traffic dropped 40%
- Documentation was how developers discovered commercial products
- Broader threat: if AI can replicate open-source code, what's the moat?

### Market-Level Data
- Global open source software market: $45.9B (2025), projected $190.1B by 2034 (17.12% CAGR)
- AI-related tools captured 48% of all developer tool investments in 2024
- 40% of dev teams globally using open source CI/CD or container orchestration (2024)

---

## Key Quotes

- Paul Copplestone: "I didn't build the startup for investors, I just built what I thought would be the best product for developers." [VERIFY source]
- Guillermo Rauch: Open source is "a speedrun to product-market fit, because if people don't use it when it's free, when it's easy to consume, when the code is available, then you probably should be working on something else" [Source: First Round Review]
- Rauch: "you could create open-source software targeted at engineers, while simultaneously building an enterprise business based on services and infrastructure" [Source: First Round Review]
- PEXT: "Control of distribution and operational infrastructure matters more than control of code" [VERIFY exact source]

---

## Sources (for further verification)

- TechCrunch: Supabase $5B valuation (Oct 2025), $2B valuation (Apr 2025)
- Fortune: Supabase $100M raise at $5B
- BusinessWire: Vercel Series F at $9.3B (Sep 2025)
- First Round Review: Vercel's path to product-market fit (Rauch interview)
- Sacra: Supabase and Vercel financial profiles
- GitLab IR: FY2025 and FY2026 earnings releases
- Grafana Labs press releases (Sep 2025, Feb 2026)
- Ghost Foundation: About page, O'Nolan's X posts
- HashiCorp blog: BSL announcement (Aug 2023)
- The New Stack, Slashdot: "rug pull" coverage
