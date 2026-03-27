# The Open Source Universe: History, Strategy, Culture, and Analogous Movements
## A Deep Research Document

**Source:** Deep research session, March 2026
**Relevance:** Chapters 3, 4, 5, 6, 7, 8, 9, 14, 15

---

## Part I: The History and Founding of Open Source

### The Prehistory: Sharing as Default (1950s–1970s)

- Before "open source" had a name, sharing code was simply how things worked
- Software shipped alongside hardware with source code freely available
- The SHARE users group, founded 1955, first documented distribution October 17, 1955
- Universities, research labs, Bell Labs all operated in open collaboration
- Ken Thompson designed first UNIX at Bell Labs, late 1960s — the shared substrate of modern computing
- UNIX distributed freely across universities and labs; users could modify at will

**The end of openness (late 1970s–early 1980s):**
- Legal decisions granted software copyright protection
- Bell Labs copyrighted UNIX in 1979
- NDAs and proprietary licenses became the norm
- Best programmers hired away from universities into closed shops

### Richard Stallman and the Free Software Movement (1983–1998)

- The rebellion started with a printer at MIT's AI Lab
- Stallman couldn't fix a malfunctioning printer because manufacturer wouldn't share source code
- 1983: Announced the GNU Project to create a complete free operating system
- Early 1985: Published "The GNU Manifesto" — founding charter of the free software movement
- 1985: Established the Free Software Foundation (FSF)

**The Four Freedoms:**
- Freedom 0: To run the program for any purpose
- Freedom 1: To study how the program works and modify it
- Freedom 2: To redistribute copies
- Freedom 3: To distribute copies of your modified versions

**GPL:**
- First version of GNU General Public License released 1989
- Encodes "copyleft" — uses copyright law to guarantee freedom rather than restrict it
- Any derivative work must carry the same license
- By early 1990s: GNU had GCC (compiler), Emacs (editor), most OS components — but no kernel

### Linus Torvalds and Linux (1991)

- Finnish student Linus Torvalds released Linux kernel in 1991 — the missing piece for GNU
- Developed in a radically new way: open, decentralized, chaotic, effective
- By mid-1990s: GNU/Linux viable alternative to proprietary UNIX
- Eric S. Raymond's 1997 essay "The Cathedral and the Bazaar" documented the phenomenon
  - "Cathedral" = centralized, planned development
  - "Bazaar" = decentralized, emergent development (Linux model)

### The Naming: "Open Source" Is Born (1998)

**January 1998:** Netscape announced it would release Navigator source code — seismic event

**The strategy session (Palo Alto, CA):**
- Attendees: Eric Raymond, Bruce Perens, Michael Tiemann, Jon "maddog" Hall, Larry Augustin, Sam Ockman
- Christine Peterson suggested the term "open source"
- Motivation: "free software" confused people and alienated business
- "Open source" emphasized practical benefits over ideology

**February 1998:** Raymond & Perens founded the Open Source Initiative (OSI)
- Linus Torvalds endorsed the following day

**April 1998:** Tim O'Reilly's "Open Source Summit" brought together:
- Torvalds (Linux), Larry Wall (Perl), Brian Behlendorf (Apache), Guido van Rossum (Python), others

**Stallman rejected the rebranding** — maintained "free software" carries essential ethical meaning that "open source" deliberately discards. Split persists.

### Key Figures Directory

| Person | Contribution |
|--------|-------------|
| Ken Thompson | Designed UNIX at Bell Labs |
| Richard Stallman | Founded GNU Project (1983), FSF (1985), authored GPL |
| Linus Torvalds | Created Linux kernel (1991), created Git (2005) |
| Eric S. Raymond | Wrote "The Cathedral and the Bazaar," co-founded OSI |
| Bruce Perens | Co-founded OSI, authored the Open Source Definition |
| Christine Peterson | Coined the term "open source" |
| Tim O'Reilly | Organized the Open Source Summit, publishing advocate |
| Larry Wall | Created Perl |
| Guido van Rossum | Created Python |
| Brian Behlendorf | Co-founded the Apache HTTP Server project |
| Ian Murdock | Founded Debian, early OSI board member |
| Michael Tiemann | OSI president, early GCC contributor |

