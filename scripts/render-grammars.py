#!/usr/bin/env python3
"""Convert Supabase grammar JSON exports into mdbook chapter markdown files."""
import json
import os
import re

def slugify(name):
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')[:60]

def extract_items(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    inner = json.loads(data[0]['text'])
    result = inner['result']
    match = re.search(r'<untrusted-data-[^>]+>\n(.*?)\n</untrusted-data', result, re.DOTALL)
    if not match:
        raise ValueError("Could not find JSON in untrusted-data wrapper")
    parsed = json.loads(match.group(1))
    return parsed[0]['items']

def render_card(card, ch_num):
    name = card.get('name', f'Card {ch_num}')
    category = card.get('category', '')
    sections = card.get('sections', {})
    metadata = card.get('metadata', {})

    lines = [f'# {name}', '']
    if category:
        lines += [f'*{category.title()}*', '']
    if isinstance(metadata, dict):
        tagline = metadata.get('tagline') or metadata.get('subtitle') or metadata.get('description', '')
        if tagline:
            lines += [f'> {tagline}', '']

    preferred = [
        'Research', 'Clinical', 'Spiritual', 'Practices', 'Rituals',
        'Songs & Playlists', 'Kids Version', 'Sci-Fi', 'Open Source', 'Cracks',
        'The Story', 'The Song', 'The Skill', 'For Parents', 'Try This', 'Reflection',
        'About', 'Overview', 'What It Is', 'How It Works', 'Colonial Pattern',
        'Decolonial Practice', 'Voices', 'Resources', 'For Readers',
        'Recursive Practice', 'The Tarot Journey', 'How to Use This Grammar',
    ]

    if not isinstance(sections, dict):
        return '\n'.join(lines)

    rendered = set()
    for key in preferred:
        if key in sections and sections[key] and str(sections[key]).strip():
            text = str(sections[key]).strip()
            text = re.sub(r'!\[.*?\]\(https://pub-[^\)]+\)', '', text)
            lines += [f'## {key}', '', text, '']
            rendered.add(key)

    for key, body in sections.items():
        if key not in rendered and body and str(body).strip():
            text = str(body).strip()
            text = re.sub(r'!\[.*?\]\(https://pub-[^\)]+\)', '', text)
            lines += [f'## {key}', '', text, '']

    return '\n'.join(lines)

def process(json_path, output_dir, slug):
    items = extract_items(json_path)
    os.makedirs(output_dir, exist_ok=True)
    filenames = []
    for i, card in enumerate(items):
        if not isinstance(card, dict):
            continue
        name = card.get('name', f'Card {i+1}')
        s = slugify(name)
        ch = str(i + 1).zfill(2)
        fname = f'ch{ch}-{s}.md'
        md = render_card(card, i + 1)
        with open(os.path.join(output_dir, fname), 'w') as f:
            f.write(md)
        filenames.append((fname, name))
        print(f'  {fname} ({len(md):,} chars)')
    return filenames

if __name__ == '__main__':
    base = '/root/.claude/projects/-home-user-freedom-paradox/47fe323f-b5c3-4466-85c3-c98090ada046/tool-results'
    books = '/home/user/freedom-paradox/books'

    grammars = [
        ('mcp-4f732e7e-b661-46af-9c5b-57d4daffd57f-execute_sql-1775068949046.txt',
         f'{books}/repair/chapters', 'repair'),
        ('mcp-4f732e7e-b661-46af-9c5b-57d4daffd57f-execute_sql-1775068950352.txt',
         f'{books}/dbt-wise-heart/chapters', 'dbt-wise-heart'),
        ('mcp-4f732e7e-b661-46af-9c5b-57d4daffd57f-execute_sql-1775068952214.txt',
         f'{books}/decolonization/chapters', 'decolonization'),
        ('mcp-4f732e7e-b661-46af-9c5b-57d4daffd57f-execute_sql-1775068953611.txt',
         f'{books}/social-working/chapters', 'social-working'),
    ]

    for json_file, output_dir, slug in grammars:
        print(f'\n=== {slug} ===')
        try:
            files = process(os.path.join(base, json_file), output_dir, slug)
            print(f'  Total: {len(files)} chapters')
        except Exception as e:
            print(f'  ERROR: {e}')
