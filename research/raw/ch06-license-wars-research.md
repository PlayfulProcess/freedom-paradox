# Chapter 6 Research: The License Wars

**Source:** Raw research compiled from deep research sessions, OSI archives, industry publications, company blog posts, SEC filings, and primary documentation.
**Relevance:** Chapter 6 — The License Wars
**Compiled:** March 2026

---

## 1. The License Spectrum

### Permissive Licenses (Maximum Adoption, Minimum Obligation)

**MIT License:**
- World's most popular open-source license
- Terms: Do anything with the code, keep the copyright notice
- Used by: React, Node.js, jQuery, VS Code, Next.js, Ghost, .NET, Rails
- Maximum adoption, zero friction — but no guarantee that derivatives stay open
- Favored by startups and developer tools
- Dominant in JavaScript/TypeScript ecosystem

**Apache License 2.0:**
- Like MIT + explicit patent grant + patent retaliation clause
- If a licensee sues the licensor over patents, their license is terminated
- Favored by corporations (Google, Microsoft, Amazon) for SDKs and enterprise tools
- Used by: Kubernetes, Android (AOSP), TensorFlow, Apache HTTP Server, Kafka, Spark
- Critical for enterprise products at scale — the patent grant provides legal certainty
- Google's default license for most open-source releases

**BSD Licenses (2-Clause and 3-Clause):**
- Similar to MIT in permissiveness, popular in academic/research contexts
- 2-Clause (Simplified): essentially identical to MIT
- 3-Clause (New BSD): adds a non-endorsement clause
- Apple built macOS on BSD components (FreeBSD, Mach kernel) — impossible under GPL
- Used by: FreeBSD, NetBSD, OpenBSD, portions of macOS/iOS
- PlayStation OS derived from FreeBSD

### Copyleft Licenses (Freedom Propagates)

**GPL v2 (1991) / GPL v3 (2007):**
- Strong copyleft: derivatives must be GPL with source code available
- GPL v2: License of the Linux kernel (Torvalds chose v2 and refused to upgrade to v3)
- GPL v3: Added anti-Tivoization clause (preventing hardware lockdown of modified software), patent provisions
- Also licenses: WordPress, MediaWiki, GIMP, GCC, Bash
- Guarantees freedom propagates but can deter corporate adoption
- Steve Ballmer's 2001 "cancer" comment was specifically about GPL's copyleft

**AGPL (Affero General Public License):**
- Closes the "SaaS loophole" — GPL only triggers on *distribution*; AGPL extends to *network interaction*
- If you modify AGPL code and run it as a web service, you must release source
- Growing in importance due to cloud computing / SaaS
- Used by: MongoDB (before SSPL switch), Grafana (core), Nextcloud
- Many companies (Google, Apple) have internal policies prohibiting AGPL code in their products

**LGPL (Lesser General Public License):**
- Allows linking from proprietary software without triggering copyleft for the linking code
- Used for libraries where the goal is broad adoption: glibc, Qt (dual-licensed), FFmpeg (parts)
- "Lesser" was originally "Library" — Stallman renamed it to discourage overuse

### Popularity Trends (2024-2025 Data)

- MIT and Apache 2.0 together comprise over 50% of top project licenses [VERIFY: exact percentage from GitHub/OSI 2025 data]
- GPL family declining in new project adoption (though dominant projects like Linux remain GPL)
- AGPL growing due to cloud computing concerns
- Permissive licenses rising; copyleft falling as share of new projects
- ISC license gaining modest traction (used by npm/OpenBSD)

---

## 2. The Business Source License (BSL)

**Origin:**
- Created by Michael "Monty" Widenius, original author of MySQL
- Widenius also founded MariaDB (MySQL fork after Oracle acquisition)
- BSL designed specifically to address cloud provider free-riding