---

## Part II: Big Tech Strategies and Open Source

### The Chrome/Chromium Gambit: Open Source as Market Capture

- Google launched Chrome 2008, simultaneously released Chromium (open source)
- Chromium provides: Blink (rendering), V8 (JavaScript), browser architecture
- Chrome adds proprietary: auto-updates, cloud sync, licensed media codecs

**Strategic goals achieved:**
1. Web standards evolved in directions favorable to Google's services
2. Attracted developer contributions worldwide
3. Created gravitational pull so strong competitors surrendered

**Microsoft's capitulation:**
- After decades of own engines (Trident, EdgeHTML)
- December 2018: Announced rebuild of Edge on Chromium
- CEO Satya Nadella told Edge team in 2017 product needed to be better; pushed for open-source engine
- New Chromium-based Edge launched January 2020

**Result:** Two-vendor ecosystem on one engine
- Chrome: ~65% market share
- Edge: second-most popular desktop browser
- Brave, Opera, Vivaldi, OpenAI and Perplexity browsers — all Chromium

**Strategic lesson:** "Open core" — open source the foundation, monetize the service layer above
**Criticism:** Dramatically reduced browser engine diversity. Only WebKit (Safari) and Gecko (Firefox) remain independent.

### Android: Open Source as Global Dominance

- Google acquired Android Inc. for $50M in 2005; first phone 2008
- Android Open Source Project (AOSP) — any manufacturer can use for free

**Market numbers (early 2026):**
- Android: ~70–73% global mobile OS, ~3.9 billion active devices
- iOS: ~27–29%
- Android: 38.94% of ALL global OS market share (all device types)

**Why open wins on volume:**
- Hundreds of manufacturers at every price point
- Sub-$200 phones = primary internet gateway for billions in Asia, Africa, Latin America
- India: Android ~95–97% share

**But iOS dominates in:**
- United States (~58–60%)
- Japan (~69%)
- Premium/ultra-premium globally
- Revenue: iOS captures ~68–70% of global app revenue despite fewer users
- App Store: $10.40/month avg vs. Android's $1.40
- 2025 total app spending: $155.8B, iOS ~70%

**Google's real monetization:** Not the OS — search, advertising, services distributed through Android. Real lock-in = Google Mobile Services (GMS), which is proprietary.

**Zuckerberg's motivation for Meta's open-source AI:**
> "One of my formative experiences has been building our services constrained by what Apple will let us build on their platforms. Between the way they tax developers, the arbitrary rules they apply, and all the product innovations they block from shipping..."

---

## Part III: Open Source Startups — Supabase, Vercel, and the New Model

### The "Open Core" Business Model

**Supabase:**
- Founded 2020 by Paul Copplestone (CEO) and Ant Wilson (CTO)
- Open-source alternative to Firebase, built on PostgreSQL
- Valuation: ~$5 billion (2025)
- GitHub Stars: 81,000+
- Active Databases: Over 1 million
- Built from: Postgres, PostgREST, GoTrue (auth), Deno (edge functions)
- Every component can be self-hosted
- 10,000 GitHub stars within six months
- $30M Series A October 2021, 16 months after founding
- Marketing spend: virtually zero — growth via community, SEO, word of mouth
- Clients: 1Password, PwC, Johnson & Johnson

**Vercel:**
- Founded by Guillermo Rauch (creator of Next.js)
- Valuation: ~$9.3 billion
- Next.js: one of the most popular React frameworks, MIT license
- Monetizes through deployment platform: zero-config CI/CD, global edge, serverless, AI SDK

**The "holy trinity" of modern startup dev:** Vercel + Supabase + GitHub

