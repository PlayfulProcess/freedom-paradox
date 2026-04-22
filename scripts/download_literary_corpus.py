"""
Download PD texts for the /whitman, /hesse agents' RAG corpus.
Jung stays paraphrase-only (most of his core work is still copyrighted).

Sources: Project Gutenberg (primary), Wikisource (backup), Internet Archive
controlled lending for edge cases.
"""
import os
import time
import urllib.request
from pathlib import Path

UA = ('book-repo-literary-corpus-download/1.0 '
      '(https://recursive.eco contact: pp@playfulprocess.com)')
BASE = Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\book-repo\transcripts\literary-corpus')

TARGETS = [
    # ─────── Walt Whitman (d. 1892 — all PD) ───────
    ('whitman/leaves-of-grass-1855.txt',
     'https://www.gutenberg.org/cache/epub/1322/pg1322.txt',
     'Leaves of Grass (Deathbed ed. 1891-92, published text)'),
    ('whitman/specimen-days.txt',
     'https://www.gutenberg.org/cache/epub/8813/pg8813.txt',
     'Specimen Days (1882) — war memoir + nature journal'),
    ('whitman/complete-prose.txt',
     'https://www.gutenberg.org/cache/epub/8801/pg8801.txt',
     'Complete Prose Works of Walt Whitman'),

    # ─────── Hermann Hesse (d. 1962; PD works are pre-1929 US) ───────
    ('hesse/siddhartha.txt',
     'https://www.gutenberg.org/cache/epub/2500/pg2500.txt',
     'Siddhartha (1922 German, trans. Gunther Olesch et al.)'),
    ('hesse/demian.txt',
     'https://www.gutenberg.org/cache/epub/41907/pg41907.txt',
     'Demian (1919) — Gutenberg English translation'),
    # Steppenwolf: checking — may not be on Gutenberg US
    ('hesse/steppenwolf.txt',
     'https://www.gutenberg.org/cache/epub/65559/pg65559.txt',
     'Steppenwolf (1927) if available'),
]


def download(local_rel, url, desc):
    path = BASE / local_rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 1000:
        print(f'  [skip] {local_rel} ({path.stat().st_size:,} bytes)')
        return True
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        path.write_bytes(data)
        print(f'  [ok]   {local_rel} ({len(data):,} bytes) — {desc}')
        time.sleep(0.5)
        return True
    except Exception as e:
        print(f'  [FAIL] {local_rel}: {e}')
        return False


print(f'Downloading to: {BASE}\n')
ok = 0
for rel, url, desc in TARGETS:
    if download(rel, url, desc):
        ok += 1

print(f'\n{ok}/{len(TARGETS)} downloaded')

# README for the corpus
readme = BASE / 'README.md'
readme.write_text('''# Literary Corpus for `/whitman`, `/hesse` agents

Local-only corpus (gitignored per CLAUDE.md). The `/whitman` and `/hesse`
slash-command agents search these files before answering.

## Copyright

All files here are public domain in the US based on pre-1929 publication
date and/or creator death date > 70 years ago. Sources: Project Gutenberg
(primary), Wikisource (backup).

- **Whitman**: d. 1892; entire output PD worldwide
- **Hesse (PD subset only)**: pre-1929 novels — Siddhartha (1922), Demian
  (1919), Steppenwolf (1927 — verify US status). Later works (Narcissus &
  Goldmund 1930, Journey to the East 1932, Glass Bead Game 1943) remain
  copyrighted in the US and are NOT in this corpus. The `/hesse` agent
  should paraphrase those from training knowledge with attribution, never
  claim to quote directly.
- **Jung**: no corpus stored. Most of Collected Works (Bollingen, 1953+)
  and *Memories, Dreams, Reflections* (1962) are still copyrighted. The
  `/jung` agent works paraphrase-only from training knowledge with clear
  attribution to Volumes/years. Pre-1929 Jung translations (Hinkle 1916)
  could be added here later if needed.

## How the agents use this

The skill files in `~/.claude/commands/whitman.md` and `~/.claude/commands/hesse.md`
instruct the agent to `Grep` these files for specific passages before
answering. For semantic queries, the agent reads the plain-text file
directly. Future: Whitman could be upgraded to Cloudflare AI Search (same
pattern as the Wallis agent's `wallis-corpus`) if semantic retrieval
becomes important.
''', encoding='utf-8')
print(f'\nWrote {readme}')
