"""
Upload the generated Axiom v5 audiobook MP3s to Cloudflare R2.

Reads credentials from recursive-kids-stories-club/.env.local (they live
there per the repo's memory). Uploads each MP3 to the grammar-illustrations
R2 bucket under audiobook/axiom-v5/ and prints the public URLs for the
landing page.
"""
import os
import sys
from pathlib import Path

# Load env
env_path = Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\recursive-kids-stories-club\.env.local')
for line in env_path.read_text(encoding='utf-8').splitlines():
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    if '=' not in line:
        continue
    k, v = line.split('=', 1)
    v = v.strip().strip('"\'')
    if v and not os.environ.get(k):
        os.environ[k] = v

ACCOUNT_ID = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
ACCESS_KEY = os.environ.get('R2_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('R2_SECRET_ACCESS_KEY')
BUCKET = os.environ.get('R2_BUCKET_NAME')
PUBLIC_URL = os.environ.get('R2_PUBLIC_URL', '').rstrip('/')

print(f'Account: {ACCOUNT_ID[:8] if ACCOUNT_ID else None}...')
print(f'Bucket: {BUCKET}')
print(f'Public URL: {PUBLIC_URL}')

if not all([ACCOUNT_ID, ACCESS_KEY, SECRET_KEY, BUCKET, PUBLIC_URL]):
    print('Missing R2 creds; check .env.local')
    sys.exit(1)

import boto3
s3 = boto3.client(
    's3',
    endpoint_url=f'https://{ACCOUNT_ID}.r2.cloudflarestorage.com',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='auto',
)

AUDIO_DIR = Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\book-repo\audiobook\axiom-v5')
mp3s = sorted(AUDIO_DIR.glob('*.mp3'))
print(f'\nFound {len(mp3s)} MP3s\n')

CHAPTER_LABELS = {
    'ch00-authors-note': "Author's Note",
    'ch00a-prelude-first-encounter': 'Prelude: The First Encounter',
    'ch00b-prelude-lilac-dance': 'Prelude: The Lilac Dance',
    'ch01-playground': 'Chapter 1: Playground',
    'ch01a-interlude-the-cracks': 'Interlude: The Cracks',
    'ch02-deha': 'Chapter 2: Deha',
    'ch03-citta': 'Chapter 3: Citta',
    'ch04-prana': 'Chapter 4: Prāṇa',
    'ch04a-the-threshold': 'Chapter 4a: The Threshold',
}

results = []
for mp3 in mp3s:
    stem = mp3.stem
    key = f'audiobook/axiom-v5/{mp3.name}'
    size_mb = mp3.stat().st_size / 1024 / 1024
    print(f'Uploading {mp3.name} ({size_mb:.1f} MB) -> r2://{BUCKET}/{key}')
    try:
        s3.upload_file(
            str(mp3), BUCKET, key,
            ExtraArgs={'ContentType': 'audio/mpeg'},
        )
        url = f'{PUBLIC_URL}/{key}'
        label = CHAPTER_LABELS.get(stem, stem)
        results.append((stem, label, url, size_mb))
        print(f'  [ok] {url}')
    except Exception as e:
        print(f'  [FAIL] {e}')

print(f'\n=== Uploaded {len(results)} files ===\n')
for stem, label, url, size_mb in results:
    print(f'{label:<45s} {size_mb:>5.1f} MB  {url}')

# Emit a JSON manifest for the landing page
import json
manifest = {
    'book': 'The Axiom Beneath the Ground: The Alignment Void',
    'version': 'v5',
    'source': 'gTTS (Google Translate TTS)',
    'note': 'First 9 of 27 chapters — rest pending (rate-limit hit). Quality is decent-not-great TTS; author may redo with ElevenLabs or Gemini for final.',
    'chapters': [
        {'id': stem, 'label': label, 'url': url, 'size_mb': round(size_mb, 1)}
        for stem, label, url, size_mb in results
    ],
}
out_path = Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\book-repo\docs\audiobook-axiom-v5-manifest.json')
out_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'\nManifest: {out_path}')
