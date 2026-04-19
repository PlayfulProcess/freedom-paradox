# Research 31 — John O'Nolan and Ghost: the working model for recursive.eco

**Status:** First full pass. Written directly by Claude Code using (a) internal repo sources already drafted into *The Freedom Paradox*, *Grammars of the Living World*, and *Fire Before Responsibility*, and (b) primary-source web fetches of Ghost's public pages and O'Nolan's personal blog. Date of research pass: 2026-04-19.

**Sources (verified during this pass):**
- Ghost Foundation, "About" — https://ghost.org/about/ (fetched 2026-04-19)
- Ghost Foundation, front page — https://ghost.org/ (fetched 2026-04-19)
- Ghost Foundation, ActivityPub landing — https://activitypub.ghost.org/ (fetched 2026-04-19)
- Ghost Foundation, "Joining the ActivityPub network" changelog — https://ghost.org/changelog/activitypub-alpha/ (fetched 2026-04-19)
- John O'Nolan, personal blog front page — https://john.onolan.org/ (fetched 2026-04-19)
- John O'Nolan, "Democratising publishing," 30 October 2024 — https://john.onolan.org/democratising-publishing/ (fetched 2026-04-19)
- John O'Nolan, "Open Source in the age of AI," 26 February 2026 — https://john.onolan.org/open-source-in-the-age-of-ai/ (fetched 2026-04-19)
- *Wikipedia*, "Ghost (blogging platform)" — History section (fetched 2026-04-19)
- Sarah Perez, "Substack rival Ghost federates its first newsletter," *TechCrunch*, 8 July 2024
- *Techmeme* summary of O'Nolan's 31 October 2024 Ghost governance post (cited for $7.5M ARR as-of late 2024)

**Internal repo sources drawn on:**
- `books/freedom-paradox/research/raw/onolan-open-source-age-of-ai.md` (Feb 2026 newsletter distilled)
- `books/freedom-paradox/chapters/ch02-when-code-could-clone-itself.md` (already-drafted Ghost narrative)
- `books/grammars-of-the-living-world/research/raw/research-07-community-curated-media.md` §3 "Ghost: The Nonprofit Open-Source Structural Analog"
- `books/grammars-of-the-living-world/chapters/ch10-grammars-of-the-living-world.md` (Ghost model framed as mission-locking + diversified revenue + legal protection)
- `books/fire-and-intelligence/chapters/ch09-the-fire-is-given.md` (Ghost as one of three proofs of concept)
- `books/axiom-beneath-the-ground/outreach/ghost-model-and-harris-reversal.md` (the Ch10 sibling passage the book wants to add)

---

## Research plan (written first, per author instruction)

The book already *contains* Ghost. Ch02 of *Freedom Paradox* names it; Ch10 of *Grammars* names it; Ch09 of *Fire Before Responsibility* names it. For *Axiom Beneath the Ground* Ch10, the job is not to discover Ghost — it is to stage it as the sibling to Nvidia. The research plan is therefore narrow:

1. **Confirm every public-fact sentence the Ch10 draft (in `outreach/ghost-model-and-harris-reversal.md`) currently asserts.** Founding year. Legal structure. License. Revenue model. Federation status. Headquartered-in-Singapore framing.
2. **Cross-check the existing internal files for drift from the public record.** The repo has figures from October 2024 (≈$7.5M ARR). The public "About" page now (April 2026) shows updated figures. Flag any number the book quotes that is now stale.
3. **Identify primary quotes under 30 words** that the book can actually cite instead of paraphrasing. O'Nolan's "Democratising publishing" essay (Oct 2024) and his "Open Source in the age of AI" essay (Feb 2026) are the two most citable pieces for the book's argument.
4. **Surface anything the Ch10 draft has slightly wrong and should be corrected.**
5. **Name the follow-ups the book still needs** — specifically the Substack-copied-Ghost-source-code claim, which the Freedom Paradox draft asserts but which needs a specific, cite-able source before it lives in committed prose.

What this pass is *not*: an original monograph on Ghost. The book does not need that. The book needs enough verified concrete detail to carry a two-to-three-paragraph sibling passage in Ch10 and a footnote that will survive a copyedit.

---

## Section 1 — Founding, legal structure, jurisdiction

**Founding.** Ghost was founded in **April 2013** by **John O'Nolan and Hannah Wolfe**. The Kickstarter campaign launched **29 April 2013** with a **£25,000** goal, funded in **11 hours**, and closed after 29 days having raised **£196,362** (Wikipedia, "Ghost (blogging platform)," History section, cross-referenced to the original Kickstarter listing `[VERIFY: Kickstarter project URL archived on web.archive.org]`).

