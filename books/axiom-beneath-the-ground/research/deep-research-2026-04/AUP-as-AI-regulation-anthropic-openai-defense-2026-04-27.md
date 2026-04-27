# Research Memo: The OpenAI Foundation as De Facto AI Regulator via AUP Enforcement — Anthropic vs. OpenAI Defense Case Study

*Compiled by parallel deep-research session, April 27, 2026.*
*Source-quality discipline: STRICT = named reporter at WSJ/Reuters/Bloomberg/FT/NYT/AP/CNBC + primary corporate/government documents; LESS STRICT = think tank, advocacy, Substack commentary. Each strand below is labeled.*

---

## I. Anthropic's Acceptable Use Policy Evolution (STRICT)

### Original posture (2023–early 2024)

Anthropic's original Usage Policy (now Acceptable Use Policy, "AUP") prohibited use of Claude to "produce, modify, design, market, or distribute weapons, explosives, dangerous materials or other systems designed to cause harm to or loss of human life," and banned use for "domestic surveillance." These specific prohibitions — including the explicit ban on Claude for **domestic surveillance** — have been continuously maintained since June 2024 (*Reason*, Liz Wolfe, Feb 28 2026 — verified policy text directly).

Important: Anthropic's AUP language references *domestic surveillance* and *weapons designed to cause harm*, NOT the more political-sounding phrases "mass surveillance of US citizens" or "remote weapons against US citizens." Those framings appear in Anthropic's litigation and public statements, not the AUP text itself.

### June 6, 2024 government carve-out

Anthropic's "Expanding Access to Claude for Government" post (anthropic.com, primary source) carved out exceptions enabling "legally authorized foreign intelligence analysis, such as combating human trafficking, identifying covert influence or sabotage campaigns, and providing warning in advance of potential military activities." Preserved restrictions on "disinformation campaigns, the design or use of weapons, censorship, and malicious cyber operations."

### November 7, 2024 Palantir / AWS / IL6 partnership

Press release (Business Wire, palantir.com, anthropic.com): Claude 3 and 3.5 made available "to U.S. intelligence and defense agencies" via Palantir's AI Platform on AWS, in **Impact Level 6 (IL6)** environment — DoD-accredited up to "Secret." Coverage: TechCrunch (Wiggers), Axios, Bloomberg, CNBC. *The Register* noted that, by contrast with Meta's Llama, "no such clear-cut [military] restrictions are included in Anthropic's acceptable use policy."

### 2025–2026 escalation

- **June 2025**: Claude Gov launched.
- **July 2025**: DoD contracts up to $200M each to Anthropic, Google, OpenAI, xAI. Claude later stated "the Department's most widely deployed and used frontier AI model" (Anthropic statement quoted in CRS Report IN12669).
- **August 2025**: Claude for Government to all three branches at $1/agency for one year.
- **February 24, 2026**: RSP v3.0 dropped unilateral pause commitment. Kaplan in *Time*: "We didn't really feel, with the rapid advance of AI, that it made sense for us to make unilateral commitments… if competitors are blazing ahead."
- **February 27, 2026**: Pentagon designated Anthropic "supply chain risk" after refusal to drop AUP language. Trump issued Truth Social directive: federal agencies "IMMEDIATELY CEASE" use of Anthropic.
- **March 9, 2026**: Anthropic sued in N.D. Cal. and D.C. Circuit.
- **March 26, 2026**: Judge Rita F. Lin (N.D. Cal.) issued preliminary injunction. April 8, 2026: D.C. Circuit denied Anthropic's stay (TechPolicy.Press timeline; CRS IN12669).

The litigation complaint quotes AUP red lines as: "Anthropic's Usage Policy has always conveyed its view that Claude should not be used for two specific applications: (1) lethal autonomous warfare and (2) surveillance of Americans en masse" (quoted in *Lawfare*, Wittes). *Lawfare* notes the actual textual prohibitions in the AUP are narrower than these litigation summaries.

---

## II. OpenAI Usage Policies and Defense Work (STRICT)

