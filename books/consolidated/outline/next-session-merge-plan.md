# Next Session Plan: Merge Edit Branch + New Research + Final Fixes

## Step 1: Merge edit branch into plan branch

The edit branch `claude/edit-species-fire-1C9TN` has 3 commits we need:
- `a08d1ab` — Linehan wager renamed → "three-filter test" across all chapters + polyvagal disclaimer strengthened
- `6013aa2` — Ostrom caveat added to Ch12 + Ch24 Kant section smoothed
- `608c864` — known-issues updated

**CONFLICTS EXPECTED** because our branch has:
- 69/31 reframe (Ch26 transition, Ch41, SUMMARY.md, index.md)
- Campbell paradox rewrite (Ch40)
- Karpathy AI psychosis (Ch19)
- Kant 4 fixes (Ch24, Ch13, Ch39)
- Chapter renumbering (old ch32-37 → new ch33-38, old ch38 → new ch32)

**Strategy:** Merge edit branch, resolve conflicts keeping:
- Our 69/31 structure + chapter numbering
- Edit branch's Linehan rename + polyvagal + Ostrom fixes
- Our Campbell, Karpathy, Kant fixes (edit branch doesn't have these)

## Step 2: Pull new research files from master

Check `origin/master` for any new files since last pull. Known new:
- podcast-philosophy-naturalism.md (Axiom)
- podcast-ezra-klein-full.md (Freedom Paradox)
- podcast-gastropod.md (Real Cost of Lunch)
- podcast-therapy-neuroscience.md (Working Architecture)

These may not exist yet — user listed them as the target but they
may need to be created from transcripts.

## Step 3: Verify the 3 critical fixes landed correctly after merge

After merge, verify:
1. "Linehan wager" appears ZERO times (replaced with "three-filter test")
2. Polyvagal disclaimer in Ch14 names the 39-expert challenge
3. Ostrom caveat in Ch12 names the category-mistake critique
4. Campbell in Ch40 uses the paradox, not the bumper sticker
5. 69/31 structure intact (Book One Ch00-32, Book Two Ch33-41)

## Step 4: Process remaining podcast transcripts

If time permits, process:
- Tim Ferriss (44 episodes downloaded, not yet a research file)
- Any remaining Sam Harris episodes not covered

## Step 5: Final build and push

```bash
cd /home/user/freedom-paradox
mkdir -p src/consolidated src/real-cost-of-lunch
cp books/consolidated/chapters/*.md src/consolidated/
cp books/real-cost-of-lunch/chapters/ch*.md src/real-cost-of-lunch/
mdbook build
```

Commit and push to `claude/plan-shareable-links-gFIq0`.

## Estimated time: 2-3 hours

Priority if time limited:
1. Merge (must do — edit branch has the Linehan fix)
2. Verify fixes
3. New research files
4. Tim Ferriss processing