**How BSL works:**
- Source code is available (can be read, modified for internal use)
- Prohibits offering the software as a hosted commercial service
- Converts to a fully open license (usually Apache 2.0) after a set period (typically 4 years)
- The "Additional Use Grant" defines exactly what's restricted
- After the conversion date, the code becomes standard open source

**Used by:**
- MariaDB (MaxScale and other tools)
- HashiCorp (Terraform, Vault, Consul, Nomad — August 2023)
- CockroachDB (changed from Apache 2.0 to BSL in June 2024) [VERIFY: CockroachDB BSL date]
- Sentry (November 2024 — switched from BSL to FSL, Functional Source License) [VERIFY: Sentry license timeline]
- ClickHouse [VERIFY]

**OSI position:** BSL is NOT an open-source license. It is "source-available." The OSI has been clear that restricting commercial hosting violates the Open Source Definition.

---

## 3. The Cloud Provider Problem: How AWS Triggered the License Wars

**The pattern:**
- Cloud providers (primarily AWS, also Azure, GCP) took popular open-source databases
- Offered them as fully managed services (pay-per-use, zero maintenance)
- Captured the monetization layer without contributing meaningfully back
- The original companies bore the cost of development; the cloud providers captured the revenue

**Specific examples of AWS wrapping open-source projects:**
- Amazon ElastiCache — wrapped Redis
- Amazon DocumentDB — compatible alternative after MongoDB switched to SSPL
- Amazon OpenSearch Service — forked Elasticsearch after Elastic's license change
- Amazon MQ — wrapped ActiveMQ and RabbitMQ
- Amazon Managed Streaming for Apache Kafka (MSK) — wrapped Kafka
- Amazon Aurora — compatible with MySQL and PostgreSQL

**The economics:**
- AWS's annual revenue exceeds $100 billion [VERIFY: most recent AWS annual revenue]
- Open-source database companies collectively generate a fraction of that
- The companies that created the databases bear R&D costs; AWS captures hosting revenue
- AWS argument: they contribute patches, employ maintainers, and grow the ecosystem
- Critics' argument: AWS extracts far more value than it contributes

**The philosophical divide:**
- Permissive license advocates: "This is what MIT/Apache allows. You chose that license."
- Original companies: "The social contract is broken. We built it; they monetize it."
- Cloud providers: "We provide value through managed services. The code alone isn't the product."

---

## 4. The SSPL Revolt: Company-by-Company

### MongoDB → SSPL (October 2018)

**Timeline:**
- October 2017: MongoDB IPO (NASDAQ: MDB)
- October 2018 (12 months later): Changed from AGPL to Server Side Public License (SSPL)

**What SSPL requires:**
- Modified AGPL Section 13
- If you offer the software as a service, you must release ALL source code for the *entire service stack*
- This includes: management software, user interfaces, APIs, monitoring tools, backup systems, hosting software, and automation — everything needed to offer the service
- The requirement is so broad it's practically impossible for cloud providers to comply without open-sourcing their entire infrastructure

**Reactions:**
- OSI refused to recognize SSPL as open source
- Red Hat, Debian, Fedora all dropped MongoDB from their repositories
- AWS responded by building Amazon DocumentDB — a MongoDB-compatible but proprietary alternative
- MongoDB's stock and revenue continued to grow despite the change [VERIFY: MongoDB revenue trajectory post-SSPL]

**Key insight:** MongoDB proved you could change licenses and survive commercially. This emboldened others.

### Elastic → SSPL + Elastic License (January 2021)

**Timeline:**
- Elasticsearch originally Apache 2.0
- January 2021: Switched to dual SSPL + Elastic License
- Elastic's CEO Shay Banon explicitly cited AWS as the reason [QUOTE NEEDED: Banon's blog post on the license change]

**The fork:**
- AWS, with Logz.io, CrateDB, Red Hat, and Aiven, forked Elasticsearch as OpenSearch
- OpenSearch placed under the Linux Foundation with Apache 2.0 license
- OpenSearch has since developed independently

