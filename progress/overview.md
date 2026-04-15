# Progress overview

Two arcs of Railway work happened in `luthien-proxy` before counterweight_ engaged.

## Arc 1 — Jai Dhyani's foundation (Jan–Mar 2026)

Jai built the Railway deploy scaffolding and the multi-tenant provisioning tooling. The load-bearing piece is [PR #176](https://github.com/LuthienResearch/luthien-proxy/pull/176) — a `saas_infra/` Click CLI that provisions isolated per-tenant Railway projects (Postgres + Redis + gateway) via a hybrid of Railway CLI subprocess (mutations) + GraphQL (reads). 71 unit tests, E2E-verified against live Railway at merge.

This arc established that **we can provision tenants programmatically**. It did not yet produce a one-click end-user flow.

## Arc 2 — Peter Stoica's hardening + one-click deploy (Mar–Apr 2026)

Scoping doc that framed the work: [PR #434](https://github.com/LuthienResearch/luthien-proxy/pull/434) — captured Jai's priority from a Feb 12 debrief: *one-click deploy, OAuth pass-through, punt auth.*

Peter delivered that as [PR #497](https://github.com/LuthienResearch/luthien-proxy/pull/497): auto-detect Railway via `RAILWAY_SERVICE_NAME`, set `AUTH_MODE=passthrough`, ship `config/railway_policy_config.yaml` with DebugLoggingPolicy + SimpleLLMPolicy chained. User flow: click deploy button → generate domain → `export ANTHROPIC_BASE_URL=https://…railway.app`. No keys, no DB setup.

The arc also includes ~5 fix PRs ([#415](https://github.com/LuthienResearch/luthien-proxy/pull/415), [#416](https://github.com/LuthienResearch/luthien-proxy/pull/416), [#450](https://github.com/LuthienResearch/luthien-proxy/pull/450), [#455](https://github.com/LuthienResearch/luthien-proxy/pull/455), [#467](https://github.com/LuthienResearch/luthien-proxy/pull/467)) — the class of rough edges we keep hitting when deploying to a fresh PaaS: missing env vars, SQLite-vs-Postgres entrypoint bugs, CDN caching, GHCR pull failures.

## State at handoff (2026-04-15)

- One-click Railway deploy **works** but has not been verified end-to-end by anyone outside Luthien. PR #497's own test plan has two unchecked boxes: "Manual test: deploy to Railway and verify one-click flow" and "Verify activity monitor works at `/activity`."
- `saas_infra` CLI is operational but internal-only — not exercised in CI, not wired to any self-serve signup surface.
- No automated smoke test runs against a live Railway instance after deploy.
- No monitoring/alerting tied to a named on-call. Sentry is available ([PR #335](https://github.com/LuthienResearch/luthien-proxy/pull/335)) but unrouted.

See `pr-index.md` for the full list of Railway-touching PRs.
