#!/bin/bash
# Build EPUBs for all books in books/
# Requires: pandoc

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_DIR="$REPO_ROOT/epub-build"
BOOKS_DIR="$REPO_ROOT/books"

echo "=========================================="
echo "Building EPUBs for all books"
echo "=========================================="

SUCCESS=0
FAIL=0
SKIP=0

for book_dir in "$BOOKS_DIR"/*/; do
  # Skip non-directories and special entries
  [ -d "$book_dir" ] || continue

  SLUG="$(basename "$book_dir")"
  CHAPTERS_DIR="$book_dir/chapters"

  # Skip if no chapters directory
  if [ ! -d "$CHAPTERS_DIR" ]; then
    echo "[$SLUG] Skipping — no chapters/ directory"
    SKIP=$((SKIP + 1))
    continue
  fi

  # Skip if no markdown files
  MD_COUNT=$(find "$CHAPTERS_DIR" -maxdepth 1 -name '*.md' 2>/dev/null | wc -l)
  if [ "$MD_COUNT" -eq 0 ]; then
    echo "[$SLUG] Skipping — no .md files in chapters/"
    SKIP=$((SKIP + 1))
    continue
  fi

  echo ""
  echo "------------------------------------------"
  if bash "$SCRIPT_DIR/build-single-epub.sh" "$SLUG"; then
    SUCCESS=$((SUCCESS + 1))
  else
    echo "[$SLUG] FAILED"
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "=========================================="
echo "Done. Built: $SUCCESS | Failed: $FAIL | Skipped: $SKIP"
echo "Output: $SCRIPT_DIR/output/"
echo "=========================================="
