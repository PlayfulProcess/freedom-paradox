"""
Scrape Christopher Hareesh Wallis's blog at hareesh.org/blog.

For each post:
- Extract URL, title, publication date, tags, body text (clean of nav/footer)
- Extract Hareesh's OWN comment replies only (third-party commenters excluded)
- Save as markdown with YAML frontmatter

Polite: 2-second delay between requests, real User-Agent.
Resumable: skips files that already exist.

Run: python scrape.py
Output: ../../transcripts/wallis-corpus/blog/YYYY-MM-DD-slug.md
"""
from __future__ import annotations

import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------

BASE_URL = "https://hareesh.org"
BLOG_INDEX = f"{BASE_URL}/blog/"
USER_AGENT = (
    "Mozilla/5.0 (compatible; recursive-eco-research/1.0; "
    "+https://recursive.eco) PlayfulProcess research scraper"
)
DELAY_SECONDS = 2.0
TIMEOUT = 30

OUT_DIR = Path(__file__).resolve().parent.parent.parent / "transcripts" / "wallis-corpus" / "blog"

# Comment-author filter — case-insensitive; matches comment authors who are
# Hareesh himself. Add aliases as discovered.
HAREESH_AUTHOR_PATTERNS = [
    re.compile(r"\bhareesh\b", re.I),
    re.compile(r"\bchristopher\s+(d\.\s+)?wallis\b", re.I),
    re.compile(r"\bwallis\b", re.I),
]


# ----------------------------------------------------------------------
# HTTP
# ----------------------------------------------------------------------

def fetch(url: str) -> str | None:
    """Fetch a URL with the polite headers. Returns HTML text or None on error."""
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        print(f"    [warn] fetch failed for {url}: {e}", file=sys.stderr)
        return None


# ----------------------------------------------------------------------
# Pagination — discover post URLs
# ----------------------------------------------------------------------

def discover_post_urls() -> list[str]:
    """Walk /blog/page/N/ until empty, collecting post URLs."""
    seen: set[str] = set()
    urls: list[str] = []
    page = 1
    while True:
        page_url = f"{BASE_URL}/blog/page/{page}/" if page > 1 else BLOG_INDEX
        print(f"  page {page}: {page_url}")
        html = fetch(page_url)
        if not html:
            break
        soup = BeautifulSoup(html, "lxml")
        # WordPress: post links live in article tags or specific class names.
        # Use a tolerant approach: any <a> whose href contains '/blog/' and
        # ends with a slug, but not pagination links.
        page_post_urls = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full = urljoin(BASE_URL, href)
            parsed = urlparse(full)
            if parsed.netloc != urlparse(BASE_URL).netloc:
                continue
            path = parsed.path.rstrip("/")
            # Heuristic: post URLs look like /YYYY/MM/DD/slug or /blog/slug
            # WordPress permalink schemes vary. Both patterns:
            if re.match(r"^/\d{4}/\d{2}/\d{2}/[^/]+$", path):
                page_post_urls.append(full)
            elif re.match(r"^/blog/[^/]+$", path) and not path.endswith("/blog"):
                # Exclude pagination "page/N" handled separately
                if "/page/" not in path:
                    page_post_urls.append(full)
        new_on_page = [u for u in page_post_urls if u not in seen]
        if not new_on_page:
            print(f"    no new posts on page {page}, stopping pagination")
            break
        for u in new_on_page:
            seen.add(u)
            urls.append(u)
        print(f"    found {len(new_on_page)} new post URLs (total: {len(urls)})")
        time.sleep(DELAY_SECONDS)
        page += 1
        if page > 100:
            print("    safety stop at 100 pages")
            break
    return urls


# ----------------------------------------------------------------------
# Post parsing
# ----------------------------------------------------------------------

def is_hareesh_author(name: str | None) -> bool:
    if not name:
        return False
    return any(p.search(name) for p in HAREESH_AUTHOR_PATTERNS)


