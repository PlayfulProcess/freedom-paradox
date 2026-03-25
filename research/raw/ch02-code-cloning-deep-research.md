# Raw Research: Code Cloning — AI Rewrites the Rules of Software

**Sources:** Cloudflare blog, O'Nolan newsletter, Willison blog, Huntley's z80 technique
**Date:** 2026-03-25
**Relevance:** Chapter 2 (primary), Chapter 16 (closing)

---

## 1. The Cloudflare/Vinext Incident

### Timeline
- **February 13, 2026**: First commit to vinext repository by Steve Faulkner
- **February 24, 2026**: Cloudflare publishes blog post announcing vinext
- **Development period**: Under one week of active work
- **Tool used**: Claude AI via OpenCode (800+ sessions)
- **Cost**: ~$1,100 in API tokens

### What Vinext Is
- A drop-in replacement for Next.js, built on Vite instead of Webpack/Turbopack
- Implements 94% of the Next.js API surface [VERIFY: exact percentage, source is The Register headline]
- Open sourced under MIT license at github.com/cloudflare/vinext
- Already deployed in production at National Design Studio [VERIFY: customer name and deployment status]

### Performance Claims
- Build time: 1.67s vs 7.38s (4.4x faster)
- Client bundles: 72.9 KB vs 168.9 KB gzipped (57% smaller)
- [VERIFY: These numbers come from the Cloudflare blog post; need to check methodology and whether these are representative benchmarks]

### Key Quotes
> "Most abstractions in software exist because humans need help... AI doesn't have the same limitation. It can hold the whole system in context and just write the code." — Steve Faulkner [QUOTE NEEDED: verify exact wording from blog post]

### Corporate Context
- Cloudflare is publicly traded ($NET) — this is not a hobbyist experiment
- Cloudflare competes directly with Vercel in the deployment/edge platform space
- Next.js is maintained by Vercel (~$9.3B valuation) [VERIFY: most recent valuation figure]
- Vercel's business model: Next.js is open source (MIT license), Vercel monetizes through hosting/deployment/DX platform
- This is effectively a corporate raid on a competitor's core open-source product, executed by AI
- The MIT license explicitly permits this — that is the point

