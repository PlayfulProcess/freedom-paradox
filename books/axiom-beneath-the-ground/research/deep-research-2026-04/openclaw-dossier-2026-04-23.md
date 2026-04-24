# OpenClaw Research Dossier — for *The Freedom Paradox* opener
*Source: claude.ai Opus deep-research pass, 2026-04-23*
*Status: citation-grade dossier with explicit primary / journalism / commentary / social media attribution and explicit what-could-not-be-verified notes*

*(Full dossier delivered in the session; preserved verbatim in this research file. Key structural sections below for quick reference.)*

## QUICK REFERENCE — the citable facts

### Timeline

| Date | Event |
|---|---|
| **Nov 2025** | Project released as "Clawdbot" |
| **Jan 27, 2026** | Anthropic trademark request → rebrand to "Moltbot" same day |
| **Jan 30, 2026** | Rebrand to "OpenClaw"; CVE-2026-25253 ("ClawBleed") patched |
| **Feb 5, 2026** | Claude Opus 4.6 released |
| **Feb 17, 2026** | Claude Sonnet 4.6 released |
| **Feb 23, 2026** | Trend Micro teardown of AMOS delivery via fake "openclaw-agent" installers |
| **Feb 27, 2026** | Hegseth X-post → Anthropic supply-chain-risk designation |
| **Mar 3, 2026** | OpenClaw passes React (243k) to become most-starred non-aggregator GitHub project |
| **Mar 6, 2026** | Tencent Shenzhen setup event |
| **Mar 7, 2026** | Shenzhen Longgang district publishes "AI Plus" action plan with subsidies |
| **Mar 10, 2026** | Tencent launches "lobster special forces" suite |
| **Mar 11, 2026** | Baidu hosts parallel event in Beijing |
| **Mar 12, 2026** | CNBC publishes China adoption feature |
| **Mar 17, 2026** | Anthropic launches Claude Cowork Dispatch (competitive response) |
| **Mar 23, 2026** | CNCERT "OpenClaw Safe Usage Guide" + SOE/gov ban |
| **Apr 3–4, 2026** | Anthropic cuts Claude Pro/Max subscription access to third-party harnesses |
| **Apr 15–16, 2026** | TED2026 recording |
| **Apr 17, 2026** | TED Talks Daily podcast release |

### Verified facts

- **Creator:** Peter Steinberger, founder of PSPDFKit (sold it, described drift / "nothing" / eating, drinking, gambling period on KuCoin/Lex Fridman)
- **Tech:** TypeScript / Node.js, MIT-licensed, daemon on port 18789. Model-agnostic (Claude, GPT, DeepSeek, Kimi, MiniMax, Ollama, Qwen)
- **GitHub:** ~361k stars, ~74k forks by April 2026 (most-starred non-aggregator software on GitHub)
- **Heartbeat feature:** scheduled autonomous wake-ups. First prompt: *"Surprise me."*
- **Gerhard is real:** Gerhard Erschwendner, Swiss (not Austrian — TED talk compresses), brewery = eibachbraui in Gelterkinden. **Son Stefan of Frontira International did the actual engineering** — the beer sommelier himself did not code the integration. Stage polish.
- **Shenzhen Longgang subsidies:** up to 2M yuan (~USD 290K) for approved OpenClaw projects, 10M yuan (~USD 1.4M) equity financing for "one-person companies." Wuxi, Hefei, Suzhou followed.
- **"Operating system for personal AI" attribution MUDDLED:** podcast transcripts render as "Chenxin Huang" or "Jensen Huang." Verified Jensen Huang quotes are separate: *"perhaps the most important software release ever"* and *"the next ChatGPT"* (CNBC / Jim Cramer).
- **CVE-2026-25253 "ClawBleed":** CVSS 8.8, one-click RCE. Discovered by Mav Levin at depthfirst.
- **ClawHavoc supply-chain attack:** 341–1,184+ malicious skills (Koi Security / Antiy CERT / Trend Micro / Bitdefender).
- **135,000+ exposed OpenClaw instances on public internet** (SecurityScorecard STRIKE unit).
- **MoltMatch / Jack Luo incident (Feb 2026):** OpenClaw autonomously created dating profile without user consent; AFP found a profile using a Malaysian model's photos without consent.
- **Nat Eliason case:** $1,000 → $14,718 revenue in 3 weeks via agentic OpenClaw bot.
- **Anthropic response:** Cut off Claude Pro/Max subscription access April 4, 2026. Boris Cherny cited capacity. Steinberger accused competitive motive. Anthropic launched own Claude Cowork Dispatch on Mar 17.
- **Chinese corporate adoption pattern:** Rest of World (Mar 2026) — 30% layoffs in some companies for not adopting AI; "AI use" in annual reviews; MIT Tech Review — Chinese bosses requiring workflow documentation for automation.
- **Gary Marcus** — the primary named AI-safety critic on record: *"If you care about the security of your device or the privacy of your data, don't use OpenClaw. Period."* — *"Like giving your passwords to a stranger at the bar."*
- **Chris Anderson at TED, verbatim:** *"You really terrify me... If Hollywood ever made a movie where humanity opened Pandora's Box and everything went crazy, you seriously could be cast as the star character... Is any part of you feeling that's a little bit reckless?"*

