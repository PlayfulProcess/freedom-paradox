#!/bin/bash
# Full publish pipeline: rebuild EPUBs, create GitHub Release, rebuild mdbook, push
# Usage: bash publish.sh [commit message]
# Example: bash publish.sh "Editorial pass on Axiom ch3"
#
# EPUBs are served from GitHub Releases (not tracked in git) to avoid binary bloat.
# Landing page links to: https://github.com/PlayfulProcess/freedom-paradox/releases/latest/download/{file}.epub

set -e

REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

MSG="${1:-Update books and rebuild site}"
TAG="v$(date +%Y.%m.%d)-$(date +%H%M)"

echo "=========================================="
echo "PUBLISH: Full rebuild pipeline"
echo "=========================================="

# Step 1: Rebuild ALL EPUBs
echo ""
echo "📖 Step 1: Rebuilding EPUBs..."
EPUB_COUNT=0
for book_dir in books/*/; do
  [ -d "$book_dir/chapters" ] || continue
  SLUG="$(basename "$book_dir")"
  bash epub-build/build-single-epub.sh "$SLUG" 2>&1 | tail -1
  EPUB_COUNT=$((EPUB_COUNT + 1))
done

# Build Axiom v3 separately (lives in chapters/v3/)
if [ -d "books/axiom-beneath-the-ground/chapters/v3" ]; then
  echo "Building Axiom v3 EPUB..."
  COMBINED_MD="$(mktemp /tmp/epub-combined-XXXXXX.md)"
  for f in books/axiom-beneath-the-ground/chapters/v3/*.md books/axiom-beneath-the-ground/chapters/the-ceremony.md; do
    grep -v '<!--' "$f" 2>/dev/null | grep -v '^\*CC BY-SA' >> "$COMBINED_MD"
    echo -e "\n\n---\n\n" >> "$COMBINED_MD"
  done
  pandoc "$COMBINED_MD" \
    --metadata-file="epub-build/per-book-metadata/axiom-beneath-the-ground.yaml" \
    --css="epub-build/epub-style.css" \
    --toc --toc-depth=2 --split-level=1 \
    -o "epub-build/output/axiom-v3.epub"
  rm -f "$COMBINED_MD"
  echo "EPUB built: epub-build/output/axiom-v3.epub"
  EPUB_COUNT=$((EPUB_COUNT + 1))
fi

echo "✅ $EPUB_COUNT EPUBs rebuilt"

# Step 2: Rebuild mdbook site
echo ""
echo "🔨 Step 2: Rebuilding mdbook site..."
bash build.sh 2>&1 | tail -3

# Step 3: Stage and commit
echo ""
echo "📦 Step 3: Staging files..."
git add books/ src/ .github/ docs/epubs/index.html CLAUDE.md publish.sh

# Check if there are changes to commit
if git diff --cached --quiet; then
  echo "ℹ️  No source changes to commit."
else
  echo "💾 Committing..."
  git commit -m "$(cat <<EOF
$MSG

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
fi

# Step 4: Push
echo ""
echo "🚀 Step 4: Pushing to GitHub..."
git push origin master

# Step 5: Create GitHub Release with EPUBs
echo ""
echo "📦 Step 5: Creating GitHub Release ($TAG)..."
gh release create "$TAG" \
  epub-build/output/*.epub \
  --title "$MSG" \
  --notes "Automated release. $EPUB_COUNT EPUBs rebuilt." \
  --latest

echo ""
echo "=========================================="
echo "✅ PUBLISH COMPLETE"
echo "   EPUBs rebuilt: $EPUB_COUNT"
echo "   Release: $TAG"
echo "   Site pushed (GitHub Pages auto-deploys)"
echo "   Downloads: https://github.com/PlayfulProcess/freedom-paradox/releases/latest"
echo "=========================================="
