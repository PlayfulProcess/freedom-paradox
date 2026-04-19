#!/usr/bin/env bash
# Build KDP-ready interior PDF + EPUB from a book's markdown chapters.
#
# Usage:
#   ./scripts/build-print.sh <book-name>
#   ./scripts/build-print.sh freedom-paradox
#
# Produces:
#   output/print/<book-name>-interior.pdf    (KDP 6x9 via pandoc+typst)
#   output/print/<book-name>.epub            (Kindle ebook via pandoc)
#
# Requires: pandoc 3.x + typst 0.10+
#   winget install Typst.Typst
#   choco install pandoc  (or pandoc.exe from pandoc.org)

set -euo pipefail

BOOK="${1:-}"
if [[ -z "$BOOK" ]]; then
  echo "Usage: $0 <book-name>"
  echo "Available books:"
  ls -1 books/ 2>/dev/null | grep -vE '^(PUBLICATION|README|\.|EPUB|output)' || true
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BOOK_DIR="$REPO_ROOT/books/$BOOK"
CHAPTERS_DIR="$BOOK_DIR/chapters"
OUT_DIR="$REPO_ROOT/output/print"

if [[ ! -d "$CHAPTERS_DIR" ]]; then
  echo "ERROR: no chapters folder at $CHAPTERS_DIR"
  exit 1
fi

mkdir -p "$OUT_DIR"

# --- Metadata (book.yaml overrides defaults) ----------------------------------
TITLE=""
SUBTITLE=""
AUTHOR="PlayfulProcess"
DESCRIPTION=""
SOURCE_URL="https://github.com/PlayfulProcess/$BOOK"

META_FILE="$BOOK_DIR/book.yaml"
if [[ -f "$META_FILE" ]]; then
  while IFS=': ' read -r k v; do
    v="${v#\"}"; v="${v%\"}"
    case "$k" in
      title)       TITLE="$v" ;;
      subtitle)    SUBTITLE="$v" ;;
      author)      AUTHOR="$v" ;;
      description) DESCRIPTION="$v" ;;
      source_url)  SOURCE_URL="$v" ;;
    esac
  done < "$META_FILE"
fi

if [[ -z "$TITLE" ]]; then
  TITLE=$(echo "$BOOK" | sed -E 's/-/ /g' | awk '{for(i=1;i<=NF;i++)$i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')
fi

echo "=== Building $BOOK ==="
echo "  Title:    $TITLE"
[[ -n "$SUBTITLE" ]] && echo "  Subtitle: $SUBTITLE"
echo "  Author:   $AUTHOR"
echo "  Source:   $SOURCE_URL"
echo ""

# --- Collect chapters ---------------------------------------------------------
mapfile -t CHAPTERS < <(find "$CHAPTERS_DIR" -maxdepth 1 -type f -name '*.md' \
  | grep -vE '/(draft|v2-|old-)' \
  | sort)

if [[ ${#CHAPTERS[@]} -eq 0 ]]; then
  echo "ERROR: no .md chapter files in $CHAPTERS_DIR"
  exit 1
fi

echo "Found ${#CHAPTERS[@]} chapter files."
echo ""

TMPDIR="$(mktemp -d)"
trap "rm -rf $TMPDIR" EXIT

# --- Metadata file (pure YAML, separate from content) ------------------------
META="$TMPDIR/meta.yaml"
cat > "$META" <<EOF
---
title: "$TITLE"
author: "$AUTHOR"
${SUBTITLE:+subtitle: \"$SUBTITLE\"}
${DESCRIPTION:+description: \"$DESCRIPTION\"}
# KDP 6x9 paperback — "us-trade" is typst's named 6in x 9in paper
papersize: "us-trade"
# KDP gutter requirements:
#   24-150 pages:  inside 0.375in (tight)
#   151-300:       inside 0.5in
#   301-500:       inside 0.625in  <-- current default, safe for most books
#   501-700:       inside 0.75in
#   701-828:       inside 0.875in
# Using 0.625 by default — safe for 301-500 page books (Freedom Paradox = 311).
# Shorter books just look a bit more generously margined; no upload rejection.
page-margin: "(inside: 0.625in, outside: 0.5in, top: 0.75in, bottom: 0.75in)"
mainfont: "Palatino Linotype"
fontsize: "11pt"
toc: true
toc-depth: 1
rights: "Creative Commons Attribution-ShareAlike 4.0 International"
EOF

# --- Front matter content (license / copyright page) --------------------------
FRONT="$TMPDIR/00-front.md"
cat > "$FRONT" <<EOF
**$TITLE**

by $AUTHOR

This work is licensed under Creative Commons Attribution-ShareAlike 4.0 International.
<https://creativecommons.org/licenses/by-sa/4.0/>

Source repository: <$SOURCE_URL>

First paperback edition.

\\newpage

EOF

# --- Build PDF via pandoc -> typst -------------------------------------------
PDF_OUT="$OUT_DIR/$BOOK-interior.pdf"
pandoc \
  --from=markdown \
  --pdf-engine=typst \
  --top-level-division=chapter \
  --metadata-file="$META" \
  -o "$PDF_OUT" \
  "$FRONT" "${CHAPTERS[@]}"
echo "✓ PDF:  $PDF_OUT"

# --- EPUB ---------------------------------------------------------------------
EPUB_OUT="$OUT_DIR/$BOOK.epub"
pandoc \
  --from=markdown \
  --to=epub3 \
  --toc --toc-depth=2 \
  --top-level-division=chapter \
  --metadata-file="$META" \
  -o "$EPUB_OUT" \
  "${CHAPTERS[@]}"
echo "✓ EPUB: $EPUB_OUT"
echo ""
echo "Next:"
echo "  1. Open $PDF_OUT, verify page count and layout."
echo "  2. If page count > 300, bump inner margin to 0.625in in scripts/build-print.sh."
echo "  3. Upload PDF + EPUB to KDP."
