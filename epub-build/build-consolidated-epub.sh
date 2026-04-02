#!/bin/bash
# Build EPUB from consolidated chapters + Real Cost of Lunch + Campfire Stories
# Requires: pandoc

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

OUTPUT_MD="epub-build/consolidated-reading-draft.md"
OUTPUT_EPUB="epub-build/the-species-that-got-fire.epub"

echo "Building EPUB from consolidated chapters..."

# Helper: strip HTML comments, editorial flags, license lines
clean() {
  grep -v '<!--' "$1" 2>/dev/null | \
    grep -v '^\*CC BY-SA' | \
    grep -v '\[QUOTE NEEDED:' | \
    grep -v '\[VERIFY:' | \
    grep -v '\[RESEARCH NEEDED:' | \
    grep -v '^{/\*'
}

# Start fresh
> "$OUTPUT_MD"

# ===== FRONT MATTER =====
cat >> "$OUTPUT_MD" << 'EOF'
---
title: "The Species That Got Fire"
---

# The Species That Got Fire

*By PlayfulProcess*

*Power, Stories, and the Responsibility We Haven't Built Yet*

42 chapters · 2 books · 8 parts · 2 appendices · ~130,000 words

CC BY-SA 4.0 · [books.recursive.eco](https://books.recursive.eco) · [recursive.eco](https://recursive.eco)

---

EOF

# ===== BOOK ONE: THE 69% =====
echo -e "\n\n# Book One: The 69%\n" >> "$OUTPUT_MD"
echo -e "*The perpetual problems. The discipline of learning to stop trying to solve the unsolvable.*\n\n---\n" >> "$OUTPUT_MD"

# Part I — The Clause
echo -e "\n## Part I — The Clause\n" >> "$OUTPUT_MD"
for ch in ch00-introduction ch01-the-anthropic-clause ch02-when-code-could-clone-itself ch03-free-as-in-freedom; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part II — The Movement
echo -e "\n## Part II — The Movement\n" >> "$OUTPUT_MD"
for ch in ch04-open-as-in-business ch05-the-recursive-public ch06-the-license-wars ch07-the-platform-play ch08-value-creation-for-whom; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part III — The Paradox
echo -e "\n## Part III — The Paradox\n" >> "$OUTPUT_MD"
for ch in ch09-the-safety-argument ch10-the-dwarkesh-problem ch11-open-behind-the-frontier ch12-the-commons-that-can-kill ch13-the-freedom-paradox; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part IV — The Body
echo -e "\n## Part IV — The Body\n" >> "$OUTPUT_MD"
for ch in ch14-your-nervous-system-is-not-yours-alone ch15-why-stories ch16-the-oldest-technology ch17-the-darkness-is-the-medicine ch18-when-stories-lose-their-homes ch19-the-polarization-of-the-polis; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part V — The Fire
echo -e "\n## Part V — The Fire\n" >> "$OUTPUT_MD"
for ch in ch20-machines-for-constructing-stories ch21-drawing-from-the-well ch22-survival-and-capture ch23-what-the-old-stories-knew ch24-the-species-that-got-fire ch25-but-collaboration-runs-deeper ch26-the-axiom; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# ===== BOOK TWO: THE 31% =====
echo -e "\n\n# Book Two: The 31%\n" >> "$OUTPUT_MD"
echo -e "*What you can actually do. Build the viewer. Tell the story. Fix the roof.*\n\n---\n" >> "$OUTPUT_MD"

# Part VI — The Ground
echo -e "\n## Part VI — The Ground\n" >> "$OUTPUT_MD"
for ch in ch27-consciousness-as-ground ch28-the-circularity ch29-what-tillich-would-say-to-wallis ch30-the-invisible-world ch31-relationship-to-what-cannot-be-seen ch32-what-ai-actually-is; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part VII — The Practice
echo -e "\n## Part VII — The Practice\n" >> "$OUTPUT_MD"
for ch in ch33-telling ch34-reading-together ch35-listening-playing-making ch36-the-family-as-grammar ch37-the-community-as-grammar ch38-the-commons; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# Part VIII — The Grammar We Need
echo -e "\n## Part VIII — The Grammar We Need\n" >> "$OUTPUT_MD"
for ch in ch39-the-grammar-we-need ch40-the-honest-practitioner ch41-the-species-that-tells-stories; do
  f="books/consolidated/chapters/${ch}.md"
  if [ -f "$f" ]; then
    clean "$f" >> "$OUTPUT_MD"
    echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
  fi
done

# ===== APPENDIX A: THE REAL COST OF LUNCH =====
echo -e "\n\n# Appendix A — The Real Cost of Lunch\n" >> "$OUTPUT_MD"
echo -e "*20 chapters on what your food actually costs.*\n\n---\n" >> "$OUTPUT_MD"

for num in $(seq -w 1 20); do
  f="books/real-cost-of-lunch/chapters/ch${num}-*.md"
  for file in $f; do
    if [ -f "$file" ]; then
      clean "$file" >> "$OUTPUT_MD"
      echo -e "\n\n---\n\n" >> "$OUTPUT_MD"
    fi
  done
done

# ===== APPENDIX B: THE CAMPFIRE STORIES =====
echo -e "\n\n# Appendix B — The Campfire Stories\n" >> "$OUTPUT_MD"
echo -e "*Ten bedtime stories from six continents.*\n\n---\n" >> "$OUTPUT_MD"

f="books/consolidated/chapters/appendix-campfire-stories.md"
if [ -f "$f" ]; then
  clean "$f" >> "$OUTPUT_MD"
fi

# ===== BUILD EPUB =====
echo ""
echo "Markdown assembled: $(wc -w < "$OUTPUT_MD") words"
echo "Building EPUB with Pandoc..."

pandoc "$OUTPUT_MD" \
  --metadata-file=epub-build/metadata.yaml \
  --css=epub-build/epub-style.css \
  --toc \
  --toc-depth=2 \
  --epub-chapter-level=1 \
  -o "$OUTPUT_EPUB"

echo "EPUB built: $OUTPUT_EPUB"
ls -lh "$OUTPUT_EPUB"
