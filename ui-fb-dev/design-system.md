# Luthien Design System

**Purpose:** Codify design decisions so that any agent (Claude Code, Codex) or human editing Luthien's landing page, README, or UI produces consistent output. Load this file into context when generating or editing any user-facing page.

**Source of truth:** This doc. Cross-referenced from `luthien-proxy/CLAUDE.md` and `luthien-pbc-site/CLAUDE.md`.
**Derived from:** 15 user feedback sessions (Jan-Mar 2026), requirements R1-R9, Darren Ellis's design process advice (Session 11), Lumen theme selection (luthien-pbc-site#41, Apr 2026).

**Last updated:** 2026-04-09 (Lumen theme rollout — replaced Inter/near-black with Raleway + Lora on Plum Dark).

---

## Voice & Tone

### Two registers, one page

| Section | Register | Example |
|---------|----------|---------|
| **Problem / quotes** | Deadpan, developer solidarity | "Claude deleted the test, then told you everything was fine." |
| **Solution / CTA / trust** | Professional, credible, concise | "Luthien enforces your rules on every request and response." |

### Copy rules

- **No exclamation points.** Humor comes from reality being absurd, not from enthusiasm.
- **Nickel words, not $10 words.** Avoid: "stochastic," "judge model," "reduce latency." If a PM can't forward it to an engineer without explaining it, simplify.
- **Say "Claude Code"** not "AI coding agent" (confusing and redundant with LLM).
- **"Enforces your rules"** is the strongest hook. Use active verbs. Lead with what Luthien does, not what it is.
- **Avoid "all without..."** infomercial patterns. State facts directly: "Works with your existing Claude Code setup."
- **"Suspicious behavior"** not "suspicious stuff." Trust products need professional register in solution sections.
- **"Active development"** signals not-ready. Avoid or reframe: "Open source. Growing fast." Let GitHub activity speak for itself.
- **"Rules and policies"** is ambiguous. Always clarify: "your rules," "the rules you define."
- **"Claude Code code"** is a mouthful. Restructure sentences to avoid three similar words in a row.
- **"Setup help"** sounds like talking to a human. Use "Setup guide" or "Quick start" for self-service CTAs.
- **No fictional examples.** Every class name, YAML config, and code snippet must reference real, working code. Fictional examples undermine trust (R6).

### Content freshness

- **Blog posts must be within ~2 months** to signal an active project. Old posts do more harm than no blog. (Jesse: "I would not know if you're in business still.")
- **If you can't keep content fresh, remove the section.** A stale blog is worse than no blog.
- **Dates on the page should feel current.** Round up experience ("a decade" not "nine years").

---

## Visual Identity

### Cross-surface consistency

All Luthien web surfaces (public landing page, gateway UI, future dashboards) share one visual language. When adding a new page or updating an existing one, match these properties:

| Property | Value | Notes |
|----------|-------|-------|
| Container max-width | `960px` | Keeps content scannable; matches PBC site |
| Card background | `#201C2A` | Lumen surface — slightly lifted from page bg |
| Card border | `1px solid #28243A` | Lumen Divider |
| Card border-radius | `3px` | Lumen aesthetic: sharp editorial corners (reduced from `8px`) |
| Card shadow (at rest) | `0 1px 6px rgba(0,0,0,0.25)` | Subtle depth; not flat |
| Card hover | border-color shift + `transform` + `box-shadow` | Match PBC quote-card hover |
| Section labels | JetBrains Mono, uppercase, `letter-spacing: 0.18em`, color `#7A7290` | Lumen Muted Label |
| Typography scale | `clamp()` responsive sizing (e.g., `clamp(1.3rem, 3vw, 1.8rem)` for h1) | Avoid fixed `px` sizes for headings |
| Section padding | `40px 0` desktop, `28px 0` mobile (breakpoint: `640px`) | |
| Card grid | `repeat(auto-fill, minmax(280px, 1fr))`, gap `16px` | |

**Rationale:** Users who see the public site and then open the gateway should feel like they're in the same product. Style drift between surfaces erodes trust (R6).

### Color & theme — Lumen

**Direction 01 — "Light from a dark room."** High contrast, teal energy, warm linen. Readable at any hour. Selected April 2026 after the redesign sprint in luthien-pbc-site#41.

**Canonical spec:** `luthien-pbc-site/site/v12/lumentheme-branding-guideline.md` is the in-repo authoritative branding guide (palette hex codes, type scale, iconography, UI components). This doc mirrors the essentials needed for cross-surface work.

**Primary palette:**

