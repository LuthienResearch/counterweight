# Value Proposition / README — Live Requirements (ARCHIVED)

**This doc has been split into two files (2026-03-23):**

- **[1.1-landing-page-versions.md](1.1-landing-page-versions.md)** — Landing page version history (v1 through v10.9.x)
- **[1.2-readme-versions.md](1.2-readme-versions.md)** — README version history + shared requirements (R1-R9) + synthesis + appendix

The content below is preserved as archive. Use the split files above for current work.

---

**Owner:** Scott
**Last updated:** 2026-03-20 (archived 2026-03-23)
**Branch:** `value-prop`
**Feedback source:** [../1-feedback-synthesis/1-value-prop-feedback.md](../1-feedback-synthesis/1-value-prop-feedback.md)
**Landing page context:** [luthien-landing-page-context.md](https://drive.google.com/...) (compiled Feb 5)

---

## README versions

GitHub README (Markdown, lives in luthien-proxy). Numbering is independent from the landing page table (v1-v7 were shared, v8+ diverge).

| Version | Date | What it was | Permalink | Who saw it | User Feedback |
|---------|------|-------------|-----------|------------|---------------|
| **v1: Current README on `main`** | Pre-Feb 2026 | Developer reference. Quick Start → launch scripts → Admin UI → Monitor → Policy → Architecture. 515 lines. | [README.md @ af3e819](https://github.com/LuthienResearch/luthien-proxy/blob/af3e819/README.md) | [Zac](../1-feedback-synthesis/1-value-prop-feedback.md#session-0-zac-saber-reacting-to-current-readme-on-main) (Jan 27) | "I'm closing the tab" · "epic shit first" — features buried, policies at the bottom. |
| **v4a: MD Option A — Problem-first** | Feb 8 | Leads with problem table, then how Luthien fixes it, then code examples. | [option-a @ cc22574](https://github.com/LuthienResearch/luthien-proxy/blob/cc22574/docs/readme-option-a-problem-first.md) | [Chris, Beth Anne, Bahar](https://otter.ai/u/4spwBLFUfA3tCACsDPOyUyn4yss) (Feb 8 Super Bowl demo) | Chris: "read it two times and still didn't get it." Bahar: scope creep example resonated. |
| **v4b: MD Option B — Visual flow** | Feb 8 | Before/after visual comparison, mermaid diagram, 3-column table, code examples. | [option-b @ cc22574](https://github.com/LuthienResearch/luthien-proxy/blob/cc22574/docs/readme-option-b-visual-flow.md) | [Chris, Beth Anne](https://otter.ai/u/4spwBLFUfA3tCACsDPOyUyn4yss) (Feb 8 Super Bowl demo) | Beth Anne: "I like this way better. Now I get it." Visual > text for both. |
| **v4c: MD Option C — Use-case-first** | Feb 8 | Opens with code block + description, "Pick your policy" expandable use cases. | [option-c @ cc22574](https://github.com/LuthienResearch/luthien-proxy/blob/cc22574/docs/readme-option-c-use-case-first.md) | [Chris, Beth Anne, Bahar](https://otter.ai/u/4spwBLFUfA3tCACsDPOyUyn4yss) (Feb 8 Super Bowl demo) | Best intro of the three. Beth Anne: "Makes more sense." But "pick your policy" confused her. |
| **v5a–c** | Feb 9 | Three variations on `value-prop` branch (Clean Minimal, Visual Demo, Narrative). | [v5a](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v5a-clean-minimal.md) · [v5b](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v5b-visual-demo.md) · [v5c](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v5c-narrative.md) | Not shown externally | Internal iterations from v4 learnings. |
| **v6** | Feb 10 | Left/right before-after layout. Expandable code sections. "Clean up writing ticks" use case. | [readme-v6.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v6.md) | [Quentin](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/), [Tyler](https://docs.google.com/document/d/1lRX5U7_2Ig1oOw775xm9uoGGK6yJx2gip8N2BlAA0JQ) | Quentin: em dashes (AI slop irony), missed expandable sections, "Does Windsurf support this?" See [S3](../1-feedback-synthesis/1-value-prop-feedback.md#session-3-quentin-feuillade-montixi-weavemind--seldon-labs). |
| **v7** | Feb 10 | Addresses Quentin: removed em dashes (R6), added supported clients (R7), Security section (R8). Tyler's install feedback. | [readme-v7.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v7.md) · [PR #179](https://github.com/LuthienResearch/luthien-proxy/pull/179) | [Tyler](https://docs.google.com/document/d/1lRX5U7_2Ig1oOw775xm9uoGGK6yJx2gip8N2BlAA0JQ) (live install) | Tyler installed v6 live. v7 incorporates his + Quentin's feedback. |
| **v8** | Feb 23 | Jai's PR review: Docker "(must be running)", `curl /health` verification, usage info back in README. | [README.md @ 0a5a6c0](https://github.com/LuthienResearch/luthien-proxy/blob/0a5a6c0/README.md) · [PR #179](https://github.com/LuthienResearch/luthien-proxy/pull/179) | [Jai](https://docs.google.com/document/d/1zGKNAenbLKcqY630gkF7Drmwafy4FeyKvCXjsfa1If8) (PR review) | "README.md needs to contain instructions for basic use." 8/10 items already done; 2 fixed. |
| **v9** | Mar 3 | No Silent Failures default policy. Before/after SVGs. LLM-as-judge examples in expandable sections. | [README.md on branch](https://github.com/LuthienResearch/luthien-proxy/tree/feature/no-silent-failures-policy) | [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI) | "What are the policies?" · fictional classes undermine trust · benchmark = #1 trust-builder. See [S12](../1-feedback-synthesis/1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback). |
| **v10** | Mar 3 | Addresses ALL 6 reviewers' SVG feedback. Redesigned both SVGs: removed fabricated "Luthien shield" UI, added `$ cat CLAUDE.md` showing the rule, added editorial annotations (red/green callout boxes). Replaced fictional code examples with real classes. Pulled policy example out of `<details>`. Added default policy note, probability threshold comment, LLM-as-judge clarification. Removed "cloud account" and "arbitrary." Sub-headers for two value props (enforce rules + log everything). ASCII diagram. ~5-15ms latency. | [README.md @ 060d116](https://github.com/LuthienResearch/luthien-proxy/blob/060d116/README.md) · [PR #265](https://github.com/LuthienResearch/luthien-proxy/pull/265) | [Mike Mantell](../1-feedback-synthesis/1-value-prop-feedback.md#session-14-mike-mantell-ux-design-contractor) (Mar 4) | Shown to Mike Mantell (Mar 4). Mike: "enforces your rules" = best hook, problem section overwhelms, CTA needs transition, "suspicious stuff" too informal, before/after height mismatch. See [S14](../1-feedback-synthesis/1-value-prop-feedback.md#session-14-mike-mantell-ux-design-contractor). Addresses feedback from [S6](../1-feedback-synthesis/1-value-prop-feedback.md#session-6-maria-paula-mendieta-landing-page-feedback) (Maria), [S7](../1-feedback-synthesis/1-value-prop-feedback.md#session-7-josh-levy-landing-page--readme-feedback) (Josh), [S8](../1-feedback-synthesis/1-value-prop-feedback.md#session-8-finn-metz-landing-page--quick-start-feedback) (Finn), [S10](../1-feedback-synthesis/1-value-prop-feedback.md#session-10-jai-dhyani--seldon-meeting-svgs--readme-direction) (Jai), [S11](../1-feedback-synthesis/1-value-prop-feedback.md#session-11-darren-ellis-landing-page-design-feedback) (Darren), [S12](../1-feedback-synthesis/1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback) (Tyler). 12 changes mapped to evidence in PR description. |
| **v10.1** | Mar 4 | `feature/team-section` branch. Adds team bios, blog section, lowercase section labels ("without luthien" / "with luthien"), expanded footer. Nav adds `team | blog` links. | On `feature/team-section` branch | [Maria + Jesse](../1-feedback-synthesis/1-value-prop-feedback.md#session-15-maria-paula-mendieta--jesse-landing-page--readme-feedback) (Mar 4) | Shown to Maria + Jesse (Mar 4). Maria: still can't explain what Luthien does (repeat reviewer). Jesse: needs mission statement, "$10 words need nickel words." Both: team bios too personal, ASCII easter egg negative, LinkedIn page needed. See [S15](../1-feedback-synthesis/1-value-prop-feedback.md#session-15-maria-paula-mendieta--jesse-landing-page--readme-feedback). |

## Landing page versions

luthienresearch.org — deployed from [LuthienResearch/luthien_site](https://github.com/LuthienResearch/luthien_site) (Eleventy + Netlify). Numbering is independent from the README table.

### Deployed

| Version | Date | What it was | Permalink | Who saw it | User Feedback |
|---------|------|-------------|-----------|------------|---------------|
| **v1: Org placeholder** | Pre-Oct 2025 | "LUTHIEN" + "Production-Ready AI Control" + contact/donate. Initially a single HTML file, then Eleventy site with About page, Updates section (ControlConf announcement, "21 Points on AI Control"), RSS feed. No product content — just nonprofit org presence. | [initial commit](https://github.com/LuthienResearch/luthien_site/commit/e434d5c) · [Wayback Mar 2025](https://web.archive.org/web/20250311082915/https://luthienresearch.org/) · [Wayback Sep 2025](https://web.archive.org/web/20250920051839/https://luthienresearch.org/) | Public | No user feedback collected on this version. |
| **v2: Proxy alpha site (LIVE)** | Oct-Nov 2025 | Current live site. "Try the Luthien Proxy Alpha" with quickstart (`quick_start.sh`), "Verify Everything is Working" (activity monitor + policy-config), SimpleJudgePolicy with RULES example, Admin API for runtime switching, "Early Development" disclaimer. Claude Code + Codex compatible. Jai authored. | [latest commit (336acea)](https://github.com/LuthienResearch/luthien_site/commit/336acea) · [Wayback Jan 2026](https://web.archive.org/web/20260103121608/https://luthienresearch.org/) | Public | Tyler's live install (Feb 10) used the GitHub README, not this site. Quentin (Feb 10) saw the GitHub README. No direct feedback on luthienresearch.org itself. |

### Prototypes (not deployed)

Organized by exploration round, not linear version sequence. Each round was a distinct design direction, not an iteration on the previous one.

**Round 1 — Dark-theme HTML** (Jan 30-31)

| Prototype | What it was | Permalink | Who saw it | User Feedback |
|-----------|-------------|-----------|------------|---------------|
| **`docs/landing.html`** | Dark-theme HTML landing page. "AI Safety for Production Agents." Monospace font, dev-friendly aesthetic. Minor meta tag fixes after Jai review. | [rendered](https://rawcdn.githack.com/LuthienResearch/luthien-proxy/5ff3982/docs/landing.html) · [source](https://github.com/LuthienResearch/luthien-proxy/blob/5ff3982/docs/landing.html) | Internal only | Not shown to external users. |

**Round 2 — Three HTML options** (Feb 5)

Jai reviewed all three. Feedback focused on strategic direction (demo-first, GitHub=landing page, value before shape) rather than per-option preferences.

| Prototype | What it was | Permalink |
|-----------|-------------|-----------|
| **Option A — Minimal Dev** | System sans-serif, sparse layout, dark background like GitHub README. Problems as red-bordered prose blocks. How-it-works as vertical timeline. "Let AI code. Stay in control." | [source](https://github.com/LuthienResearch/luthien-org/blob/fc72439/claude-code-docs/value-prop-feb-5/option-a-minimal.html) |
| **Option B — Bold Gradient** | Vercel/Supabase energy. Gradient hero text, glowing hover cards, horizontal 5-step grid. "Stay in control" fades purple→teal. | [source](https://github.com/LuthienResearch/luthien-org/blob/fc72439/claude-code-docs/value-prop-feb-5/option-b-bold.html) |
| **Option C — Terminal Native** | Full hacker aesthetic. Monospace (SF Mono), simulated terminal in hero, git-diff problem display, log-output how-it-works. | [source](https://github.com/LuthienResearch/luthien-org/blob/fc72439/claude-code-docs/value-prop-feb-5/option-c-terminal.html) |

**Round 3 — "Assume Nothing"** (Feb 21-22)

Major direction shift after all prior user feedback. Three iterations in quick succession: spec → first render → full implementation with simplification pass.

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **Build spec** | Feb 21 | New tagline "Assume Nothing." Three-layer model (sus / claude.md / prompt). 9-section spec: hero, failure mode grid (204 documented frustrations), three-layer diagram, timeline, quick start, custom policy, research basis, CTA, footer. Design: JetBrains Mono + Syne + Inter, near-black #09090b, color-coded layers. Voice: cynical senior-engineer energy, not SaaS marketing. | [spec](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-21_luthien-pbc-site-prompt.md) · [FigJam board](https://www.figma.com/board/pTaiBB8K4ON359TDWimOSk/Luthien-PBC-Website---Design-Direction?node-id=0-1) · [brainstorm](https://claude.ai/chat/689f0b73-d4fb-44ef-a582-5af7b2307ab8) |
| **eng-1st-principles** | Feb 22 | First render. Refined spec + HTML "How It Works" page — compact, single-scroll explainer showing agent→Luthien→LLM flow with three-layer enforcement. ~200 lines. | [spec](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22_eng-1st-principles/luthien-landing-page-spec.md) · [HTML](https://github.com/LuthienResearch/luthien-org/blob/main/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22_eng-1st-principles/luthien-v3.html) |
| **PBC landing page** | Feb 22 | Full implementation, then radical simplification. **Detailed (24KB):** 9 sections, blinking cursor, 19 problem bullets in color-coded grid, ASCII diagram with green glow. **Simplified (12KB):** Musk's 5-step — cut 9→5 sections, 19 bullets→3 user quotes, new tagline "Assume the model will mess up your repo." | [detailed](https://github.com/LuthienResearch/luthien-org/blob/2bed8ec/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22-pbc-landing-page/v3-detailed.html) · [simplified](https://github.com/LuthienResearch/luthien-org/blob/2bed8ec/ui-fb-dev/3-ui-mocks/1-value-prop/2026-02-22-pbc-landing-page/v5-simplified.html) |

### Round 4 — Humor/relatability prototypes (Feb 24)

Three prototypes exploring R9 (funny/relatable copy). All share: dark mode #09090b, JetBrains Mono + Inter, 11-quote carousel with layer tags, three-layer diagram, quick start code block. Each explores a different humor angle.

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **A — Escalation Ladder** | Feb 24 | "Polite correction — ignored." Dark humor angle. Quote carousel, three-layer diagram, quick start. Explores R9 option B (developer solidarity). | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/a-escalation.html) |
| **B — Stochastic Parrot** | Feb 24 | "You're a PM for a stochastic parrot." World-weary resignation → empowerment. Explores R9 option C (quote-led). | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/b-parrot.html) |
| **C — HR Discussion** | Feb 24 | "If this was a junior dev, you'd be having an HR discussion." Corporate satire — AI as problematic employee, three layers as progressive discipline. Explores R9 option A (deadpan). | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/c-hr.html) |

**Round 4 feedback (Scott, Feb 24):** "They are all too AI-sloppy. I want the tweets and dev quotes to speak for themselves." Direction: strip out AI-generated filler copy. Real developer quotes ARE the content. Minimal scaffolding around them. Round 4b below.

**Design rule — platform-authentic cards (Scott, Feb 24):** Incident cards and quote cards must look exactly like their source platform (Twitter/X dark mode, GitHub issue, HN light theme, blog pull-quote, forum post). No "View on GitHub →" or "Source →" links — these break the illusion. Instead, the entire card is clickable (opens source in new tab). The card IS the citation.

### Round 4b — Humor prototypes v2 (Feb 24, quotes-forward)

Same three concepts, rebuilt with radically less copy. Developer quotes and tweets speak for themselves. No AI-generated marketing filler between sections.

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **A2 — Escalation Ladder** | Feb 24 | v2: Stripped AI slop. Hero + quotes + diagram + quickstart. Quotes speak for themselves. | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/a2-escalation.html) |
| **B2 — Stochastic Parrot** | Feb 24 | v2: Stripped AI slop. Quotes-forward. Minimal copy between sections. | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/b2-parrot.html) |
| **C2 — HR Discussion** | Feb 24 | v2: Stripped AI slop. Corporate satire framing, but quotes do the talking. | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/c2-hr.html) |
| **4b — Incidents gallery + architecture** | Feb 24 | `bf66ff0`. Added incidents.html gallery page. Updated CTAs (Book a Call with Scott, GitHub Try it out). Detailed 3-layer architecture section (sus/claude.md/prompt). Removed quickstart section. | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/) |
| **4b-v2 — "Suspicious stuff" + parrot card** | Feb 24 | `29e09d6`. Changed wording to "suspicious stuff" everywhere. Deleted "Real, documented..." subtitle. Added parrot/test-cheating card as first incident (GitHub #7074). | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/) |
| **4b-v3 — Visual question flow** | Feb 24 | `e7da0df`. Replaced text-heavy architecture with visual question-based flow ("Did it do what you asked?" → "Did it follow your rules?" → "Did it do something suspicious?") with example chips. Added emoji icons to proxy flow. Removed category tags from incident cards. | [source](../3-ui-mocks/1-value-prop/2026-02-24_humor-prototypes/) |

**Round 4b feedback ([Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw), Feb 25):** Strip emojis, scrolling > clicking, architecture too detailed, "book a call" = anti-pattern, differentiate from system prompt (context rot = sweet spot), needs metrics. See [S7](../1-feedback-synthesis/1-value-prop-feedback.md#session-7-josh-levy-landing-page--readme-feedback).

**Round 4b feedback ([Maria](https://otter.ai/u/P0Lkx1rvdiMYjwTEH0fkP4Lmrro), Feb 26):** Reorder to value prop → demo → quotes, say "Claude Code" not "AI coding agent", show actual rule text, de-emphasize install. Sketched thought-bubble overlays. See [S6](../1-feedback-synthesis/1-value-prop-feedback.md#session-6-maria-paula-mendieta-landing-page-feedback).

### Round 5 — v8 production landing page (Feb 24)

Shipped version incorporating dot visualization, section labels, "meanwhile..." meme, full architecture section. Built from Round 4b iterations (7 sub-rounds of dot viz design in [exploration log Round 7](../3-ui-mocks/1-value-prop/landing-page-scott-explorations.md#round-7-dot-visualization--section-labels-feb-24-session-2)). Single-card carousel with 34 quotes, auto-advance. Shown to Josh, Maria, and Peter for feedback.

| Prototype | Date | What it was | Permalink | Who saw it | User Feedback |
|-----------|------|-------------|-----------|------------|---------------|
| **v8 — Production baseline** | Feb 24 | Dark-theme. Hero → 34-quote carousel (4s auto-advance) → dot viz → "Meanwhile..." meme → Before/After SVGs → architecture → CTA. 1538 lines. | [source](https://github.com/scottwofford/personal-site/blob/main/luthien/landing_v8/index.html) · [live](https://scottwofford.com/luthien/landing_v8/) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v8/) | [Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw), [Maria](https://otter.ai/u/P0Lkx1rvdiMYjwTEH0fkP4Lmrro), [Peter](https://docs.google.com/document/d/1xugPuJjtfxXw3ale54rdhqAlsH5wcvo31RtPVPJLgz4) | Josh: cards too fast, differentiate from system prompt. Maria: reorder sections, show policy text. Peter: "Very clear, love how it looks." |

### Round 6 — v9 multi-card grid variants (Feb 26)

Four variants addressing Josh/Maria/Peter feedback on v8. Built for Jai/Finn/Esben meeting. Tests **two variables**: section order AND guided CTA copy. Common changes across all variants: single-card carousel → multi-card responsive CSS grid, hero copy tightened (~20 words, says "Claude Code"), context rot differentiator line, architecture collapsed by default (`<details>`), dual CTA ("Try it yourself" GitHub + guided CTA), mobile horizontal swipe with scroll-snap. See [exploration log Round 8](../3-ui-mocks/1-value-prop/landing-page-scott-explorations.md#round-8-multi-card-grid--section-order-variants-feb-26).

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **9a — Current order + grid** | Feb 26 | Same structure as v8 but carousel → multi-card grid. Problem-first emotional hook. Guided CTA: "Set it up for your use case." Section order: Hero → Problem → Demo → Arch → CTA. | [source](../3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card/a-current-order.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v9/a-current-order.html) |
| **9b — Demo first** | Feb 26 | Show what Luthien does immediately. Problem cards become reinforcement. Maria + Josh recommended this order. Guided CTA: "15-min setup call." Section order: Hero → Demo → Problem → Arch → CTA. | [source](../3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card/b-demo-first.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v9/b-demo-first.html) |
| **9c — Problem-solution sandwich** | Feb 26 | 3 strong quotes hook, demo solves, more quotes reinforce. Classic "hook → solve → reinforce" marketing pattern. Grid split into two sections. Guided CTA: "Get help with your setup." Section order: Hero → 3 cards → Demo → More cards → Arch → CTA. | [source](../3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card/c-sandwich.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v9/c-sandwich.html) |
| **9d — Interleaved** | Feb 26 | Everything is cards. Quote cards and before/after terminal demo cards alternate in a single grid. Eliminates section-order question entirely. Novel approach. Guided CTA: "We'll configure it for your workflow." Section order: Hero → Mixed grid → Arch → CTA. | [source](../3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card/d-interleaved.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v9/d-interleaved.html) |
| **v9 variant selector** | Feb 26 | Index page with context box (changes from v8), links to all 4 variants with section order diagrams and CTA copy labeled. For Jai/Finn/Esben meeting navigation. | [source](../3-ui-mocks/1-value-prop/2026-02-26_v9-multi-card/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/) |

### Round 7 — v10 fresh start from 6 reviewers (Mar 3)

Fresh start addressing ALL 6 reviewers' feedback (Maria, Josh, Finn, Jai, Darren, Tyler). Built from 9b (demo-first, validated by Maria + Josh) as base template. v10 SVGs (`$ cat CLAUDE.md`, editorial annotations, plain English). "Without/With Luthien" labels. 70-incident database with theme badge filters (matching incidents.html). "Under the hood" architecture (always visible, not collapsed). Dual CTA: "Setup help" (primary) + "Try it yourself" (secondary). Meme hidden as easter egg.

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **v10 — Fresh start** | Mar 3 | Demo-first order. 70 incident cards from DB with multi-category filter pills. ASCII architecture diagram. ~5-15ms latency. "Open source. Early stage. Apply to be a design partner." | [source @ 93eb0dd](https://github.com/LuthienResearch/luthien-pbc-site/blob/93eb0dd/site/v10/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.5/) (renamed from v10 → v10.5) |

### Round 8 — v10.5-v10.9 incremental iterations (Mar 5-20)

Incremental improvements to v10, each preserved as a versioned directory. Hosted at luthienresearch.github.io/luthien-pbc-site/ (redirect points to latest). No v10.2-v10.4 — v10 was renamed directly to v10.5.

| Prototype | Date | What it was | Permalink |
|-----------|------|-------------|-----------|
| **v10.5** | Mar 5 | Renamed from v10. Team bios updated (accurate LinkedIn content). Footer tagline: "Power is nothing without control." Feedback page renamed from /qa-trial/ to /feedback/. | [source @ 10fc3bd](https://github.com/LuthienResearch/luthien-pbc-site/blob/10fc3bd/site/v10.5/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.5/) |
| **v10.6** | Mar 9 | Agentic session language: "whether it's minute one or hour ten" hero differentiator; compaction/multi-session persistence line in architecture section. Addresses Josh Levy's Slack feedback that Luthien felt focused on chat/one-off interactions. | [source @ 908570f](https://github.com/LuthienResearch/luthien-pbc-site/blob/908570f/site/v10.6/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.6/) |
| **v10.7** | Mar 12 | Simplified hero, CLI install CTA, Substack link. Custom Jai photo replacing GitHub avatar. Option A stacked card CTA layout. | [source @ 8b00fbb](https://github.com/LuthienResearch/luthien-pbc-site/blob/8b00fbb/site/v10.7/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.7/) |
| **v10.8** | Mar 18 | Engage section + separate hackathon page (D1 structure). Discord link. Restructured nav: separate hackathon + feedback sections. | [source @ fdf77f2](https://github.com/LuthienResearch/luthien-pbc-site/blob/fdf77f2/site/v10.8/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.8/) |
| **v10.9** | Mar 19 | Hackathon banner (AI Control Hackathon, Mar 20). Updated install command to match README. Em dash cleanup per design system. | [source @ 5518d6e](https://github.com/LuthienResearch/luthien-pbc-site/blob/5518d6e/site/v10.9/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.9/) |
| **v10.9.1** | Mar 20 | "Quotes" testimonial section with Nico Mesa quote + GitHub avatar. First user testimonial on landing page. Moved 2nd CTA to bottom. YouTube added to footer. Copy tweaks. Nico approved via WhatsApp Mar 20. | [source @ 693be2b](https://github.com/LuthienResearch/luthien-pbc-site/blob/693be2b/site/v10.9.1/index.html) · [hosted](https://luthienresearch.github.io/luthien-pbc-site/v10.9.1/) · [PR #20](https://github.com/LuthienResearch/luthien-pbc-site/pull/20) |
| **v10.9.2** | Mar 21 | Blog infrastructure: new "blog" section on landing page with one-liner card previews + nav link. 3 initial posts: Theory of Change (new, full Google Doc conversion), 21 Points (existing), ControlConf London (existing). Removed "Why Proxying the API" post. Fixed /updates/* redirect on luthien_site. | [PR #3](https://github.com/LuthienResearch/luthien-pbc-site/pull/3) · [Trello](https://trello.com/c/Zq9V4Vkz) |
| **v10.9.3** | Mar 21 | LessWrong-style table of contents sidebar for blog posts. Fixed left sidebar with h2/h3 headings, highlights current section on scroll, smooth scroll on click. Hidden below 1100px. Added to all 3 posts. Also: grey text made readable sitewide (#52525b -> #a1a1aa), nav links made consistent across all pages (hackathon, feedback, blog posts all point to v10.9.1), feedback callout on Theory of Change post, design system updated with text color hierarchy. | [PR #22](https://github.com/LuthienResearch/luthien-pbc-site/pull/22) |

---

## What this doc is

The **single source of truth** for what we're building for Luthien's value prop / README / landing page. Requirements come from user feedback and get questioned before entering the backlog.

**Feedback lives elsewhere** — this doc links to it but doesn't duplicate it:
- [../1-feedback-synthesis/1-value-prop-feedback.md](../1-feedback-synthesis/1-value-prop-feedback.md) — raw quotes from Zac (Jan 27), Chris + Beth Anne (Feb 8), Bahar (Feb 8), Jai (Feb 5 internal), Peter (Feb 25), Josh (Feb 25), Finn (Feb 25), Maria (Feb 26), Jai (Feb 26 Seldon), Darren (Mar 2), Tyler (Mar 3), Paolo (Mar 3), Mike Mantell (Mar 4), Maria + Jesse (Mar 4)
- [5-policy-config-requirements-live.md](5-policy-config-requirements-live.md) — sister doc for the policy config UI

---

## Requirements (Musk 5-Step: question → delete → simplify)

25 raw requirements from 5 users + Jai → grouped into [macro themes](../1-feedback-synthesis/1-value-prop-feedback.md#macro-themes-consolidated-from-18-cross-cutting-observations) → merged duplicates → questioned each → **5 consolidated requirements**. + 3 new requirements from Quentin (Feb 10) + 1 from Feb 24 COE session = **9 total**. Peter (Feb 25), Josh (Feb 25), Finn (Feb 25), Maria (Feb 26), Mike Mantell (Mar 4), and Maria + Jesse (Mar 4) added as evidence to existing requirements. Mike and Maria/Jesse feedback reinforces existing R1-R9. Two potential new requirements surfaced: **R10 (content freshness signals viability)** and **R11 (team section builds Luthien credibility, not personal brands)** — R11 may fold into R8 as a design note.

### Consolidated requirements

| # | Requirement | Theme | Old #s | Users (n) | Top evidence (see [synthesis](../1-feedback-synthesis/1-value-prop-feedback.md) for full quotes) |
|---|-------------|-------|--------|-----------|----------|
| **R1** | **Demo-first: open with a visual showing Luthien in action, then name what it does.** Design: align before/after vertically (Maria), strip emojis (Josh), `<details>` for architecture (Josh vs Finn compromise). **SVG annotation critical** — all 6 SVG reviewers flagged before/after as unclear. Mike (S14): before/after height mismatch + invisible captions. Mike: "What can it do" section loses visual energy after diagrams. Maria/Jesse (S15): quotes require too much thinking for non-devs — fewer but punchier, reframe excess as use cases. | [A](../1-feedback-synthesis/1-value-prop-feedback.md#theme-a-demo-first-55-external-users--jai) | #1,3,4,5,13 | 14 | Zac: "epic shit first." [Finn](https://docs.google.com/document/d/1Foi5Qjcyyn0vxCOXgqooV2EXdE5b3806kYXguS9xz1w): "too much...would have skipped this entire section." [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI): "cat the CLAUDE.md." [Darren](https://docs.google.com/document/d/1cf4N71qxWVWA9c_FvwrO-7PB-qRw2kBcsC2qjEXzL4c): "what is the difference?" [Jai](https://otter.ai/u/bL1wnC35Hji_6HWkfPPUABHFY3k): "reshape as stories." Mike (S14): before/after height mismatch, "I like this diagram a lot." Jesse (S15): "I have to think really hard to understand what happened." |
| **R2** | **Plain English first: write for PMs who forward to engineers.** Design: say "Claude Code" not "AI coding agent" (Maria), differentiate from system prompt baseline (Josh), benchmark data = ultimate proof (Tyler). Paolo: "proxy" undersells — suggest "guard proxy." Mike (S14): "Claude Code code" is awkward — "Let AI Code" reads better. Mike: "enforces your rules" = strongest hook ("that's active"). Mike: "rules and policies" ambiguous — whose? Jesse (S15): needs "one sentence mission statement" at top. Jesse: jargon kills — "judge model," "stochastic," "reduce latency" = "$10 words, need nickel words." | [B](../1-feedback-synthesis/1-value-prop-feedback.md#theme-b-plain-english-for-both-audiences-3-users) | #8,10,15 | 10 | Beth Anne ([S2](../1-feedback-synthesis/1-value-prop-feedback.md#session-2b-beth-anne-superbowl-party-demo)): "I'll send it to my PE." [Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw): "what is Luthien doing special that can't just be instructions passed to the prompt?" [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI): "I don't have any data to know that yours is better." [Paolo](https://drive.google.com/drive/folders/1MPmvqqIXWp3M03yUCCukEKpiNr4u8kNs): "a proxy, somebody will imagine something that just passes through blindly." Mike (S14): "enforces your rules — that's active." Jesse (S15): "$10 words, need nickel words." |
| **R3** | **Two layers: we handle universal dangers, you customize for your business.** Design: use storytelling not technical detail (Maria), at least one policy example visible without clicking (Tyler), no fictional class names. Maria (S15): "a rich policy repository would go a long way" — wants to see available policies. Maria: trouble linking claimed use case with actual tool. | [C](../1-feedback-synthesis/1-value-prop-feedback.md#theme-c-universal-protection--your-custom-rules-4-independent-users) | #2,9,23,25 | 8 | Beth Anne ([S2](../1-feedback-synthesis/1-value-prop-feedback.md#session-2b-beth-anne-superbowl-party-demo)): "shit ton everyone gets wrong AND specific to your business." Zac: "creating my own policy = the hook." [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI): "what the hell are the policies?" Maria (S15): "a rich policy repository would go a long way." |
| **R4** | **Complete the block story: what happened → what you see → what to do next.** Design: show policy name that triggered block, not just "Blocked." | [C](../1-feedback-synthesis/1-value-prop-feedback.md#theme-c-universal-protection--your-custom-rules-4-independent-users) | #14,22 | 4 | Beth Anne ([S2](../1-feedback-synthesis/1-value-prop-feedback.md#session-2b-beth-anne-superbowl-party-demo)): "Violated. Do I have to take an action?" [Maria](https://otter.ai/u/P0Lkx1rvdiMYjwTEH0fkP4Lmrro): "what did the policy say? Which policy." [Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw): "blocking pip install per [policy]." |
| **R5** | **Zero-friction setup: 2 env vars, keep your client, say what's running.** Design: CTA = "try it yourself" not "book a call" (Josh), de-emphasize install (Maria), paste README into Claude Code (Finn). Remove "cloud account" (Tyler). Default policy must be clear. Mike (S14): CTA too early, needs bridging transition — gym trainer analogy ("one more step"). Mike: "active development" = "I can't use this right now." Maria (S15): "Setup help" sounds like talking to a human. | [D](../1-feedback-synthesis/1-value-prop-feedback.md#theme-d-zero-friction-setup-2-users-7-quotes) | #6,7,12,16,17 | 9 | Zac: "I'm closing the tab" (re: scripts). [Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw): "book a call...I'm just like next." [Peter](https://docs.google.com/document/d/1xugPuJjtfxXw3ale54rdhqAlsH5wcvo31RtPVPJLgz4): hit Python 3.10 vs 3.13+ mismatch. [Finn](https://docs.google.com/document/d/1Foi5Qjcyyn0vxCOXgqooV2EXdE5b3806kYXguS9xz1w): "Yo, do this. Let me know what you need." [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI): "cloud account" confusion. Mike (S14): CTA too early — "one more step." Maria (S15): "Setup help" sounds like talking to a human. |
| **R6** | **Avoid AI slop irony: README must not exhibit the problems Luthien claims to solve.** Extends beyond em dashes — fabricated product UI (Jai) and fictional class names (Tyler) are worse. Mike (S14): grammar issues in compound sentence (mixed subjects). Jesse (S15): grammar/formatting issues spotted. | New (Quentin) | #26 | 5 | [Quentin](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/): "I see some em dash on the GitHub, be careful." [Jai](https://otter.ai/u/bL1wnC35Hji_6HWkfPPUABHFY3k): fabricated Luthien shield overlay "not okay." [Tyler](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI): fictional SimpleJudgePolicy examples undermine trust. Mike (S14): grammar issues. Jesse (S15): formatting issues. |
| **R7** | **Articulate what is and is not supported: clients, streaming, limitations.** | New (Quentin) | #27,28,29 | 1 (hard blocker) | [Quentin](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/): "Does Windsurf support this?" — turned out to be a blocker. |
| **R8** | **Address security and trust: encryption, private code, SOC 2.** Maria (S15): black color scheme "not conveying safety" (Jesse disagrees — dev preference split). Maria: LinkedIn company page needed for trust. Maria/Jesse: don't link personal websites — "value prop centered on Luthien." | New (Quentin) | #30 | 3 | [Quentin](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/): worried about data transmission security, encryption at rest, private code in prompts. Maria (S15): "black is not conveying safety." Maria: "I do [check LinkedIn] for every single early stage startup." |
| **R9** | **Landing page copy should be funny and immediately relatable — match Jai's deadpan register.** Design: no exclamation points, humor from reality being absurd, pair incidents with "how Luthien handles this" (Finn). Mike (S14): "suspicious stuff" too informal for a trust claim — use "suspicious behavior." Mike: "all without changing your dev setup" reads infomercial-y. Jesse (S15): ASCII art easter egg — "I hate it... looks like an accident." Jesse: simpler the better. | New (Feb 24 COE) | #31 | 7 sources | [Finn](https://docs.google.com/document/d/1Foi5Qjcyyn0vxCOXgqooV2EXdE5b3806kYXguS9xz1w): "I do definitely get the emotional arc." [Josh](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw): "'Meanwhile' seems corny." Mike (S14): "suspicious stuff — I want you to sound really credible." Jesse (S15): ASCII art "looks like an accident." See [agent overconfidence quotes](../1-feedback-synthesis/1-value-prop-feedback.md#external-developer-quotes-agent-overconfidence-and-lack-of-tool-use) for copy options. |

### Decisions

**Decided (facts, not requirements):**

- **GitHub README = landing page.** Jai decided Feb 5. No separate website. "Trying to maintain two landing pages is hard."
- **Demo video is the hero.** Jai + Chris + Beth Anne all want visual > text. Show Claude Code with Luthien intervening. (Agreed Feb 5, validated Feb 8. Part of R1.)
- **"Try in browser" is not the path.** Jai: "Too much work, may confuse." One-click cloud deploy (when SaaS is ready) is the pragmatic answer to Chris's desire. (Decided Feb 5.)

**Open decisions:**

1. **Demo GIF/video — what specific scenario to show?** Options: pip→uv replacement (common, relatable — Jai's preference), rm-rf block (evocative, no context needed), scope creep block (Zac's pain point, harder to show quickly). **Recommendation:** rm-rf or pip→uv. Both are "succinct and evocative" (Jai). Can show both — screenshot for one, video for the other.
2. **Tagline — which one?** Four candidates from Jai, plus "Let AI code. Stay in control." from tagline research. Need to test with external users.
3. **When to replace README.md on main?** Current README is a developer reference. v5 README should replace it, with reference content moved to `docs/`. Timing: after one more round of external feedback?

**Deferred (not README scope):**

- **One-click cloud deploy** (#18) + **pass-through auth** (#19) — backend/SaaS work that enables onboarding
- **Interactive playground** (#20) — Chris's desire, Jai vetoed. Cloud deploy is the pragmatic answer.
- **Package safety** (#21) — real use case for the policy backlog, not a README change
- **Testing at scale** (#24) — Bahar's core insight. Real product direction for enterprise, but beyond current README scope.

---

## Synthesis: What the README should do

Based on Zac (Jan 27), Jai (internal, Feb 5), Chris + Beth Anne + Bahar (Feb 8), Quentin + Tyler (Feb 10), Peter (Feb 25), Josh (Feb 25), Finn (Feb 25), Maria (Feb 26), Jai (Feb 26 Seldon), Darren (Mar 2), Tyler (Mar 3), Paolo (Mar 3), Mike Mantell (Mar 4), Maria + Jesse (Mar 4), and cross-referenced with prior policy config sessions (Jack, Finn).

### Bullseye target customer (Jai, Feb 7)

> "Forget about who pays you — find a human who loves what you've built." — Finn (Dec 2025)

**Must-haves** — the person who will love Luthien today:
- Hands-on developer who uses **Claude Code or Codex daily** for production code
- Has a detailed `claude.md` (or equivalent) — they've already invested in shaping agent behavior
- Familiar with LLM APIs and how they relate to agentic applications
- English-speaking, ideally west coast US timezone
- Has recently had (or is worried about) an AI agent doing something unexpected

**Two personas, one bullseye:**

| Persona | Motivation | Job titles | What they need from README | Example users |
|---------|-----------|------------|---------------------------|---------------|
| **A: "Accelerate AI tooling"** | Maximize upside — get more value from AI agents | CTO, VP Eng, Staff Engineer, DevTools Lead, Founding Engineer, CEO who codes | Quick start (2 env vars), what policies exist, how to customize, "I can write my own" | Zac, Jack, Finn |
| **B: "Make sure AI tools don't cause problems"** | Minimize downside — prevent agent failures | Head of Security, AppSec Lead, CTO wearing compliance hat | What it catches, how blocking works, what happens next, "we handle the basics" | Bahar |

At small startups (2–50 people), the same person often wears both hats. Persona A buys; Persona B justifies. Both need to see themselves in the README.

**Distribution channel — the PM champion:**

| Audience | Example | Role in adoption | What they need |
|----------|---------|-----------------|----------------|
| **Technical PM** | Chris, Beth Anne | Forwards to engineer ("I'll send it to my PE") | Plain English, real use cases, "send to my engineer" moment |

PMs don't use Luthien directly, but they're how many engineers discover it. The README must be legible to a PM who forwards it. (See R2.)

**Reference companies** (similar buyer profile): Lakera, OpenRouter, LiteLLM — developer-first infrastructure tools adopted by ICs before procurement.

### What "done" looks like (v5 README)

The README satisfies all 5 consolidated requirements in order:

1. **R1 — Demo hero** → GIF/video showing Luthien blocking a dangerous command in Claude Code. This is the first thing you see.
2. **R2 — Plain English** → Tagline + 1-sentence explanation a PM can understand. "Who it's for" visible immediately. No jargon ("pick your policy" → "use cases").
3. **R3 — Two layers** → "We handle the universal dangers. You customize for your business." Show built-in protections, then custom policies as the hook.
4. **R4 — Block story** → What happened → what the user sees → what to do next (alternative suggested, not just rejection).
5. **R5 — Zero-friction setup** → 2 env vars + docker compose. "Keep your own Claude Code." Say what Docker spins up, which port, how to change it.
6. **R6 — No AI slop irony** → README must be clean of the exact problems Luthien claims to solve. No em dashes, no AI-generated preamble, no curly quotes. Audit before publishing.
7. **R7 — Supported clients** → Clearly state: works with Claude Code, Codex, Cursor. Does NOT work with Windsurf. Streaming IS supported. Expandable sections should be visually obvious or default open.
8. **R8 — Security trust** → Address data transmission security, encryption at rest, private code handling. Mention SOC 2 plans if applicable. For a proxy that sees all code conversations, trust is a prerequisite.
9. **R9 — Funny, deadpan copy** → Landing page copy uses humor that comes from reality being absurd, not from exclamation points. Match Jai's register. Test three directions: deadpan ("deleted the test, told you everything was fine"), developer solidarity ("five times, with confidence"), quote-led ("product manager for a stochastic parrot").

### What it should NOT do (progressive disclosure)

Per [5-policy-config-requirements-live.md](5-policy-config-requirements-live.md#design-principle-progressive-disclosure) and Jai's feedback:

- Don't show Python code above the fold — code examples are a drill-down
- Don't lead with a bulleted problem list — let the demo do the work
- Don't explain policy internals (lifecycle hooks, SimplePolicy base class)
- Don't show YAML config or SaaS management UI
- Don't list every feature — just answer "why should I try this?"
- Don't describe "the shape" (proxy architecture) before the value

### Tagline candidates (to test with users)

From Jai (Feb 5), not yet validated externally:
- "Make Claude Code follow your rules"
- "Rules that Claude can't ignore"
- "Keep Claude Code on track"
- "Let AI code. Stay in control." (from tagline research — see `dev/OBJECTIVE.md`)

---

## Appendix A: Merge map (25 → 5, + 5 new → 8 total)

| Old # | Old requirement | → Merged into | Reasoning |
|-------|----------------|---------------|-----------|
| #1 | Lead with features / value, not setup | **R1** | Same as "demo-first" |
| #2 | Custom policies = the hook, make prominent | **R3** | Custom policies = "your rules" layer |
| #3 | Demo video/screenshot is the hero | **R1** | Core of demo-first |
| #4 | Value before shape | **R1** | Don't open with "proxy" — show what it does |
| #5 | Lead with example, then name the category | **R1** | Show pip→uv, THEN say "control your agent" |
| #6 | Env vars, not scripts | **R5** | Setup friction |
| #7 | Keep your own Claude Code | **R5** | Setup friction |
| #8 | Simpler language for non-SDE | **R2** | PM audience |
| #9 | Universal protection + customizability | **R3** | Identical to #23 |
| #10 | "Who it's for" visible early | **R2** | PM forwarding behavior |
| #11 | GitHub README = landing page | **DECIDED** | Architecture choice, not a requirement |
| #12 | "Without changing your dev environment" | **R5** | Setup friction |
| #13 | Show actual experience (demo GIF) | **R1** | Same as demo-first |
| #14 | Clarify what happens when blocked | **R4** | Block story gap |
| #15 | Don't call it "pick your policy" | **R2** | Jargon — PM audience |
| #16 | Tell users what Docker spins up | **R5** | Setup transparency |
| #17 | Configurable ports | **R5** | Setup transparency |
| #18 | One-click cloud deploy | **DEFERRED** | Backend/SaaS work |
| #19 | Pass-through auth | **DEFERRED** | Backend work |
| #20 | Interactive playground | **DEFERRED** | Jai vetoed; cloud deploy is the answer |
| #21 | Package safety | **DEFERRED** | Policy backlog, not README |
| #22 | Suggest alternatives when blocking | **R4** | Block story gap |
| #23 | Handle fundamentals, focus on domain-specific | **R3** | Identical to #9 |
| #24 | Testing at scale | **DEFERRED** | Product direction, not README |
| #25 | "Write your own" must not oversimplify | **R3** (design note) | Folded into R3 as a design constraint, not a standalone requirement |
| #26 | Avoid AI slop in README (em dashes, AI-generated preamble) | **R6** | Quentin (Feb 10): "I see em dash on the GitHub, be careful." Credibility risk. |
| #27 | State which clients are supported (Claude Code, Codex, Cursor) | **R7** | Quentin (Feb 10): "Does Windsurf support this?" → blocker |
| #28 | State that streaming is supported | **R7** | Quentin (Feb 10): "How do you handle streaming?" |
| #29 | Make expandable sections more obvious | **R7** | Quentin (Feb 10): "Oh, I didn't see I could expand the thing." |
| #30 | Address security (encryption, private code, SOC 2) | **R8** | Quentin (Feb 10): Most worried about data transmission + encryption at rest + private code context |
| #31 | Landing page copy should be funny, deadpan, immediately relatable | **R9** | Feb 24 COE session: developer quotes on agent overconfidence. Three copy directions (deadpan/solidarity/quote-led). Tone = Jai's register, not SaaS marketing. |

---

## Changelog

- **2026-02-08**: Created. Added Jai's internal feedback (Feb 5) + Super Bowl demo feedback (Chris + Beth Anne Porter, Feb 8) + landing page context doc. 15 requirements gathered, 11 kept, 2 deferred, 2 decided.
- **2026-02-08**: Added Zac's README feedback (Jan 27) — 6 new requirements (#1, #2, #6, #7, #16, #17). Total: 21 requirements, 17 kept, 2 deferred, 2 decided. Added current README on `main` and `docs/landing.html` to version table.
- **2026-02-08**: Added Bahar Erar's feedback (Feb 8) — 4 new requirements (#22–#25). Total: 25 requirements, 19 kept, 3 deferred, 2 decided. Key new themes: testing at scale, don't oversimplify policy creation, suggest alternatives when blocking. Updated version table with Bahar's evaluations of Options A + C.
- **2026-02-08**: Musk 5-Step consolidation. 18 cross-cutting themes → 5 macro themes. 25 requirements → 5 consolidated (R1–R5) + 5 deferred + 3 decided. R6 ("don't oversimplify") deleted as standalone — folded into R3 as design note. Policy metrics insight moved to 5-policy-config-requirements-live.md.
- **2026-02-08**: Restructured doc. Consolidated Decided/Deferred/Open decisions into single Decisions section. Replaced generic audience table with Jai's bullseye target customer framework (Feb 7): two personas (A: accelerate AI tooling, B: minimize AI risk) + PM distribution channel. Added must-haves, reference companies, Finn quote. Moved merge map to Appendix A.
- **2026-02-10**: Added Quentin's feedback (Feb 10) — 5 new raw requirements (#26–#30) → 3 new consolidated requirements (R6: avoid AI slop irony, R7: articulate supported clients/streaming/expandable sections, R8: security trust). Added v6 to version table. Updated "What done looks like" section. Total: 30 raw → 8 consolidated + 5 deferred + 3 decided.
- **2026-02-10**: Added v5a/v5b/v5c and v7 to version table. Added Tyler as v6 viewer. v7 addresses R6/R7/R8 from Quentin's feedback.
- **2026-02-22**: Added v8 ("Assume Nothing" build spec, Feb 21) and v9 (eng-1st-principles, Feb 22) to version table. v8 introduced three-layer model (sus/claude.md/prompt) and new cynical-engineer voice direction. v9 is first rendered HTML from that spec. Added FigJam board and Claude brainstorm session links.
- **2026-02-23**: Split combined version table into separate "README versions" and "Landing page versions" tables. README v8 = Jai feedback round. Landing page renumbered with independent sequence: v1 (org placeholder, pre-Oct 2025), v2 (current live proxy alpha site, Oct-Nov 2025), v3-v7 (prototypes, never deployed). Added deployed vs prototype distinction. Added Wayback Machine snapshots and luthien_site repo links for v1/v2. Source: [Wayback CDX](https://web.archive.org/cdx/search/cdx?url=luthienresearch.org&output=text&fl=timestamp,statuscode) + [LuthienResearch/luthien_site](https://github.com/LuthienResearch/luthien_site) commit history.
- **2026-02-24**: Added R9 (landing page copy tone: funny, deadpan, immediately relatable). Three copy directions from developer quotes on agent overconfidence collected during a Feb 24 COE session. New raw requirement #31. Total: 31 raw → 9 consolidated + 5 deferred + 3 decided.
- **2026-02-24**: Added Round 4 humor prototypes (A: Escalation Ladder, B: Stochastic Parrot, C: HR Discussion). Explores R9 copy directions. New policy idea added to 3.2 (require verification before factual instructions). TLDR updated with Feb 24 dogfooding COE.
- **2026-02-26**: Added Maria Paula Mendieta's feedback (Feb 26) as evidence to R1–R5. No new requirements — her feedback reinforces existing ones with design notes. R1: 6th independent user on reorder + vertical alignment design note. R2: "Claude Code" not "AI coding agent" + action-first phrasing. R3: use case storytelling. R4: show actual policy rule text. R5: de-emphasize install in demo. Added Round 4b feedback note. Updated TLDR and value-prop-feedback Session 6.
- **2026-02-26**: Added Josh Levy's feedback (Feb 25) as evidence to R1, R2, R4, R5, R9. No new requirements — but Josh's value prop differentiation question (what does Luthien do that a system prompt can't?) sharpens R2, and his metrics request (bar chart: nothing → prompting → Luthien) is flagged for future consideration. R1: demo section tight/succinct, architecture → separate tab, scrolling > clicking. R2: differentiate from system prompt baseline, context rot = sweet spot. R4: active verb phrasing, remove colon. R5: "try it yourself" + GitHub, not "book a call." R9: "Meanwhile" too corny. Updated TLDR and value-prop-feedback Session 7.
- **2026-02-26**: Added Peter Teodosiu's feedback (Feb 25) as evidence to R1, R3, R5. Peter was already documented in TLDR + value-prop-feedback Session 5 but wasn't mapped to specific R# requirements. R1: 8th user — "Very clear," "I don't find this confusing at all." Strongest validation signal alongside Tyler. R3: 6th user — convergence on universal + custom layers. R5: 5th user — onboarding friction (Python version, API key, error messages). Also added Peter to comparison table.
- **2026-02-26**: Added Round 5 (v8 production landing page, Feb 24) and Round 6 (v9 multi-card grid variants 9a-9d, Feb 26) to landing page versions. v8 was shown to Josh/Maria/Peter and is the production baseline. v9 variants address their feedback: multi-card grid replacing carousel, section order experiments, dual CTAs. Hosted at luthienresearch.github.io/luthien-pbc-site/ for Jai/Finn/Esben review.
- **2026-02-26**: Added Finn Metz's feedback (Feb 25 landing page review) as evidence to R1, R5, R9. No new requirements. R1: 9th user — cards spin too fast (convergence with Josh), before/after demo too dense ("I would have just skipped this"), architecture should be bigger (contrast with Josh → `<details>` compromise). R5: 6th user — "just ask Claude to do it" quickstart approach (copied README into Claude Code). R9: 5th source — emotional arc resonates, incident cards are "cool proof" but wants incident→fix mapping. Also: first explicit request for "about section" / team identity. Updated TLDR, value-prop-feedback Session 8, comparison table.
- **2026-03-03**: Added Tyler (Mar 3 Session 12), Darren (Mar 2 Session 11), Jai (Feb 26 Session 10) as evidence to R1, R2, R3, R5, R6. Added v9 README to version table. No new requirements — all feedback reinforces existing ones. Key findings: ALL 6 reviewers flagged SVG before/after as unclear (R1 design note: explicit annotation needed). Tyler's benchmark request (Bash Arena, safety vs utility 2D frontier) flagged for future consideration — trust gap for senior engineers. Tyler's fictional class names and Jai's fabricated UI overlay strengthen R6 beyond em dashes to "don't show product features that don't exist." Video tutorial (Tyler) flagged as deferred trust signal. Trial doc generic version (Tyler) flagged for cold-send distribution. Updated synthesis section participant list.
- **2026-03-05**: Added Mike Mantell (Mar 4, Session 14) and Maria + Jesse (Mar 4, Session 15) as evidence to R1, R2, R3, R5, R6, R8, R9. Updated v10 entry with Mike's feedback. Added v10.1 (`feature/team-section` branch) to version table — shown to Maria + Jesse. Mike: professional UX/copy feedback — "enforces your rules" = strongest hook, problem section overwhelms, CTA needs transition, "suspicious stuff" too informal, before/after height issues. Maria (repeat reviewer v8→v10.1): still can't explain the product — persistent messaging gap for non-devs. Jesse: needs one-sentence mission statement, jargon kills ("$10 words, need nickel words"), team bios too personal, blog freshness signals viability. Both: center on Luthien not individuals, LinkedIn page needed, ASCII easter egg negative. Two potential new requirements surfaced: R10 (content freshness signals viability — Jesse: "I would not know if you're in business still") and R11 (team section builds Luthien credibility, not personal brands — may fold into R8). Updated synthesis participant list and feedback source links.
- **2026-03-20**: Backfilled landing page versions v10.5-v10.9 (Round 8). These were built Mar 5-20 in luthien-pbc-site but never tracked here. Added v10.9.1 (Nico Mesa testimonial, approved via WhatsApp Mar 20, merged PR #20). Added "always update this doc" rule to luthien-pbc-site CLAUDE.md to prevent future gaps.
