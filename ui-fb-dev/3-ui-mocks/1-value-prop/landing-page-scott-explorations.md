# Landing Page — Scott's Explorations

Detailed iteration log for prototypes only Scott reviewed. For versions shown to users/Jai (with their feedback and permalinks), see [requirements](../2-versions-requirements/1-value-prop-requirements-live.md).

---

## Round 5: Direction shift (Feb 21–22)

Internal explorations — not shown externally.

| Version | Date | What | Link | Scott Notes |
|---------|------|------|------|-------------|
| **v8: "Assume Nothing" spec** | Feb 21 | Major pivot. Three-layer model (sus/claude.md/prompt). Cynical senior-engineer voice. 9-section landing page spec. | [spec](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-21_luthien-pbc-site-prompt.md) | Build spec brainstormed from all prior feedback. |
| **v9: eng-1st-principles** | Feb 22 | Compact HTML "How It Works" — agent→Luthien→LLM flow, 3-layer enforcement. ~200 lines. | [spec](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22_eng-1st-principles/luthien-landing-page-spec.md) · [HTML](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22_eng-1st-principles/luthien-v3.html) | Built on other machine. |
| **v10: PBC landing page** | Feb 22 | v3-detailed (24KB, 9 sections) → v5-simplified (12KB, 5 sections, 3 user quotes). | [detailed](https://github.com/LuthienResearch/luthien-org/blob/2bed8ec/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22-pbc-landing-page/v3-detailed.html) · [simplified](https://github.com/LuthienResearch/luthien-org/blob/2bed8ec/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22-pbc-landing-page/v5-simplified.html) | Applied Musk's 5-step. user quotes > bullet lists, plain-English diagram > taxonomy labels. |

---

## Round 6: Humor prototypes — iteration log (Feb 24)

Base prototypes (6.1, 6.2) documented in [requirements Round 4/4b](../2-versions-requirements/1-value-prop-requirements-live.md#round-4--humorrelatability-prototypes-feb-24). Below is the detailed iteration log from 6.3 onward.

### 6.3 — "Suspicious stuff" + parrot card ([`b0c6f7d`](https://github.com/LuthienResearch/luthien-org/commit/b0c6f7d))

- Changed wording to "suspicious stuff" everywhere
- Deleted "Real, documented..." subtitle
- Added parrot/test-cheating card (GitHub #7074)

**Scott:** Liked #7074 card but wanted it shown as "Closed as not planned" to play up the irony. Also: remove all non-Claude-Code references.

### 6.4 — Visual question flow ([`88990d3`](https://github.com/LuthienResearch/luthien-org/commit/88990d3))

- Replaced text-heavy architecture with visual question-based flow ("Did it do what you asked?" → "Did it follow your rules?" → "Did it do something suspicious?")
- Added example chips, emoji icons to proxy flow
- Removed category tags from incident cards

**Scott:** Direction approved. Keep iterating.

### 6.5 — Gold quotes expansion + infinite scroll

- Expanded from 11 to 36 quotes in carousels (pulled from Grok research, frustrations database)
- Added 18 new incident cards to incidents.html
- Added IntersectionObserver infinite scroll to incidents page

**Scott:** Good. Keep going.

### 6.6 — "Weird stuff" + #7074 closed as not planned

- Changed "suspicious stuff" → "weird stuff" on landing pages
- Changed incidents title to "weird and suspicious stuff"
- Made #7074 card show "Closed as not planned" with gray circle-slash icon

**Scott:** Approved.

### 6.7 — Claude-Code-only focus

- Removed ALL non-Claude-Code product references: Replit (2), Claude Cowork (1), Cursor (5), OpenClaw (1), Devin (1), Copilot (1)
- Removed Replit + Cursor/Cyrus quotes from all 3 carousel prototypes
- Down to 24 incidents, 34 carousel quotes

**Scott:** "We're only focused on Claude Code here." Approved.

### 6.8 — Platform source logos

- Added GitHub octocat SVG, HN orange "Y" badge, Twitter/X logo, "MEDIUM" and "THE REGISTER" text badges

**Scott:** "Instead of BLOG say 'medium' or substack." Then: "use medium logo" — wanted actual Medium mark SVG.

### 6.9 — Medium mark + condensed spacing

- Replaced globe+BLOG with Medium mark SVG (three ellipses path)
- Condensed top spacing: `padding-top` 120px→48px, margins 48px→24px and 32px→16px
- Luthien value prop now above the fold on desktop

**Scott:** "Condense; too much blank space at the top; Luthien value prop should be above the fold."

### 6.10 — CEO/agents meme (text version)

- Added protest chant meme as text-based interstitial

**Scott:** "No, search online for the best memes as in GIFs or static images (not text)."

### 6.11 — Side-by-side layout + image meme

- Flex row: quotes carousel (left) + meme image (right)
- Imgflip "What Do We Want" template with CSS text overlay

**Scott:** Image didn't render (imgflip blocking hotlinks). "Looks like shit." Also: "add 'meanwhile...' header above the CEO meme."

### 6.12 — High-res meme from LinkedIn + "meanwhile..."

- Downloaded 1024x1536 CEO/AI meme from LinkedIn (John Hansman post)
- Added "meanwhile..." header, CSS crop to hide baked-in header

**Scott:** "Meanwhile more prominent. Fix card scroller to dynamically adjust to window size. Meme right aligned with very little margin." Also: "remove AI CONFUSION IN A NUTSHELL."

### 6.13 — Layout polish

- "meanwhile..." bigger, gap reduced, cards fill available width, responsive stacking

**Scott:** "Add a very minimal top nav."

### 6.14 — Top nav bar

- Frosted glass nav, blue L logo + "Luthien" wordmark, Problem | Solution | Architecture | GitHub | "Book a Call"

**Scott:** 5 refinements: LUTHIEN wordmark formatting, problem active by default, delete solution, github logo not text, remove blue L, lowercase labels.

### 6.15 — Nav refinements + scroll spy

- LUTHIEN wordmark only, "problem" and "architecture" lowercase, GitHub octocat, scroll spy

**Scott:** "Make cards smaller and stack. If narrow, boxes above CEO meme. CTA only at end and in top nav."

### 6.16 — Stacked vertical cards + CTA cleanup (CURRENT — a2 only)

- Vertical scrollable feed, compact stacked cards, removed carousel controls, shuffled on load
- CTA only in: top nav + end-of-page

**Scott:** Pending review. Only applied to a2 so far.

---

## Files reference

All prototypes: [`2026-02-24_humor-prototypes/`](https://github.com/LuthienResearch/luthien-org/tree/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes)

| File | Status | Link |
|------|--------|------|
| `a2-escalation.html` | **Most current** (all 6.16 changes) | [view](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/a2-escalation.html) |
| `b2-parrot.html` | Partial (6.14 + meme, NOT stacked cards) | [view](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/b2-parrot.html) |
| `c2-hr.html` | Partial (6.14 + meme, NOT stacked cards) | [view](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/c2-hr.html) |
| `incidents.html` | Updated through 6.8 | [view](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/incidents.html) |

---

## Round 7: Dot visualization + section labels (Feb 24, session 2)

Explored adding a visual representation of the 124-entry frustrations/incidents database as colored dots, and section labels for visual hierarchy.

### 7.1 — Section labels

- Added "the problem" label above carousel section
- Added "architecture" label above how-it-works section
- Monospace, tiny, uppercase, muted gray (`#3f3f46`)

**Scott:** Approved. Committed.

### 7.2 — Dot visualization mockup v1

Mockup at `/tmp/dot-viz-mockup.html` — 5 variants using all 124 entries as colored dots:
- A: 6px dots, color-coded by failure category
- B: 4px dense cluster
- C: 3px galaxy constellation
- D: Stat "124" + dot field side by side
- E: Dots inline with text

**Scott:** "I like version A."

### 7.3 — Pairing dots with carousel v1

6 options for pairing dots with the "see more" link. All had both carousel nav dots AND data dots.

**Scott:** "Delete some parts. We shouldn't have two sets of dots." (Musk step 2: delete the part.)

### 7.4 — One set of dots v2

6 options removing carousel nav dots entirely:
- A: Dots replace carousel nav, card auto-rotates
- B: No carousel at all, just 124 + dot field with hover tooltips
- C: One static card + dot field
- D: Dots first, card second (inverted hierarchy)
- E: Compact dot strip as section divider
- F: Dots only, zero words, hover tooltips

**Scott:** "I liked the autoscroll with the arrows, so keep that. Play around with the dots. Don't think we need to show all of them."

### 7.5 — Fewer dots, keep carousel v3

6 options keeping carousel arrows, showing fewer dots:
- A: ~20 dots replacing nav, trailing fade
- B: One dot per category (11 dots)
- C: "124" count + small cluster
- D: Proportional dot bar — thin ticks sorted by category size
- E: Three dots + ellipsis (maximum restraint)
- F: Dot arc beneath card

**Scott:** "I like D." And: "124 number doesn't matter; reader just needs to think 'wow that's a lot'."

### 7.6 — Labels under dot bar

3 variants of D with category labels:
1. Labels below each segment (always visible)
2. Staggered labels (alternating offset)
3. Hover labels (taller ticks, labels on hover only)

**Scott:** "Words below dots are too crowded. Just do a hover thing."

### 7.7 — Round dots (option C) in two rows

3 variants with round dots stacked in two rows, fading cutoff:
- A: Two full rows, hard fade cutoff right edge
- B: Two rows, second row fades progressively
- C: Two rows, second row is shorter

**Scott:** "I don't like any of those. The dot that corresponds to the current card should be bigger. Dots and 'see more' should be centered."

### 7.8 — Active dot tracking + centered (v5)

5 centered options where active category highlights as carousel rotates:
- A: Two rows with fade. Middle dot in active segment grows + glows.
- B: Single row. Active segment's middle dot pulses.
- C: Two rows. Active segment lifts up.
- D: Single row. All dots in active segment enlarge.
- E: One big dot per category, active one rings with glow.

**Scott:** "A, but don't show 'other' category. Ship it."

### 7.9 — Shipped to production

- Replaced carousel nav dots with category dot bar (10 categories, no "other")
- Two rows of round colored dots, grouped by category
- Active category's middle dot grows + glows as carousel rotates
- Hover tooltip shows category name
- "see more →" link centered below dots
- Added `cat` field to all quote objects

**Commit:** [`2418208`](https://github.com/scottwofford/personal-site/commit/2418208)
**Live:** https://scottwofford.com/luthien/landing_v8/

---

## Round 8: Multi-card grid + section order variants (Feb 26)

Built 4 variants for Jai/Finn/Esben meeting to test **two variables**: section order and guided CTA copy.

### Common changes across all variants

- **Multi-card grid** replaces single-card carousel (Josh feedback: cards scroll too fast, wanted multiple visible)
- **Desktop:** CSS Grid `repeat(auto-fill, minmax(280px, 1fr))` — 2-3 cards depending on viewport
- **Mobile (<640px):** Horizontal flex + `scroll-snap-type: x mandatory`, native swipe
- ~8 curated "best hit" cards, bottom fade gradient, "see more" link to incidents.html
- **Dual CTA:** "Try it yourself" (GitHub README) + guided CTA (varies per variant)
- **Hero copy tightened** to ~20 words, says "Claude Code" explicitly, added context rot differentiator line
- **Architecture collapsed** by default (`<details><summary>How it works</summary>`)

### Variants

| Variant | Section Order | Guided CTA | Rationale |
|---------|-------------|------------|-----------|
| **A** | Hero → Problem → Demo → Arch → CTA | "Set it up for your use case" | Minimal disruption from v8. Problem-first emotional hook. |
| **B** | Hero → Demo → Problem → Arch → CTA | "15-min setup call" | Maria + Josh independently recommended demo-first. |
| **C** | Hero → 3 cards → Demo → More cards → Arch → CTA | "Get help with your setup" | Hook → solve → reinforce sandwich pattern. |
| **D** | Hero → Mixed grid (quotes + demo cards) → Arch → CTA | "We'll configure it for your workflow" | Novel: everything is cards. Demo cards interleaved with quotes. |

### Hosted (for Finn/Esben review)

All variants hosted on GitHub Pages:
- **Selector:** https://luthienresearch.github.io/luthien-pbc-site/v9/
- **v8 baseline (for reference):** https://luthienresearch.github.io/luthien-pbc-site/v8/

### Files

Source in [`2026-02-26_v9-multi-card/`](https://github.com/LuthienResearch/luthien-org/tree/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card):

| File | Description |
|------|-------------|
| `index.html` | Variant selector with descriptions |
| `a-current-order.html` | Variant A |
| `b-demo-first.html` | Variant B |
| `c-sandwich.html` | Variant C |
| `d-interleaved.html` | Variant D |

---

*Last updated: 2026-02-26*