**Partial return:**
- Late 2024: Elastic added AGPLv3 as a third licensing option
- Partial return to open source, acknowledging the community cost of the SSPL switch [VERIFY: exact date of AGPL addition]

### Redis → SSPL/RSAL (March 2024)

**Timeline:**
- Redis historically BSD-licensed (extremely permissive)
- March 2024: Redis Labs moved core Redis to dual RSAL (Redis Source Available License) + SSPL
- Within weeks: Amazon, Google, Oracle, Ericsson backed Valkey fork under Linux Foundation

**The Valkey fork:**
- Started from Redis 7.2.4 (last BSD-licensed version)
- 83% of large companies using Redis had adopted or were testing Valkey by late 2024 [VERIFY: source for 83% figure]
- Valkey quickly reached feature parity and developed its own roadmap
- Reached v9 with independent features [VERIFY: current Valkey version]
- Linux Foundation backing gave it institutional legitimacy

**Redis's reversal:**
- Antirez (Salvatore Sanfilippo), Redis's original creator, rejoined the project
- Pushed for return to open source
- May 2025: Redis added AGPLv3 as a licensing option, effectively returning to open source [VERIFY: exact date]
- But Valkey continued independently — the fork had already established its own community
- Classic example: you can change back, but you can't unfork

### HashiCorp → BSL (August 10, 2023)

**Timeline:**
- Terraform licensed under Mozilla Public License 2.0 (weak copyleft, permissive for most uses)
- August 10, 2023: HashiCorp announced ALL products (Terraform, Vault, Consul, Nomad, etc.) switching to BSL v1.1
- August 15, 2023: OpenTF Manifesto published
- August 25, 2023: Fork announced
- September 20, 2023: Linux Foundation accepted OpenTF → renamed OpenTofu
- January 2024: OpenTofu first stable release (v1.6.0)

**Community response:**
- 33,000+ GitHub stars on the OpenTF manifesto repository
- ~140 companies pledged support
- ~700 individuals pledged support
- CNCF could no longer use Terraform (policy requires 100% open-source toolchains)

**The IBM acquisition:**
- 2025: IBM acquired HashiCorp for approximately $6.4 billion [VERIFY: exact acquisition price and close date — announced April 2024, closed late 2024 or early 2025]
- Irony: HashiCorp's BSL switch may have been partially motivated by making the company more attractive for acquisition (cleaner revenue story without cloud provider competition)

---

## 5. The Fork Response Pattern

**Pattern observed across all cases:**

1. Company changes license to restrict cloud hosting
2. Community erupts (manifesto, open letter, social media campaign)
3. Fork announced within days or weeks
4. Linux Foundation (or CNCF) provides institutional home
5. Major cloud providers back the fork (ironic: the same companies the license change targeted)
6. Fork achieves feature parity and develops independently
7. Some companies reverse course (Redis, Elastic) — but the fork persists anyway

**The Linux Foundation's role:**
- Has become the institutional home for "community response" forks
- OpenSearch (from Elasticsearch)
- Valkey (from Redis)
- OpenTofu (from Terraform)
- Provides governance, trademark protection, and corporate neutrality
- Funded by membership dues from major tech companies (including the cloud providers)

**The power dynamic:**
- The fork threat is real and potent — but it's backed by the same cloud providers that caused the license change
- AWS, Google, Microsoft fund the Linux Foundation
- They have a direct financial interest in keeping databases under permissive licenses
- The "community" response is partly genuine grassroots and partly corporate interest masquerading as community
- This makes the narrative more complex than "company vs. community"

---

## 6. Creative Commons

- Founded 2001 by Lawrence Lessig, Hal Abelson, and Eric Eldred
- Not a software license — for creative works (text, images, music, educational materials)
- License types: CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC0
- Wikipedia uses CC BY-SA
- Kelty's *Two Bits* uses CC BY-NC-SA
- Billions of works licensed under CC worldwide
- Essential to broader "commons culture" beyond software
- State of the Commons (2023): over 2.5 billion CC-licensed works [VERIFY: most recent figure]
- Lessig's broader argument: copyright has expanded far beyond its original purpose, enclosing culture that should be shared

