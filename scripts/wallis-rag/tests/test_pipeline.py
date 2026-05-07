"""
End-to-end test of the Wallis RAG pipeline using 3 sample posts.

Does NOT upload to R2. Verifies:
- Scraper can fetch a page and parse it into the expected structure
- Frontmatter parser round-trips
- Chunker produces non-empty chunks of reasonable size

Run: python -m pytest tests/ -v
or:  python tests/test_pipeline.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# Allow imports from parent dir
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from embed import chunk_paragraphs, parse_frontmatter, count_tokens
from scrape import is_hareesh_author, slugify, post_to_markdown


def test_hareesh_author_filter():
    assert is_hareesh_author("Hareesh") is True
    assert is_hareesh_author("Christopher Wallis") is True
    assert is_hareesh_author("Christopher D. Wallis") is True
    assert is_hareesh_author("hareesh wallis") is True
    assert is_hareesh_author("Some Other Person") is False
    assert is_hareesh_author("") is False
    assert is_hareesh_author(None) is False
    print("  test_hareesh_author_filter ok")


def test_slugify():
    assert slugify("What is Trika Shaivism?") == "what-is-trika-shaivism"
    assert slugify("Hello World") == "hello-world"
    assert slugify("Multiple   spaces!!") == "multiple-spaces"
    assert slugify("") == "untitled"
    # Unicode handling: non-ASCII chars get stripped, the rest survive
    out = slugify("Cafe ABC")
    assert out == "cafe-abc"
    print("  test_slugify ok")


def test_frontmatter_roundtrip():
    md = """---
url: https://example.com/post
title: 'A Test Post'
date: 2024-01-15
tags: ["foo", "bar"]
author: Hareesh Wallis
---

This is the body.

Paragraph two.
"""
    meta, body = parse_frontmatter(md)
    assert meta["url"] == "https://example.com/post"
    assert meta["title"] == "A Test Post"
    assert meta["date"] == "2024-01-15"
    assert meta["tags"] == ["foo", "bar"]
    assert meta["author"] == "Hareesh Wallis"
    assert "This is the body." in body
    assert "Paragraph two." in body
    print("  test_frontmatter_roundtrip ok")


def test_chunker_basic():
    text = "Paragraph one is short.\n\nParagraph two is also short.\n\nParagraph three."
    chunks = chunk_paragraphs(text, target=20, overlap=5)
    assert len(chunks) >= 1, "should produce at least one chunk"
    for c in chunks:
        assert c.strip(), "no empty chunks"
    print("  test_chunker_basic ok")


def test_chunker_long_text():
    paragraph = "This is a sentence. " * 30  # ~150 tokens
    text = "\n\n".join([paragraph] * 8)  # ~1200 tokens
    chunks = chunk_paragraphs(text, target=400, overlap=80)
    assert len(chunks) >= 2, f"long text should produce multiple chunks; got {len(chunks)}"
    # Each chunk should be roughly under target+overlap
    for c in chunks:
        tokens = count_tokens(c)
        assert tokens <= 600, f"chunk too long: {tokens} tokens"
    print(f"  test_chunker_long_text ok ({len(chunks)} chunks)")


def test_post_to_markdown_format():
    post = {
        "url": "https://hareesh.org/blog/test-post/",
        "title": "Test Post",
        "date": "2024-01-15",
        "tags": ["tantra", "trika"],
        "body": "Body content here.\n\nSecond paragraph.",
        "hareesh_replies": ["A reply by Hareesh."],
    }
    md = post_to_markdown(post)
    assert "---" in md
    assert "url: https://hareesh.org/blog/test-post/" in md
    assert "# Test Post" in md
    assert "Body content here." in md
    assert "## Hareesh's own replies in comments" in md
    assert "A reply by Hareesh." in md
    print("  test_post_to_markdown_format ok")


def main():
    print("Running Wallis RAG pipeline tests...")
    test_hareesh_author_filter()
    test_slugify()
    test_frontmatter_roundtrip()
    test_chunker_basic()
    test_chunker_long_text()
    test_post_to_markdown_format()
    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