### January 10, 2024 quiet removal

Until Jan 10 2024, OpenAI's policy banned "weapons development" and "military and warfare." On Jan 12, 2024, **Sam Biddle of *The Intercept*** broke the story that OpenAI quietly removed the "military and warfare" prohibition. Confirmed by TechCrunch (Coldewey), Engadget. Niko Felix (OpenAI): rewritten to "create a set of universal principles."

### December 4, 2024 Anduril partnership

Joint statement (anduril.com): "If the United States cedes ground, we risk losing the technological edge that has underpinned our national security for decades." Coverage: Bloomberg (Chapman, Ghaffary), *Washington Post* (De Vynck), *Axios* (Rosenberg), CNBC. *MIT Technology Review*: "completing OpenAI's military pivot."

### June 16, 2025 — $200M Pentagon contract

DoD CDAO awarded OpenAI a contract with $200M ceiling, $1,999,998 obligated at award (DoD daily contracts list; *Breaking Defense*, Freedberg; CNBC). To "develop prototype frontier AI capabilities to address critical national security challenges." OpenAI launched **OpenAI for Government** simultaneously.

### February 28, 2026 — classified Department of War agreement

OpenAI's "Our agreement with the Department of War" (openai.com) named three "red lines":
1. No mass domestic surveillance
2. No autonomous weapons systems direction
3. No high-stakes automated decisions

Reported by Bloomberg (McArthur), NPR. Came **hours after** Trump's Anthropic blacklist directive.

OpenAI's March 2 update added: "Consistent with applicable laws, including the Fourth Amendment… FISA Act of 1978, the AI system shall not be intentionally used for domestic surveillance of U.S. persons."

In the same blog, OpenAI explicitly contrasted with Anthropic: **"Other AI labs have reduced or removed their safety guardrails and relied primarily on usage policies as their primary safeguards in national security deployments. We think our approach better protects against unacceptable use."** OpenAI is publicly arguing against AUPs as the primary governance mechanism while embracing in-the-loop technical safeguards.

### Caitlin Kalinowski resignation, March 7, 2026

Kalinowski (joined OpenAI Nov 2024 as hardware/robotics lead) posted at 10:30 AM March 7, 2026: "I resigned from OpenAI… surveillance of Americans without judicial oversight and lethal autonomy without human authorization are lines that deserved more deliberation than they got. This was about principle, not people."

Follow-up: "To be clear, my issue is that the announcement was rushed without the guardrails defined. It's a governance concern first and foremost."

Coverage: NPR, *Fortune*, TechCrunch (Ha), *San Francisco Standard*. OpenAI spokesperson Kayla Wood: "We believe our agreement with the Pentagon creates a workable path for responsible national security uses."

### April 17, 2026 senior departures — relationship to defense unclear

Three OpenAI executives departing same day: **Kevin Weil** (VP, OpenAI for Science, formerly CPO), **Bill Peebles** (head of Sora), **Srinivas Narayanan** (CTO B2B/enterprise applications). Coverage: TechCrunch (Bellan), CNBC, *Wired*. **Reported drivers in named reporting: strategic restructuring + personal reasons. None of the three named departures was tied in WSJ/Reuters/Bloomberg/FT/NYT/AP/CNBC reporting to Pentagon/defense concerns specifically.** TheNextWeb reported "some executives left over ethical concerns about a Defense Department AI contract" — unclear who, not corroborated.

---

## III. The "Pentagon Threatened Anthropic First, OpenAI Filled the Opening" (LESS STRICT)

### What is documented in major-outlet reporting (STRICT)

