# Phase 1 — Stabilize the one-click flow

Weeks 1–3 after kickoff.

## Summary

The one-click Railway deploy works on paper but isn't bulletproof. We've merged ~10 "fix: deploy broke because …" PRs in the last six weeks. Users hitting one of those during a trial = a lost user. Phase 1's job is to close that gap — burn down the papercuts you identified in the dogfood day, and add the automation that would have caught them.

## Context pointers

- Read `progress/overview.md` and the fix-PR list in `progress/pr-index.md` for the class of rough edges we've been hitting.
- Your `adoption-log.md` and `recommendations.md` from the day-1 dogfood ask drive priorities. If those don't exist yet, do that first.
- Sentry is already integrated ([PR #335](https://github.com/LuthienResearch/luthien-proxy/pull/335)) but not routed to a named on-call. Wire it to a channel you monitor.

## Deliverables

- [ ] Burn down the **top-N friction items** from your dogfood recommendations. "Top-N" is your call — we'd expect at least 5, but the bar is "all the papercuts a new trial user would hit in the first hour."
- [ ] **Automated post-deploy smoke test** that runs on every merge to `main` in `luthien-proxy`: deploys to a throwaway Railway project, sends a request through the proxy, verifies `/activity` renders, tears the project down. CI-visible pass/fail.
- [ ] **Sentry → named channel** (Slack, email, PagerDuty — you pick). Luthien sees the channel in read-only mode; counterweight_ is first responder during Phase 1.
- [ ] **Status page** (as simple as a `/status` endpoint + a static page, or as fancy as you want) so a trial user can tell "is it me or is it them?"
- [ ] Your dogfood Luthien setup stays running unattended for a full week without you touching it.

## Non-goals

- Multi-tenant self-serve. That's Phase 2.
- Building an admin UI. Internal ops can stay CLI-driven for now.
- Rearchitecting the proxy itself. Stabilization means the *deploy* is stable; the proxy is out of scope.

## Access needed

- Same as day-1 ask, plus:
- Ability to spin up Railway projects programmatically (either Railway API token in your own account or a Luthien-provided one — your call in `open-questions.md`).
- CI write access on `luthien-proxy` (or Luthien runs the CI config you PR).
- Whatever channel you pick for pager routing.

## Success criteria

- **10 consecutive one-click deploys succeed unattended** (CI smoke test passes for 10 straight merges).
- **MTTFR < 5 minutes.** Mean time from "click deploy button" to "first successful proxied request." We'll measure this however you measure it — honor system.
- **Your dogfood setup runs for 7 consecutive days** without you opening the Railway dashboard.
- Every friction item in your recommendations doc is either shipped, filed as a Phase 2/3 item, or explicitly dropped with a reason.

## Verification

- CI history shows the smoke-test green streak
- Sentry → your channel delivers a synthetic test alert within 5 minutes
- `/status` (or equivalent) is reachable from a trial user's browser
- Scott does a fresh one-click deploy (no prep, cold account, timer on) and confirms MTTFR target

## Authority

- **You decide:** which friction items to fix, which tools to add (smoke test framework, status page shape, pager channel), how to instrument MTTFR, how to shape the CI config.
- **Surface to Scott:**
  - If a "friction item" turns out to be a product/strategy question (e.g. "the default policy config is wrong for trial users") — Scott weighs in before you ship a new default.
  - If Phase 1 is going to run over 3 weeks. Let us know by week 2 so we can adjust.

Everything else: ship it.