---

## 7. The Commons Intellectual Framework

**Elinor Ostrom (1933–2012):**
- Political economist at Indiana University
- 2009 Nobel Prize in Economic Sciences (first woman to win)
- Challenged Garrett Hardin's 1968 "Tragedy of the Commons" thesis
- Hardin argued: shared resources inevitably get overexploited without privatization or state control
- Ostrom showed: communities CAN successfully govern shared resources — if they have the right institutional structures

**Ostrom's eight design principles for governing commons:**
1. Clearly defined boundaries (who has rights, what is the resource)
2. Rules adapted to local conditions
3. Collective-choice arrangements (affected parties participate in rule-making)
4. Monitoring by the community
5. Graduated sanctions for rule violators
6. Conflict-resolution mechanisms
7. Minimal recognition of rights to organize (external authorities don't interfere)
8. Nested enterprises (for large-scale resources, governance at multiple levels)

**Application to open source:**
- Open source has some of these (collective choice, some monitoring, conflict resolution via forks)
- But it conspicuously lacks: clear boundaries (who is "in" the community?), graduated sanctions (what happens to free-riders?), monitoring of extraction
- The BSL revolt can be read as an attempt to add boundaries and sanctions to the open-source commons
- The fork response can be read as the community rejecting those boundaries

**The paradox Ostrom illuminates:**
- Open source resisted boundaries because boundaries felt like enclosure
- But without boundaries, there's no way to enforce reciprocity
- Cloud providers exploited this gap — they were "in" the commons for extraction and "out" for contribution
- The commons worked when participants shared roughly similar resources (code for code)
- It broke when one class of participant (cloud providers) could extract at a scale the commons couldn't match

---

## 8. Key Quotes to Track Down

- Shay Banon (Elastic CEO) on why they changed the license [QUOTE NEEDED]
- Armon Dadgar (HashiCorp co-founder) on the BSL switch: "a balanced approach" [QUOTE NEEDED]
- Salvatore Sanfilippo (Antirez) on Redis's return to open source [QUOTE NEEDED]
- Ostrom on why commons governance requires boundaries [QUOTE NEEDED]
- Lessig on Creative Commons and the enclosure of culture [QUOTE NEEDED]

---

## 9. Financial Data Points

| Company | Event | Financial Context |
|---------|-------|-------------------|
| MongoDB | SSPL switch (Oct 2018) | 12 months post-IPO. Revenue continued growing. Market cap ~$30B by 2024 [VERIFY] |
| Elastic | SSPL switch (Jan 2021) | Public company (NYSE: ESTC). Revenue ~$1.26B FY2024 [VERIFY] |
| Redis Labs | SSPL switch (Mar 2024) | Private, raised $347M total. Valued at ~$2B [VERIFY] |
| HashiCorp | BSL switch (Aug 2023) | Public (NASDAQ: HCP). Acquired by IBM for ~$6.4B [VERIFY] |
| AWS | Cloud services | Annual revenue >$100B. Open-source databases are a small fraction but significant draw |

---

## 10. Open Questions for Further Research

1. Did Ostrom ever comment on software commons specifically? Her work focused on fisheries, irrigation, forests — but the principles transfer. Any direct application?
2. What is the current status of the OSI's position on SSPL? Have they softened?
3. How has the BSL conversion clause worked in practice? Has any BSL-licensed code actually converted to Apache yet?
4. What does the CockroachDB license change tell us? They went BSL after watching MongoDB, Elastic, and HashiCorp — a second wave.
5. Is there a comprehensive study of revenue impact for companies that changed licenses?

---

*Compiled March 2026. Sources include OSI archives, company blog posts, Linux Foundation announcements, SEC filings, GitHub repositories, and industry analysis.*
