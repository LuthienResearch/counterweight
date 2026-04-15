# Phase 2 — Self-serve onboarding

Weeks 4–8 after kickoff (dependent on Phase 1 exit).

## Summary

Today, to onboard an external user, someone at Luthien runs `saas_infra create <tenant>` from a laptop. That doesn't scale past a few dozen users, and it keeps Luthien on the critical path for every signup. Phase 2 operationalizes the [`saas_infra`](https://github.com/LuthienResearch/luthien-proxy/tree/main/saas_infra) CLI (PR #176) into a self-serve flow: an external user signs up, gets a working endpoint, and makes their first request without any human touching a console.

## Context pointers

- [PR #176](https://github.com/LuthienResearch/luthien-proxy/pull/176) — the existing `saas_infra` Click CLI that provisions isolated per-tenant Railway projects. Hybrid architecture: Railway CLI subprocess for mutations, GraphQL for reads. Your foundation.
- The signup surface is **open** — web form on `luthienresearch.org`, Railway template + callback, a CLI that takes a GitHub OAuth and provisions, something else. Your call.
- User-interview data on what "signup" looks like to our target developer is available from Scott on request.

## Deliverables

- [ ] **Signup surface.** An external user hits it, provides minimum identifying info + OAuth, and triggers provisioning. Shape is your call.
- [ ] **Per-tenant domain + TLS.** Each tenant gets a stable URL they can point their Claude Code client at.
- [ ] **Per-tenant usage visibility.** At minimum: request count, last-active timestamp. Exposed in a way Luthien can see across all tenants, and each tenant can see for themselves.
- [ ] **Self-serve teardown.** User can delete their own instance without help.
- [ ] **Runbook** covering the common ops tasks (rotate secrets, upgrade image, roll back a tenant, investigate a failed provision). Lives in `luthien-proxy/deploy/runbook.md` or similar — your call on location.
- [ ] `saas_infra` CLI gets a thin CI harness (smoke test that exercises `create`/`status`/`delete` against a throwaway project).

## Non-goals

- SLAs, cost alerting, staged rollouts. That's Phase 3.
- Billing infrastructure. Phase 2 = "it works self-serve"; Phase 3 = "it works like a product."
- Custom per-tenant policy config at signup. Default policy is fine for now; customization is a future ask.
- Multi-cloud. Railway-native is fine.

## Access needed

- Same as Phase 1, plus:
- Domain control for the signup surface (subdomain of `luthienresearch.org` or a vendor-owned domain — your call in `open-questions.md`)
- Whatever third-party services you pull in (auth provider, TLS issuer, etc.)

## Success criteria

- **External-user end-to-end:** an external developer (not you, not Scott, not Jai) signs up, gets an endpoint, and makes their first successful proxied Claude Code request — all without a human at Luthien or counterweight_ touching a console. Timing: under 15 minutes from "clicked signup button" to "first request."
- **Support via runbook:** any common failure mode a new user would hit is recoverable by reading the runbook.
- **Per-tenant metrics are live** for at least 5 real tenants (your own, Scott's, and 3 external recruits).

## Verification

- Scott recruits an external developer (uncoached) and watches them attempt signup → first request. Timer on. Pass = they succeed without asking anyone a question.
- Runbook is readable end-to-end by Scott (who is not an engineer). Anything that requires "you just have to know" gets rewritten.
- `saas_infra` CI smoke test green for at least 10 consecutive runs.

## Authority

- **You decide:** signup-surface shape, auth provider, metrics stack, domain structure, runbook location + format, which third-party services to adopt.
- **Surface to Scott:**
  - Signup UX copy + onboarding messaging (that's customer-requirements territory — Scott cares about how we talk to users).
  - Anything that commits Luthien to a recurring third-party cost above a threshold — agree the threshold at kickoff.
  - If you find the `saas_infra` architecture needs a significant rewrite (not an extension). Wholesale rewrites go through Scott.

Everything else: ship it.
