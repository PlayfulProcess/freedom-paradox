# The Freedom Paradox — Project Plan & Gap Assessment

**Last updated:** 2026-03-27

## Current State

- **16 chapters + epilogue drafted** (~63,400 words total)
- **All chapters have synthesis files** in `research/synthesis/`
- **Raw research exists for all chapters** (17 raw files)
- **Research prompts exist only for Ch 1 and Ch 2** — a gap for the rest
- **14 author (PP) comments remain unaddressed** across 6 chapters

---

## Chapter-by-Chapter Assessment

### Word Counts & Research Flag Density

| Chapter | Words | [VERIFY]/[QUOTE]/[RESEARCH] Flags | PP Comments | Status |
|---------|-------|-----------------------------------|-------------|--------|
| Ch 1: The Anthropic Clause | 2,913 | 3 | 0 | **Strongest. Ready for revision.** |
| Ch 2: When Code Could Clone Itself | 2,977 | 8 | 0 | Solid draft. Needs fact-checking pass. |
| Ch 3: Free as in Freedom | 3,336 | 5 | 0 | **Weakest opening. Needs vivid case, not abstraction.** |
| Ch 4: Open as in Business | 2,958 | 6 | 0 | Quick win — adapt existing draft. |
| Ch 5: The Recursive Public | 3,868 | 5 | 0 | Good shape. Needs Kelty quotes verified. |
| Ch 6: The License Wars | 4,766 | 10 | 0 | **Heavy on flags.** HashiCorp, Elastic, Redis timelines need verification. |
| Ch 7: Open Core, Closed Profit | 4,014 | 13 | 0 | **Most flags in the book.** PEXT finding needs sourcing. Revenue figures need verification. |
| Ch 8: The Platform Play | 3,866 | 13 | 0 | **Tied for most flags.** Chromium, Android, EU fine details need checking. |
| Ch 9: Meta's Confession | 3,179 | 3 | 4 | Good draft. PP wants LlamaCon flavor, "open weights = compiled binary" emphasis. |
| Ch 10: The Safety Argument | 4,764 | 8 | 4 | Strong but PP wants concrete soul-doc examples and RSP v3.0 retreat felt, not just described. |
| Ch 11: Open Behind the Frontier | 3,196 | 5 | 1 | PP wants "strategic dumping" section expanded. |
| Ch 12: The Dwarkesh Problem | 3,810 | 1 | 2 | PP wants concrete surveillance assembly scenario and "theater vs. rehearsal" nuance on safety research. |
| Ch 13: Value Creation for Whom? | 3,464 | 3 | 0 | Clean. The equity-analyst chapter. |
| Ch 14: The Commons That Can Kill | 4,022 | 2 | 0 | Solid Ostrom application. |
| Ch 15: Gateway Building | 4,221 | 1 | 0 | Ghost/Wikipedia/Chosen models. Clean. |
| Ch 16: The Freedom Paradox | 5,563 | 1 | 2 | PP wants it to read as "pro-honesty, not anti-open-source." Philosophical core. |
| Epilogue | 2,470 | 3 | 1 | PP questioning whether the closing line lands. |

---

## Critical Weaknesses (Priority Order)

### 1. Ch 3 needs a new opening
The chapter opens with "The previous chapter ended with a programmer at MIT who was very angry about a printer." This is transitional throat-clearing. The Stallman printer story doesn't arrive until paragraph 8. **Fix:** Open with the printer scene itself — Stallman walking to the Xerox machine, the jam, the refusal. Make the reader feel the violation. Then zoom out to the SHARE culture and the economics that changed. The abstract history of sharing (1955-1970s) should come second, not first.

### 2. Ch 7 and Ch 8 have the most unverified claims
Combined 26 research flags. The PEXT finding (cited in both Ch 6 and Ch 7) has no confirmed source — this needs to be either verified or removed. Revenue figures for Supabase, Vercel, and Ghost need primary-source confirmation. The EU fine amounts, Huawei sales decline, and ATT revenue impact in Ch 8 all need sourcing.

### 3. Unaddressed PP comments (14 total)
These represent the author's voice and judgment. They should be the first thing addressed in any revision pass:
- **Ch 9 (4 comments):** LlamaCon atmosphere, "open weights = compiled binary" emphasis, CNBC headline, bridge to Part IV
- **Ch 10 (4 comments):** Soul doc example, RSP v3.0 retreat significance, "constitutional convention of one" expansion, bridge to Ch 11
- **Ch 12 (2 comments):** Concrete surveillance scenario, "theater vs. rehearsal" nuance
- **Ch 16 (2 comments):** Pro-honesty framing, full chapter assessment
- **Ch 11 (1 comment):** Strategic dumping expansion
- **Epilogue (1 comment):** Whether the closing line works

### 4. Ch 4 is the shortest substantive chapter (2,958 words)
The OSI founding and the ethics-to-pragmatism shift is a pivotal moment in the book's argument. It currently feels thin compared to the chapters around it. The Raymond/Perens/Halloween Documents material deserves more depth.

---

## Research Gaps

### Missing Research Prompts (Ch 3-16)
Only Ch 1 and Ch 2 have prompts in `prompts/`. If you're doing more deep-research sessions in Claude, you'll need prompts for:
- **Ch 3:** Stallman primary sources (his own accounts, Levy's *Hackers*, Williams's *Free as in Freedom*)
- **Ch 4:** Raymond's *Cathedral and the Bazaar*, the Netscape announcement, OSI founding docs, Halloween Documents
- **Ch 6:** HashiCorp BSL timeline, Elastic/Redis license switches, exact dates
- **Ch 7:** Supabase/Vercel/Ghost financials from primary sources (press releases, SEC if available, founder interviews)
- **Ch 8:** Google antitrust case documents, EU Commission decisions, Huawei post-sanctions data