- **Temporal sequence:** NPR, CNBC: Anthropic blacklisted Friday Feb 27 afternoon; OpenAI agreement announced Friday evening / Saturday.
- **Pentagon CTO Emil Michael (CBS News):** "At some level, you have to trust your military to do the right thing… We'll never say that we're not going to be able to defend ourselves in writing to a company."
- **Hegseth's X statement:** Anthropic was attempting "to seize veto power over the operational decisions of the United States military."
- **Hegseth's January 2026 AI Strategy Memorandum:** all DoD AI contracts to incorporate standard "any lawful use" language within 180 days (*Lawfare*).
- **Reuters reporting (in CRS):** "Anthropic representatives opposed the use of the company's products for surveillance or to develop lethal autonomous weapons." Per CRS: "Anthropic inquired about DOD's use of Claude, generating concerns within the department that Anthropic might not approve of certain use cases."
- **Axios:** Pentagon "hoping that its negotiations with Anthropic will force OpenAI, Google, and xAI to also agree to the 'all lawful use' standard." Anthropic's partnership reevaluated specifically because Anthropic asked whether Claude was used in the Jan 3, 2026 Maduro/Caracas operation.
- **Defense Production Act threat:** Reported by *Lawfare*, *Axios* — Hegseth threatened to invoke DPA against Anthropic in the Feb 24, 2026 meeting with Amodei.

### What is alleged but NOT corroborated by major-outlet named reporting (LESS STRICT)

- **Zvi Mowshowitz "Don't Worry About the Vase" Substack:** Frames campaign as politically motivated. Quotes Aakash Gupta: "OpenAI, Google, and xAI all signed deals giving the military access to their models with minimal safeguards. Only Claude is deployed on the classified networks used for actual sensitive operations."
- **Tyler Cowen (in *The Free Press*):** "The United States government, when it has a disagreement with a company, should not respond by trying to blacklist the firm."
- **Jacobin (E.A. Halevi, April 2026):** "OpenAI capitalized on the fracas by signing a new $200 million military contract. The deal reportedly came together under the direction of [Joseph] Larson, the former Secretary of Defense staffer turned OpenAI head of government, whom the Pentagon contacted when its attempt to renew its contract with Anthropic began to flounder." Most explicit version of "OpenAI capitalized" narrative; sourced to *Jacobin*'s anonymous "reports."
- **EFF (Guariglia, Feb 24 / March 3 / March 24 2026):** "the state of your privacy is being decided by contract negotiations between giant tech companies and the U.S."

### Public statements (STRICT)

- **Hegseth on X:** Anthropic was "sanctimonious" and "arrogant"; "America's warfighters will never be held hostage by the ideological whims of Big Tech."
- **Amodei (CBS News, Feb 27 2026):** government actions "retaliatory and punitive"; restrictions rooted in "the safety and reliability" of current models.
- **Amodei's Oct 2025 Anthropic blog:** rebuffed "inaccurate claims" from Trump administration (per WSJ).
- **David Sacks on All-In podcast (Oct 2025):** Anthropic are "AI doomers" running "sophisticated regulatory capture strategy based on fear-mongering."

### Bottom line on the "blacklist threat" narrative

**Documented:** Pentagon escalated to blacklist over Anthropic's AUP-based refusals; OpenAI signed a deal hours later; OpenAI publicly argued AUPs are worse safeguard than its layered approach; Pentagon publicly stated it wants "all lawful use" standard from all vendors.

**Speculation:** That OpenAI orchestrated or capitalized on the blacklist; that the campaign was driven by competitor lobbying (Andreessen et al.); that there was a coordinated "destroy Anthropic" effort. Substack/advocacy commentary; should be labeled if cited.

The **strong** version ("Pentagon punished Anthropic for enforcing its AUP") works on STRICT sourcing alone. The **stronger** narrative ("OpenAI strategically positioned itself") is mostly less-strict commentary.

---

## IV. AUP/TOS as De Facto AI Governance — Broader Context

### Absence of binding US AI regulation through April 2026 (STRICT)

