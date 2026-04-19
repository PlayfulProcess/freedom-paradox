#!/bin/bash
# Build a single EPUB from a book slug
# Usage: bash epub-build/build-single-epub.sh <book-slug>
# Example: bash epub-build/build-single-epub.sh fire-and-intelligence
# Requires: pandoc

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <book-slug>"
  echo "Example: $0 fire-and-intelligence"
  exit 1
fi

SLUG="$1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BOOK_DIR="$REPO_ROOT/books/$SLUG"
CHAPTERS_DIR="$BOOK_DIR/chapters"
OUTPUT_DIR="$REPO_ROOT/epub-build/output"
EPUB_CSS="$REPO_ROOT/epub-build/epub-style.css"

# Validate book exists
if [ ! -d "$CHAPTERS_DIR" ]; then
  echo "Error: No chapters directory found at $CHAPTERS_DIR"
  exit 1
fi

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# --- Clean function: strip editorial artifacts ---
clean() {
  grep -v '<!--' "$1" 2>/dev/null | \
    grep -v '^\*CC BY-SA' | \
    grep -v '\[QUOTE NEEDED:' | \
    grep -v '\[VERIFY:' | \
    grep -v '\[RESEARCH NEEDED:' | \
    grep -v '^{/\*'
}

# --- Resolve metadata ---
PER_BOOK_META="$REPO_ROOT/epub-build/per-book-metadata/${SLUG}.yaml"
BOOK_LOCAL_META="$BOOK_DIR/metadata.yaml"
TEMP_META=""

if [ -f "$PER_BOOK_META" ]; then
  METADATA_FILE="$PER_BOOK_META"
elif [ -f "$BOOK_LOCAL_META" ]; then
  METADATA_FILE="$BOOK_LOCAL_META"
else
  # Generate sensible defaults
  TEMP_META="$(mktemp /tmp/epub-meta-XXXXXX.yaml)"
  PRETTY_TITLE="$(echo "$SLUG" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')"
  cat > "$TEMP_META" << METAEOF
---
title: "$PRETTY_TITLE"
author: PlayfulProcess
lang: en-US
rights: "CC BY-SA 4.0"
date: $(date +%Y-%m-%d)
description: "$PRETTY_TITLE by PlayfulProcess"
METAEOF
  METADATA_FILE="$TEMP_META"
fi

# --- Concatenate chapters ---
COMBINED_MD="$(mktemp /tmp/epub-combined-XXXXXX.md)"

echo "Building EPUB for: $SLUG"
echo "Using metadata: $METADATA_FILE"

CHAPTER_COUNT=0
for f in "$CHAPTERS_DIR"/*.md; do
  if [ -f "$f" ]; then
    clean "$f" >> "$COMBINED_MD"
    echo -e "\n\n---\n\n" >> "$COMBINED_MD"
    CHAPTER_COUNT=$((CHAPTER_COUNT + 1))
  fi
done

if [ "$CHAPTER_COUNT" -eq 0 ]; then
  echo "Error: No markdown files found in $CHAPTERS_DIR"
  rm -f "$COMBINED_MD" "$TEMP_META"
  exit 1
fi

WORD_COUNT=$(wc -w < "$COMBINED_MD")
echo "Chapters found: $CHAPTER_COUNT"
echo "Word count: $WORD_COUNT"

# --- Build EPUB ---
OUTPUT_EPUB="$OUTPUT_DIR/${SLUG}.epub"

pandoc "$COMBINED_MD" \
  --metadata-file="$METADATA_FILE" \
  --css="$EPUB_CSS" \
  --toc \
  --toc-depth=2 \
  --split-level=1 \
  -o "$OUTPUT_EPUB"

echo "EPUB built: $OUTPUT_EPUB"
ls -lh "$OUTPUT_EPUB"

# --- Cleanup ---
rm -f "$COMBINED_MD" "$TEMP_META"