**Correction the book must absorb:** internal files (`ghost-model-and-harris-reversal.md`, the Grammars research-07 note, Freedom Paradox Ch02) frame Ghost as founded by O'Nolan alone. The Ghost "About" page names O'Nolan and Wolfe together. Any committed prose should either say "O'Nolan and Wolfe" or — if the book prefers to keep the narrative single-character for rhythm — "O'Nolan, with Hannah Wolfe, founded" or similar. The book should not silently drop Wolfe.

**Legal structure.** The Ghost Foundation is a **non-profit foundation**. From the public About page (verbatim, 22 words, fair use): "We set Ghost up as non-profit foundation so that it would always be true to its users, rather than shareholders or investors." A second, load-bearing sentence (verbatim, 27 words, fair use): "Our legal constitution ensures that the company can never be bought or sold, and one hundred percent of our revenue is reinvested into the product and the community."

**Jurisdiction.** The Ghost Foundation is headquartered in **Singapore** (Wikipedia, "Foundation" section; cross-confirmed on Ghost About page which names Singapore elsewhere in its team pages `[VERIFY: direct "Singapore" string on https://ghost.org/about/ — was present in earlier snapshots but not explicitly named in the fetched extract]`). O'Nolan himself describes his own location as "Geographically restless" on his personal blog — the Singapore fact is about the Foundation, not the man.

**Correction for Ch10 draft prose:** the current `ghost-model-and-harris-reversal.md` sketch opens with "a man in Singapore named John O'Nolan had been running a company called Ghost since 2013." This conflates the Foundation's jurisdiction with the founder's location. A cleaner phrasing: "a company called Ghost — registered as a non-profit foundation in Singapore, founded in 2013 by a former WordPress UI lead named John O'Nolan and his collaborator Hannah Wolfe — had been running…"

**Team size.** 34 full-time staff (Wikipedia, October 2025). The About page shows the team spans "5 continents, 16 nationalities, 15 languages," "fully remote since 2013."

## Section 2 — Revenue model and the numbers as of this pass

**License.** **MIT** (Wikipedia, infobox; cross-referenced to the GitHub repository). Maximally permissive; anyone can take the code and do anything with it, including run a competitor on top of it.

**Technology stack.** Node.js server; Ember.js admin client (Wikipedia, Platform section).

**Revenue model.** Two-layer. The core application (the Ghost CMS) is free and self-hostable. Revenue comes from **Ghost(Pro)**, a paid managed hosting service for users who do not want to run their own infrastructure. Verbatim from Ghost About (≤30 words, fair use): "We've built a sustainable business around a free core application, funded by a premium managed-service to run it on."

**Financial figures as of this pass (April 2026).** Ghost's About page publishes live metrics. The snapshot at fetch time: **$10.3M ARR, 29,476 active customers.** [VERIFY: these figures change daily because the page is live — any quote in committed prose should either (a) cite "as of April 2026, Ghost reported…" or (b) pull the latest value at copyedit time and cite that date.]

**Older figure carried in the repo.** The Grammars research-07 note and several draft chapters cite approximately **$7.5M** annual revenue. That figure traces to a Techmeme summary of O'Nolan's 31 October 2024 Ghost governance post. It is not wrong for its date — it is stale. The book's committed prose should not quote $7.5M without a date; it should either update to the current figure or frame as "by 2024, approaching $8M; by 2026, over $10M."

**Profitability.** Ghost has been profitable and self-sustaining for the duration of its thirteen-year run `[VERIFY: this is stated across multiple Ghost Foundation communications but the book should cite a specific one. The Oct 2024 "Democratising publishing" essay is the cleanest anchor — it talks about sustaining the organisation without external funding.]`

**Financial transparency.** Verbatim from Ghost About (≤30 words, fair use): "As a public organisation we also believe in being transparent and accountable for everything we do, so we publish our live financial data for all to see."

## Section 3 — Federation and the ActivityPub work