### Specific Unresolved Research Items
1. **The PEXT finding** — cited in Ch 6 and Ch 7 as a "research consortium studying 44 open-source developer tools." No full citation exists. This is either a real study that needs proper sourcing or a synthesis artifact that needs to be rewritten as the book's own analysis.
2. **Stallman's account of the printer incident** — [QUOTE NEEDED] in Ch 3. This is foundational. Sam Williams's *Free as in Freedom* (2002) has the definitive version. Steven Levy's *Hackers* (1984) has context.
3. **Copplestone quotes** — Two [QUOTE NEEDED] flags in Ch 7. Check Accel podcast, Y Combinator interviews, or Supabase blog.
4. **Guillermo Rauch "speedrun to product-market fit"** — [QUOTE NEEDED] in Ch 7. Likely from First Round Review or a podcast.
5. **Shay Banon (Elastic) blog post** — [QUOTE NEEDED] in Ch 6 on the license switch rationale.
6. **Dadgar (HashiCorp) announcement language** — [QUOTE NEEDED] in Ch 6.
7. **v0 launch and growth metrics** — [RESEARCH NEEDED] in Ch 7.
8. **Manifest V3 current status** — [RESEARCH NEEDED] in Ch 8.
9. **Google-Mozilla search deal value & DOJ remedies** — [RESEARCH NEEDED] in Ch 8.
10. **Huawei sales decline figures** — [RESEARCH NEEDED] in Ch 8.
11. **EU unbundled license uptake** — [RESEARCH NEEDED] in Ch 8.

### Missing Philosophical Sources
The book references Tillich, Yalom, Kelty, and Ostrom in the author bio but:
- **Tillich** appears nowhere in the current drafts. If the "courage to be" / "ground of being" framework matters to the argument, it should surface in Ch 14 or Ch 16.
- **Yalom** (existential psychotherapy, death anxiety, freedom anxiety) is absent. Could strengthen Ch 16's freedom paradox argument — the anxiety of unlimited freedom is a core Yalom theme.
- **Ostrom** is well-integrated in Ch 14 and referenced in Ch 6. Good.
- **Kelty** is well-integrated in Ch 5 and referenced throughout. Good.

---

## Recommended Writing Order

### Phase 1: Quick Wins (address PP comments + low-flag chapters)
1. **Ch 9 revision** — Address 4 PP comments. Draft is solid, just needs texture.
2. **Ch 12 revision** — Address 2 PP comments. Add the concrete scenario.
3. **Ch 16 revision** — Address 2 PP comments. This is the book's climax; get the framing right.
4. **Epilogue revision** — Address closing-line question.

### Phase 2: Research-Heavy Revisions
5. **Ch 3 rewrite opening** — New vivid opening with the printer scene. Needs Stallman primary sources.
6. **Ch 7 fact-checking pass** — Resolve 13 flags. Needs revenue data, PEXT sourcing.
7. **Ch 8 fact-checking pass** — Resolve 13 flags. Needs antitrust case details.
8. **Ch 6 fact-checking pass** — Resolve 10 flags. Needs license-switch timelines.

### Phase 3: Deepening
9. **Ch 4 expansion** — Flesh out the ethics-to-pragmatism pivot. Currently thin.
10. **Ch 10 revision** — Address PP comments on RSP v3.0 and soul doc.
11. **Ch 11 expansion** — Strategic dumping section.
12. **Integrate Tillich/Yalom** into Ch 16 if the author wants the philosophical framework to land.

### Phase 4: Polish
13. Cross-reference pass (ensure forward/backward references are consistent)
14. Final fact-check of all remaining [VERIFY] flags
15. Word-count balancing (Ch 1 at 2,913 vs Ch 16 at 5,563 — is this intentional?)

---

## Structural Notes

- **Part I (Ch 1-2):** Strong. The Anthropic Clause is the best chapter in the book. The O'Nolan chapter is a compelling follow-up.
- **Part II (Ch 3-6):** History section. Ch 3 opening is weak. Ch 4 is thin. Ch 5 is strong (Kelty). Ch 6 is the longest history chapter and the most flag-heavy — consider whether it's trying to do too much.
- **Part III (Ch 7-9):** Business section. Strong conceptually but the most unverified. Ch 9's PP comments suggest the author sees "open weights = compiled binary" as a marquee insight — make sure it's prominent.
- **Part IV (Ch 10-13):** AI reckoning. Ch 10 and Ch 12 have the strongest PP engagement. The author clearly cares most about this section.
- **Part V (Ch 14-16 + Epilogue):** Philosophy section. Ch 14 (Ostrom) and Ch 15 (positive models) are clean. Ch 16 is the longest chapter and carries the book's thesis. The Tillich/Yalom gap is notable here.

---

## Interview Candidates — Status

All 13 candidates in `notes/interviews-wanted.md` are listed but none are marked as contacted or confirmed. Priority:
1. **O'Nolan** — His newsletter is already a primary text. Most accessible.
2. **Copplestone** — Would resolve multiple [QUOTE NEEDED] flags in Ch 7.
3. **Kelty** — Would add authority to Ch 5's "recursive public" argument.
