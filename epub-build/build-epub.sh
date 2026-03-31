#!/bin/bash
cd /home/user/freedom-paradox

OUTPUT="epub-build/complete-reading-draft.md"

# Front matter
cat epub-build/00-front-matter.md > "$OUTPUT"

# ===== BOOK 1: THE FREEDOM PARADOX =====
echo -e "\n\n# BOOK ONE: THE FREEDOM PARADOX\n" >> "$OUTPUT"
echo -e "## Open Source, AI, and the Limits of Openness\n\n---\n" >> "$OUTPUT"

for ch in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16; do
  f="books/freedom-paradox/chapters/ch${ch}-*.md"
  for file in $f; do
    if [ -f "$file" ]; then
      grep -v '<!--' "$file" | grep -v '^{/\*' >> "$OUTPUT"
      echo -e "\n\n---\n\n" >> "$OUTPUT"
    fi
  done
done

# Epilogue
if [ -f "books/freedom-paradox/chapters/epilogue.md" ]; then
  grep -v '<!--' books/freedom-paradox/chapters/epilogue.md >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
fi

# ===== BOOK 2: THE SPECIES THAT GOT FIRE =====
echo -e "\n\n# BOOK TWO: THE SPECIES THAT GOT FIRE\n" >> "$OUTPUT"
echo -e "## Grammars of the Living World\n\n---\n" >> "$OUTPUT"

echo -e "## PART I: THE BODY\n" >> "$OUTPUT"
for f in books/grammars-of-the-living-world/chapters/ch01-the-oldest-technology.md \
         books/grammars-of-the-living-world/chapters/ch02-the-darkness-is-the-medicine.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART II: FIRE\n" >> "$OUTPUT"
for f in books/grammars-of-the-living-world/chapters/ch03-what-the-old-stories-knew.md \
         books/grammars-of-the-living-world/chapters/ch04-the-prisoners-dilemma.md \
         books/grammars-of-the-living-world/chapters/ch05-the-colonial-reflex.md \
         books/grammars-of-the-living-world/chapters/ch06-the-degradation-of-coregulation.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART III: GRAMMARS\n" >> "$OUTPUT"
grep -v '<!--' books/grammars-of-the-living-world/chapters/ch07-responsibility-structures.md | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

echo -e "## PART IV: THE FILTER\n" >> "$OUTPUT"
grep -v '<!--' books/grammars-of-the-living-world/chapters/ch08-what-holds.md | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

echo -e "## PART V: THE GESTURE\n" >> "$OUTPUT"
grep -v '<!--' books/grammars-of-the-living-world/chapters/ch09-the-adaptive-wager.md | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

# ===== BOOK 3: WORKING ARCHITECTURE =====
echo -e "\n\n# BOOK THREE: WORKING ARCHITECTURE\n" >> "$OUTPUT"
echo -e "## A Practical Book About Stories That Work\n\n---\n" >> "$OUTPUT"

echo -e "## PART I: THE SCIENCE YOU NEED\n" >> "$OUTPUT"
for f in books/working-architecture/chapters/ch0{1,2,3}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART II: THE PRACTICE\n" >> "$OUTPUT"
for f in books/working-architecture/chapters/ch0{4,5,6,7,8,9}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART III: THE ARCHITECTURE\n" >> "$OUTPUT"
for f in books/working-architecture/chapters/ch1{0,1,2}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

# ===== BOOK 4: THE SPECIES THAT TELLS STORIES (partial) =====
echo -e "\n\n# BOOK FOUR: THE SPECIES THAT TELLS STORIES (3 of 7 chapters)\n" >> "$OUTPUT"
echo -e "## The Narrative Heart\n\n---\n" >> "$OUTPUT"

for f in books/grammars-of-the-living-world/chapters/ch01-the-oldest-technology.md \
         books/grammars-of-the-living-world/chapters/ch02-the-darkness-is-the-medicine.md \
         books/grammars-of-the-living-world/chapters/ch03-what-the-old-stories-knew.md; do
  # Skip — these are already in Book 2
  :
done

# Actually Book 4 chapters ARE the same as Book 2 Part I chapters in v4
# So skip to avoid duplication. Note this in the text.
echo -e "*Note: Book 4 (The Species That Tells Stories) shares its first three chapters with Book 2. The remaining four chapters (Ch 4-7) are outlined in the research prompts but not yet drafted. See the outline at books/grammars-of-the-living-world/outline/new-skeleton-species-tells-stories-v1.md for the full plan.*\n\n---\n\n" >> "$OUTPUT"

# ===== RESEARCH NOTES (selected) =====
echo -e "\n\n# APPENDIX: SELECTED RESEARCH NOTES\n\n---\n" >> "$OUTPUT"

echo -e "## Research 44: The Economics of Mythic Infrastructure\n" >> "$OUTPUT"
grep -v '<!--' books/grammars-of-the-living-world/research/raw/research-44-economics-mythic-infrastructure.md >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

echo -e "## Research 48: Extractive Cultures and Viral Strategies\n" >> "$OUTPUT"
cat books/grammars-of-the-living-world/research/raw/research-48-extractive-cultures-viral-strategies.md >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

echo -e "## Thesis Breakthrough (March 2026)\n" >> "$OUTPUT"
cat books/grammars-of-the-living-world/drafts/thesis-breakthrough-march-2026.md >> "$OUTPUT"
echo -e "\n\n---\n\n" >> "$OUTPUT"

# ===== CHARTS NOTE =====
echo -e "\n## Computational Models\n" >> "$OUTPUT"
echo -e "Six charts from the cultural resilience agent-based model are included in the models/charts/ directory:\n" >> "$OUTPUT"
echo "- Population dynamics" >> "$OUTPUT"
echo "- Monoculture vs diverse timeseries" >> "$OUTPUT"
echo "- Diversity reduces variance" >> "$OUTPUT"
echo "- Insurance effect floor" >> "$OUTPUT"
echo "- Commons resource health" >> "$OUTPUT"
echo "- Three strategies summary" >> "$OUTPUT"
echo -e "\n*These charts support the book's argument that cultural diversity functions as adaptive insurance — the same way biodiversity protects ecosystems from catastrophic failure.*\n" >> "$OUTPUT"

wc -w "$OUTPUT"
echo "Built: $OUTPUT"

# ===== BOOK 5: THE AXIOM BENEATH THE GROUND =====
echo -e "\n\n# BOOK FIVE: THE AXIOM BENEATH THE GROUND\n" >> "$OUTPUT"
echo -e "## On Inherent Value, the Courage to Be as a Part, and the Honest Nonduality\n\n---\n" >> "$OUTPUT"

echo -e "## PART I: THE VOID\n" >> "$OUTPUT"
for f in books/axiom-beneath-the-ground/chapters/ch0{1,2,3}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART II: THE RECOGNITION\n" >> "$OUTPUT"
for f in books/axiom-beneath-the-ground/chapters/ch0{4,5,6}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done

echo -e "## PART III: THE PART\n" >> "$OUTPUT"
for f in books/axiom-beneath-the-ground/chapters/ch0{7,8,9}*.md; do
  grep -v '<!--' "$f" | grep -v '^{/\*' | sed '/^\*CC BY-SA/d' >> "$OUTPUT"
  echo -e "\n\n---\n\n" >> "$OUTPUT"
done