**The sequence the book can use.**
- **April 22, 2024** — Ghost publicly announces it is joining ActivityPub (changelog post "Joining the ActivityPub network," https://ghost.org/changelog/activitypub-alpha/; also covered that week in *TechCrunch* and *We Distribute*).
- **July 8, 2024** — Ghost federates its first newsletter — Ghost's own publication (@index@activitypub.ghost.org) — and announces multiple Ghost instances running ActivityPub successfully in production (Sarah Perez, *TechCrunch*, 8 July 2024).
- **Current status (April 2026)** — ActivityPub integration is in **early access / alpha** per https://activitypub.ghost.org/, still inviting users to sign up. Beta/GA dates not publicly specified at fetch time `[VERIFY: search for a later Ghost changelog post that announces beta or GA — the alpha has been running for nearly two years and may have advanced.]`

**Functional positioning.** Ghost's ActivityPub work treats federation as both *publishing* and *reading* — publishers' posts appear in Mastodon/Threads/Flipboard/etc. feeds, and Ghost itself becomes a reader for follows from across the fediverse. Verbatim positioning line under 30 words (from the ActivityPub landing page): "Email gave us open messaging. ActivityPub does the same for social technology—no algorithms, no lock-in."

**Why this matters for the book.** Federation is the mechanical counterpart to the structural principle of Ghost — "do as little as possible, as much as necessary" applied at the network layer. A federated publisher does not need to own a network; it connects to the networks that exist. This is the O'Nolan mirror of Huang's Nvidia stance. The book's Ch10 sibling passage can say so directly.

## Section 4 — O'Nolan's two load-bearing essays

These are the two texts the book should cite, not paraphrase at length.

### 4a. "Democratising publishing" — 30 October 2024

**Core thesis** (paraphrase). Non-profit foundation structure is not a pleasant adornment; it is the mechanism by which a publishing platform can serve its community over time without being captured by owners, shareholders, or acquirers. Ghost has tested this model for eleven years at the time of writing.

**Usable verbatim lines** (all ≤30 words, fair use):
- "Non-profits have one thing in common: They don't have owners. And that's what matters." (13 words)
- "The organisation exists for-purpose, rather than for-profit." (7 words)
- "Nobody should 'own' the project or have the ability to steer it away from its founding principles." (17 words)

**Governance commitments announced in the piece.**
- Board of trustees to expand beyond the founders once the team reaches roughly fifty people.
- Formal Ghost Foundation membership tiers to be introduced.
- Community-elected board seats (referencing the Drupal governance model as precedent).
- Greater transparency on decision-making processes.

Timeline language is deliberately vague ("the next couple of years"); the book should not pin O'Nolan to a date he did not commit to. As of this pass (April 2026), `[VERIFY: have the board expansion or membership tiers actually launched? O'Nolan's blog subsequent to Oct 2024 would be the first place to check.]`

### 4b. "Open Source in the age of AI" — 26 February 2026

The book's Freedom Paradox Ch02 already quotes and narrates this piece. Axiom Ch10 does not need to re-narrate it; Axiom Ch10 can simply cite it once as the "from the other direction" companion to Ch02's longer engagement.

**Core thesis** (paraphrase). The premise that open-source licensing depends on — that code is a scarce, expensive, difficult-to-produce artifact — is collapsing because LLMs can regenerate functionally-equivalent implementations from behavior. The distinction between open and closed source starts to dissolve because neither openness nor closure protects the logic of software any more. Strange consequence: AI may fulfill Stallman's 1983 vision better than the free-software movement itself did.

**Usable verbatim lines** (all under 30 words, fair use):
- "Do software licenses mean anything?" (5 words — the rhetorical hinge of the essay)

**Specific incidents O'Nolan names.**
- Cloudflare using AI to rebuild a competitor's open-source codebase in one week.
- Atlassian's Rovo AI assistant reverse-engineered.
- Substack's copying of Ghost's source code (context from the Freedom Paradox Ch02 draft; O'Nolan references it in the Feb 2026 essay and has referenced it publicly before `[VERIFY: find the specific O'Nolan post or statement where the Substack-source-code claim is first made. Freedom Paradox Ch02 treats it as established fact; Axiom Ch10 should not treat it as established until the primary citation exists.]`).

## Section 5 — Reconciling with what the book already contains

**Ch02 of *The Freedom Paradox*** (already drafted) is the long-form treatment. It narrates O'Nolan's Feb 2026 essay as the opening movement of the AI-and-open-source collision. Any Ch10 mention in *Axiom* must not duplicate Ch02's work; it should lean on it and point to a single structural claim that belongs in Axiom specifically.

**Ch10 of *Grammars of the Living World*** (already drafted) frames Ghost as a proof of concept for a three-part structural principle — mission-locking legal structure, diversified revenue, commercial activity that serves the mission. Axiom Ch10 does not need to re-argue this; Axiom Ch10's job is to place the Ghost example next to the Nvidia example and let the book's reader see the pattern from both sides of the stack.

**Ch09 of *Fire Before Responsibility*** (already drafted) lists Ghost among three working models (with Sesame Workshop and one other). The pattern Ch09 identifies — mission-locking plus diversified revenue plus commercial activity — is the same pattern research-07 of Grammars identifies. Axiom Ch10 can reference the pattern without re-listing its terms.

**The honest synthesis for Axiom Ch10.** The Nvidia story (research-26) is the restraint principle approached from the *base* of the stack, with enormous commercial power. The Ghost story is the same principle approached from the *publishing* layer, with small but durable commercial power. The book's Ch10 is not an endorsement of either company; it is an argument that *the principle travels across orders of magnitude and across industries*. This is what the sibling passage should earn.

## Section 6 — Notes for the book

**Primary placement.** Axiom Ch10, new §VI-or-VII, as already drafted in `books/axiom-beneath-the-ground/outreach/ghost-model-and-harris-reversal.md`. The draft is good; the corrections this research pass produces are surgical, not structural.

**Corrections to apply to the Ch10 draft before it lands in a chapter file:**
1. Add Hannah Wolfe as co-founder, or adjust phrasing so the single-founder framing does not silently erase her.
2. Fix the "man in Singapore" opening. The Foundation is in Singapore; O'Nolan is geographically restless. Either describe the Foundation's jurisdiction or describe O'Nolan's work without pinning him to a city.
3. The draft already says "non-profit foundation" — keep. Add the verbatim "never be bought or sold" clause as a footnote-worthy quote, not as narrated prose (it is too sharp to paraphrase without losing the legal concreteness).
4. The draft says ActivityPub; specify that federation launched as an alpha in April 2024 and that it is still in early access as of April 2026 — this is precise and testable.
5. Do not quote the $7.5M revenue figure. If a revenue figure is used at all, use the live-data-at-publication approach: "publishing live financial data that, as of April 2026, showed annual recurring revenue above $10M and customers approaching 30,000."

**Secondary placement.** Ch11 closing gesture, as the existing `ghost-model-and-harris-reversal.md` already proposes:
> *"Ghost was the model. The ghost model is not a gimmick. Someone had been running it for a decade. The ghost model is what she was trying to do, in her smaller way, at her desk."*
This is good. The corrections above (co-founder, jurisdiction, figures) do not affect Ch11's closing line because it does not name specifics.

**What the book does *not* need to do.**
- Adjudicate whether Substack behaved well or badly in copying Ghost code. That is Freedom Paradox's territory (and Ch02 already narrates it).
- Re-argue the "code as commodity" claim. That is also Freedom Paradox Ch02.
- Assert that Ghost will definitely succeed over the long run. The draft's honest line — "She did not yet know whether the model would work for her" — is the epistemic posture the book should keep.

## Section 7 — Follow-ups and open flags

- `[VERIFY]` Ghost Foundation's Singapore jurisdiction — string confirmed on Wikipedia, confirmed implicitly on the About page, but not in the specific sentence I fetched. A 30-second grep of https://ghost.org/about/ at copyedit time will settle it.
- `[VERIFY]` ActivityPub integration status: is it still in alpha as of actual copyedit date, or has it advanced to beta/GA? Check the Ghost changelog for any post after April 2026.
- `[VERIFY]` Ghost's live financial data at the moment of copyedit. The numbers above are a snapshot from 2026-04-19.
- `[RESEARCH NEEDED]` Primary-source citation for the Substack-copied-Ghost-source-code claim. Freedom Paradox Ch02 asserts this; Grammars research-07 asserts this; it may be accurate, but the book should not commit the claim to print without a citable O'Nolan statement or third-party report. Search `john.onolan.org` and Ghost's changelog for the specific post; check *The Verge*, *Platformer*, *TechCrunch* for reporting.
- `[RESEARCH NEEDED]` Board-expansion status: did Ghost actually expand the board of trustees or introduce membership tiers in 2025 per the Oct 2024 governance post? If yes, the book can say so; if not yet, the book can keep the governance commitment as a stated plan rather than an executed change.
- `[VERIFY]` The "Hannah Wolfe" spelling and current role at Ghost. The About page names her as co-founder; her current title should be confirmed before the book names her.

## Working footnote (draft)

> Ghost Foundation, "About" (https://ghost.org/about/, accessed 19 April 2026); John O'Nolan and Hannah Wolfe founded Ghost in April 2013, funding the initial build by a Kickstarter campaign (29 April 2013) that raised £196,362 against a £25,000 goal. Ghost is distributed under the MIT License; revenue comes from Ghost(Pro), a paid managed-hosting service built on the same open-source core. As of April 2026 the Foundation publishes live financial data showing annual recurring revenue above ten million U.S. dollars and approaching thirty thousand active customers. Ghost's ActivityPub federation work, announced 22 April 2024 (https://ghost.org/changelog/activitypub-alpha/) and first production-federated on 8 July 2024, remains in early access at the time of writing. On the non-profit structure and the governance reforms the Foundation has announced, see John O'Nolan, "Democratising publishing," 30 October 2024 (https://john.onolan.org/democratising-publishing/); on O'Nolan's position that AI is collapsing the premises of open-source licensing, see "Open Source in the age of AI," 26 February 2026 (https://john.onolan.org/open-source-in-the-age-of-ai/), discussed at length in *The Freedom Paradox*, Chapter 2. `[VERIFY: final revenue/customer numbers, ActivityPub status, and Substack-source-code citation at copyedit.]`
