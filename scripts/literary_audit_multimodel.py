"""
Multi-model literary audit of the Axiom v5 manuscript.

Sends the same persona + content to Claude, Gemini, and optionally OpenAI,
saves each response, and produces a side-by-side comparison. For literary
/ interpretive questions, disagreement between models is itself data.

Usage:
    python scripts/literary_audit_multimodel.py --persona whitman --chapter ch10b-the-ai-mirror
    python scripts/literary_audit_multimodel.py --persona critic --chapter all
    python scripts/literary_audit_multimodel.py --persona hesse --chapter ch00b-prelude-lilac-dance \
                                                 --models claude gemini

Personas (loaded from ~/.claude/commands/*.md):
    whitman, hesse, jung, critic, wallis, economist, msw

Models:
    claude (Opus 4.5 via Anthropic API)
    gemini (2.5 Pro via Google)
    openai (GPT-5 via OpenAI) — opt-in only

Output:
    research/literary-audit-<persona>-<chapter>-<date>.md
"""
import argparse
import datetime as dt
import os
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_DIR = Path.home() / '.claude' / 'commands'
CHAPTERS_DIR = REPO / 'books' / 'axiom-beneath-the-ground' / 'chapters' / 'v5'
RESEARCH_DIR = REPO / 'books' / 'axiom-beneath-the-ground' / 'research'
FULL_TEXT = REPO / 'docs' / 'axiom-v5-full-text.md'


# ────────── env loading ──────────

def load_env_files():
    """Load API keys from the various .env.local files across the user's repos."""
    env_paths = [
        Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\recursive-kids-stories-club\.env.local'),
        Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\recursive-eco\.env.local'),
        Path(r'C:\Users\ferna\OneDrive\Documentos\GitHub\recursive-eco\apps\flow\.env.local'),
    ]
    for p in env_paths:
        if not p.exists():
            continue
        for line in p.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            v = v.strip().strip('"\'')
            if v and not os.environ.get(k):
                os.environ[k] = v


# ────────── persona + content loading ──────────

def load_persona(name: str) -> str:
    path = SKILL_DIR / f'{name}.md'
    if not path.exists():
        sys.exit(f'No persona found at {path}. Available: '
                 f'{sorted(p.stem for p in SKILL_DIR.glob("*.md"))}')
    return path.read_text(encoding='utf-8')


def load_content(chapter: str) -> tuple[str, str]:
    """Return (label, text). chapter='all' loads the full book."""
    if chapter == 'all':
        if not FULL_TEXT.exists():
            sys.exit(f'Full text not found at {FULL_TEXT}. '
                     f'Run scripts/build-full-text.py or equivalent first.')
        return 'full-book', FULL_TEXT.read_text(encoding='utf-8')
    candidates = list(CHAPTERS_DIR.glob(f'{chapter}*.md'))
    if not candidates:
        sys.exit(f'No chapter matching {chapter!r} in {CHAPTERS_DIR}')
    path = candidates[0]
    return path.stem, path.read_text(encoding='utf-8')


# ────────── model callers ──────────

def call_claude(system: str, user: str) -> str:
    try:
        import anthropic
    except ImportError:
        return '[claude] anthropic SDK not installed. pip install anthropic'
    key = os.environ.get('ANTHROPIC_API_KEY')
    if not key:
        return '[claude] no ANTHROPIC_API_KEY in environment'
    client = anthropic.Anthropic(api_key=key)
    try:
        resp = client.messages.create(
            model='claude-opus-4-5',
            max_tokens=8192,
            system=system,
            messages=[{'role': 'user', 'content': user}],
        )
        return resp.content[0].text
    except Exception as e:
        return f'[claude] error: {e}'


def call_gemini(system: str, user: str) -> str:
    try:
        import google.generativeai as genai
    except ImportError:
        return '[gemini] google-generativeai SDK not installed. pip install google-generativeai'
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not key:
        return '[gemini] no GEMINI_API_KEY in environment'
    genai.configure(api_key=key)
    try:
        model = genai.GenerativeModel(
            'gemini-2.5-pro',
            system_instruction=system,
        )
        resp = model.generate_content(user, generation_config={'max_output_tokens': 8192})
        return resp.text
    except Exception as e:
        return f'[gemini] error: {e}'


def call_openai(system: str, user: str) -> str:
    try:
        import openai
    except ImportError:
        return '[openai] openai SDK not installed. pip install openai'
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        return '[openai] no OPENAI_API_KEY in environment'
    client = openai.OpenAI(api_key=key)
    try:
        resp = client.chat.completions.create(
            model='gpt-5',
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user},
            ],
            max_completion_tokens=8192,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f'[openai] error: {e}'


# ────────── main ──────────

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--persona', required=True,
                    help='Persona to invoke: whitman, hesse, jung, critic, wallis, economist, msw')
    ap.add_argument('--chapter', required=True,
                    help='Chapter slug (e.g. ch10b-the-ai-mirror) or "all" for the full book')
    ap.add_argument('--models', nargs='+', default=['claude', 'gemini'],
                    choices=['claude', 'gemini', 'openai'],
                    help='Which models to query. Default: claude + gemini.')
    ap.add_argument('--prompt', default=None,
                    help='Optional extra instruction appended to the user message. '
                         'Default: ask the persona to audit the given chapter.')
    args = ap.parse_args()

    load_env_files()

    persona_md = load_persona(args.persona)
    chapter_label, content = load_content(args.chapter)

    default_prompt = (
        f'Read the following chapter from the manuscript *The Axiom Beneath the Ground: '
        f'The Alignment Void* v5, and audit it in your voice as defined in the system '
        f'prompt above. Be specific. Cite passages. Offer 3-5 concrete revisions if you '
        f'see places the text could be stronger. '
        f'\n\n=== CHAPTER: {chapter_label} ===\n\n{content}'
    )
    user_msg = args.prompt or default_prompt
    if args.prompt:
        user_msg = f'{args.prompt}\n\n=== CHAPTER: {chapter_label} ===\n\n{content}'

    print(f'Persona: {args.persona}')
    print(f'Chapter: {chapter_label} ({len(content):,} chars)')
    print(f'Models:  {args.models}\n')

    results = {}
    callers = {'claude': call_claude, 'gemini': call_gemini, 'openai': call_openai}
    for m in args.models:
        print(f'[{m}] calling...')
        t0 = time.time()
        results[m] = callers[m](persona_md, user_msg)
        print(f'[{m}] done ({time.time() - t0:.1f}s, {len(results[m]):,} chars)')

    # Save comparison
    date = dt.date.today().isoformat()
    out_path = RESEARCH_DIR / f'literary-audit-{args.persona}-{chapter_label}-{date}.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f'# Multi-model audit — /{args.persona} on {chapter_label}\n\n')
        f.write(f'*Date: {date} · Models: {", ".join(args.models)}*\n\n')
        f.write(f'Content: {CHAPTERS_DIR / (chapter_label + ".md")} ({len(content):,} chars)\n\n')
        f.write('---\n\n')
        for m in args.models:
            f.write(f'## {m.upper()}\n\n')
            f.write(results[m])
            f.write('\n\n---\n\n')
    print(f'\nWrote: {out_path}')


if __name__ == '__main__':
    main()
