# Luthien PBC Landing Page — Build Prompt

**Copy everything below this line into a fresh Claude Code session.**

---

**OBJECTIVE: Build a single-page static HTML landing page for Luthien.**

Create `~/luthien-pbc-site/index.html` — one file, no frameworks, no build tools. Under 3000 lines.

Luthien is an open-source proxy that enforces rules on AI coding agents (Claude Code, Codex, Cursor). Target audience: senior engineers who use AI agents 40+ hrs/week and are frustrated by agents ignoring instructions, scope-creeping, and doing dangerous things. Secondary: security leads who need to prevent these failures across a team. Tertiary: PMs who forward the link to their engineers.

---

## DESIGN SYSTEM

**Typography:**
- Headings: `Syne` (700) via Google Fonts. Fallback: system sans-serif.
- Body: `Inter` (400, 500) via Google Fonts. Fallback: system sans-serif.
- Code: `JetBrains Mono` (400) via Google Fonts. Fallback: monospace.

**Colors:**
```
--bg:           #09090b    /* near-black background */
--surface:      #18181b    /* cards, code blocks */
--surface-raised: #27272a  /* hover states, borders */
--text:         #fafafa    /* primary text */
--text-secondary: #a1a1aa  /* secondary text */
--text-muted:   #71717a    /* muted, footnotes */
--red:          #ef4444    /* danger / sus */
--red-glow:     rgba(239, 68, 68, 0.15)
--amber:        #f59e0b    /* warning / rules */
--amber-glow:   rgba(245, 158, 11, 0.15)
--blue:         #58a6ff    /* info / intent */
--green:        #4ade80    /* success / CTA */
--green-glow:   rgba(74, 222, 128, 0.15)
```

**Layout:** Max content width 960px centered. Sections get 80-120px vertical padding. Horizontal rules between sections: 1px `--surface-raised`. CSS Grid for grids/tables, Flexbox for simpler layouts.

**Code blocks:** Prism.js (CDN, tomorrow dark theme). Background `--surface`, 1px `--surface-raised` border, 16px padding, 8px radius. Small language label in top-right corner.

**Navigation:** Fixed top bar, 48px height, `--bg` with `backdrop-filter: blur(8px)` and `rgba(9,9,11,0.8)`. Left: "luthien" in JetBrains Mono lowercase, green. Right: anchor links in text-secondary. Smooth scroll with `scroll-margin-top: 64px` on targets.

**Responsive:** Breakpoints at 768px and 480px. Failure grid collapses to single column. Code blocks get `overflow-x: auto`. Properties table scrolls horizontally. Timeline stacks vertically.

**Aesthetic inspiration:** Fireship.io (energy, cynicism, density), Linear.app (dark, clean, generous whitespace), Vercel (minimal nav/footer, scrolling rhythm). Do NOT borrow: gradients, animated backgrounds, parallax, product screenshots in browser frames.

---

## VOICE

Write like a senior engineer explaining to another senior engineer why they built this. Dry, knowing, competent. Conference hallway conversation, not keynote stage.

- YES: "Your agent tried `rm -rf /`. Luthien caught it."
- YES: "5 lines of Python. That's the whole policy."
- NO: "Supercharge your AI workflow with next-generation..."
- NO: Any use of "revolutionary", "game-changing", "seamless", "empower", "unlock", "cutting-edge"

Every sentence must pass: would a staff engineer at a Series B startup read this without rolling their eyes?

---

## SECTIONS (9 total, in order)

### SECTION 1: HERO

Centered text. No images.

```
[small caps, text-muted, JetBrains Mono, letter-spacing: 0.1em]
OPEN SOURCE AI CONTROL PROXY

[h1, Syne 700, 48-56px, white]
Assume Nothing.

[subtitle, Inter 400, 20px, text-secondary, max-width: 600px]
AI coding agents ignore your rules, scope-creep your PRs, and occasionally
try to delete your filesystem. Luthien is a proxy that sits between your
agent and the LLM — enforcing the rules you set, catching the ones you
didn't think to set.

[Two CTAs]
[Green outline button] Quick Start ->    (anchor to #quick-start)
[Text link, text-secondary] View on GitHub ->  (https://github.com/LuthienResearch/luthien-proxy)

[Trust badge row, small, text-muted]
Open source · Apache 2.0  |  Works with Claude Code, Cursor, Codex  |  Inspired by Redwood Research's AI Control agenda
```

---

### SECTION 2: THE PROBLEM — FAILURE MODE GRID

3-column CSS Grid. Each column is a failure category with a color-coded header.

**Section heading:**
```
[h2, Syne 700]
You've seen this before.

[subtitle, text-secondary]
204 documented frustrations across 6 data sources. These are the patterns.
```

**Column headers:**

| Column | Label | Color |
|--------|-------|-------|
| 1 | SUS: Dangerous | Red |
| 2 | RULES: Ignored your claude.md | Amber |
| 3 | PROMPT: Didn't do what you asked | Blue |

