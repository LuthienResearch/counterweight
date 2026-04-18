# Landing Page — Plan of Attack

## Where we are

We've been through several rounds of brainstorming and prototyping for the Luthien PBC landing page. The work is scattered across different sessions and machines but now consolidated here.

## Key artifacts

| What | Where |
|------|-------|
| FigJam mind map (design DNA, site structure, 3 design directions) | [Figma board](https://www.figma.com/board/pTaiBB8K4ON359TDWimOSk/Luthien-PBC-Website---Design-Direction?node-id=0-1&p=f&t=o4y9Lgy1Dw7i4qhs-0) |
| Full brainstorming session (content ingestion, design research, build spec creation) | [Claude chat](https://claude.ai/chat/689f0b73-d4fb-44ef-a582-5af7b2307ab8) |
| Build spec for "Assume Nothing" landing page | `2026-02-21_luthien-pbc-site-prompt.md` |
| First engineering-principles take (spec + v3 HTML) | `2026-02-22_eng-1st-principles/` |
| Earlier landing page variants ("Let AI code. Stay in control.") | `2026-02-05_landing-page-variants/` |
| Competitor screenshot research | `2026-01-16_site-research/` |
| Tagline brainstorming and analysis | `2026-02-05_inspire_v2/` |
| Policy config UI mocks + demo script | `2026-02-08_v5-policy-config-mocks/` |
| Demo research data | `2026-01-20_demo-research/` |
| Validated messaging (README v7, value prop requirements R1-R8) | `../2-versions-requirements/` |

## What evolved during brainstorming

The FigJam session and Claude chat produced several key shifts from earlier versions:

1. **Tagline**: "Let AI code. Stay in control." (validated with users) → "Assume Nothing." (punchier, more engineer-cynical). Both are worth testing.

2. **Framework**: Two-layer model (universal + custom) → **Three-layer model** (sus / claude.md / prompt). This is the intellectual centerpiece of the page.

3. **Positioning**: "Where Luthien sits" — upstream of everything. CI/CD, CodeRabbit, human review all catch problems *after* they're in code. Luthien catches them *before they exist*.

4. **Voice**: Shifted from "developer marketing" to "senior engineer explaining to another senior engineer." Dry, knowing, competent. Fireship energy, not SaaS energy.

5. **Design direction**: Narrowed to dark-mode, terminal-native aesthetic. JetBrains Mono + Syne + Inter. Color-coded by layer (red=sus, amber=rules, blue=prompt, green=success).

## How to pick this up

### Step 1: React to what exists

Open these HTML files in a browser and form opinions:
- `2026-02-22_eng-1st-principles/luthien-v3.html` (latest)
- `2026-02-05_landing-page-variants/option-c-terminal.html` (terminal variant from earlier round)
- `2026-02-05_landing-page-variants/option-a-minimal.html` (minimal variant)

What works? What doesn't? What's missing?

### Step 2: Iterate on the build spec

The build spec (`2026-02-21_luthien-pbc-site-prompt.md`) is a self-contained prompt you can paste into a fresh Claude Code session. It has all 9 sections, exact copy, design system, and anti-patterns.

To iterate:
- Paste the full spec into Claude Code (use `--dangerously-skip-permissions` for fast rendering cycles)
- React to the output, note what to change
- Update the spec, re-run

### Step 3: Use FigJam for divergent thinking

The [FigJam board](https://www.figma.com/board/pTaiBB8K4ON359TDWimOSk/Luthien-PBC-Website---Design-Direction?node-id=0-1&p=f&t=o4y9Lgy1Dw7i4qhs-0) maps design DNA → site structure → 3 design directions (Minimal Dev, Bold Gradient, Terminal Native). When you need to brainstorm new directions or compare approaches, add to the board rather than jumping straight to code.

### Step 4: Test copy with users

Key copy decisions still open:
- "Assume Nothing" vs "Let AI code. Stay in control." vs hybrid
- Three-layer model — does it resonate or confuse?
- Failure mode grid — do the examples land?

Run these past the next user interview. The [value prop requirements](../2-versions-requirements/) have the validated patterns (R1-R8) to check against.

### Step 5: Ship to luthien_site

When a version is ready:
1. Push final `index.html` to `LuthienResearch/luthien_site`
2. Netlify auto-deploys from that repo to luthienresearch.org
3. The old Eleventy scaffolding in that repo should be cleaned out first

## Open questions

- **Domain**: No PBC-specific domain yet. Ship to luthienresearch.org first, or wait?
- **Eleventy cleanup**: luthien_site still has old Eleventy files. Rip out and replace with static HTML, or migrate to Astro for future blog needs?
- **README vs landing page**: Jai's guidance (PR #179) is that README should be the primary landing. How does the standalone site relate?