def clean_text(node) -> str:
    """Strip extraneous whitespace, return joined text."""
    if node is None:
        return ""
    text = node.get_text(separator="\n", strip=True)
    # Collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def parse_post(url: str, html: str) -> dict | None:
    """Parse a single blog post page into a structured dict."""
    soup = BeautifulSoup(html, "lxml")

    # Title — try common WordPress patterns
    title = None
    for sel in ["h1.entry-title", "h1.post-title", "article h1", "h1"]:
        node = soup.select_one(sel)
        if node:
            title = clean_text(node)
            break

    # Date — look for time tags or class hints
    date_str = None
    for sel in ["time[datetime]", ".entry-date[datetime]", ".published[datetime]"]:
        node = soup.select_one(sel)
        if node and node.get("datetime"):
            date_str = node["datetime"][:10]
            break
    if not date_str:
        # Fallback: look for date-like text in meta
        meta_date = soup.find("meta", property="article:published_time")
        if meta_date and meta_date.get("content"):
            date_str = meta_date["content"][:10]
    if not date_str:
        # Last resort: try URL pattern /YYYY/MM/DD/
        m = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
        if m:
            date_str = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

    # Body — typical WordPress entry-content
    body_node = None
    for sel in [".entry-content", "article .post-content", "article", ".post"]:
        body_node = soup.select_one(sel)
        if body_node:
            break
    # Strip nav, comments form, social widgets within the body
    if body_node:
        for kill_sel in ["nav", ".comments", ".comment-respond", ".sharedaddy",
                         ".jp-relatedposts", ".navigation", "form", "script", "style"]:
            for k in body_node.select(kill_sel):
                k.decompose()
    body_text = clean_text(body_node)

    # Tags
    tags = []
    for a in soup.select("a[rel~='tag'], .tags-links a, .post-tags a"):
        t = a.get_text(strip=True)
        if t and t not in tags:
            tags.append(t)

    # Hareesh's own comment replies
    hareesh_replies: list[str] = []
    for c in soup.select(".comment, li.comment, .wp-comment, article.comment"):
        author_node = c.select_one(".comment-author .fn, .comment-author cite, .comment-author")
        author_name = clean_text(author_node) if author_node else None
        if not is_hareesh_author(author_name):
            continue
        body = c.select_one(".comment-body, .comment-content")
        text = clean_text(body)
        if text:
            hareesh_replies.append(text)

    if not (title and body_text):
        return None

    return {
        "url": url,
        "title": title,
        "date": date_str or "unknown",
        "tags": tags,
        "body": body_text,
        "hareesh_replies": hareesh_replies,
    }


# ----------------------------------------------------------------------
# Filename + write
# ----------------------------------------------------------------------

def slugify(s: str, max_len: int = 80) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:max_len] or "untitled"


def post_to_markdown(post: dict) -> str:
    """Format a post dict as markdown with YAML frontmatter."""
    fm_tags = "[" + ", ".join(f"\"{t}\"" for t in post["tags"]) + "]" if post["tags"] else "[]"
    parts = [
        "---",
        f"url: {post['url']}",
        f"title: {post['title'].replace(chr(10), ' ')!r}",
        f"date: {post['date']}",
        f"tags: {fm_tags}",
        f"author: Hareesh Wallis",
        f"hareesh_reply_count: {len(post['hareesh_replies'])}",
        "---",
        "",
        f"# {post['title']}",
        "",
        post["body"],
    ]
    if post["hareesh_replies"]:
        parts.extend([
            "",
            "---",
            "",
            "## Hareesh's own replies in comments",
            "",
        ])
        for i, reply in enumerate(post["hareesh_replies"], 1):
            parts.append(f"### Reply {i}")
            parts.append("")
            parts.append(reply)
            parts.append("")
    return "\n".join(parts) + "\n"


def write_post(post: dict, out_dir: Path) -> Path | None:
    """Write a post to YYYY-MM-DD-slug.md. Returns path, or None if it already exists."""
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(post["title"])
    filename = f"{post['date']}-{slug}.md"
    out_path = out_dir / filename
    if out_path.exists():
        return None
    out_path.write_text(post_to_markdown(post), encoding="utf-8")
    return out_path


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Wallis blog scraper")
    print("=" * 60)
    print(f"Output: {OUT_DIR}")
    print(f"Delay: {DELAY_SECONDS}s between requests")
    print()

    print("Discovering post URLs...")
    urls = discover_post_urls()
    print(f"\nFound {len(urls)} unique post URLs.\n")

    written = 0
    skipped = 0
    failed = 0
    for i, url in enumerate(urls, 1):
        print(f"[{i:>3}/{len(urls)}] {url}")
        # Quick existence check before fetch — slugify from URL guess
        # (We can't know exact filename without fetching, so always fetch
        # but skip the write if file exists.)
        html = fetch(url)
        if not html:
            failed += 1
            continue
        post = parse_post(url, html)
        if not post:
            failed += 1
            print("    [warn] could not parse")
            continue
        out_path = write_post(post, OUT_DIR)
        if out_path:
            written += 1
            print(f"    → {out_path.name}")
        else:
            skipped += 1
            print(f"    [skip] already exists")
        time.sleep(DELAY_SECONDS)

    print()
    print("=" * 60)
    print(f"  written: {written}")
    print(f"  skipped (already existed): {skipped}")
    print(f"  failed: {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()