**Cards (each card: colored left border, ~40 words max):**

SUS column (red):
- "Deleted failing tests to make the suite green. 'All tests passing!'"
- "Ran `rm -rf /` claiming it was 'cleaning up test files.'"
- "Committed `.env` with hardcoded API keys to a public repo."
- "Spawned 36 parallel subagents. Burned through $200 in API credits."

RULES column (amber):
- "claude.md says 'use uv, not pip.' Agent ran `pip install`. Every. Single. Time."
- "CLAUDE.md says 'atomic commits.' You got a 2,400-line PR touching 15 files."
- "'Never modify package.json.' Agent modified it and didn't mention it."

PROMPT column (blue):
- "Asked to fix the login bug. Got the login bug plus a 'refactored' auth system."
- "Asked for a unit test. Got a unit test, two integration tests, and a new testing framework."
- "'Done! I've implemented the feature.' Core logic is a TODO comment."

**Punchline (below the grid, text-secondary, italic):**
> Both Claude Code and Codex self-rate these failure modes at 9/10 persistence. They know they do this. They can't stop themselves.

---

### SECTION 3: THREE-LAYER MODEL (centerpiece)

**This is the intellectual core of the page.** Show the mental model that organizes all those problems.

**Section heading:**
```
[h2] Three layers. One proxy.
[subtitle] Every agent failure maps to one of these layers. Luthien enforces all three.
```

**Three stacked horizontal bars** (full content width, rendered as styled divs — NOT an image):

```
Layer 1 (Red left border + red-glow bg):
  sus             "Did it try something dangerous or stupid?"        -> BLOCK
  [small text]    Luthien-set. Non-overridable safety floor.

Layer 2 (Amber left border + amber-glow bg):
  claude.md       "Did it follow the rules you already wrote?"      -> FLAG or BLOCK
  [small text]    Per-project. You write the rules.

Layer 3 (Blue left border + blue-glow bg):
  prompt          "Did it do what you asked?"                       -> FLAG
  [small text]    Per-turn. Even after /compact, Luthien remembers.
```

Each bar: ~80px tall. Layer name in JetBrains Mono bold left. Question in Inter middle. Action as pill badge right.

**Properties table (below bars, CSS Grid):**

| Property | sus | claude.md | prompt |
|----------|-----|-----------|--------|
| Who sets it | Luthien | You | You |
| Scope | Global | Per-project | Per-turn |
| Override | No | Yes | Yes |
| Violation = | Dangerous | Disobedient | Wrong |
| Action | Block | Flag or Block | Flag |

Style column headers with respective colors. Clean rows, subtle dividers.

---

### SECTION 4: WHERE LUTHIEN SITS

**Section heading:**
```
[h2] Catches problems before they exist.
```

**Timeline (horizontal on desktop, vertical on mobile):**

| When | What | Catches |
|------|------|---------|
| **At generation** | **Luthien** (highlighted, green) | Intercepts every request + response. Enforces rules. Logs full history. |
| At push / PR | CI/CD, CodeRabbit, human review | Tests, build failures, code review |
| In production | Monitoring, alerting | Runtime errors, incidents |

**Punchline:**
> Everything after Luthien catches problems *after they're already in your code.* Luthien catches them *before they exist.* Earlier is cheaper. Memory is consistency.

**Two-column callout (side by side on desktop, stacked on mobile):**

Left card (red-tinted):
```
--dangerously-skip-permissions
No CI, no PR review, yolo to main.
Luthien is your only safety net.
The sus layer alone saves you from the Replit incident.
```

Right card (green-tinted):
```
Mature pipeline
Luthien sits upstream of your PR.
It notifies you the moment Claude Code does something sus —
so you stay in flow instead of context-switching to review a bad diff later.
```

---

### SECTION 5: QUICK START

```
[h2] Running in 5 minutes.
```

**Step 1: Clone and configure**
```bash
git clone https://github.com/LuthienResearch/luthien-proxy
cd luthien-proxy
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

**Step 2: Start**
```bash
docker compose up -d
```

**Step 3: Point Claude Code at it**
```bash
export ANTHROPIC_BASE_URL=http://localhost:8000/v1
export ANTHROPIC_API_KEY=sk-luthien-dev-key
claude
```

**What you get:**
- Gateway at localhost:8000
- Activity monitor at localhost:8000/activity/monitor
- Policy config at localhost:8000/policy-config
- PostgreSQL + Redis, fully configured

```
[text-muted]
Works with Claude Code, Codex, Cursor — anything that speaks Anthropic or OpenAI API.
```

---

### SECTION 6: WRITE YOUR OWN POLICY

```
[h2] Your rules. Enforced. 5 lines of Python.
```

**Code block (with Prism.js Python highlighting):**
```python
from luthien_proxy.policies.simple_judge_policy import SimpleJudgePolicy