- **Biden EO 14110** (Oct 30 2023) **rescinded by Trump's EO 14148 on Jan 20, 2025.** Jan 23 2025: Trump's "Removing Barriers to American Leadership in Artificial Intelligence." Biden EO's safety reporting and red-teaming requirements lapsed. AISI rebranded as Center for AI Standards and Innovation (CAISI).
- **California SB-1047** vetoed Sept 29 2024. Successor **SB 53** (Transparency in Frontier AI Act) signed Sept 29 2025, effective Jan 1 2026. Civil penalties capped at $1M. Transparency law, not substantive use-restriction law. Does not regulate AUPs.
- **NY RAISE Act** — passed June 2025, on Hochul's desk through Jan 1 2026.
- **EU AI Act:** prohibitions and AI literacy obligations Feb 2 2025; GPAI obligations Aug 2 2025; bulk of remaining obligations Aug 2 2026; high-risk product-related rules Aug 2 2027. Regulates *systemic risk* and *transparency*, not "may not be used for mass surveillance of Americans."

**Strict-sourcing conclusion:** between April 2025 and April 2026, no enforceable U.S. federal regulation prohibits an AI lab from supplying its models for mass surveillance or autonomous weapons. **AUPs are doing the actual line-drawing.**

### Specific AUP/ToS tests (STRICT)

- **Microsoft / Israel / IDF Unit 8200 (2025):** Microsoft's primary blog (Brad Smith, May 15 / Aug 15 / Sept 25 2025). Guardian / +972 Magazine / Local Call investigation (Aug 2025, Davies and others) reported Unit 8200 used Azure to store mass-surveillance recordings of Palestinian phone calls. Microsoft Sept 25 2025: **disabled specific IDF subscriptions** for ToS violation. *This is a clean case of an AUP enforced ex post by the vendor against a sovereign customer in the absence of binding regulation.*
- **Google AI Principles, Feb 4 2025:** Tiku and De Vynck (*Washington Post*) reported Google removed 2018 commitments not to apply AI to "weapons" or "surveillance." Confirmed by CNBC, CNN, Al Jazeera, TechCrunch.
- **DeepSeek and Qwen open-weights:** AUPs unenforceable because developer loses control after release.

---

## V. OpenAI Foundation Powers Relevant to AUP Enforcement (STRICT)

### Primary source: California AG MOU (Oct 27, 2025)

- Foundation holds **Class N Common Stock** giving exclusive ability to appoint or remove all PBC board members. ~26% of OpenAI Group PBC ($130B+ at Oct 2025 valuation).
- §7: prior-written-approval rights for Foundation over six categories of PBC actions.
- **Safety and Security Committee (SSC)** sits at nonprofit Foundation, has authority "to require mitigation measures up to and including halting the release of models or AI systems."
- AG Bonta statement (Oct 28 2025): "we secured concessions that ensure charitable assets are used for their intended purpose, safety will be prioritized."

### Tyler Whitmer interview (LESS STRICT but on-record)

Whitmer, attorney for the AG-led investigation, on *80,000 Hours* podcast (Oct 30 2025): "The current announcement gives the board of the nonprofit — through a special class of shares, the N class of shares — the right to elect the board members of the PBC. So they have control over who sits on the board, and although non-exclusive, the right to fire board members of the PBC as well."

### Whether the Foundation can veto PBC AUP changes (interpretive)

The MOU does NOT explicitly list "Acceptable Use Policy changes" among §7 categories requiring Foundation prior approval. However:
- Foundation can **appoint and remove** all PBC board members. AUP changes are board-supervised.
- SSC's authority to "halt model releases even where applicable risk thresholds would otherwise permit release" is broad enough that an SSC determination that an AUP change would expand misuse risk could be invoked. **Not publicly tested.**
- OpenAI mission statement was changed in 2024 to drop the word "safely" — IRS Form 990 disclosure released Nov 2025.

### Has Zico Kolter (SSC chair, Foundation-only director) made public AUP statements?

**As of April 27, 2026, no major-outlet named reporting has documented a Kolter statement on the AUP.** **This is conspicuous.** If the Foundation's #1 job is AUP enforcement, the SSC chair's public silence on the most consequential AUP-relevant deal in the company's history is itself notable.

---

## VI. Theoretical support — AUPs as de facto regulation (LESS STRICT)

