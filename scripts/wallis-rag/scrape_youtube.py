"""
Scrape Christopher Hareesh Wallis's YouTube channel for auto-captions.

Uses yt-dlp to:
- Walk @HareeshWallis channel
- For each video: download auto-captions (--write-auto-sub --skip-download)
- Save VTT files to transcripts/wallis-corpus/youtube/
- Convert VTT to markdown with YAML frontmatter (so embed.py can ingest it)

Source URLs in the markdown frontmatter include `&t=Ns` timestamp anchors so
the AI can cite back to the exact second of the video.

Polite: yt-dlp's default rate-limiting is reasonable. Resumable: skips files
that already exist.

Run: python scrape_youtube.py [--channel @HareeshWallis] [--limit 10]

Requires: yt-dlp (already installed at C:\\Users\\ferna\\AppData\\Roaming\\Python\\Python313\\Scripts\\yt-dlp.exe)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_CHANNEL = "https://www.youtube.com/@HareeshWallis"
OUT_DIR = Path(__file__).resolve().parent.parent.parent / "transcripts" / "wallis-corpus" / "youtube"
WORK_DIR = OUT_DIR / "_raw_vtt"


# ----------------------------------------------------------------------
# yt-dlp invocations
# ----------------------------------------------------------------------

def list_videos(channel_url: str, limit: int | None = None) -> list[dict]:
    """Use yt-dlp to dump the channel's video list as JSON."""
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--ignore-errors",
        channel_url,
    ]
    if limit:
        cmd.insert(-1, "--playlist-end")
        cmd.insert(-1, str(limit))
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    videos = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        try:
            v = json.loads(line)
            videos.append(v)
        except json.JSONDecodeError:
            continue
    if proc.returncode != 0 and not videos:
        print(f"  [error] yt-dlp listing failed: {proc.stderr[:500]}", file=sys.stderr)
    return videos


def download_captions(video_url: str, work_dir: Path) -> Path | None:
    """Download auto-captions for one video. Returns path to VTT file or None."""
    work_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "yt-dlp",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--sub-format", "vtt",
        "--skip-download",
        "--no-warnings",
        "--output", str(work_dir / "%(id)s.%(ext)s"),
        video_url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        return None
    # Look for the VTT file just produced
    vid_id = video_url.split("v=")[-1].split("&")[0] if "v=" in video_url else None
    if not vid_id:
        return None
    candidates = list(work_dir.glob(f"{vid_id}.en*.vtt"))
    return candidates[0] if candidates else None


# ----------------------------------------------------------------------
# VTT → markdown
# ----------------------------------------------------------------------

def parse_vtt(vtt_text: str) -> list[tuple[float, str]]:
    """Parse a VTT file, returning [(start_seconds, text), ...].

    Auto-captions tend to repeat lines. We dedupe consecutive duplicates.
    """
    # Strip header
    body = re.sub(r"^WEBVTT.*?\n\n", "", vtt_text, count=1, flags=re.S)
    blocks = re.split(r"\n\n+", body)
    out = []
    last_text = None
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip()]
        if not lines:
            continue
        # Find timestamp line "HH:MM:SS.mmm --> HH:MM:SS.mmm"
        ts_idx = None
        for i, line in enumerate(lines):
            if "-->" in line:
                ts_idx = i
                break
        if ts_idx is None:
            continue
        ts_line = lines[ts_idx]
        m = re.match(r"(\d+):(\d+):(\d+)\.\d+\s+-->", ts_line)
        if not m:
            continue
        start_seconds = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        text = " ".join(lines[ts_idx + 1:])
        # Strip in-text formatting tags like <c> </c> and <00:00:00.000>
        text = re.sub(r"<[^>]+>", "", text).strip()
        if not text or text == last_text:
            continue
        out.append((start_seconds, text))
        last_text = text
    return out