### Media Coverage
- The Register headline: "Cloudflare vibe codes 94% of Next.js API 'in one week'" [VERIFY: exact headline]
- Widespread developer discussion on Hacker News, X, and Reddit
- [RESEARCH NEEDED: Vercel's official response, if any. Did Guillermo Rauch or anyone at Vercel comment publicly?]

---

## 2. John O'Nolan's Newsletter: "Open Source in the age of AI"

### Publication Details
- **Author**: John O'Nolan, founder and CEO of Ghost
- **Date**: February 26, 2026
- **Platform**: Ghost newsletter
- **Context**: Published two days after Cloudflare's vinext announcement

### O'Nolan's Credibility
- Founded Ghost in April 2013 (Kickstarter: raised £196,362 against £25,000 goal in 29 days)
- Former WordPress core contributor — left to build a more principled alternative
- Ghost is MIT-licensed, run by a nonprofit foundation (Singapore)
- No investors, cannot be sold — structurally incapable of enshittification
- ~28,000 paying customers, $8.86M ARR [VERIFY: most recent figures]
- 0% transaction fees (vs Substack's 10%)
- Ghost 6.0 (August 2025): added ActivityPub support for federated publishing
- This is the model case of ethical, sustainable open source — and even he is questioning the paradigm

### Ghost's Experience with Code Copying
- Substack "wholesale copied and pasted significant chunks of Ghost's source code" [QUOTE NEEDED: verify exact language]
- This happened under the MIT license — it was perfectly legal
- The experience gave O'Nolan firsthand knowledge of what it feels like when your open code becomes a competitor's product

### Key Arguments
1. **Code scarcity was the premise.** Open source licenses were designed when code was expensive and difficult to write. The license framework assumed code was intrinsically valuable.
2. **AI removes the scarcity.** If anyone can point an AI at a codebase and have it rewritten from scratch, the code itself has no moat.
3. **The trajectory applies to closed source too.** Reverse-engineering from public interfaces will become trivial with sufficiently powerful AI.
4. **The Stallman paradox.** AI might fulfill Stallman's vision (all software effectively free to modify) while destroying the infrastructure (community maintenance, shared libraries, collaborative development) that made open source work.

### Key Quotes
> "Any open source project that achieves a degree of success will at some point face the reality of a competing company taking your open source code and using it to compete with you."

> "The dictating of the rules has largely been built upon a premise that code is intrinsically valuable because it's a scarce resource. Difficult to maintain. Expensive to write. AI is now rapidly overturning that premise."

> "If anyone can point Claude at an open source codebase and have it rewritten from scratch, without actually using any of the original code, what does that mean for software licenses? More specifically: Do software licenses mean anything?"

> "In a strange way, I'm beginning to wonder if AI might end up fulfilling [Stallman's] vision more completely than open source ever did."

### The Ghibli Comparison
- O'Nolan compares the code-cloning moment to software's "Studio Ghibli moment" — the AI art controversy where AI-generated images in Ghibli's style went viral
- The parallel: AI doesn't need to copy your work; it can produce functional equivalents at near-zero cost
- The emotional resonance: artisans watching machines replicate what took years to learn

---

## 3. Simon Willison's Code Porting Experiment

### The Experiment (December 2025)
- Ported JustHTML (HTML5 parsing library) from Python to JavaScript
- Tool: GPT-5.2 via Codex CLI [VERIFY: model version — may have been o3 or different model]
- Duration: 4.5 hours
- Scale: 9,000 lines of code, 43 commits
- Test coverage: 9,200 tests passing
- Cost: $29.41 in API tokens (effectively free on a ChatGPT Plus subscription)

### Willison's Own Questions
- Explicitly raised legal/ethical questions in the original blog post
- "Does this library represent a legal violation of copyright of either the Rust library or the Python one?" [QUOTE NEEDED: verify exact wording]

### January 11, 2026 Follow-up: "My answers to the questions I posed about porting open source code with LLMs"
- Acknowledged some open-source maintainers are angry about LLM-derived works
- Bigger concern: LLMs reduce *demand* for open-source libraries
- Why search for a cron parser when you can prompt one into existence?
- The Tailwind example: LLMs make custom implementations cheap enough to build from scratch instead of using shared libraries
- **This threatens the ecosystem model**: open source works because thousands of developers use the same shared infrastructure; if everyone generates bespoke code, the commons collapses

### Willison's Credibility
- Co-creator of Django web framework
- One of the most respected voices in the Python/open-source community
- Prolific blogger on AI tools and their implications
- His willingness to raise these questions publicly carries weight precisely because he is not anti-open-source or anti-AI

---

## 4. Geoffrey Huntley's "z80 Technique"

### What Happened (2025-2026)
- Used LLMs to reverse-engineer Atlassian's Rovo AI assistant from the compiled ACLI binary
- Extracted 100+ Python source files, system prompts, and complete implementation details
- [VERIFY: exact number of files, timeline, and tool used]

### Why It Matters
- Demonstrates that LLMs can convert compiled/obfuscated code back to readable source
- This means CLOSED-source software can also be "opened" by AI
- O'Nolan referenced this work in his newsletter
- The implication: neither open nor closed licenses protect the underlying logic of software

### The Broader Pattern
- Historically, decompilation was possible but produced ugly, hard-to-use code
- LLMs produce *clean*, *readable*, *maintainable* reverse-engineered code
- The barrier between compiled and source code was always more practical than theoretical — LLMs remove the practical barrier entirely

---

## 5. Structural Connections for the Book

### The Scarcity Inversion
- Open source was built on a moral and practical framework that assumed code was scarce and valuable
- The license system (GPL, MIT, Apache) governs how scarce resources are shared
- AI makes code abundant — not just easy to copy, but easy to regenerate from scratch
- When the resource is abundant, the rules for governing scarcity become meaningless
- This is the economic equivalent of the post-scarcity thought experiment: what happens to property rights when replicators exist?

### The Ghost/Stallman Paradox
- Stallman's original complaint: proprietary software restricts user freedom
- His solution: copyleft licenses that force code to remain open
- AI's solution: make all code effectively rewritable, regardless of license
- The paradox: AI achieves Stallman's end (all software is modifiable) but destroys the means (community maintenance, shared libraries, collaborative development)
- O'Nolan sees this clearly: the commons doesn't work when everyone can generate their own bespoke version

### The Three Levels of Code Cloning
1. **Direct copying** (Substack copying Ghost): legal under MIT, ethically contested, been happening for decades
2. **AI rewriting** (Cloudflare rewriting Next.js): no original code used, so copyright doesn't apply at all — this is new
3. **AI reverse-engineering** (Huntley's z80): closed source decompiled and reconstructed — this means even proprietary protection fails

### Bridge to Chapter 3
- Chapter 2 establishes that the current crisis is real and happening now
- But to understand WHY this matters, the reader needs to understand what was built
- The open-source movement started with a moral claim about freedom (Stallman's printer, GNU Manifesto)
- Chapter 3 traces that moral claim from 1983 to the present
- The question Chapter 2 raises — "do licenses mean anything?" — can only be answered by understanding what licenses were FOR

---

## Sources to Verify

| Claim | Status | Source Needed |
|-------|--------|---------------|
| Vinext 94% API coverage | [VERIFY] | Cloudflare blog post or GitHub README |
| $1,100 in API tokens | [VERIFY] | Faulkner's blog post or interview |
| 800+ sessions | [VERIFY] | Same |
| Build time comparison (4.4x) | [VERIFY] | Cloudflare benchmarks |
| Bundle size comparison (57%) | [VERIFY] | Same |
| Vercel ~$9.3B valuation | [VERIFY] | Most recent funding round reporting |
| Ghost ~28,000 customers | [VERIFY] | Ghost's public metrics page or O'Nolan's statements |
| Ghost $8.86M ARR | [VERIFY] | Same |
| Willison used GPT-5.2 | [VERIFY] | Original blog post — may have been different model |
| Huntley extracted 100+ files | [VERIFY] | Original blog post or presentation |
| National Design Studio deployment | [VERIFY] | Cloudflare blog or case study |
| Vercel's public response | [RESEARCH NEEDED] | Search for Rauch/Vercel statements post-vinext |