### Named voices

- **Helen Toner** (interim ED CSET, ex-OpenAI board): May 2024 *Economist* op-ed with McCauley argued "private companies pushing forward the frontier of a revolutionary new technology [cannot] be expected to operate in the interests of both their shareholders and the world." Senate testimony, X account. Sept 29 2025 thread re: SB 53 — OpenAI sent her a subpoena to her home, corroborated by *Politico* and *San Francisco Standard*.
- **Jan Leike**: left OpenAI for Anthropic May 2024 citing safety prioritization.
- **Lawfare** (Wittes, March 2026 posts): most substantive public legal analysis of "what the AUP means as law" in the Anthropic-DoW dispute.
- **Margot Kaminski / Mark Lemley**: established academic frame on platform ToS as private governance.

### Foundation-controlled-public-company precedents (STRICT where possible)

- **Hershey Trust:** ~24% economic / ~80% Class B voting (Bloomberg Dec 11 2024). **Used control to block multiple acquisitions** (Wrigley/Nestle 2002, Mondelēz 2016, Mondelēz again late 2024). 2002 attempt to *sell* blocked by PA Orphans' Court (*In re Milton Hershey School Trust*). **However, Hershey is about M&A, not operating-conduct rules.**
- **Novo Nordisk Foundation:** ~28% economic / ~77% voting via Novo Holdings. **No major-outlet reporting** of Foundation overriding Novo Nordisk pricing or pharma practices on conduct grounds. Hands-off on operational matters.
- **Carlsberg Foundation:** Similar pattern — no public record of Foundation overriding operating-company conduct decisions.

**Honest read:** There is no clean precedent for a controlling foundation enforcing operating-company conduct rules (such as AUPs). Hershey is closest but is M&A. **The OpenAI Foundation enforcing AUPs against the PBC would be doing something novel.**

---

## VII. Bottom line for the essay

### Strands that are STRONG (STRICT-sourceable)

1. The absence of binding US AI regulation through April 2026.
2. AUPs are doing actual governance work right now; the Anthropic-DoW dispute is canonical proof.
3. OpenAI Foundation has on-paper powers (Class N, SSC veto, prior-approval) sufficient to enforce or veto AUP changes in principle.
4. The contrast between Anthropic and OpenAI is concrete and quotable. OpenAI explicitly argues AUPs are inferior safeguard to layered technical approach.

### Strands that are WEAKER

1. The "OpenAI strategically capitalized on Anthropic's blacklisting" narrative — mostly Substack/advocacy, not WSJ/Reuters/etc.
2. The "Pentagon threatened to blacklist Anthropic over its AUP" framing is partly documented but partly speculation.
3. **No named public statement by Kolter / SSC connects Foundation governance powers to AUP enforcement.** Conspicuous silence.
4. Hershey/Novo/Carlsberg precedents do NOT support AUP-style conduct enforcement by parent foundations. AUP enforcement would be unprecedented.
5. April 17 2026 senior departures (Weil, Peebles, Narayanan) NOT tied in named reporting to defense concerns. Only Kalinowski's March 7 resignation has documented defense-concern motivation.

### Calibrated argument

"In the absence of binding regulation, AI labs' Acceptable Use Policies have become the de facto regulatory floor for what AI may not be used for in the United States — and the OpenAI Foundation, holding Class N Common Stock and SSC authority over the PBC, is the only structurally well-positioned body to enforce them."

This is supportable on STRICT sourcing with these calibrations:
- Premise (no regulation) is solid.
- Diagnostic case study (Anthropic vs. DoW; OpenAI's same-day deal; substantive AUP language) is solidly documented.
- Foundation-powers analysis is solid as to what's *possible*, but the Foundation has not publicly claimed AUP enforcement as a core function and the SSC has not (publicly) reviewed the Feb 28 2026 deal on AUP grounds.
- The Foundation-as-AUP-enforcer thesis is *prescriptive* (what the Foundation should do) more than *descriptive* (what the Foundation has done). Foreground this.
