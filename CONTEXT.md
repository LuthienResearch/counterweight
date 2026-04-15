# Context

## What Luthien is

Luthien is a proxy that enforces rules on AI coding agents (Claude Code, Codex, etc.). It sits between the agent and the model provider; policies run in the middle and can inspect, modify, block, or log traffic. It's an AI-safety nonprofit. Main codebase: [`LuthienResearch/luthien-proxy`](https://github.com/LuthienResearch/luthien-proxy).

## Who our users are

Senior developers living in agentic tools 40+ hours/week. They already pay for Claude subscriptions, they already use Claude Code as their IDE, and they already hit problems we want to solve (runaway agents, secrets in prompts, policies their employer needs enforced).

For those users to try Luthien at all, they need a hosted endpoint. Most won't run Docker Compose on their laptop to pilot a proxy.

## Why Railway specifically

Railway is the lowest-friction path to a hosted trial right now:

- **One-click deploy** — user clicks a button, gets a running gateway in a few minutes
- **OAuth pass-through** — user brings their own Claude subscription; no Luthien-owned API key to juggle
- **No DB setup** — Postgres + Redis provisioned by the template
- **Punt auth** — we're not pretending to be a secure SaaS yet; the trial is BYO-everything

This is a deliberate choice of "ship the trial path that has the fewest moving parts." It is not a multi-cloud commitment. If Railway's economics change, we want to be able to move; see `asks/phase-3-operate.md` for the portability requirement.

## End state Luthien is buying

**Luthien eng spends zero scheduled hours per week on Railway.** Inbound Railway-related work routes to counterweight_. Luthien stays focused on the product (policies, the proxy itself, user research) and treats hosted deployment as a domain someone else owns.

That's the shape of the engagement. The phases in `asks/` are how we get there.
