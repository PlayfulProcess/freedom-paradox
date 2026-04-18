# Deep Research Prompt — Axiom v4

This file is a prompt you can paste into a local Claude Code session (or any Claude session with web access) to execute the targeted research pass for the v4 restructure. The goal is six small, citation-grade research outputs — not dumps, not long synthesis, just the materials the v4 chapters need to stand up.

---

## How to use

Open a local Claude Code session in the repo root (`/home/user/freedom-paradox`) and paste the prompt below. The session should create six research files in `books/axiom-beneath-the-ground/research/`, numbered `research-21-*.md` through `research-26-*.md`.

**Copyright rule (absolute):** Do not store substantial verbatim passages from copyrighted works in any committed file. The research notes should capture *what the passage says*, *where it appears* (page, chapter), and *how it fits the argument*. Brief attributed quotations under ~30 words are permitted where essential. Longer material stays in the private working notes only and is paraphrased in the committed files.

---

## PROMPT TO CLAUDE

You are doing a focused research pass for the Axiom Beneath the Ground book, v4 restructure. The book is at `books/axiom-beneath-the-ground/`. The v4 plan is at `outline/v4-restructure-plan-2026-04-18.md`. Read that plan first so you understand the architecture before you start.

Produce six research files in `books/axiom-beneath-the-ground/research/`, following the numbering and format of the existing research files (research-01 through research-20). Each file should be 500–1500 words, focused, and citation-grade.

### research-21-ti-cit-transcendent-immanent.md

Target passage: the *Tantra Illuminated* (Wallis, 2nd ed., 2013, Mattamayura Press) passage describing Cit / samvit as "absolute nondual nonlocal Consciousness, beyond all other layers yet pervading them," and as "simultaneously transcendent and immanent."

Find and record:
- Chapter and approximate page range where this passage appears
- Surrounding context (what topic the chapter is on, what comes before and after)
- Wallis's precise framing of the transcendent/immanent simultaneity
- Any related passages on the layered self (Vastu, Deha, Citta, Prāṇa, Shunya, Cit)
- Cross-references to the diagram of concentric layers (which figure number, caption)

**Do not store the passage verbatim.** Paraphrase the core content, record page/chapter for later citation, and note which lines will be quoted under fair-use in the final chapter (≤30 words per quotation).

### research-22-ti-svatantrya-freedom.md

Target concept: *svātantrya* (autonomy, freedom) as a central attribute of Consciousness in nondual Shaiva Tantra, as Wallis presents it in *Tantra Illuminated* (particularly around p. 105 where he speaks of consciousness operating its five powers "as an expression of its innate freedom and total autonomy").

Find and record:
- Every place in *Tantra Illuminated* where svātantrya is defined or discussed
- Wallis's distinction between freedom-of-the-whole and freedom-of-the-part
- The relationship between svātantrya and the five powers (cit/ānanda/icchā/jñāna/kriyā)
- Cross-references to the Sutras of Recognition (*Pratyabhijñā-hrdayam*) on the same theme
- Any passages where Wallis explicitly distinguishes this tradition's freedom from Western notions of personal free will

Format: summary + citation map, no long verbatim extracts.

### research-23-tillich-courage-absolute-faith.md

Target: Paul Tillich, *The Courage to Be* (Yale University Press, 1952). The v3 book already draws on this. v4 needs confirmed primary-source formulations for three specific claims:

1. Courage as ontological act ("self-affirmation of being in spite of the fact of nonbeing") — chapter and page
2. Absolute faith as "the accepting of acceptance without somebody or something that accepts" — chapter and page
3. The three anxieties (fate/death, guilt/condemnation, emptiness/meaninglessness) — section and page

Also record:
- Tillich's biographical background (Western Front chaplaincy, Verdun, "shattered") with primary-source citations
- Any passages that distinguish "absolute faith" from faith-in-a-specific-content

Format: direct citation with page numbers, brief paraphrase, fair-use quotation only where the exact wording is argumentatively necessary.

### research-24-kybalion-truth-in-between.md

Target: *The Kybalion* (Yogi Publication Society, 1908), attributed to "Three Initiates." The book references the Hermetic principle often paraphrased as "the truth lies in between" (related to the Principle of Polarity and the Principle of Gender, and more broadly to the rejection of binary oppositions).

Find and record:
- The exact Kybalion passages that are paraphrased as "truth lies in between"
- Honest sourcing: note the contested authorship (likely William Walker Atkinson), the 1908 publication date, the text's relationship to actual Hermetic traditions
- How the concept connects to the dialectical move in the book (holding two truths simultaneously rather than choosing)
- Whether the exact phrase "the truth lies in between" appears in the text or is a later paraphrase

Format: honest citation, including the provenance caveats.

### research-25-linehan-adaptive-not-moral.md

Target: Marsha Linehan's treatment philosophy on the distinction between adaptive/non-adaptive framing and moral good/bad framing.

Find and record:
- Primary-source passages in *Cognitive-Behavioral Treatment of Borderline Personality Disorder* (1993) and *DBT Skills Training Manual* (2nd ed., 2015) where Linehan frames behaviors as adaptive/non-adaptive rather than moral
- The dialectical stance (acceptance + change) and how it relates to the adaptive frame
- Linehan's "radical acceptance" — exact formulation, where it appears
- Any direct statements from Linehan on why moral framing (good/bad) is avoided clinically
- Linehan's own explicit or implicit three-filter formulation (useful / fits data / compassionate) — confirm whether these three appear in her words or whether the formulation is the author's synthesis

Format: primary-source citations, paraphrase, short fair-use quotation where needed.

### research-26-nvidia-ecosystem-restraint.md

Target: Nvidia's public positioning on the open-source / ecosystem strategy, and specifically any direct Jensen Huang quotes on the theme of "do as little as possible and as much as necessary" (or its equivalent).

Find and record:
- Public statements from Huang, Nvidia leadership, or official materials about ecosystem-first strategy
- How Nvidia's posture toward CUDA openness, partnerships, and open-source AI models illustrates relational restraint
- The specific "do as little as possible and as much as necessary" formulation — is this a real Huang quote, a paraphrase, or the author's synthesis? Source honestly.
- Two or three concrete examples of Nvidia acting relationally (investing in ecosystem rather than hoarding) that would land with readers in 2026

Format: cite current public sources (Nvidia investor materials, published interviews, keynote transcripts) with dates. No scraped content.

---

## After the research pass

When all six files are written, append a short entry to `books/axiom-beneath-the-ground/CHANGELOG.md` summarizing what was added. Do not modify any chapter files — the research outputs will be consumed by the chapter-drafting passes that come next.

If any research item cannot be completed (missing source, paywalled material, unclear citation), leave the file in place with a clear `[RESEARCH NEEDED: specific question]` flag rather than fabricating a citation. Never invent page numbers or fabricate quotes.

---

## Copyright compliance

This prompt and all outputs must comply with the repository's copyright rule: no substantial verbatim passages from copyrighted works stored in any committed file. Brief fair-use quotations (≤30 words) with full citation are permitted. When in doubt, paraphrase.