class MyPolicy(SimpleJudgePolicy):
    RULES = [
        "Never allow 'rm -rf' commands",
        "Never delete or skip existing tests",
        "Always use uv, never pip",
        "Block requests to delete production data",
        "Require docstrings on all public functions",
    ]
```

**Below:**
```
[text-secondary]
Write rules in plain English. An LLM judge evaluates them against every request and response.
Policies are hot-reloadable at localhost:8000/policy-config — no restart needed.
```

---

### SECTION 7: BUILT ON RESEARCH

```
[h2] Built on research, not vibes.
```

Brief paragraph:
> Luthien implements the AI Control agenda from Redwood Research — the idea that you can get useful work from AI systems you don't fully trust by structuring oversight into the execution path, not bolting it on after.
>
> Apache 2.0 open-source project backed by a 501(c)(3) nonprofit focused on AI safety.

**Links (small, footnote-style):**
- [Redwood's AI Control landing page](https://www.redwoodresearch.org/research/ai-control)
- [AI Safety Atlas: Control](https://ai-safety-atlas.com/chapters/03/03#03)
- [Original paper (arXiv)](https://arxiv.org/abs/2312.06942)

---

### SECTION 8: CTA

```
[h2, Syne 700, 36px]
Open source. Early. Come build with us.

[subtitle, text-secondary, max-width: 600px]
We're looking for design partners — senior engineers using AI coding tools
40+ hours per week. Luthien is free for individual developers, and we plan
to keep it that way.

[Large green filled button]
Get Started on GitHub ->
(https://github.com/LuthienResearch/luthien-proxy)

[Text link below]
Schedule a call ->
(https://calendar.app.google/CDq4LTpKj966cuPx8)

[Small text]
contact@luthienresearch.org
```

---

### SECTION 9: FOOTER

Minimal. Single row, centered, text-muted.

```
Luthien Research · Apache 2.0 · GitHub · Donate · Contact
```

Links: luthienresearch.org, GitHub repo, https://manifund.org/projects/luthien, contact@luthienresearch.org

---

## TECHNICAL CONSTRAINTS

1. **Single file.** Everything in `index.html`. CSS in `<style>`, JS in `<script>` at bottom.
2. **CDN only:** Google Fonts (Syne, Inter, JetBrains Mono with `display=swap` + preconnect), Prism.js (async, defer).
3. **No JS for layout.** JS only for: Prism highlighting, mobile nav toggle. Page fully readable with JS disabled.
4. **Performance:** No images. Zero image requests. Page weight < 100KB excluding fonts.
5. **Accessibility:** Semantic HTML (`nav`, `main`, `section`, `footer`), proper heading hierarchy, keyboard accessible, `prefers-reduced-motion` disables smooth scroll.
6. **Meta tags:**
```html
<title>Luthien -- AI Control Proxy for Coding Agents</title>
<meta name="description" content="Open-source proxy that enforces rules on AI coding agents. Catches dangerous behavior, enforces your claude.md, and keeps agents on task.">
<meta property="og:title" content="Luthien -- Assume Nothing">
<meta property="og:description" content="Your AI agent ignored your rules again. Luthien makes sure it won't.">
<meta property="og:type" content="website">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

## ANTI-PATTERNS TO AVOID

1. **Wall of text.** No paragraph > 3 sentences. Break up with code blocks or visual elements.
2. **Over-engineered CSS.** No animations on load. No gradient text. No parallax. Only transitions: button hover (150ms) and smooth scroll.
3. **Code blocks too long.** Quick start: 4-6 lines each. Policy: under 10 lines.
4. **Diagram breaks on mobile.** Build the three-layer diagram as styled `<div>` elements with Flexbox. NOT: SVG, canvas, ASCII art, complex CSS shapes. Test at 960px, 768px, 375px.
5. **Font loading flash.** Use `display=swap` in Google Fonts URL.
6. **Forgot `scroll-margin-top`.** Anchor targets need `scroll-margin-top: 64px`.
7. **Failure grid too uniform.** Three columns should feel different via color coding. Red = dangerous. Amber = frustrating. Blue = relatable.
8. **Placeholder text.** No "Lorem ipsum" or "[Your text here]" anywhere. All copy above is final.
9. **Too many font weights.** Exactly: Syne 700, Inter 400, Inter 500, JetBrains Mono 400.
10. **Marketing slop.** Read every sentence aloud. If it sounds like a SaaS landing page generator wrote it, rewrite it.

---

## FINAL CHECK

Before delivering:
- [ ] Every section has an anchor ID linked from nav
- [ ] Three-layer diagram renders at 960px, 768px, 375px
- [ ] All code blocks have Prism.js language classes
- [ ] Page reads in under 2 minutes of scrolling
- [ ] No marketing buzzwords anywhere
- [ ] All links correct (GitHub, calendar, manifund, contact email)
- [ ] Google Fonts load with preconnect + display=swap
- [ ] `prefers-reduced-motion` handled
- [ ] Total line count under 3000

Build the complete `~/luthien-pbc-site/index.html` now.
