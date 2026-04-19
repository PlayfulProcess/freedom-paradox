# Changelog — Axiom Beneath the Ground

## 2026-04-19 — research-31 landed (Ghost / O'Nolan, Thread 5)

**Research added.** `research/research-31-onolan-ghost-platform.md` — citation-grade note on Ghost, the Ghost Foundation, and John O'Nolan as the working model for recursive.eco and the publishing-layer sibling to Ch10's Nvidia example. Primary sources: Ghost Foundation About and ActivityPub pages (ghost.org, accessed 2026-04-19); O'Nolan's "Democratising publishing" (30 Oct 2024) and "Open Source in the age of AI" (26 Feb 2026) on john.onolan.org; Wikipedia History/Foundation sections for Kickstarter and jurisdiction anchors; TechCrunch (8 July 2024) for the first-federated-newsletter date.

**Findings that change the book's argument — none structural.** The Ch10 sibling passage drafted in `outreach/ghost-model-and-harris-reversal.md` holds up. The principle is right: Ghost is "do as little as possible, as much as necessary" approached from the publishing layer, the mirror of Nvidia at the chip layer. Research-26 (Nvidia) and research-31 (Ghost) now sit together as the two halves of Ch10 §VI.

**Corrections the research-31 pass surfaced, to apply before Ch10 prose lands:**
- Ghost was co-founded by **John O'Nolan and Hannah Wolfe** in April 2013, not O'Nolan alone. Multiple internal files (Freedom Paradox Ch02, Grammars research-07, the `ghost-model-and-harris-reversal.md` Ch10 sketch) frame the founding as single-author. Either add Wolfe or rephrase so she is not silently erased.
- The Ch10 sketch's "a man in Singapore named John O'Nolan" conflates the Foundation's Singapore jurisdiction with O'Nolan's location (he describes himself as "Geographically restless"). Either describe the Foundation's registration or describe O'Nolan without pinning him to a city.
- Do not quote the $7.5M ARR figure without a date. That number traces to October 2024; Ghost's live-data page as of this research pass (2026-04-19) shows approximately $10.3M ARR and 29,476 active customers. The book should either use the live-data approach ("as of April 2026, revenue above $10M, customers approaching 30,000") or avoid a specific number and let the qualitative point carry.
- ActivityPub specifics: announced 22 April 2024, first newsletter federated 8 July 2024, still in early access / alpha as of 2026-04-19. Precise, testable, and ready for a footnote.

**Open flags.**
- `[RESEARCH NEEDED]` primary citation for the Substack-copied-Ghost-source-code claim. Freedom Paradox Ch02 and Grammars research-07 treat it as established; Axiom Ch10 should not assert it without a citable O'Nolan statement or third-party report.
- `[VERIFY]` whether the governance reforms O'Nolan announced in October 2024 (board expansion beyond founders, formal membership tiers, community-elected seats) have shipped as of this date, or remain stated intent.
- `[VERIFY]` Ghost's ActivityPub status has likely advanced beyond alpha by now; check the changelog.

