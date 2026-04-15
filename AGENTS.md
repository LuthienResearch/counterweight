# AGENTS.md

Guidance for AI agents (and humans) working in this repo. Telegraphic — only things specific to this repo that you'd get wrong without guidance.

## Purpose

Vendor handoff brief from Luthien to counterweight_. Docs-only. No code expected here (for now). If scratch code ends up here, add structure before it grows.

## Decision authority

- **counterweight_ / Zach:** unilateral authority on Railway implementation — what to deploy, where, how to instrument, which tools, what to measure. Make the call, document it, move on.
- **Luthien:** authority on scope + strategy + customer requirements. Luthien will not second-guess implementation choices.

## What Luthien answers

- Business strategy (what Luthien is trying to become, target users, pricing model)
- Customer requirements (source data from user interviews available on request — spreadsheet link on ask)
- Changes to the defined phases (scope escalation or de-scope)

## What you answer from the docs

- Anything about `luthien-proxy` code, Railway mechanics, deploy architecture
- Tool choices (monitoring, alerting, CI, infra-as-code)
- Implementation timelines within an agreed phase
- "Is this decision reversible?" — if yes, ship it

## Invariants

- **`progress/` is historical record.** Read-only. If facts change, add a dated note in `CHANGELOG.md` — don't edit in place.
- **New asks go in `asks/`** and follow the template in [`asks/AGENTS.md`](asks/AGENTS.md).
- **Commits prefixed `docs:`** (this repo is docs-only).
- **Push directly to `main`** is fine here. No PR review required for this repo.
- **Each ask is self-contained.** No "see other ask first" chains.

## Anti-patterns

- Re-routing routine decisions through Luthien. If it's implementation, decide it.
- Duplicating content across ask files. Link instead.
- Speculative phases beyond Phase 3. The three defined phases are the current scope.
- Editing `progress/` to revise history.
- Long, discursive docs. Telegraphic and project-specific beats verbose and generic.

## Commit message style

`docs: <what changed in imperative mood>`

Examples:
- `docs: add day-1 dogfood ask`
- `docs: clarify pager-routing open question`
- `docs: update progress narrative after adoption log`

## Related reading

- [`CLAUDE.md`](CLAUDE.md) — Claude Code pointer
- [`luthien-proxy/AGENTS.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/AGENTS.md) — the codebase you'll work on (PR #583)
