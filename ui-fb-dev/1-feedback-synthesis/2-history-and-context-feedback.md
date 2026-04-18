# History & Context Management — User Feedback Log

> Modeled after [3.1-policy-config-feedback.md](3.1-policy-config-feedback.md)

## What this covers

Feedback related to **conversation history**, **cross-session context**, **cross-user knowledge sharing**, and **context management** — anything about preserving and reusing information across AI coding sessions.

This emerged as a distinct theme starting with Quentin (Feb 10 2026) but has roots in earlier sessions. Separated from policy config feedback because it's a different product surface.

---

## Session 1: Finn Metz (Seldon Labs)

- **Date:** Feb 6, 2026 (Thursday)
- **Full session:** [3.1-policy-config-feedback.md, Session 3](3.1-policy-config-feedback.md#session-3-finn-metz-seldon-labs)

### History / context feedback (extracted from full session)

1. **History feature has potential but needs work.** "If this worked and was nice, it'd be cool... nicely clustered and easy to view the conversations." Session didn't appear in history (bug).

2. **Wants raw API data accessible but not primary.** "I would love to play around with this some more, but get it in a nicer way." JSON is fine as a drill-down, not as the landing page.

3. **LLM transferability is important.** Siloed front-end in Lovable, back-end in Claude Code, SDK in Codex. "I didn't want to switch because Codex already has all the sessions." Wants seamless context transfer between models.

4. **Wants meta stats about Claude Code usage.** "I would love to know when Claude Code thinks I'm stupid... in the reasoning traces." Wants to triangulate the most efficient way to communicate with Claude.


## Session 2: Jack Wittmayer (Counterweight AI)

- **Date:** Feb 3, 2026 (Tuesday)
- **Full session:** [3.1-policy-config-feedback.md, Session 2](3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber)

### Context-related feedback (extracted from full session)

5. **"Understanding debt" from vibing.** Jack shifted from code review mindset to "viby" (ship fast) — accumulates "understanding debt." Lost track of what the AI actually built. Implies need for session summaries and history review.


## Session 3: Quentin Feuillade-Montixi (WeaveMind / Seldon Labs)

- **Date:** Feb 10, 2026 (Monday)
- **Forum:** Google Meet
- **Attendees:** Scott Wofford, Quentin Feuillade-Montixi
- **Full session:** [3.1-policy-config-feedback.md, Session 5](3.1-policy-config-feedback.md#session-5-quentin-feuillade-montixi-weavemind--seldon-labs)
- **Notes:** [Gemini notes](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/Scott%20%26%20Quentin%20Feuillade--Montixi%20-%202026%EF%BC%8F02%EF%BC%8F10%2009%3A46%20PST%20-%20Notes%20by%20Gemini.md), [Scott's discovery call notes](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/Quentin%EF%BC%8FLuthien%20discovery%20call.md)

**Key constraint:** Uses Windsurf. Cannot be a design partner. But this is his **#1 requested feature** — far above policy enforcement.

### Context management feedback

6. **Context management is his most common failure.** "I have to repeat myself." This is his biggest daily frustration with AI coding, above any policy compliance issue.

7. **Would pay for context building tools.** "I'd pay for something that's helping me build context." + "Knowledge base across people." Explicit willingness to pay.

8. **Cross-session context sharing.** Manually scrolls back through old conversations to find previous design decisions. Copy/pastes context back into new sessions. "Windsurf is horrible" for this.

9. **Cross-user knowledge sharing.** "Common knowledge for all employees would be crucial for future growth." Envisions a shared knowledge base that all team members' AI assistants can access.

10. **Time savings estimate: ~1hr/day.** "Could be 1hr/day not repeating myself." This is a concrete, quantifiable pain point.

11. **More valuable than policy enforcement.** Quentin "strongly suggested that cross-session and cross-user context sharing is a more valuable and difficult problem to solve than fixing minor AI mistakes like using 'npm' over 'pnpm'." He emphasized this multiple times.

12. **Conversation history excited him.** Lost an hour of feature design conversation recently. "Excited about" the PostgreSQL database storage of all conversations and tool calls. Saw immediate value in being able to search through past sessions.

13. **B2B value: context reconstruction for debugging.** Sees potential for reproducing bugs by sharing conversation history and verbose logs across team members. "Help Scott debug issues by reproducing bugs with shared conversation history."

14. **Memories dramatically improve compliance.** Before adding project-specific memories: ~10% compliance. After: ~90%. "Building context reduces the need for [me] to be involved." Implies that better context management tools would compound — they improve both productivity AND AI compliance.


## Session 4: Nicolás "Nico" Mesa (Veleiro)

- **Date:** Feb 9, 2026 (Sunday)
- **Full session:** [3.1-policy-config-feedback.md, Session 6](3.1-policy-config-feedback.md#session-6-nicolás-nico-mesa-veleiro)
- **Notes:** [Gemini transcript](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Nico/), [Nico's rules + CLAUDE.md](https://docs.google.com/document/d/1xTGh4_eNoK9zrCARg7ehhZTbFaLYkjR5x3sI9wJkxI4/edit?tab=t.0)

**Key constraint:** Not shown Luthien yet, but uses Claude Code (can route through Luthien). Builds Veleiro — an AI agent platform for Salesforce. Their agent interaction patterns are relevant to Luthien's history feature.

### History / context / agent visibility feedback

15. **Version history with diff comparison.** Veleiro shows version history per turn — users can compare current vs previous version to see "only what changed." Partially solves the "users don't read AI output" problem. "If they read it once and then ask for changes, they can see only what changed."

16. **Agent tool calls visible inline.** Their conversation UI shows agent thinking, tool calls (file edits, bash commands, glob searches), and validation results inline with the conversation. Similar to what Luthien stores in PostgreSQL but rendered visually.

17. **Progressive discovery of agent context.** Each folder in their virtual file system has a README that the agent reads on-demand — no upfront context dump. Reduces context window usage. Could inspire how Luthien surfaces context to users: show summary first, drill into details.

18. **CLAUDE.md as knowledge management.** Their CLAUDE.md got too big → split into topic files + `@file` references. Shows that even small teams need structured knowledge management for their AI rules. Related to Quentin's cross-session context pain.

19. **Sentry + Claude Code integration for debugging.** Created `/sentry-fix <issue-URL>` slash command — Claude Code reads logs, proposes fix. Relevant to Quentin's B2B vision of "reproducing bugs by sharing conversation history and verbose logs."

### UI inspiration for Luthien /history

Nico demo'd Veleiro's agent conversation UI during the call. Screenshot saved in [3-ui-mocks/2-history-and-context/](../3-ui-mocks/2-history-and-context/). Key features:
- Conversation thread with tool calls visible inline
- File system browser sidebar
- Diff/validation panel showing errors and corrections
- Version comparison across turns

Could inspire: interactive history (resume at a turn), detailed tool call logs, "what changed?" diff view.


## Cross-cutting themes

| Theme | Finn | Jack | Quentin | Nico |
|-------|------|------|---------|------|
| **Core pain** | Siloed context across tools (Lovable, Claude Code, Codex) | "Understanding debt" — lost track of what AI built | Repeating himself across sessions (~1hr/day) | CLAUDE.md too big, split into topic files + @file refs |
| **What they want** | Seamless context transfer between models | Session summaries, better history | Cross-session + cross-user shared knowledge base | Version history with diff, inline tool call visibility |
| **Would pay?** | Not explicitly | Not explicitly | Yes — "I'd pay for something that helps me build context" | Not discussed (builds his own tools) |
| **History feature reaction** | "If this worked and was nice, it'd be cool" | Not shown | "Excited about" PostgreSQL storage | Not shown Luthien, but built version history + diff in Veleiro |
| **Relationship to policies** | Wants LLM judge, not simple rules | Wants CLAUDE.md enforced | "Enforcing policies not as big for me" — context mgmt is bigger | Explicit CLAUDE.md rules with forbidden patterns + code examples |

### Emerging insight: Context management > policy enforcement?

Four signals suggest context management may be a higher-leverage product surface than policy enforcement:

1. **Quentin explicitly ranked it higher** than policy enforcement for his use case
2. **Finn's transferability pain** is about context, not policies
3. **Quentin's compliance data** shows that better context (memories) improves compliance more than rules do (10% → 90%)
4. **Nico's CLAUDE.md management** — even his 3-person team hit the "too big" wall and had to split into topic files + @file refs. Structured knowledge management is a universal need.

This doesn't mean policies don't matter — but it suggests that **good context management IS a form of policy enforcement**, and potentially a more effective one. Nico's approach (explicit rules with forbidden code patterns) shows the spectrum: his policies ARE his context.

---


## Session 5: Peter Teodosiu (QADNA)

- **Date:** Feb 25, 2026
- **Full session:** [3.1-policy-config-feedback.md, Session 8](3.1-policy-config-feedback.md#session-8-peter-teodosiu-qadna--qa-trial) · [TLDR](0-tldr-user-interview-takeaways.md#peter-teodosiu--qadna-qa-trial-feb-25-2026)
- **Peter:** CTO of QADNA. Runs 14 Claude Code instances daily. Building AI-driven QA SaaS platform.

### Context management feedback

20. **Context loss after compacting is uncontrollable.** "Especially after compacting, where that's not something you can actually control how well it compacts and how much it actually keeps around." Repeatedly-stated instructions forgotten after compaction events. Severity: high — directly impacts his automated QA workflows where 14 agents run in parallel.

21. **Agent drift under long unsupervised sessions.** "If you leave them unattended and unsupervised, they will just go to a very comfortable place... the end prompts were so conservative that they weren't really doing anything." Agents self-optimize for token savings, become overly conservative. Related to context degradation — as context grows, agents drift toward minimal-effort responses.


## Session 6: Tyler Tracy (Redwood Research, Mar 3)

- **Date:** Mar 3, 2026
- **Full session:** [1-value-prop-feedback.md, Session 12](1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback) · [TLDR](0-tldr-user-interview-takeaways.md#tyler-tracy--redwood-research-feb-10--mar-3-2026)

### Context-related feedback

22. **Meeting notes aggregation interest.** "Other 60% if I had all these meeting notes, pull my..." — Tyler sees value in aggregating context across sessions. Trails off in notes but signals demand for cross-session knowledge compilation.

23. **Dual-audience documentation problem.** Uses `claude.md` / `agent.md` symlink for Claude Code + Cursor interoperability. "Hard to write docs for humans and AIs." Docs aren't up to date because maintenance burden is high. Related to Nico's CLAUDE.md-too-big problem — team-wide documentation management is a pain point.


## Session 7: Sergi Lange-Soler (EAG SF, Feb 15)

- **Date:** Feb 15, 2026
- **Full session:** [TLDR](0-tldr-user-interview-takeaways.md#sergi-lange-soler--eag-sf-feb-15-2026)

### Context-related feedback

24. **CLAUDE.md compliance degrades over time (independent confirmation).** Instructions followed at start of conversation, then "kind of gets lazy and stops doing it." Third independent confirmation of context rot pattern (after Quentin and Josh).

25. **"Seems kind of similar to CLAUDE.md files" — differentiation question.** Sergi's first reaction to Luthien: "Can I just put this in the CLAUDE.md file?" The answer (context rot, enforcement, observability) is exactly why proxy-level context management matters.


## Session 8: Ronak Mehta (Mar 8)

- **Date:** Mar 8, 2026
- **Full session:** [TLDR](0-tldr-user-interview-takeaways.md#ronak-mehta-mar-8-2026)

### Context-related feedback

26. **Conversations are ephemeral — only artifacts matter.** "Conversations are ephemeral enough for me. The artifacts that are being created are the only thing I need." Represents the minority position: some power users don't value conversation history. His workflow (10K+ lines/day, tmux sessions) treats Claude Code as a disposable tool, not a knowledge partner.

27. **Separate tools for separate concerns.** "I don't want Claude Code to be the all-in-one thing." Has separate scripts for Git worktrees, tmux management. Prefers composable tools over integrated solutions. Counter-signal to the "one dashboard for everything" direction.


## Updated cross-cutting themes

| Theme | Finn | Jack | Quentin | Nico | Peter | Tyler | Sergi | Ronak |
|-------|------|------|---------|------|-------|-------|-------|-------|
| **Core pain** | Siloed context across tools | "Understanding debt" | Repeating himself (~1hr/day) | CLAUDE.md too big | Context loss after compacting; agent drift | Docs for humans AND AIs; meeting notes aggregation | CLAUDE.md compliance degrades over time | Conversations are disposable; artifacts are what matter |
| **What they want** | Seamless context transfer between models | Session summaries, better history | Cross-session + cross-user shared knowledge base | Version history with diff, inline tool call visibility | Instruction persistence through compaction | Cross-session context compilation | Proxy that adds value beyond CLAUDE.md | Composable tools, not all-in-one |
| **Relationship to policies** | Wants LLM judge, not simple rules | Wants CLAUDE.md enforced | "Enforcing policies not as big for me" | Explicit rules with code examples | Code for simple rules, LLM for subjective | Backward compat 60% FPR with cursor rules | "Seems like CLAUDE.md" — needs differentiation | Pre-tool-use hooks (type checkers, code review) |

### Updated emerging insight: Context rot as Luthien's sweet spot

Eight sessions now confirm the pattern:

1. **Quentin:** Context management is more common failure than policy violation. Compliance degrades with conversation length.
2. **Peter:** Compaction is lossy and uncontrollable. Instructions forgotten after compaction events.
3. **Josh Levy:** "Luthien will be maybe most effective in a context rot scenario" — identified this as the differentiation angle.
4. **Sergi:** CLAUDE.md compliance "kind of gets lazy" over time — independent confirmation.
5. **Tyler:** Dual-audience documentation problem; docs aren't up to date because maintenance is hard.
6. **Finn:** Siloed context across different LLM tools.
7. **Nico:** CLAUDE.md got too big, had to split and use @file references.
8. **Ronak:** Counter-signal — some users don't care about context persistence at all (artifacts-only workflow).

The proxy has a unique advantage here: it sees every request and response regardless of context window state. Post-compaction instruction re-injection (see [3.2-failures-policy-ideas.md](3.2-failures-policy-ideas.md#post-compaction-instruction-enforcement)) is a concrete product feature that addresses the #1 context pain point.

---

*Last updated: 2026-03-11 (added Sessions 5-8: Peter, Tyler Mar 3, Sergi, Ronak)*