| Name | Hex | Usage |
|------|-----|-------|
| Plum Dark | `#141216` | Page background |
| Linen | `#EDE5D8` | Primary text — headings, body, nav |
| Verdigris | `#3B9494` | Accent, CTAs, keywords, links, positive states |
| Amber | `#C47B42` | Warmth, secondary accent |
| Signal Red | `#C45050` | Errors only — never for emphasis |

**Supporting tones:**

| Name | Hex | Usage |
|------|-----|-------|
| Surface | `#201C2A` | Card / elevated surface backgrounds |
| BG Elevated | `#1A1720` | Slight lift above page background |
| Divider | `#28243A` | Borders, separators, card borders |
| Muted Label | `#7A7290` | Section headers, small labels, dim text |
| Soft Label | `#B0A8BE` | Swatch names, metadata, secondary text |
| Code BG | `#0E0C16` | Code block backgrounds |

**Font stack:**
- **Headings:** Raleway SemiBold 600, tracking `-0.02em`. Elegant geometry; approachable precision.
- **Body:** Lora Regular 400, line-height `1.6`. Editorial warmth and rich readability.
- **Code:** JetBrains Mono Regular 400.

**Rationale:** Built from 15 user feedback sessions. Sans-serif headlines that everyone preferred (Raleway), Patina's teal that won hearts (Verdigris), and dramatically improved contrast over the old `#09090b`. Lora in body text gives editorial warmth that distinguishes Luthien from every other VC-deck-looking developer tool. Dark mode preserved (Jesse's ICP preference) but the Plum Dark base is warmer and more humane than the old near-black. Maria's "not conveying safety" concern is partially addressed by the warmer plum undertone.

### Text color hierarchy (updated 2026-04-09 for Lumen)

Lumen intentionally collapses the old 5-value text hierarchy (`#fafafa` / `#e4e4e7` / `#a1a1aa` / `#71717a` / `#3f3f46`) to **3 values**. Emphasis comes from weight or accent color (Verdigris), not from a brighter white.

| Role | Color | Usage |
|------|-------|-------|
| Primary text | `#EDE5D8` (Linen) | Headings, titles, body, nav active state — single bright text color |
| Muted text | `#B0A8BE` (Soft Label) | Meta text, dates, authors, descriptions, nav links, footer links, blockquotes |
| Dim text | `#7A7290` (Muted Label) | Section labels, footer meta, decorative elements, easter eggs |
| Borders only | `#28243A` (Divider) | Card borders, section dividers. Never for text. |
| Accent | `#3B9494` (Verdigris) | Links, active ToC indicator, TLDR labels, CTAs |
| Errors only | `#C45050` (Signal Red) | Error messages, destructive actions. Never for emphasis. |

**Do NOT use** the deprecated old-theme values `#fafafa`, `#e4e4e7`, `#a1a1aa`, `#71717a`, `#52525b`, `#3f3f46`, `#27272a`, `#6b9fff`, `#22c55e`, `#ef4444`, or `#f59e0b` anywhere in new work. If you see them in existing code, they're legacy from the pre-Lumen theme and should be migrated on the next substantive edit of that file.

### Before/After comparison

- **Heights must match.** Mismatched heights disrupt visual comparison. (7+ reviewers flagged this.)
- **Captions must be visible.** Not small/faint — readers need them to understand what they're looking at.
- **Annotate explicitly.** Don't rely on readers to spot the diff. Use editorial annotations (callout boxes, arrows) that are clearly NOT part of the terminal UI.
- **Show the rule first.** `$ cat CLAUDE.md` showing the rule that gets violated/enforced. (Tyler: "literally just cat the CLAUDE.md.")
- **Strip emojis** from terminal screenshots. Emojis are ambiguous — unclear if from LLM, user, or Luthien. (Josh)

### HTTP method badges

- **Colors follow the universal convention:** green (GET), yellow (POST), blue (SSE/WebSocket). Swagger, Postman, and Insomnia all use this. Don't fight it.
- **Developer reference only.** Method badges belong in collapsed developer sections, never at the same visual level as user-facing navigation cards.
- **On mixed-audience pages** (e.g., gateway landing page), developer reference must be collapsed by default and visually subordinate when expanded.

### Architecture diagram

- **Always visible** (not collapsed). Collapsed reads as "afterthought" (Darren). But keep it compact.
- **Strong positive signal** across all reviewer types. Mike: "I like this diagram a lot." Finn: "should be bigger."

### Quote cards

- **Self-explanatory quotes first.** "Claude destroyed my entire project" works universally. Context-dependent quotes ("it used pip instead of uv") go lower.
- **Fewer but punchier.** Quantity ≠ quality. Maria: reframe excess quotes as use cases ("If you're running into this problem...").
- **Clickable links are optional.** Users don't discover them (Mike, Jesse). Cards work as standalone proof-of-pain.
- **External links = exit opportunities.** Each link competes with the CTA. Consider removing source links from cards on the landing page (keep them in a separate incidents page).

