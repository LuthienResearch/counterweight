# Requirements — How to Write and Use Them

**Last updated:** 2026-03-19

---

## What a requirement is

A requirement describes **a user problem**. Not a solution, not a feature, not a design pattern.

- **User is the protagonist.** Write in first person or describe what the user needs. "I can't tell if the proxy is running" not "add a status indicator."
- **Timeless.** Don't reference versions, branches, or current implementation state. Requirements should read the same whether it's March 2026 or March 2027.
- **Problem only.** Strip all solution language. If you find yourself writing "should have a button" or "needs a dropdown," you're writing a solution. Back up and ask: what problem does that button solve?
- **Measurable.** You should be able to look at a requirement and answer: "Did we solve this? Yes or no."

### Format (match this exactly)

Table columns: `#`, `Requirement (problem only)`, `Current state as of [date]`, `Key evidence`

Each requirement cell uses this pattern:

```html
<u>Short scannable title.</u> Full requirement sentence describing the user problem.
```

- The short title is **underlined** with `<u>` tags. NOT bolded.
- Followed by 1-2 sentences describing the problem in plain language.
- "Current state" column describes where things stand today (this column IS allowed to reference implementation).
- "Key evidence" column links to user session quotes or observed behavior.

### Template row

```
| R1 | <u>Proof of life.</u> Users should be able to tell whether the proxy is running. | Gateway landing page is static, no live data. | [Zac S1]: "I want to see what got rejected." |
```

### Good examples (from this repo)

- `<u>Obvious first value.</u> The user's first experience trying a policy must make Luthien's value obvious.` (R1, policy-config)
- `<u>Meet users where they work.</u> Users must be able to interact with policies from where they already work.` (R2, policy-config)
- `<u>Proof of life.</u> Users should be able to tell whether the proxy is running.` (R1, gateway)

### Bad examples

- "Add a health check badge to the nav bar." (solution, not problem)
- "v1 doesn't show live data." (references current state in requirement column)
- "The landing page should use progressive disclosure." (design principle, not requirement)
- **Bold text for requirement title.** (wrong formatting, use `<u>underline</u>`)

---

## What a requirement is NOT

### Design principles are not requirements

Design principles describe **how** we solve problems. Requirements describe **what** problems exist. Don't mix them.

If you catch yourself writing a requirement that sounds like advice to a designer ("use progressive disclosure," "follow mobile-first," "keep it minimal"), move it to the design principles section of the relevant doc.

### Solutions are not requirements

"Add a status bar" is a solution. "Users can't tell if the proxy is running" is the requirement. The solution might be a status bar, or a heartbeat animation, or a dashboard, or a CLI command. The requirement stays the same regardless.

---

## Design Principles

Design principles guide HOW we solve requirements. They apply across all pages and features.

### From Nielsen's 10 Usability Heuristics

Applied to Luthien and documented in detail in [ux-exploration.md](../ux-exploration.md):

| # | Heuristic | What it means for Luthien |
|---|-----------|---------------------------|
| 1 | **Visibility of system status** | Users should always know: Is Luthien running? What policy is active? Is it doing anything? |
| 2 | **Match between system and real world** | Use "policies" not "configurations." Show concrete examples, not abstractions. |
| 3 | **User control and freedom** | Easy to switch policies, undo changes, go back. |
| 4 | **Consistency and standards** | Same nav, same card style, same dark theme across all pages. See [design-system.md](../design-system.md). |
| 5 | **Error prevention** | Warn before destructive actions. Don't let users break things silently. |
| 6 | **Recognition rather than recall** | Don't make users remember which page does what. Show, don't tell. |
| 7 | **Flexibility and efficiency** | Shortcuts for power users, simple defaults for new users. |
| 8 | **Aesthetic and minimalist design** | Hide complexity until needed. Progressive disclosure. |
| 9 | **Help users recover from errors** | Clear error states with recovery actions. |
| 10 | **Help and documentation** | Embedded guidance, not separate docs. |

### Luthien-specific design principles

| Principle | What it means | See also |
|-----------|---------------|----------|
| **Progressive disclosure** | Show the minimum needed to act. Reveal details only after the user has decided to engage. Complexity is opt-in. | [ux-exploration.md](../ux-exploration.md) H8, [design-system.md](../design-system.md) section hierarchy |
| **Cross-surface consistency** | Gateway UI, public site, and CLI should feel like the same product. Same colors, typography, card styles. | [design-system.md](../design-system.md#cross-surface-consistency) |
| **No surprises on auth** | Users should know before clicking whether a page requires login. One consistent login flow, not per-page prompts. Unauthenticated users see what exists (with indicators), not blank pages. | Gateway R4 |
| **Developer reference is subordinate** | API endpoints, HTTP methods, and internal routes live in collapsed sections, never at the same visual level as user-facing features. | [design-system.md](../design-system.md#http-method-badges) |
| **Copy follows the design system** | No exclamation points, nickel words, say "Claude Code," no inside baseball. | [design-system.md](../design-system.md#copy-rules) |

---

## Structure of a requirements doc

Each requirements doc follows this structure:

1. **Header** — owner, last updated, feedback source
2. **Every version of this page/feature** — table of versions with permalinks, PRs, and user feedback
3. **5 Whys** — trace the surface problem to the root problem
4. **Requirements table** — numbered, problem only, with key evidence from user sessions
5. **Questioning the requirements** — open questions about whether each requirement is real

### Evidence must come from users

Requirements need evidence. "Internal review" is acceptable for initial drafts, but every requirement should eventually have at least one user quote or observed behavior backing it up. Requirements with only internal evidence should be flagged for validation.

---

## Index of requirements docs

| # | Doc | Scope |
|---|-----|-------|
| 0 | [0-uber-requirements.md](0-uber-requirements.md) | Cross-cutting requirements (onboarding, infrastructure) |
| 1 | [1-value-prop-requirements-live.md](1-value-prop-requirements-live.md) | README, landing page, value proposition |
| 2 | [2-feedback-hack-requirements-live.md](2-feedback-hack-requirements-live.md) | Outreach, feedback collection, hackathon CTAs |
| 3 | [3-gateway-requirements-live.md](3-gateway-requirements-live.md) | Gateway landing page (`/`) |
| 4 | [4-history-and-context-requirements-live.md](4-history-and-context-requirements-live.md) | Conversation history and context management |
| 5 | [5-policy-config-requirements-live.md](5-policy-config-requirements-live.md) | Policy configuration UI |

---

## Related docs

- [design-system.md](../design-system.md) — visual identity, copy rules, anti-patterns
- [ux-exploration.md](../ux-exploration.md) — Nielsen heuristic analysis, information architecture, design mockup concepts