**The research finding (PEXT, 44 open-source developer tools 2020–2025):**
> "Control of distribution and operational infrastructure matters more than control of code."

**Other examples:** GitLab, HashiCorp (acquired by IBM for $6.4B in 2025), PlanetScale, Grafana Labs

---

## Part IV: AI — The Open vs. Closed Frontier

### The Landscape

- **Closed:** OpenAI's GPT, Google's Gemini, Anthropic's Claude — proprietary weights, data, architecture
- **Open-weight:** Meta's Llama, Mistral, Alibaba's Qwen, DeepSeek's R1 — weights public, training data often not
- **Truly open source:** EleutherAI's GPT-NeoX, BigScience's BLOOM — everything public

### Meta's Llama Bet — and Reversal

- Zuckerberg: Meta's ad business model means releasing models doesn't undercut revenue
- Llama models downloaded over 1.2 billion times
- OSI: Llama models "fail in spectacular ways" at qualifying as open source (restrictive terms, undisclosed training data)
- **The reversal:** After Llama 4 "Behemoth" underperformed and DeepSeek R1 replicated Llama architecture:
  - Meta pivoted to proprietary model "Avocado" for 2026
  - CapEx raised to $70–72 billion

### OpenAI's Unexpected Turn

- August 2025: Released GPT-OSS — first open-weight models since GPT-2 (2019)
- Altman on Reddit: OpenAI had been "on the wrong side of history" re: open source
- **But:** GPT-OSS released behind the frontier (GPT-5 launched two days later)

### DeepSeek: The Earthquake

- Chinese startup; R1 model released as open source
- Demonstrated open models could rival proprietary at fraction of cost
- Yann LeCun: "Open source models are surpassing proprietary ones"
- Accelerated erosion of assumption that only massive, closed labs could produce frontier AI

### Emerging Consensus

> Open source behind the frontier, closed source at the cutting edge

- 38,000 derivatives of Mistral
- 140,000 derivatives of Llama
- 160,000 derivatives of Qwen

---

## Part V: Literature — "Two Bits" and the Theory of Recursive Publics

### Christopher M. Kelty's Two Bits (2008)

- Duke University Press, ethnographic research from Boston to Berlin to Bangalore
- Kelty: then Rice University, now UCLA

### The Key Concept: Recursive Publics

> A public organized around the ability to build, modify, and maintain the very infrastructure that gives it life in the first place.

- Distinguishes free software communities: they don't just USE a medium, they CREATE and MAINTAIN it
- Extends Habermas's public sphere and Michael Warner's work on publics
- Adds: the technical infrastructure IS part of the political contestation
- "Geeks don't just argue about freedom — they build the systems that embody it"

### The Five Components

1. Sharing source code — the baseline
2. Conceiving open systems — standards and protocols (TCP/IP)
3. Writing copyright licenses — GPL, copyleft, legal infrastructure
4. Coordinating collaboration — mailing lists, version control, governance
5. Proselytizing — the moral and technical vision

### Broader Resonance

- Extends to Creative Commons, open textbook projects
- The movement shaped the internet as a single, open network
- Published under Creative Commons license — embodying its own principles

### Essential Reading List

- Raymond, *The Cathedral and the Bazaar* (1999)
- Levy, *Hackers* (1984)
- Lessig, *Free Culture* (2004)
- Benkler, *The Wealth of Networks* (2006)
- Coleman, *Coding Freedom* (2012)
- Tozzi, *For Fun and Profit* (2017, MIT Press)

---

## Part VI: Commons Culture and Open Source Licenses

### The License Landscape

**Permissive Licenses:**

- **MIT License:** World's most popular. Do whatever you want, keep copyright notice. Used by React, Node.js, jQuery, VS Code.
- **Apache License 2.0:** Like MIT + explicit patent grant + patent retaliation clause. Favored by corporations (Google, Microsoft, Amazon).
- **BSD Licenses (2/3-Clause):** Similar to MIT, popular in academic/research. Apple built macOS on BSD — impossible under GPL.