### Section hierarchy

- **Visual energy must not drop** after the architecture diagram. If the next section is text-heavy, add visual treatment (icons, cards, story structure).
- **Story flow down the page:** problem → what is it → how it works → evidence → CTA. Sections should feel like a narrative, not a reference doc. (Darren, Maria)
- **CTA needs a transition.** Don't jump from demo to "sign up." Build a bridge — "one more step" between showing value and asking for action. (Mike's gym trainer analogy)

---

## Trust Signals

### Organizational credibility

- **LinkedIn company page:** Required. PMs check LinkedIn for every early-stage startup. (Maria: "I do that for every single early stage startup.")
- **Team bios: professional, Luthien-focused.** Show relevant expertise and what each person brings to Luthien. No personal details (kids, spouse), no personal website links. (Jesse: "delete." Maria: "value prop centered on Luthien.")
- **About section with founding story.** Why Luthien exists, what problem the founders saw. The story IS the trust signal. (Maria, Finn)
- **Don't link personal websites** from the landing page. Keep attention on the product. Personal brands dilute the product message. (Maria, Jesse)

### Content credibility (R6: no AI slop irony)

- **Audit before publishing:** No em dashes, no AI-generated preamble, no curly quotes, no grammar errors.
- **No fabricated UI.** Never show product features that don't exist. (Jai: "not okay.")
- **No fictional class names.** Every code example must be real, working code. (Tyler)
- **Grammar/formatting check.** Multiple reviewers (Mike, Jesse) have caught errors. A product that claims to catch AI mistakes can't have mistakes in its own copy.

### Policy visibility (R3)

- **At least one policy example visible without clicking.** Don't hide all examples behind `<details>`. (Tyler)
- **Show the policy name in block messages.** Not just "Blocked" — show which policy triggered it and why. (Maria, Josh)
- **"A rich policy repository would go a long way."** Show what's available. (Maria)

---

## Page Structure Template

Based on validated order from 15 sessions:

```
1. Hero: one-sentence mission statement + "enforces your rules" hook
2. Demo: before/after (height-matched, annotated, with CLAUDE.md context)
3. Problem: 3-5 punchy, self-explanatory quotes (not 70)
4. Architecture: diagram (always visible, compact)
5. Use cases: reframed quotes as "If you have this problem..."
6. Trust: team bios (professional), about/founding story
7. CTA: bridging transition → "Try it yourself" (GitHub) + "Setup guide"
8. Footer: GitHub, LinkedIn company page
```

### CTA guidelines

- **Primary:** CLI install command (show `pipx install luthien-cli` or equivalent) + "View on GitHub". Engineers want self-service. (Josh: "book a call = next.")
- **Secondary:** "Book a call" → calendar link. Acceptable as secondary CTA per Jai's Mar 10 design sprint feedback. Engineers who want to talk will find it; those who don't will self-serve.
- **Never:** "Book a call" as *primary* CTA. Anti-pattern for developer tools.
- **Never:** "Setup help" — sounds like talking to a human. Use "Setup guide" or "Quick start" for self-service.
- **Placement:** After the reader has enough context. Not before the demo. (Mike)

---

## Easter Eggs & Humor

- **ASCII art: remove or truly hide** (page source only). If it "looks like an accident" to non-developers, it damages credibility. (Jesse: "I hate it.")
- **Meme content:** Keep as hidden easter eggs, not visible page elements.
- **The real quotes ARE the humor.** Developer frustration quotes do the comedy work better than any crafted joke. Don't add AI-generated filler between them. (Round 4 lesson)

---

## Anti-Patterns (don't do these)

| Anti-pattern | Why | Source |
|-------------|-----|--------|
| "AI coding agent" | Confusing, redundant with LLM | Maria S6 |
| "All without changing your dev setup" | Infomercial | Mike S14 |
| "Suspicious stuff" | Too informal for trust claims | Mike S14 |
| "Active development" | Signals not-ready | Mike S14 |
| "Book a call" as primary CTA | Anti-pattern for engineers | Josh S7 |
| "Setup help" | Sounds like talking to a human | Maria S15 |
| Fictional code examples | Undermines trust | Tyler S12, Jai S10 |
| Collapsed architecture | Reads as afterthought | Darren S11 |
| 70 quotes on one page | Quantity overwhelms | Mike S14, Maria S15 |
| Personal details in bios | Dilutes product message | Jesse S15 |
| External links in quote cards | Exit opportunities | Maria S15 |
| Em dashes anywhere | AI slop irony | Quentin S3, R6 |
