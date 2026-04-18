# Design Sprint Part 2 — Board Reorganization Plan

**Created:** 2026-03-10
**Status:** Executed

## Context

Part 1 produced direction: CLI-first onboarding (`pipx run luthien-cli --help`), tokens-through-proxy as key metric, cloud offering, generate-policy-from-claude.md. Part 2 systematically reorganized Trello to execute against milestones.

**"Demo Day" (April 16)** = graph of tokens through proxy going up and to the right + user quotes about how much they love it. Not a stage presentation.

## Milestones

| Milestone | Date | Definition of Done |
|-----------|------|-------------------|
| Wave 1 (handholding) | Thu Mar 12 9am | Scott can email 5 design partners, hand-hold them through a 30-min trial where tokens flow through proxy. **Jai committed to CLI delivery by Thursday.** |
| Wave 2 (self-serve) | Wed Mar 18 9am | Cold engineer runs `pipx run luthien-cli --help`, has proxy running in 10 min, zero Slack messages to Scott. Design partner feedback from Wave 1 informs what "self-serve ready" actually means. |
| Demo Day | Apr 16 | Graph shows week-over-week token growth from external users, 2+ user quotes |

### March 12 Done Criteria
- Trial doc exists (generic, not Tyler-specific)
- Quick start works with hand-holding
- No showstopper bugs during a 30-min session
- Email copy written and ready to send

### March 18 Done Criteria
- CLI works: `luthien-cli` installable via pipx, runs setup, starts proxy
- Default demo policy loaded (logging + one English-language rule)
- Quickstart in README matches the CLI flow
- Token counting live (even if dashboard is basic)
- No showstopper bugs for 30 min of real use
- Team (Peter, Paolo) completes CLI onboarding successfully

> **TODO:** These criteria are minimum bar, not ambitious enough. Revisit after Wave 1 feedback from design partners — their feedback should directly inform what "self-serve ready" actually means.

### April 16 Done Criteria
- Telemetry dashboard showing tokens over time
- 5+ external users with real usage
- 2+ quotes from non-friends
- Landing page with benchmark results (if available)

## Owner Assignments

### Jai (priority order)
1. CLI: `luthien-cli` via pipx — **committed to Thursday Mar 12 delivery**
2. Telemetry: token tracking — the Demo Day metric, ~half day
3. Default demo policies — ~1 day
4. Rewrite quickstart — aligns with CLI
5. Cloud deploy free tier — STRETCH for Mar 18
6. Generate policy from claude.md — ~1 day
7. Remove Codex support — 16-25 hrs, 14 files, ~1500 lines (scope estimate from codebase scan)
8. Bash Arena benchmark — Mar 19-Apr 16 window

### Scott
- Wave 1 emails (Thu Mar 12)
- Seldon prep, flights, incorporation docs
- Design partner decisions
- Landing page negative content redesign (with Mike)
- Rollout phase tracking setup
- Newsletter for PBC transition
- Trial doc generic version

### Peter (~10 hrs/wk)
- Bug testing and re-testing
- Graceful failure handling
- Re-test bugs to confirm fixed vs remaining

### Paolo (~25 hrs/wk)
- Stability work

> **TODO:** Give Paolo more specific guidance on what "stability work" means — define concrete tasks and acceptance criteria.

### Mike (~5 hrs/wk)
- Landing page negative content (with Scott)
- Trial doc formatting

### Jen
- Tyler YouTube message (existing card)
- Email copy help

## Board Reorganization Summary (Executed 2026-03-10)

### Phase A: Triage Mar 18 Column
- **Started with:** ~80 cards in "Due Wed@9am (March 18)"
- **Moved to "after April 16":** 52 cards (SaaS infra, medium-priority code quality, testing, docs, policy internals, infrastructure not blocking demos)
- **Moved to "Mar 19-Apr 16":** 14 cards (benchmark, video tutorial, credible quote, landing page items, Apollo/Marius, Prometheus/Grafana, Docker-free install)
- **Kept in Mar 18:** ~14 cards (the real March 18 work)

### Phase B: Triage Mar 12 Column
- Kept 6 clearly-due-Thu cards
- Moved /compact bug + HTTPException format bug → Mar 18
- Moved 2 UX bugs → Mar 18
- Moved 4 medium bugs + alerting → after Apr 16
- Moved Sentry → Mar 19-Apr 16

### Phase C: Created 6 New Cards
1. Telemetry: total tokens through proxy (Jai) → Mar 18
2. Cloud offering setup [STRETCH] (Jai) → Mar 18
3. Generate policy from claude.md (Jai) → Mar 18
4. Landing page: redesign negative content (Scott) → Mar 18
5. Rollout phase tracking (Scott) → Mar 12
6. Graceful failure handling (Peter) → Mar 18

### Phase E: Done Criteria
Created MILESTONE cards with checklists in Mar 12, Mar 18, and Apr 16 columns.

### Phase G: Owner Assignments
All critical-path cards assigned to owners per plan.

### Phase A-extra: Codex Removal Scope
Updated "Remove Codex support" card with codebase scan results: 16-25 hours, 14 files, ~1500 lines. Jai to decide timing.

## Velocity Snapshot (2026-03-10, post-reorg)

| Column | Cards |
|--------|-------|
| Due Th @ 9am (March 12) | 8 |
| Due Wed@9am (March 18) | 24 |
| Mar 19 - Apr 16 | 16 |
| In Progress | 6 |
| Done | 5 |
| After April 16 | 57 |
| **Total** | **116** |

## Open Decisions

### Cloud vs CLI for March 18
**Recommendation:** CLI is must-ship. Cloud deploy is stretch goal — in Mar 18 column but marked [STRETCH]. If Jai finishes CLI early, cloud deploy is next. If not, Wave 2 still works.

### Benchmark Timing vs Hackathon (Mar 20-22)
**Recommendation:** Benchmarks in "Mar 19-Apr 16" column. Hackathon might be a good forcing function. Let Jai decide exact timing.
