"""
Generate an Axiom v5 audiobook using gTTS (Google Translate TTS — free, no API key).

Produces one MP3 per chapter + a concatenated whole-book MP3 she can sync
to her phone. Voice quality is decent-not-great (not a neural model);
the advantage is zero setup cost and zero per-character fees. For a
higher-quality pass later, switch to Gemini 2.5 TTS or ElevenLabs.

Output:
    audiobook/axiom-v5/*.mp3

Usage:
    pip install gTTS
    python scripts/generate_axiom_audiobook_gtts.py          # all chapters
    python scripts/generate_axiom_audiobook_gtts.py --test   # just ch00 as pilot
"""
import os
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = REPO / 'books' / 'axiom-beneath-the-ground' / 'chapters' / 'v5'
OUT_DIR = REPO / 'audiobook' / 'axiom-v5'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Read SUMMARY-order
CHAPTER_ORDER = [
    'ch00-authors-note.md',
    'ch00a-prelude-first-encounter.md',
    'ch00b-prelude-lilac-dance.md',
    'ch01-playground.md',
    'ch01a-interlude-the-cracks.md',
    'ch02-deha.md',
    'ch03-citta.md',
    'ch04-prana.md',
    'ch04a-the-threshold.md',
    'ch05-shunya.md',
    'ch06-walking-out.md',
    'ch06a-where-the-maps-crack.md',
    'ch07-prana-returning.md',
    'ch08-citta-returning.md',
    'ch09-deha-returning.md',
    'ch10-vastu-returning.md',
    'ch10a-four-orthogonalities.md',
    'ch10b-the-ai-mirror.md',
    'ch10e-what-intelligence-was-never-doing.md',
    'ch10c-the-dance-not-the-human-dance.md',
    'ch10d-the-constructive-half.md',
    'ch10f-balance-from-differences.md',
    'ch10g-love-brings-accountability.md',
    'ch11-writing-desk.md',
    'ch12-composting.md',
    'ch13-the-right-size.md',
    'appendix-a-zusya.md',
]


def clean_for_tts(md: str) -> str:
    """Strip markdown syntax so the TTS doesn't read asterisks etc out loud."""
    # Remove front matter / separators
    md = re.sub(r'^---.*?---\s*', '', md, flags=re.DOTALL)
    # Remove headings (but keep the heading text)
    md = re.sub(r'^#{1,6}\s*', '', md, flags=re.MULTILINE)
    # Remove horizontal rules
    md = re.sub(r'^---+\s*$', '', md, flags=re.MULTILINE)
    # Remove footnote markers [^...] and footnote definitions
    md = re.sub(r'\[\^[^\]]+\]:.*?(?=\n\n|\Z)', '', md, flags=re.DOTALL)
    md = re.sub(r'\[\^[^\]]+\]', '', md)
    # Bold/italic
    md = re.sub(r'\*\*([^*]+)\*\*', r'\1', md)
    md = re.sub(r'\*([^*]+)\*', r'\1', md)
    # Links: keep text, drop URL
    md = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md)
    # Inline code
    md = re.sub(r'`([^`]+)`', r'\1', md)
    # Quote markers at start of line
    md = re.sub(r'^>\s*', '', md, flags=re.MULTILINE)
    # Collapse whitespace
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    return md


def chunk_text(text: str, max_chars: int = 4500) -> list[str]:
    """gTTS works best with <5000 char chunks. Split at paragraph boundaries."""
    chunks = []
    buf = ''
    for para in text.split('\n\n'):
        if len(buf) + len(para) + 2 > max_chars and buf:
            chunks.append(buf.strip())
            buf = para
        else:
            buf += ('\n\n' if buf else '') + para
    if buf:
        chunks.append(buf.strip())
    return chunks


def synth_chapter(filename: str, test_mode: bool = False) -> Path | None:
    """Generate MP3 for a single chapter."""
    from gtts import gTTS  # type: ignore
    path = CHAPTERS_DIR / filename
    if not path.exists():
        print(f'  [skip] {filename} not found')
        return None
    out_name = filename.replace('.md', '.mp3')
    out_path = OUT_DIR / out_name
    if out_path.exists() and not test_mode:
        print(f'  [skip] {out_name} already exists ({out_path.stat().st_size:,} bytes)')
        return out_path
    raw = path.read_text(encoding='utf-8')
    text = clean_for_tts(raw)
    words = len(text.split())
    print(f'  [gen] {filename}: {words:,} words, {len(text):,} chars')
    chunks = chunk_text(text)
    import tempfile
    temp_parts = []
    try:
        for i, chunk in enumerate(chunks):
            tmp = tempfile.NamedTemporaryFile(suffix=f'_{i}.mp3', delete=False)
            tmp.close()
            # Retry on transient failures
            last_err = None
            for attempt in range(5):
                try:
                    tts = gTTS(text=chunk, lang='en', slow=False)
                    tts.save(tmp.name)
                    last_err = None
                    break
                except Exception as e:
                    last_err = e
                    wait = 2 ** attempt
                    print(f'    chunk {i+1}/{len(chunks)} attempt {attempt+1} failed: {e} — retrying in {wait}s')
                    time.sleep(wait)
            if last_err:
                raise last_err
            temp_parts.append(tmp.name)
            time.sleep(1)  # politeness between chunks
            print(f'    chunk {i+1}/{len(chunks)}: {len(chunk):,} chars OK')
        # Concatenate
        with open(out_path, 'wb') as out:
            for p in temp_parts:
                with open(p, 'rb') as f:
                    out.write(f.read())
        size = out_path.stat().st_size
        print(f'  [ok] {out_name}: {size:,} bytes ({size/1024/1024:.1f} MB)')
        return out_path
    except Exception as e:
        print(f'  [FAIL] {filename}: {e}')
        return None
    finally:
        for p in temp_parts:
            try:
                os.unlink(p)
            except OSError:
                pass


def main():
    test = '--test' in sys.argv
    targets = [CHAPTER_ORDER[0]] if test else CHAPTER_ORDER
    print(f'Generating audiobook to {OUT_DIR}')
    print(f'Chapters: {len(targets)}')
    generated = []
    for ch in targets:
        p = synth_chapter(ch, test_mode=test)
        if p:
            generated.append(p)
    print(f'\nGenerated {len(generated)}/{len(targets)} chapter MP3s.')
    total_size = sum(p.stat().st_size for p in generated)
    print(f'Total size: {total_size/1024/1024:.1f} MB')
    if len(generated) == len(CHAPTER_ORDER):
        # Merge all into one
        merged = OUT_DIR / 'axiom-v5-complete.mp3'
        with open(merged, 'wb') as out:
            for p in generated:
                out.write(p.read_bytes())
        print(f'Whole-book: {merged} ({merged.stat().st_size/1024/1024:.1f} MB)')


if __name__ == '__main__':
    main()
