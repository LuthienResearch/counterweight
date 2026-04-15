# Phase 3 — Operate as a product

Weeks 9+ after kickoff (dependent on Phase 2 exit).

## Summary

Once real users depend on the hosted version, "it works" isn't enough. Phase 3 turns Railway deployment into something Luthien can point at and stop worrying about — defined SLOs, cost predictability per tenant, an upgrade story that doesn't break tenants, and a documented off-Railway path in case the economics ever change. End state: Luthien eng spends zero scheduled hours per week on Railway, and Railway-related inbound work routes to counterweight_ first.

## Context pointers

- Phase 2 must be in place. Phase 3 operationalizes a working product.
- The observability layer in `luthien-proxy` has Sentry (#335) and open PRs for Prometheus metrics (#517), health checks (#515/#516/#570). Use or extend those.
- Portability concern: Railway has historically been good for us, but hosted-PaaS economics shift. We're not planning to leave; we want to know we *could*.

## Deliverables

- [ ] **Defined SLO** — published. Example targets (subject to your recommendation): 99.5% request success, p95 added latency under 200ms. Dashboard that Luthien can open and see current-quarter SLO attainment.
- [ ] **Per-tenant cost model** + alerting when a tenant crosses a threshold. Abuse cases (runaway agent loops) and accidental cases (a tenant left a benchmark running) are real — you want to know before the bill does.
- [ ] **Upgrade story:** rolling new `luthien-proxy` versions to tenants without surprise breakage. Staged rollout + canary tenant + documented rollback playbook. At least one "canary tenant" agreed in advance (could be you).
- [ ] **Portability documentation:** a written path from Railway to another hosted substrate (e.g. Fly.io, Render, a user's own cloud). Doesn't need to be executed, but the knobs should exist and the gaps should be named. Lives in `luthien-proxy/deploy/portability.md` or similar.
- [ ] **Quarterly-review cadence** — a standing 60-minute quarterly meeting: counterweight_ + Scott walk SLO attainment, incidents, cost, and the next quarter's roadmap.
- [ ] **Incident playbook** — when something breaks, who does what, what's communicated to tenants, what's the postmortem format.

## Non-goals

- HA / multi-region. Railway is single-region by default; we're not buying 99.99%.
- SOC 2 / compliance work. Out of scope unless the commercial frame changes materially.
- Building a marketing site. Luthien handles that.
- Custom per-enterprise tenants with negotiated SLAs. If one shows up, it's a new ask — not a scope creep on Phase 3.

## Access needed

- Same as Phase 2, plus:
- Whatever SLO / dashboard tooling you pick (Grafana, Datadog, Railway-native, something custom)
- Cost-alerting backend (Railway usage API, third-party cost tooling, etc.)
- Read-only access for Scott to the SLO dashboard

## Success criteria

- **Zero scheduled Luthien eng hours per week** on Railway for a full month.
- **All Railway-related inbound** (support tickets, alerts, outage reports) routes to counterweight_ first by default. Luthien is escalation only.
- **SLO dashboard is live** and Luthien can read it without asking.
- **Staged rollout has shipped** at least one `luthien-proxy` version to tenants without a tenant-facing incident.
- **Portability doc exists** and at least one reader (Scott + one external technical reviewer, e.g. Jai at quarterly review) signs off that it's executable.

## Verification

- Week-by-week time tracking (honor system): Luthien logs zero Railway-domain hours for 4 consecutive weeks.
- Dashboard URL is in this repo's `README.md`.
- Rollout log shows at least one staged rollout completed without incident.
- First quarterly review happens within 90 days of Phase 3 start.

## Authority

- **You decide:** SLO targets (within reason — bring a recommendation to the first quarterly review), tooling choices, runbook/playbook formats, cost thresholds, canary tenant selection, rollout cadence.
- **Surface to Scott:**
  - Any SLO miss that would be tenant-visible (Scott decides tenant comms).
  - Any third-party spend that changes Luthien's monthly costs materially — threshold agreed at kickoff.
  - Quarterly review agenda items.
  - Commercial-frame evolution (Phase 3 is also when we should be evaluating whether the engagement structure still fits — propose changes to Scott).

Everything else: ship it.