**Copyleft Licenses:**

- **GPL v2/v3:** Strong copyleft. Derivatives must be GPL with source. License of Linux, WordPress, MediaWiki. Guarantees freedom propagates but can deter corporate adoption.
- **AGPL:** Closes SaaS loophole. Network interaction triggers source-code obligation.
- **LGPL:** Allows linking from proprietary software without triggering copyleft.

**The New "Source-Available" Category:**

- **Business Source License (BSL):** Popularized by MariaDB, HashiCorp. Nearly permissive but prohibits hosting as commercial service. Converts to fully open (usually Apache) after ~4 years.
- HashiCorp's 2023 switch of Terraform from MPL to BSL → community forked as OpenTofu under Linux Foundation

**Creative Commons:**
- Not a software license but essential to broader commons culture
- CC BY, CC BY-SA, CC BY-NC, etc.
- Wikipedia: CC BY-SA
- Kelty's Two Bits: CC BY-NC-SA

### The Commons Intellectual Framework

- Elinor Ostrom's Nobel-winning work on common pool resources (challenging "tragedy of the commons")
- Lawrence Lessig's work on free culture and Creative Commons
- Yochai Benkler's "commons-based peer production"

---

## Part VII: Nonprofit and Community Projects

### Ghost

- Founded April 2013 by John O'Nolan (former WordPress core contributor) and Hannah Wolfe
- Kickstarter: raised £196,362 (against £25,000 goal) in 29 days
- MIT license, managed by Ghost Foundation (nonprofit, Singapore)
- No investors, cannot be sold
- ~28,000 active paying customers, $8.86M annual run rate (2025)
- 34 employees, 16 nationalities, 5 continents
- 0% transaction fees (vs. Substack's 10%)
- 100 million installs, 51,000+ GitHub stars
- Users: Stanford Review, The Atlantic, Y Combinator, Kickstarter, Harvard International Review
- August 2025: Ghost 6.0 added ActivityPub for federated publishing

### Python Software Foundation (PSF)

- Python fully open source 1999; PSF founded 2001
- BSD-style license
- Guido van Rossum: BDFL until stepping down 2018; now Steering Council
- World's most popular language (TIOBE index)
- Critical for AI/ML, web dev, data science, education

### The Linux Foundation

- Founded 2000 (merger of OSDL and Free Standards Group)
- Hosts 100+ projects: Kubernetes, Node.js, Hyperledger, Let's Encrypt
- Members: Google, Microsoft, IBM, Intel, Huawei, Samsung, virtually every major tech company
- Linux: virtually every server, every Android phone, 100% of Top 500 supercomputers

### The Apache Software Foundation (ASF)

- Founded 1999; manages 350+ projects
- Apache HTTP Server, Kafka, Spark, Hadoop, Cassandra
- Volunteer board; all contributions from individuals

### Other Foundations

- **Mozilla Foundation:** Firefox, last major independent browser engine
- **Eclipse Foundation:** Enterprise Java, IoT
- **CNCF:** Kubernetes, Prometheus, containerd

---

## Part VIII: Analogous Movements — Open Culture Beyond Code

### Crowdfunding: Disintermediation of Capital

- Kickstarter (2009), Indiegogo (2008), GoFundMe (2010), Patreon (2013)
- Kickstarter: $5.6B+ across 284,000+ funded projects
- Ghost launched via Kickstarter; Pebble raised $10.3M; Oculus raised $2.4M (then acquired by Facebook for $2B)
- Kickstarter became Public Benefit Corporation in 2015

**Structural analogy to open source:**
- Bottom-up decision-making
- Bypassing traditional gatekeepers
- Validation by community rather than institutional authority

### The Chosen: Crowd-Funded Media at Scale

- Multi-season TV series about Jesus
- First season: 16,000+ investors, $11M — largest crowdfunded media project ever
- Used equity crowdfunding (JOBS Act of 2016), one share per dollar
- "Pay-it-forward" model
- Season 5: funded by 100,000+ donors
- 356 million views, 50+ languages, free through own app
- Challenge: fewer than 5% of viewers contribute financially

### Wikipedia and Wikimedia

- Launched 2001; CC BY-SA license
- Millions of volunteer editors, community consensus governance
- Nonprofit Wikimedia Foundation, funded by donations
- Runs on MediaWiki (GPL)

### Creative Commons and Public Domain

- Founded 2001 by Lawrence Lessig
- CC licenses adopted for billions of works
- Project Gutenberg (1971), Internet Archive, Wikimedia Commons

### Open Science and Open Access

- PLOS, arXiv, Plan S initiative
- Preprint servers transformed science communication (especially during COVID-19)

### Open Hardware

- OSHWA, Arduino, RepRap, RISC-V, Open Compute Project (Facebook/Meta)

### Cooperative and Platform Cooperative Movements

- Platform cooperativism: worker-owned alternatives to Uber, Airbnb
- Stocksy, Up & Go

---

## Part IX: Current State and Future Directions (2025–2026)

### The Consolidation Paradox

- Open source has won — and become entangled with power structures it challenged
- Every Fortune 500 relies on open-source infrastructure
- GitHub (Microsoft-owned): 400M+ repositories

**Concerns:**
- **Sustainability crisis:** Critical projects maintained by 1–2 unpaid volunteers. Log4j (2021) exposed how much internet rests on unfunded labor.
- **Corporate capture:** Companies benefit while contributing unevenly. BSL/SSPL shifts = pushback.
- **"Open-source washing":** Meta uses language of open source while maintaining restrictions.
- **Demographic aging:** Linux kernel community faces "graying" problem.

### The Open Source AI Question

- OSI released Open Source AI Definition in 2024 — remains contested
- Meta's Llama doesn't qualify by OSI standards
- Unresolved: Must training data be disclosed? Are weights alone "source"? What does "freedom to modify" mean when retraining costs millions?

### What Endures

> From the SHARE users group in 1955 to DeepSeek in 2025, the pattern repeats: when knowledge is shared, it multiplies.

> The deepest significance of open source isn't just the code — it's the demonstration that communities can build, maintain, and govern their own infrastructure.

---

## Supplement: The Book Gap (Why 2008–2020 Had Few Major Books)

The 2005–2008 boom was the "meaning-making" phase. The movement had crossed from subculture to mainstream but was still contested enough to be interesting to scholars.

**Key cluster:** Raymond (1999), Lessig (2004), von Hippel (2005), Benkler (2006), Chesbrough (2005/2006), Tapscott (2006), Kelty (2008), Coleman fieldwork began (published 2012), Fogel (2005), Weber (2004).

**Why the discourse dried up:**
1. Open source won — winning killed narrative tension. By 2010–2012, debate was over.
2. Questions fragmented into domain-specific (healthcare, government, AI, education)
3. Tension shifted to maintenance and sustainability — unglamorous reality
4. Intellectual energy moved to adjacent domains: platform capitalism, surveillance capitalism, AI governance

**Recent era books:**
- Eghbal/Asparouhova, *Working in Public* (2020) — maintenance, creator dynamics, "stadium" model
- Tozzi, *For Fun and Profit* (2017) — historical synthesis
- Coleman, *Coding Freedom* (2012) — anthropology of hacking
- Coleman, *Hacker, Hoaxer, Whistleblower, Spy* (2014) — Anonymous
- Brasseur, *Forge Your Future with Open Source* (2018)

**The gap worth filling:** No current book synthesizes the 2020s landscape — AI open/closed wars, BSL revolts, sustainability crisis, Supabase/Vercel model, DeepSeek, Meta's flip-flop — with the cultural-philosophical depth Kelty brought to the 2000s. The material is there. The narrator hasn't shown up yet.

---

*Compiled March 2026. Sources include Wikipedia, OSI archives, academic research, industry publications, and primary documentation.*
