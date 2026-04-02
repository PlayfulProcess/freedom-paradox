# Agent Prompt — Chapter Rewriting with New Research

Copy everything below the line and send it to the rewriting agent.

---

You are rewriting chapters of "The Species That Tells Stories" (formerly "The Freedom Paradox") using newly gathered research. Work on branch `claude/edit-species-fire-1C9TN` in the `book-repo` repository.

## Ground Rules

1. **INSERT, don't replace.** Add new material to existing chapters. Do not rewrite existing passages.
2. **Keep insertions tight.** One paragraph (~80-150 words) per integration unless the plan says otherwise.
3. **Commit after each integration.** One commit per chapter touched.
4. **Don't touch**: the 69/31 structure, the Gottman transition (Ch26), the Silverstein poem, or chapter ordering.
5. **Conflict flags (Tier 3)**: Name them, acknowledge them, let them stand. Don't resolve the tensions.
6. **Voice**: Match the existing book's voice — warm, intellectually serious, non-academic, uses concrete images.

## New Research Sources (all in `research/`)

### Transcripts
- `research/francheska-perepletchikova-transcripts.md` — 30 videos: DBT-C, Core Problem Analysis (CPA), supersensers, superparenting, emotional dysregulation, dialectics, self-reinforcement, validation
- `research/eckhart-tolle-transcripts.md` — 48 recent videos: presence, ego dissolution, non-reactivity, acceptance, overthinking, trauma, purpose, awakening

### Tier 4 Research Findings
- `research/tier4-research-findings.md` — All 8 previously-missing research items, fully resolved

## Execution Plan

### BATCH 1 — Tier 1 High-Impact (read `books/consolidated/outline/research-integration-plan-april-2026.md` for full context)

**1.1** Ant death spiral → `ch09-the-safety-argument.md` near RSP revision discussion. One paragraph.
**1.2** Bittersweet thesis (Susan Cain) → `ch17-the-darkness-is-the-medicine.md`. Two passages: (a) minor-key music neuroscience near "graduated dosing," (b) disenfranchised grief near "what was lost when stories were sanitized."
**1.3** Hayes attention-as-labor → `ch08-value-creation-for-whom.md` near platform economics. One paragraph with labor-commodification parallel.
**1.4** Hwang business model path dependence → `ch05-the-recursive-public.md` or `ch08-value-creation-for-whom.md` near how open-source infrastructure gets monetized.
**1.5** MacIntyre moral collapse → `ch24-the-species-that-got-fire.md` near Enlightenment's Gift and Gap. Use the specific page numbers and Kant critique from `tier4-research-findings.md` §1. One paragraph framing MacIntyre, one acknowledging the emotivism challenge to the book's own three-filter test.
**1.6** Liming loneliness data → `ch18-when-stories-lose-their-homes.md` near communal storytelling spaces disappearing.

### BATCH 2 — Tier 2 Medium-Impact

**2.1** Drugification of connection (Lembke) → `ch18-when-stories-lose-their-homes.md` near screen-fragmentation.
**2.2** Haidt "What Is Childhood For?" → `ch16-the-oldest-technology.md` near bedtime stories as containment.
**2.3** Flett "The Need to Matter" → `ch18-when-stories-lose-their-homes.md` near container-collapse consequences. Can now cross-reference Goldstein's mattering instinct.
**2.4** Tatkin couples architecture → `ch36-the-family-as-grammar.md` near the core argument.
**2.5** Van Bavel group identity → `ch19-the-polarization-of-the-polis.md` near polarization mechanism.
**2.8** Camus as alternative → `ch26-the-axiom.md` near Tillich-Wallis dialogue.

### BATCH 3 — Tier 3 Conflict Flags

**3.1** Akomolafe 69/31 challenge → `ch39-the-grammar-we-need.md` near trap-of-solving. One paragraph acknowledging.
**3.3** Harris sufficiency-of-reason → `ch32-what-ai-actually-is.md` (was ch38 in old numbering). Use RSP v3.0 reversal from `tier4-research-findings.md` §4 as evidence. Acknowledge Waking Up app as "grammar by another name."
**3.5** Introvert container design (Cain) → `ch35-listening-playing-making.md` (was ch34). Quaker silence, solo walks, child reading alone.
**3.6** Gottman four horsemen — grep for "four horsemen" and "contempt" across chapters. Qualify if found. If only 69/31 and masters/disasters, no change needed.
**3.8** Goldstein naturalism → `ch26-the-axiom.md`. Use the published book details from `tier4-research-findings.md` §2. Brief note near Tillich-Wallis resolution.

### BATCH 4 — Tier 4 NEW Integrations (from the research just completed)

**4.1** Andreotti *Burnout from Humans* → `ch39-the-grammar-we-need.md`. Acknowledge the AI-as-mirror thesis: "Andreotti would say open source AI simply reproduces modernity's grammar faster if the builders haven't composted the logic of separation." One paragraph. Reference the free PDF.
**4.2** Harris-Amodei / RSP v3.0 reversal → `ch09-the-safety-argument.md`. The strongest real-world evidence: Anthropic dropped its pause commitment under competitive pressure within 2.5 years. One paragraph near the competitive dynamics discussion.
**4.3** Four Mountains / CARE Principles → `ch24-the-species-that-got-fire.md` methodology note. Cite John Crier (Cree elder, Maskwacis Community) and Cash Ahenakew (UBC). Follow CARE citation requirements from `tier4-research-findings.md` §7.
**4.4** Kevin Hall metabolism → Appendix chapters if they exist, or flag for future Appendix A integration. Cite the 3 key papers with DOIs.
**4.5** Deligny fugitive camps → `ch39-the-grammar-we-need.md`. The Cévennes network as a literal example of building outside systems — no credentials, no hierarchy, just a network sharing territory. One paragraph. Cite *The Arachnean and Other Texts* (2015).
**4.6** Okun revisions → Flag for decolonization book context (not the main book). Note the 2021 revision added fear as overarching driver and Okun's own acknowledgment of misuse.

### BATCH 5 — Transcript Integrations (Perepletchikova + Tolle)

Scan the transcripts for material that strengthens existing chapters. Likely targets:
- **Perepletchikova on dialectics** → `ch13-the-freedom-paradox.md` or wherever dialectical thinking appears. Her "both/and" framing of emotional sensitivity is a clinical illustration of the book's dialectical argument.
- **Perepletchikova on supersensers** → `ch14-your-nervous-system-is-not-yours-alone.md`. Emotional sensitivity as gift AND challenge — fits the nervous system chapter.
- **Perepletchikova CPA (Core Problem Analysis)** → `ch26-the-axiom.md` or `ch36-the-family-as-grammar.md`. CPA's four domains (safety, self-love, belonging, mastery) parallel the book's container concept.
- **Tolle on ego/presence** → `ch27-consciousness-as-ground.md` or `ch30-the-invisible-world.md`. Use sparingly — Tolle is a secondary voice, not a load-bearing argument.
- **Tolle on non-reactivity** → `ch19-the-polarization-of-the-polis.md`. The ability to not react is the prerequisite for the Doherty fishbowl (Tier 2.6).

**Important**: Don't force transcript material. Only integrate where it genuinely strengthens an existing argument. These are supporting voices, not new theses.

## Commit Format

```
Integrate [source] into Ch[XX]: [brief description]

- [What was added and where]
- Source: [citation]
```

## When Done

After all batches, run `grep -rn "TODO\|FIXME\|TBD" books/consolidated/chapters/` to check for any loose ends. Then create a summary commit listing all integrations made.