**Next thread to run (per author's ordering).** Thread 4 — Dario Amodei's public thought 2024–2026. Target file: `research-30-amodei-2024-2026-thought.md`. Hooks: *Machines of Loving Grace* (October 2024); Dwarkesh Patel interview; the June 2025 Huang/Amodei disagreement; the 18 November 2025 Anthropic/Nvidia $10B commit. Research-26 already partially stages this.

---

## 2026-04-18 — v4 restructure begins

**Context.** Author feedback during planning: the originating question for the book is *freedom*, not *value*. Value is the moral question (to whom do I direct what I have?); freedom is the spiritual question (what is the I that directs at all?). The pull that led to the retreat was pre-conceptual desire, not a reasoned "why." v3's opening — "why is the only honest place to start" — is a category error against the book's own epistemology.

**Structural frame.** The book is now organized around the Tantric map of nested layers: Vastu (stuff), Deha (body), Citta (heart-mind), Prāṇa (life-force), Shunya (void), Cit (core Consciousness). Tillich's *courage* maps to Shunya; Wallis's *svātantrya* (freedom) maps to Cit. The book moves inward through the layers to the retreat and outward again into the world.

**Changes this pass.**
- Archived all v3 chapters to `drafts/archive/2026-04-18-v3/`
- Created `chapters/v4/` for the new draft
- Drafted `chapters/v4/ch00-authors-note.md` — new opening (playground scene, desire before reason; preserved teacher quotes and filter framing from v3)
- Added `outline/v4-restructure-plan-2026-04-18.md` — full v4 plan
- Added `research/v4-deep-research-prompt.md` — prompt to run in a local Claude Code session for the 6-item research pass
- Added `CHANGELOG.md` (this file)
- Updated root `CLAUDE.md` with copyright-compliance rule

**Next.**
1. Author reads v4 ch00
2. Run research pass
3. Draft Ch1 (Playground)

**Notes.**
- v3 remains at `chapters/v3/` as a working copy until v4 is stable. After v4 stabilizes, v3 can be removed (archive copy at `drafts/archive/2026-04-18-v3/` is the durable preservation).
- No build/deploy changes this pass. `src/SUMMARY.md` and `build.sh` still point at v3 paths; the public site is unchanged.

---

## 2026-04-18 (later) — research-21 landed, plan refined

**Research added.** `research/research-21-ti-cit-transcendent-immanent.md` — citation-grade note on Wallis's layered-self teaching in *Tantra Illuminated* (2nd ed., 2013), anchored at pp. 92–103, esp. 92 (five-layered self introduced) and 101 (Five Powers of Awareness). Cross-referenced to Wallis's October 23, 2015 blog post for the "transcendent and immanent" formulation of Cit.

**Structural corrections to the plan.**
- Wallis's canonical model is the **five-layered self** (Deha, Citta, Prāṇa, Śūnya, Cit), not six. **Vastu** is an optional outer layer Wallis sometimes adds as pedagogical extension. Plan updated to describe this accurately and to relabel the Tillich/Wallis pivot: courage = Śūnya (layer 4); svātantrya = Cit (layer 5).
- Chapter structure preserved: Ch1 uses Vastu as narrative frame, Ch2–Ch6 walk the strict five layers Deha → Cit.
- Pratyabhijñā (Recognition) school attribution added, with Kṣemarāja's *Pratyabhijñā-hṛdaya* sūtra 8 as primary classical anchor.

**AI-tension correction.** Ch10 now holds the AI-offer scene as an unresolved tension rather than a closed decline. Seeds of openness at the retreat (walking-back scene, teacher "a bit open"); later decline in writing; book refuses to settle the question. The AI/scale/presence thread becomes the book's second spine, meeting the interior freedom/value spine in Ch10.

**Cutting/piercing correction (v2).** The exchange is **pre-retreat**, not post-retreat. It belongs at the end of Ch1 (Vastu) as the closing beat — the narrator's first direct dialogue with the teacher through the mediated channel, filter applied before she sets foot in the barn. Teacher corrects "cutting" to "piercing" and concedes the daily-practice framing. Whether the app has been updated is unknown and irrelevant.

**Ch6 as one sustained scene.** The walking-out encounter on the final day is one scene — hug, question, full dialogue (reincarnation → pattern → destruction/suicide → "there always is" a hole) — not two chronologically separated beats. The Cit chapter is a single threshold scene, structurally echoing the Author's Note's insight that the deepest teachings arrive in the thinnest moments.

**Closing-circle moves to Ch5.** The retreatant with one foot in and one foot out testified to their own return because of the goddess work *and* vouched to newcomers that the community has integrity. Both halves belong in the scene, at the closing circle on the last night before the narrator walks out the next morning.

**Walking-back-scene addition to Ch4.** The teacher's humble "what is wrong with these people?" admission, and the first seed of the AI suggestion, belong mid-retreat in a group-walking conversation (post-lunch, during Prāṇa / Kali chapter).

**Ch7 rewrite.** With cutting/piercing moved to Ch1, Ch7 becomes the post-retreat life-force beat: continuing practice in daily rhythm. May merge with Ch9 (Deha returning) if the two overlap — decision deferred until drafting.

**Remaining research prompts (2–6).** Still open. Prompts live in `research/v4-deep-research-prompts-claude-ai.md` for sequential execution.

---

## 2026-04-18 (later still) — research-22 landed

**Research added.** `research/research-22-ti-svatantrya-freedom.md` — citation-grade note on svātantrya in *Tantra Illuminated*, pp. 101–109 ("The Five Powers of God"), with the "innate freedom and total autonomy" framing at approximately p. 105. Freedom-of-the-whole vs. freedom-of-the-part distinction is textually confirmed: Wallis attributes svātantrya to Awareness, not to mind or body. Classical anchors: Abhinavagupta's *Tantrāloka* 1.67–69 (only one fundamental quality); Kṣemarāja's *Pratyabhijñā-hṛdayam* sūtra 1 (*citiḥ svatantrā viśva-siddhi-hetuḥ*).

**Structural note for the book.** Wallis has a published engagement with Sam Harris's *Free Will* (hareesh.org, 8 July 2015, two parts). The narrator's "not choosing between Sam Harris and the Catholic frame" is grounded in a real dialogue her teacher has joined. Ch1 (reading year) can plausibly include this blog essay as a text she encountered; Ch3 can footnote the counter-position.

**Candidate line for Ch6 prose (synthetic, not quoted):** *Courage is svātantrya owning itself in the dark; svātantrya is courage in the light.* Preserved in research-22 Section 7 as drafting material.

**Spanda thread.** Spanda is svātantrya in vibratory aspect (Kṣemarāja's *Spanda-nirṇaya* lists them as synonyms). Usable in the Ch4 Kali interlude without naming the term — the pulse that makes any action, including destruction, part of the one self-determining field.

---

## 2026-04-18 (later still still) — research-23 + first chapter drafts

**Research added.** `research/research-23-tillich-courage-absolute-faith.md` — citation-grade dossier on Tillich. *Courage to Be* (Yale 1952/2000), three anxieties (pp. 32–63), courage as ontological act (p. 152), absolute faith and the God above God (pp. 171–190, "accepting of acceptance" at p. 185). *Dynamics of Faith* (1957) on faith as ultimate concern. *Protestant Era* (1948) on the Protestant Principle. Pauck & Pauck biography on Verdun. Notes for the book's Śūnya → Cit pivot in Section 7.

**Chapters drafted.**
- `chapters/v4/ch01-playground.md` — opener. Playground scene (Tantra 112 app, Cit passage, the *yes* before reason). The reading year compressed. The tia and the espírita inheritance. The decision. Closes with the pre-retreat cutting/piercing WhatsApp exchange — narrator's filter applied to her teacher for the first time, his correction (cutting → piercing), his concession on the daily-practice framing.
- `chapters/v4/ch06-walking-out.md` — structural heart. The final-day walking-out scene. Hug, joke, question. The dialogue: nothing would change → reincarnation → pattern → destruction/suicide → "there always is" a hole. Held dialectically per the destruction-thread ground rules.

**Open for next pass.**
- Research-24 (Kybalion), 25 (Linehan), 26 (Nvidia)
- Chapters 2, 3, 4, 5 (inward arc filling out)
- Chapters 7, 8, 9, 10, 11 (outward arc and coda)
- Italicized interludes (Kali, Cit, Śūnya, Temple)
- SVG diagram

---

## 2026-04-19 — research pass complete (24, 24b, 25, 26)

**Research added.**
- `research/research-24-kybalion-truth-in-between.md` — broad dossier. *The Kybalion* (1908, Yogi Publication Society, Chicago) is a New Thought book authored by William Walker Atkinson, not ancient Hermetica — established via Deslippe (2011), Chapel (2013), Hanegraaff, Ebeling. "The truth lies in between" is a later paraphrase, not verbatim. Principle of Polarity quoted accurately from Ch. II/X. Dialectical family compared: Hegel's *Aufhebung*, Aristotle's agent-relative mean, Nāgārjuna's tetralemma, Heraclitus's *palintropos harmoniē*, Daoist yin-yang, Jung's *coincidentia oppositorum*, Linehan's DBT dialectic.
- `research/research-24b-kybalion-ch12-free-will-gradient.md` — focused refinement on Ch. XII ("Causation"). "Not total free will, not none" is a convergent position across six traditions: Kybalion Ch. XII, William James, Chrysippus (cylinder analogy in *De Fato* 43), Aristotle (*NE* III.1–5), Buddhist middle way (SN 12.17, SN 12.15, Nāgārjuna), Fischer & Ravizza / Wolf / List gradualist compatibilism, and Linehan's clinical dialectic ("may not have caused all their problems, have to solve them anyway"). Binary positions are dialectical losers; degreed freedom is the mainstream.
- `research/research-25-linehan-adaptive-not-moral.md` — **critical attribution correction.** The "useful / fits the data / compassionate" triad popularly attributed to Linehan as a clinical thought-evaluation filter is actually her **meta-theoretical criterion for selecting her biosocial theory of BPD**: "(1) guide treatment implementation, (2) engender compassion, and (3) fit the research data" (2015 *DBT Skills Training Manual*; Linehan & Wilks 2015). The book's use of the triad as a framework-selection filter is structurally correct — she applied it at the theory-selection level and so does the book — but attribution needs to be explicit, not framed as a clinical technique.
- `research/research-26-nvidia-ecosystem-restraint.md` — "do as little as possible, as much as necessary" **confirmed** as a Huang quote (four utterances, Dwarkesh Patel podcast, April 15, 2026). Lineage: Montessori, German *Verhältnismäßigkeit*, Catholic subsidiarity, ALARA. Open-source evidence (Cosmos, Nemotron, Dynamo) held against counter-evidence (antitrust scrutiny, CUDA EULA, China exposure, CoreWeave equity-allocation). Anthropic's Nov 2025 $10B commit despite June 2025 Huang/Amodei disagreement as evidence that disagreement and cooperation coexist in mature ecosystems. DeepSeek R1 market event (~$589B loss) and Nvidia's gracious response as an applied example of sovereign restraint. Note: source output truncated mid-section; follow-up pass needed on the "Relationship" material and primary-source verifications.

**Edits to chapters.**
- `chapters/v4/ch00-authors-note.md` — "A note on method" paragraph tightened to make the Linehan attribution explicit: the three filters are named as her criteria for selecting her biosocial theory of BPD, adopted here at the same theory-selection level as a framework-selection filter. Removes the prior framing that could read as a clinical thought-evaluation technique.
- `chapters/v4/ch01-playground.md` §III — Linehan paragraph rewritten to match the corrected attribution: the three criteria are Linehan's theory-selection criteria (guide treatment, engender compassion, fit the research data), not "the method" of DBT. Subsequent paragraph adjusted so the narrator's recognition is of a filter-for-choosing-theories adopted at the same level, not a clinical technique.
- `chapters/v4/ch01-playground.md` §III — Kybalion paragraph extended by one sentence to seed research-24b's finding: Ch. XII's polarity-applied-to-freedom is the specific shape the book's later argument rests on ("neither total, neither absent, a graded field a person lives inside and not a binary a person picks"). Prepares the free-will through-line without front-loading the philosophy.

**Open for next pass.**
- Chapters 2, 3, 4, 5 (inward arc filling out)
- Chapters 7, 8, 9, 10, 11 (outward arc and coda)
- Italicized interludes (Kali, Cit, Śūnya, Temple)
- SVG diagram
- Research-26 follow-up: complete the truncated "Relationship" section, antitrust jurisdiction list, Hugging Face contribution counts, Dwarkesh transcript timestamps
- Ch3 (Citta / filter chapter): present Linehan's three criteria in her actual language before paraphrasing; drop any implication that this is a clinical thought-evaluation technique

---

## 2026-04-19 (later) — inward arc Ch2–Ch5 drafted

**Chapters drafted.**
- `chapters/v4/ch02-deha.md` — Body. Arrival at the barn; first night (Catholic-alarm non-firing); first formal teaching in the converted hayloft; the "It is, until you experience it" exchange on morning two; two days of body-catching-up; the lentil-soup moment on the second evening as the clean small truth the body noticed first.
- `chapters/v4/ch03-citta.md` — Heart-Mind. Third-day walk around the property alone. Tillich's three anxieties, with meaninglessness named as the one she carries. Linehan's three criteria applied to Tillich and to the tradition; both pass. Freedom (spiritual, absolute, field-property) vs. value (moral, relative, distribution-property). The Harris/Wallis engagement — narrator recalls reading her teacher's 2015 two-part response to *Free Will* during the reading year, which dissolves the binary rather than refutes the neuroscience. Adaptive/non-adaptive as the bridge; "all is balance" as the aunt's near-enemy; prisoner's dilemma as the stable-but-non-adaptive equilibrium. The Wild Wild Country reference now placed as the community's failure-mode reminder.
- `chapters/v4/ch04-prana.md` — Life-Force / Kali. The fourth afternoon's Kali practice. The intrusive "what would change?" question interrupting the programmer at lunch — she apologizes; he says "your question is real too." The walking-back scene: teacher's humble "I sometimes wonder what is wrong with these people" on a post-lunch walk; narrator floats the assistant idea carefully ("an assistant" not "an AI"; "carry some of the load" not "replace"); teacher: "I'd be a bit open to thinking about that." She does not ask her destruction question that day; she carries it. Closes with an italicized Kali interlude (1-page archetypal voice, per the plan).
- `chapters/v4/ch05-shunya.md` — Void. Last full day; carrying the unasked question. Tillich read on the porch between first sit and breakfast — the sentence that had been a formulation in the bathtub has become a description on the porch. Absolute faith as "accepting of acceptance" working on her from inside. Closing circle: the silver-haired retreatant with one foot in and one foot out testifies to his own return via the goddess work and vouches for the community's integrity to the newcomers. Night before final morning; the path waiting. Closes with an italicized Śūnya interlude.

**Architectural notes for these drafts.**
- All three research corrections applied in-prose: Linehan's three criteria as theory-selection (Ch3, Ch1-style attribution); Harris response treated as dissolving-the-binary rather than refuting neuroscience (Ch3); Kybalion Ch. XII free-will-graded-field seeded in Ch1 §III earlier this pass and referenced implicitly in Ch3.
- Teacher interactions now captured in the drafted chapters: "It is, until you experience it" (Ch2 §III); the humble "what is wrong with these people" and the first assistant/AI seed on the walking-back (Ch4 §III); the closing-circle testimony set in his presence (Ch5 §IV).
- POV holds close-third throughout. First-person only in the Author's Note. Italicized interludes (Kali, Śūnya) introduced in the archetypal register — no proper names, no plot, addressed to "you."
- The destruction question is carried unasked from Ch4 §II through Ch5 §III into the already-drafted Ch6 walking-out scene. The chronological chain is now continuous: Kali practice → intrusive lunch question → walking-back → last full day carrying → closing circle → night → walking out → hug → nothing would change → there always is.

**Open for next pass.**
- Outward arc: Ch7 (Prāṇa returning), Ch8 (Citta returning), Ch9 (Deha returning), Ch10 (Vastu returning / AI tension), Ch11 (Writing Desk coda)
- Cit interlude: the plan calls for one after Ch6. Decision deferred — Ch6's emotional landing may not want an italicized overlay.
- Temple interlude: location not yet decided — possibly Ch10 companion.
- SVG diagram at `src/images/diagram-tantrik-layers.svg`
- Research-26 follow-up pass (still open)
- Author pass on Ch2–Ch5: register, pacing, whether the Harris/Wallis paragraph in Ch3 §IV is the right placement or whether it belongs earlier in Ch1's reading year instead

---

## 2026-04-19 (later still) — outward arc Ch7–Ch11 drafted

**Chapters drafted.**
- `chapters/v4/ch07-prana-returning.md` — Prāṇa, returning. The Acela after a work meeting; practice in earbuds as daily technology, not retreat. A mantra whispered in the ten minutes between the child's sleep and the husband's arrival in bed. A small technical question posted to the group chat; the teacher's three-sentence answer; the sensation migrating toward expansion rather than constriction; no reply needed because the migration was the answer. Closes: *she was, most days, riding it.*
- `chapters/v4/ch08-citta-returning.md` — Citta, returning. Two mandalas drawn on the backs of envelopes — blessings (outward flow that replenishes) and curses (inward hoarding that starves the field). The aunt reconsidered: the narrator asks her aunt on the phone what *all is balance* has meant in her practice; the aunt's answer is the whole-holds-the-hole posture the teacher had given on the path, in a Brazilian espírita register. Prisoner's dilemma as the mandala-of-curses in mathematical form. The filter at the desk, in equity-analyst vocabulary.
- `chapters/v4/ch09-deha-returning.md` — Deha, returning. First Monday after the retreat as the real test. Ten minutes on the cushion before the child wakes; the jaw-clench noticed-and-returning as material rather than enemy. The dishes different (warmer water, thicker mug base, lavender soap). The child's bath question — *Mama, is there a place where I am still even when I'm moving?* — answered simply (*yes*) with no explanation needed. The husband at breakfast: *you're in the room more*; offers to keep watch. The body as the most honest layer; reports, does not argue.
- `chapters/v4/ch10-vastu-returning.md` — Vastu, returning / the second spine / AI tension. The book's second spine named: her builder work with scalable systems, meeting the first spine at the AI question. The tool she built: a retrieval interface over her teacher's public lectures, with a tarot-deck grammar for entry points, labeled a study tool, not a teacher. The decline: his careful message — *the form is not accidental to the teaching; the form is how the teaching transmits.* What was right in the decline (form is not neutral; absence of teacher changes what transmits). What was right in the building (scale is not neutral either; the refusal to build is also a choice with costs). She makes the tool quieter, smaller, less synthetic, and lets it exist. Nvidia's "do as little as possible, as much as necessary" held carefully — principle worth testing, operating record where the test plays out. Closes on the genuine unresolved: *she did not know whether he would ever say yes. She knew she would keep asking, and that the asking itself was the filter.*
- `chapters/v4/ch11-writing-desk.md` — Writing desk coda. Short first-person chapter; the only first-person material in the book apart from the Author's Note. It is late in the working-day sense, not the metaphysical sense. The question was never one that had an answer at the layer at which she was asking it. She has rendered her teacher faithfully without rendering him fully. The AI tool continues as a private building; the book is another kind of building. *Svātantrya is a field I am moving through.* A reference to a study kept in a drawer for years out of fear of being foolish — the drawer is a version of the mandala of curses; publishing is a version of the mandala of blessings. The book ends. The practice does not.

**Structural summary.**
The v4 draft is now complete at the chapter level: Ch0 (Author's Note) + Ch1 (Playground) + Ch2 (Deha) + Ch3 (Citta) + Ch4 (Prāṇa + Kali interlude) + Ch5 (Śūnya + Śūnya interlude) + Ch6 (Walking Out) + Ch7 (Prāṇa returning) + Ch8 (Citta returning) + Ch9 (Deha returning) + Ch10 (Vastu returning / AI tension) + Ch11 (Writing Desk). The inward arc (Ch1–Ch6) walks the five-layered self from Vastu frame through Deha / Citta / Prāṇa / Śūnya into Cit. The outward arc (Ch7–Ch10) walks the same five layers in reverse as application. Ch11 closes in first person.

**Open for next pass.**
- Author read of the full v4 draft (Ch2–Ch11 are first drafts, unreviewed; Ch0, Ch1, Ch6 have been touched in previous passes)
- Cit interlude after Ch6 (decision deferred; may not want the overlay)
- Temple interlude placement (possibly within or after Ch10)
- SVG diagram at `src/images/diagram-tantrik-layers.svg`
- Research-26 follow-up (Prompt 6b prepared in `research/v4-deep-research-prompts-claude-ai.md`)
- Build/deploy: update `src/SUMMARY.md` and `build.sh` to point at v4 paths (still v3); rebuild EPUB; rebuild mdbook

---

## 2026-04-19 (later still still) — outreach draft: Tristan Harris blessing

**Added.** `outreach/tristan-harris-blessing-email.md` — draft email to Tristan Harris requesting his blessing to screen one of his documentaries at a free library class PlayfulProcess is teaching on "vibe coding." Frame: Bhagavad Gita / Arjuna-Krishna — *is this battle ours to fight?* — with PlayfulProcess positioning honestly on the build-with-awareness side ("on Dario's team") while respecting Harris's warnings as the clearest contemporary version of Arjuna's question. Echoes Axiom Ch10's structure: ask the living person, respect the refusal, keep building smaller if declined.

Document also contains practical follow-up (which film, public performance rights, library logistics, class framing, fallback materials if declined) and open items (confirm name spelling — Tristan, not Travis; whether to name Anthropic directly; length calibration).

**Structural note for the next pass (Kundera).** PlayfulProcess has named the intended structure of the book: Kundera-style alternation between narrative and non-fictional chapters (*The Unbearable Lightness of Being*, *The Book of Laughter and Forgetting*). The current v4 draft mixes registers within chapters. A separate structural pass is open: either (a) split each chapter into a clean narrative chapter + a clean essay chapter, doubling the chapter count, or (b) keep the five-layer architecture but re-sort so odd-numbered chapters are narrative and even-numbered chapters are essayistic. Decision deferred to the next drafting session.
