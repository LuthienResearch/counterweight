# Day 1 — Dogfood Luthien

## Summary

You become user #1. Adopt Luthien for your own Claude Code and development-environment deploys. Whatever friction you hit becomes Luthien's backlog. This is simultaneously a vendor-fit test, user research, and the input that defines Phase 1 priorities.

**The question we want answered:**

> *What would it take for you to adopt Luthien in all of your own Claude Code and development-environment deploys?*

## Context pointers

- Start with [`deploy/README.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/deploy/README.md) for the one-click Railway flow (PR #497).
- If you'd rather run locally: `docker compose up` from the repo root is the standard dev loop. See [`dev-README.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/dev-README.md).
- You pick the deploy shape (Railway, local Docker, your own infra). Whatever lets you actually use the thing.

## Deliverables

- [ ] Route your own Claude Code traffic through Luthien for at least one full working day. (Railway one-click, local Docker, self-hosted — your call.)
- [ ] Keep a **friction log** — every place the product pushed back, broke, required off-path knowledge, confused you, or made you reach for the docs.
- [ ] Publish the log as `adoption-log.md` in this repo (PR to main, or push directly). Raw, unedited, timestamped. Don't clean it up — the rough edges are the data.
- [ ] File one GitHub issue per friction item worth fixing against `LuthienResearch/luthien-proxy`, labeled `railway-papercut` or `dogfood`. Link each issue to the adoption-log entry.
- [ ] Write a short recommendation: **"To adopt Luthien across all my Claude Code deploys, the top N things to change are…"** — ordered by impact to you. One paragraph per item is fine. Publish as `recommendations.md` in this repo.

## Non-goals

- Auditing the deploy docs end-to-end (that's a separate ask; don't get pulled in).
- Running PR #497's unchecked test-plan items as a verification script — *only* if they happen to be part of your own adoption path.
- Writing code changes to `luthien-proxy`. Day 1 is observation + documentation. Code changes come in Phase 1 once priorities are ranked.

## Access needed

- **GitHub:** TRIAGE on `LuthienResearch/luthien-proxy` (fork PRs also fine). Push access on this repo (`LuthienResearch/counterweight`).
- **Railway:** your own account, billed to you during the trial.
- **Claude subscription:** your own, for the OAuth pass-through test.
- **Anything else you need:** file a `question-for-luthien` issue here.

## Success criteria

Either of:

1. You're running Luthien in your daily workflow and routing your Claude Code traffic through it unattended.
2. You have a concrete recommendation doc explaining exactly what would need to change for you to.

Both outcomes are wins. A "I tried and bounced off here's why" is the most valuable version of this ask.

## Verification

- Adoption log exists as `adoption-log.md` in this repo.
- Recommendations doc exists as `recommendations.md` in this repo.
- Papercut issues filed in `luthien-proxy` (filter by your label).
- Scott reads the adoption log + recommendations once and confirms we have a backlog to run Phase 1 against.

## Authority

- **All implementation choices are yours:** where to deploy, how to instrument, whether to run locally vs. Railway, which friction items to consider "worth fixing."
- **Surface to Scott:**
  - Anything that feels like a customer-requirements question (does this even match what developers want?) — Scott has user-interview source data.
  - Anything that feels like a strategy/scoping question (is Railway the right substrate at all?) — Scott weighs in.

Everything else: decide, document the decision in the adoption log, move on.
