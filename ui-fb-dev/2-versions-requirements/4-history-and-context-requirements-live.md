# History & Context Management — Live Requirements

**Owner:** Scott
**Last updated:** 2026-02-10
**Feedback source:** [2-history-and-context-feedback.md](../1-feedback-synthesis/2-history-and-context-feedback.md)

---

## What this doc is

The **single source of truth** for what we're building in conversation history and context management. Requirements come from user feedback and get questioned before entering the backlog.

**Feedback lives elsewhere** — this doc links to it but doesn't duplicate it:
- [2-history-and-context-feedback.md](../1-feedback-synthesis/2-history-and-context-feedback.md) — raw quotes from Finn (Feb 6), Jack (Feb 3), Quentin (Feb 10)
- [3.1-policy-config-feedback.md](../1-feedback-synthesis/3.1-policy-config-feedback.md) — overlapping feedback from policy config sessions
- [UI-feedback-dev-tracker.md](../UI-feedback-dev-tracker.md) — backlog (this doc feeds into it)

---

## Raw Requirements

Gathered from user interviews. Not yet questioned or prioritized — applying [Musk's 5-Step Design Process](https://modelthinkers.com/mental-model/musks-5-step-design-process) next.

| # | Requirement | Who said it | Evidence | Priority signal |
|---|-------------|-------------|----------|-----------------|
| 1 | **Searchable conversation history** | Quentin, Finn | Quentin: "store conversations and easily search through them" — saves ~1hr/day. Finn: "If this worked and was nice, it'd be cool." | HIGH — two users, one quantified time savings |
| 2 | **Cross-session context injection** | Quentin | "Common knowledge for all employees." Wants context from past sessions automatically available in new sessions without manual copy/paste. | HIGH — Quentin's #1 priority, would pay |
| 3 | **Cross-user shared knowledge base** | Quentin | "Knowledge base across people." Team members' AI assistants should share a common context. | MEDIUM — one user, but aligns with B2B vision |
| 4 | **Clean history UI (not raw chunks)** | Finn | "Why present the chunks?" Activity Monitor is overwhelming. History should be "nicely clustered and easy to view the conversations." | HIGH — current UI actively repels users |
| 5 | **Cross-tool context transfer** | Finn | Uses Lovable (frontend), Claude Code (backend), Codex (SDK). "Didn't want to switch because Codex already has all the sessions." Context is siloed per tool. | MEDIUM — one user, but universal pain |
| 6 | **Session summaries / understanding debt** | Jack | Shifted from code review to "vibing" — accumulated "understanding debt." Implies need for post-session summaries of what the AI built. | LOW — inferred, not explicitly requested |
| 7 | **Meta-stats about AI usage** | Finn | "I would love to know when Claude Code thinks I'm stupid... in the reasoning traces." Wants to understand communication efficiency. | LOW — nice-to-have, one user |
| 8 | **Debug/reproduce via shared history** | Quentin | Sees B2B value in "reproducing bugs by sharing conversation history and verbose logs across team members." | MEDIUM — one user, but practical B2B use case |

---

## Step 1: Question every requirement

_TODO: Apply Musk Step 1 — each requirement should come from a named person. If you haven't questioned it recently, question it now. Ask: does this still hold? Should it be deleted?_

### What we already have

Before adding features, understand what Luthien already provides:
- **PostgreSQL storage of all conversations and tool calls** — this exists today. Quentin was excited about it.
- **Activity Monitor** — shows real-time data but is overwhelming (Finn: "way too much")
- **History page** — exists but had bugs during Finn's session. Needs polish, not a rebuild.

### Key open questions

1. **How does this relate to memories/CLAUDE.md?** Quentin's compliance jumped from 10% → 90% with project-specific memories (in the IDE, not in Luthien). Is Luthien's role to *be* the memory system, or to *feed* the existing memory systems (CLAUDE.md, IDE memories)?

2. **What's the smallest useful version?** Is it just "make the history page work and be searchable"? Or does it require context injection into new sessions?

3. **Cross-user sharing = security/privacy complexity.** Company-paid AI conversations are shareable, but users need a private mode. Quentin: "sharing company-paid AI conversations is acceptable, provided the user can switch to a private, unpaid session."

4. **Windsurf/Cursor compatibility.** Quentin's #1 pain is with Windsurf, which we can't proxy. Does this feature only work for Claude Code + Cursor users?

---

## Step 2: Delete any part you can

_TODO: After questioning, delete requirements that don't hold up. Target: delete at least 10% of what you initially wrote down._

---

## Step 3: Simplify and optimize

_TODO: Only after Steps 1-2. Collapse surviving requirements into the smallest set of things to build._

---

## Decisions made

_(none yet)_

## Open decisions

1. **Scope: history polish vs. context management system?** Two very different ambition levels:
   - **Option A: Polish history** — make existing history page searchable, clean UI (not chunks), session summaries. Low effort, already partly built.
   - **Option B: Context management system** — cross-session injection, cross-user knowledge base, IDE integration. High effort, new architecture.
   - **Recommendation:** TBD after more user feedback (EAG SF, Feb 14-16).

---

## Changelog

- **2026-02-10**: Created. Extracted history/context feedback from Quentin (Feb 10), Finn (Feb 6), and Jack (Feb 3) sessions. 8 raw requirements listed. Steps 1-3 not yet applied.