def vtt_to_markdown(vtt_path: Path, video_meta: dict) -> str:
    """Convert a VTT into a markdown file with YAML frontmatter and timestamped text."""
    vtt_text = vtt_path.read_text(encoding="utf-8", errors="replace")
    cues = parse_vtt(vtt_text)

    title = video_meta.get("title", "(untitled)")
    video_id = video_meta.get("id", vtt_path.stem.split(".")[0])
    upload_date = video_meta.get("upload_date") or "00000000"
    # YYYYMMDD → YYYY-MM-DD
    if len(upload_date) == 8 and upload_date.isdigit():
        date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    else:
        date_str = "unknown"
    duration_seconds = video_meta.get("duration") or 0
    base_url = f"https://www.youtube.com/watch?v={video_id}"

    parts = [
        "---",
        f"url: {base_url}",
        f"title: {title.replace(chr(10), ' ')!r}",
        f"date: {date_str}",
        f"video_id: {video_id}",
        f"duration_seconds: {duration_seconds}",
        f"source_type: youtube",
        f"author: Hareesh Wallis",
        "---",
        "",
        f"# {title}",
        "",
        f"YouTube: {base_url}",
        "",
    ]

    # Group cues into ~30-second windows; emit a paragraph per window with a
    # timestamp anchor URL.
    WINDOW_S = 30
    if not cues:
        parts.append("(no captions captured)")
        return "\n".join(parts) + "\n"
    window_start = cues[0][0] // WINDOW_S * WINDOW_S
    window_text: list[str] = []
    for ts, text in cues:
        if ts >= window_start + WINDOW_S:
            if window_text:
                anchor = f"{base_url}&t={int(window_start)}s"
                parts.append(f"**[{format_ts(window_start)}]({anchor})** {' '.join(window_text)}")
                parts.append("")
            window_start = ts // WINDOW_S * WINDOW_S
            window_text = []
        window_text.append(text)
    if window_text:
        anchor = f"{base_url}&t={int(window_start)}s"
        parts.append(f"**[{format_ts(window_start)}]({anchor})** {' '.join(window_text)}")

    return "\n".join(parts) + "\n"


def format_ts(seconds: float) -> str:
    s = int(seconds)
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def slugify(s: str, max_len: int = 60) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:max_len] or "untitled"


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", default=DEFAULT_CHANNEL, help="YouTube channel URL or @handle")
    parser.add_argument("--limit", type=int, default=None, help="max number of videos (for testing)")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Listing videos from {args.channel}...")
    videos = list_videos(args.channel, args.limit)
    print(f"  found {len(videos)} videos")
    if not videos:
        print("  nothing to do")
        return

    written = 0
    skipped = 0
    failed = 0
    for i, v in enumerate(videos, 1):
        title = v.get("title", "(untitled)")
        vid_id = v.get("id")
        if not vid_id:
            failed += 1
            continue
        upload_date = v.get("upload_date") or "00000000"
        date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}" if len(upload_date) == 8 else "unknown"
        out_filename = f"{date_str}-{slugify(title)}.md"
        out_path = OUT_DIR / out_filename
        if out_path.exists():
            print(f"  [{i:>3}/{len(videos)}] [skip] {out_filename}")
            skipped += 1
            continue

        print(f"  [{i:>3}/{len(videos)}] {title[:60]}...")
        url = f"https://www.youtube.com/watch?v={vid_id}"
        vtt_path = download_captions(url, WORK_DIR)
        if not vtt_path:
            print(f"    [warn] no captions for {vid_id}")
            failed += 1
            continue
        # Need full video metadata for date / duration. Re-fetch with --dump-single-json.
        proc = subprocess.run(
            ["yt-dlp", "--dump-single-json", "--no-warnings", "--skip-download", url],
            capture_output=True, text=True, encoding="utf-8",
        )
        try:
            full_meta = json.loads(proc.stdout)
        except Exception:
            full_meta = v

        md = vtt_to_markdown(vtt_path, full_meta)
        out_path.write_text(md, encoding="utf-8")
        written += 1
        print(f"    → {out_filename}")

    print()
    print(f"  written: {written}")
    print(f"  skipped: {skipped}")
    print(f"  failed:  {failed}")
    print()
    print(f"Output dir: {OUT_DIR}")
    print(f"Now run embed.py to chunk + embed + upload to R2.")


if __name__ == "__main__":
    main()
