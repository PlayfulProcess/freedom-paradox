# Recursive.eco App Features — Book Integration Reference

**Source:** PlayfulProcess, April 2026
**Purpose:** Map platform features to book chapters as proof-of-concept examples

---

## 1. Kiosk Mode as Bounded Container
**Book connection:** "Rules that work target the container, not the content" (WA Ch10)
**Where it fits:** Ch33 (Reading Together)

Adding `?kiosk=true` to any viewer URL transforms it into a locked-down experience. CSS hides: site header/footer, sign-in modal, fork/copy/edit buttons, calendar, YouTube mode toggle. What stays: video player, playlist, print button, "Tell a Grown-Up" report button. The child cannot navigate out. The parent notice at the bottom shows the full URL (without ?kiosk) so caregivers can access admin features.

The same device that delivers infinite scroll becomes a bounded container through a single URL parameter. The technology isn't good or bad — the architecture determines whether it serves the child or the algorithm.

---

## 2. Fork System as Communal Tending
**Book connection:** "The I Ching has been continuously modified for three thousand years." (Grammars Ch10)
**Where it fits:** Ch37 (The Commons)

Any published grammar can be forked via `useForkGrammar.ts`. The fork creates a full copy in the user's account — they can modify interpretations, add cards, change images, restructure sections. The original remains untouched. Attribution tracks provenance. A forked tarot deck is still connected to its lineage but belongs to the person who modified it.

Implementation: `useForkGrammar({ sourceId, redirectTo: 'offer' })` → copies `document_data` from Supabase → redirects to editor. Works for both Supabase documents and GitHub-hosted community grammars.

---

## 3. "Tell a Grown-Up" as Immune Response
**Book connection:** Cell membrane model — the commons monitors itself
**Where it fits:** Ch33 (Reading Together) — kids.recursive.eco section

In kiosk mode, a large red "Tell a Grown-Up" button replaces the standard report system. It opens an anonymous modal: no email, no sign-in, no personal data — just an optional 500-character description and a submit button. The report goes to admins via `/api/notify-report` with the content ID, timestamp, and viewer URL. A green parent notice below the content shows the full (non-kiosk) URL for caregivers.

Two-tier reporting: Adults see a different modal with options to "Send an email for Administrators to analyze" OR "Unpublish immediately" (requires sign-in). The system recognizes different levels of authority.

Database: `content_reports` table stores: content_id, reason, details, reporter_id (null for anonymous), created_at.

---

## 4. AI Credits with Intentional Friction
**Book connection:** Gateway building — access WITH structure
**Where it fits:** Ch37 (The Commons)

AI features cost real credits (10x markup over provider costs). New users get $0.01 grant. Users explicitly choose between models (Gemini Flash, Gemini Pro, Claude Sonnet, Claude Opus). The friction is intentional: you must select a model, see the cost, confirm. No "auto-generate everything" button. About page: "There's intentional friction: the tools ask you to do your own thinking first."

Removing all friction (free unlimited AI) would produce a grammar factory — symbols collected without being sat with. The friction IS the container.

---

## 5. No Algorithm / Arrival-Based UX
**Book connection:** "A story consumed alone, without co-regulation, can traumatize rather than inoculate" (Grammars Ch03)
**Where it fits:** Ch33 (contrast with engagement-optimized platforms)

About page: "There's no algorithm deciding what you see. No notifications pulling you back. You arrive when you arrive." Library is manual search/filter by channel, author, type, status. No recommendation engine, no feed optimization, no engagement metrics, no notification system.

---

## 6. The Recursive Cycle (Contemplate → Journal → Create → Library)
**Book connection:** The practice loop IS the recursive public in action
**Where it fits:** Ch37 (The Commons) or conclusion

Visualized as 2x2 grid on About page:
- **Contemplate** — "sit with questions"
- **Journal** — "cast, draw, write"
- **Create** — "play, build, share"
- **Library** — "browse, fork, tend"

Tagline: "We shape grammars, and the grammars shape us."

---

## 7. Private Repo, Shared Format
**Book connection:** "Openness is not a value. It is a strategy." (FP Ch16)
**Where it fits:** Ch37 (The Commons)

Source code is private GitHub repo. Grammar JSON format is fully documented and portable. Books published CC BY-SA 4.0 in public repos. Courses are free. A cell membrane — selectively permeable.

---

## 8. Campfire Stories Written in 2 Claude Prompts
**Book connection:** AI as co-creator inside a human container
**Where it fits:** Ch33 (Reading Together)

10 bilingual bedtime stories from Akan, Aboriginal Australian, Haudenosaunee, Japanese, and Yoruba traditions. Written using Claude Code in two prompts. Human chose traditions, values, audience, age range, bilingual format. AI wrote stories within those constraints.

Source: https://github.com/PlayfulProcess/campfire-stories (CC BY-SA 4.0)

---

## 9. Courses as Recursive Practice
**Book connection:** The platform teaches people to build for the commons
**Where it fits:** Ch37 (The Commons)

8 free courses in 4 paths:
- **Getting Started:** Learn Recursive.eco → Vibe Coding 101 → Create Grammars with AI
- **Vibe Coding:** Build 3 AI Tools → Create Audiobooks
- **Vibe Writing:** Magic Stories for Kids → Open-Source Books with Claude Code
- **Creative AI:** Grammars from Books → Vibe Writing → Short Movies DIY → Family Songs

Every course produces something shareable — a grammar, a story, a book, a film, a song. The output goes into the Library. The courses themselves are grammars. The commons grows through use.

URL: https://recursive.eco/pages/courses/index.html

---

## kids.recursive.eco Specifics

- LIVE at kids.recursive.eco — COPPA-compliant kids story viewer (Next.js PWA)
- Source: https://github.com/PlayfulProcess/recursive-channels (private)
- Kiosk mode (`?kiosk=true`): hides ALL navigation, sign-in, fork/copy/edit buttons
- "Tell a Grown-Up" — large red button, anonymous report modal, zero personal data
- URL validation: kids-stories channel ONLY accepts recursive.eco playlists — all external URLs blocked
- Parent curates through their altar: `kids.recursive.eco/?altar={user-id}`
- Community layer: parents publish playlists to kids-stories Library channel; others browse, fork, modify
- Flagship content: Mister Rogers, Daniel Tiger, MINUSCULE
- Age-range channels planned (kids-0-2, kids-2-4, etc.) using Christakis framework
- PWA with TV casting guidance, fullscreen playback
- Complementary to Campfire Stories (text for reading, video for watching)

### Origin Story
YouTube was too addictive and there was no way to make playlists of kids content without the algorithm pulling children into infinite scroll. Then a creator's domain got hijacked — a safe link suddenly went somewhere harmful. That incident triggered the safety architecture: kiosk mode, URL validation, anonymous reporting.
