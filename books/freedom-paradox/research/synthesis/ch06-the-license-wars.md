# Synthesis: Chapter 6 — The License Wars

**Based on:** ch06-license-wars-research.md, open-source-universe-deep-research.md (Part VI), chapters 3-5 for continuity
**Purpose:** Chapter-ready summary for drafting

---

## Narrative Arc

Chapter 6 is the legal infrastructure chapter — but it must read as drama, not taxonomy. The central tension: licenses encode philosophy, and when the philosophy breaks down, the licenses become battlefields.

**Opening hook:** August 10, 2023 — HashiCorp changes Terraform's license. Within five days, a manifesto appears. Within six weeks, the Linux Foundation accepts a fork. 33,000 GitHub stars on a document about licensing. This is what it looks like when a community feels betrayed.

**Core argument:** Licenses are not paperwork. They are the legal encoding of values. GPL = Stallman's ethics made enforceable. MIT = the 1998 pragmatists' bet that maximum adoption matters more than guaranteed freedom. Apache = the corporate compromise (patent protection without copyleft's obligations). The license you choose IS your philosophy.

---

## Key Narrative Threads

### Thread 1: The Spectrum as Philosophy

The permissive-to-copyleft spectrum maps directly onto the free-software vs. open-source split from Chapters 3-4:

- **MIT/BSD** = "We trust the ecosystem. Give freely, let the market sort it out." This is the 1998 rebranding's license — pragmatic, corporate-friendly, no moral demands.
- **GPL** = "We do not trust the ecosystem. Freedom must be enforced or it will be enclosed." This is Stallman's license — moral, protective, deliberately inconvenient for those who would close what has been opened.
- **Apache** = "We mostly trust the ecosystem, but we want patent protection." The corporate-grade permissive license.
- **AGPL** = "We saw the SaaS loophole and we're closing it." GPL updated for the cloud era.

The shift from GPL dominance (2000s) to MIT/Apache dominance (2020s) is the license-level expression of the cultural shift described in Chapter 4: from ethics to pragmatism, from Stallman to Raymond.

### Thread 2: The Cloud Provider Problem

The BSL/SSPL revolt is the central drama. Structure it as:

1. **The setup:** Permissive licenses invited corporate participation (Chapter 4's story). Companies like MongoDB, Redis, Elasticsearch chose permissive or weak-copyleft licenses to maximize adoption.
2. **The betrayal (as the companies see it):** AWS and other cloud providers took these databases and offered them as managed services, capturing the monetization layer.
3. **The response:** MongoDB SSPL (2018), Elastic SSPL (2021), HashiCorp BSL (2023), Redis SSPL (2024). Each a company saying: "The social contract is broken."
4. **The counter-response:** Forks. OpenSearch, OpenTofu, Valkey. The community (backed by cloud providers) saying: "If you close, we fork."
5. **The paradox:** Everyone is right. The companies built on open source and feel their work is being exploited. The cloud providers built on open source and are exercising the freedoms the license granted. The community built on open source and will not accept enclosure. The system has no mechanism to resolve these competing claims.

### Thread 3: Ostrom's Missing Boundaries

This is the intellectual payoff. Ostrom's work on commons governance provides the framework for understanding WHY the license wars happened:

- Successful commons require clear boundaries, monitoring, and graduated sanctions
- Open source deliberately resisted all three — boundaries felt like gatekeeping, monitoring felt like surveillance, sanctions felt like enclosure
- The result: a commons without mechanisms for enforcing reciprocity
- Cloud providers exploited the gap between "legally permitted" (the license) and "socially expected" (contribute back)
- The BSL revolt was an attempt to add Ostrom's boundaries after the fact
- The fork response showed the community rejecting those boundaries
- Neither side is wrong; the commons was structurally ungovernable

---

## Connective Tissue

### Callbacks to Earlier Chapters:
- Ch 3: GPL as Stallman's "immune system" — copyleft prevents enclosure. But it couldn't prevent the SaaS loophole.
- Ch 4: The 1998 rebranding chose permissive licenses as the default. The BSL revolt is the bill for that choice.
- Ch 5: Kelty's third component (writing copyright licenses) is now the site of the most active conflict. Eghbal's maintenance crisis connects — underfunded maintainers are more vulnerable to cloud extraction.

### Bridge to Chapter 7:
- The companies that figured out a sustainable model — Supabase, Vercel, GitLab — did so by accepting that the code is NOT where the value lives.
- Open core: give away the code, monetize the infrastructure around it.
- The PEXT finding: "Control of distribution and operational infrastructure matters more than control of code."
- This is the answer the BSL companies were looking for — but it requires accepting that trying to control the code is the wrong strategy.

---

## Tone Notes

- This chapter should feel like a war correspondent's dispatch, not a law review article
- The license taxonomy needs to move FAST — readers are here for the drama, not the fine print
- The HashiCorp opening provides the emotional hook: real people, real anger, real consequences
- Ostrom at the end provides the intellectual framework that makes sense of the chaos
- The equity analyst frame: follow the money. AWS's revenue vs. the database companies' revenue. The fork backed by cloud providers. Who benefits?

---

## Verification Needed

- [ ] HashiCorp/IBM acquisition: announced April 2024, closed date? Price confirmed $6.4B?
- [ ] Valkey adoption: 83% figure source
- [ ] AWS annual revenue: most recent figure
- [ ] MongoDB revenue trajectory post-SSPL
- [ ] CockroachDB BSL timeline
- [ ] Sentry FSL timeline
- [ ] OSI 2025 license popularity data (MIT + Apache = 50%+?)
- [ ] Ostrom's specific application to digital/software commons

---

*Synthesis completed March 2026. Ready for chapter drafting.*