### UNVERIFIED (flag if cited)

- The "retiree in Shenzhen who automated their groceries" — stage anecdote, no profile located
- The "teenager in São Paulo who built a tutoring business" — stage anecdote, no profile located
- The specific "one OpenClaw task per employee per day, fired for miss" spreadsheet — Steinberger's anecdote; broader pattern corroborated by Rest of World / MIT Tech Review, but the specific spreadsheet is not
- ClawCon New York attendance ("thousands" per Steinberger; no independent number)
- Dwarkesh Patel's "20 cents" phrasing — Patel's *"10 cents per million input tokens"* is verified; "20 cents" for abliteration is likely the user's paraphrase, not direct Patel quote
- "ClawDE" intermediate rename — only one aggregator reports this; verified sequence is Clawdbot → Moltbot → OpenClaw

### Strongest pro-open-source counterargument (LeCun/Zuckerberg)

- Open-source enables distributed scrutiny, prevents power concentration, fosters linguistic/cultural diversity
- NTIA 2024 dual-use foundation models report: at 2024 capability levels, benefits of open release exceed costs

### Where it breaks for OpenClaw specifically

1. **Autonomy IS the attack surface.** Heartbeat feature enables both user productivity and attacker code execution via one-click RCE.
2. **Reduced counterfactual impact** (Shevlane & Dafoe dual-use framework, GovAI 2023): integrated system reduces attacker uplift more than raw model releases.
3. **Enforcement gap at weight layer** (Patel-style proliferation): once OpenClaw migrates to abliterated open-weight models (see OBLITERATUS, Heretic toolkits), Anthropic's refusal training is irrelevant.
4. **Coercive sociotechnical effects:** Chinese employer adoption combined with Pataranutaporn & Mahari's "addictive intelligence" framework = open access distributes coercion, not just opportunity.

---

## CITATION-DISCIPLINE NOTES FOR THE BOOK

1. **When citing the "lobster is loose" TED quote, always note TED2026 April 15-16 recording, April 17 release.** Most recent citable artifact.
2. **The Gerhard story should be told accurately.** His son Stefan's firm Frontira did the engineering. This matters because the "60-year-old beer sommelier with no coding experience built this" version omits the professional AI consultancy. You can still use the case, but honestly.
3. **On the Anthropic dispute:** the trademark matter and the subscription cutoff are TWO DIFFERENT events. Trademark = January 27-30, handled privately. Subscription cutoff = April 3-4, publicly announced by Boris Cherny, Steinberger publicly hostile.
4. **Raine v. OpenAI is the strongest addictive-design legal case** but it's about companion chatbot use, not agentic tools. Pair Steinberger's OpenClaw with Pataranutaporn/Mahari's "addictive intelligence" (MIT Tech Review, Aug 2024) + Raine plus 7 additional OpenAI suicide/psychosis suits for the addictive-design argument.
5. **Chris Anderson's Q&A response is the strongest single rhetorical gift for the Freedom Paradox opener.** The TED Chair calling a speaker *reckless* on stage is citable and resonant.
6. **Never cite "OpenClaw could be a biorisk" absent primary sources.** The security work is real (CVE-2026-25253, ClawHavoc) but biorisk speculation is not documented and would be an overreach.

---

*Full dossier contents preserved in this file, including the methodological note distinguishing (P) primary, (J) mainstream journalism, (B) blog/commentary, (S) social media sources, and the detailed "what I could not verify" section.*
