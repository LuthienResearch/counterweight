# PR index

Every Railway-touching PR in `luthien-proxy`, grouped by arc. Load-bearing PRs in **bold**.

## Arc 1 — Jai Dhyani (Jan–Mar 2026)

| PR | Title | Merged |
|---|---|---|
| [#153](https://github.com/LuthienResearch/luthien-proxy/pull/153) | Deploy/railway demo | 2026-01-30 |
| [**#176**](https://github.com/LuthienResearch/luthien-proxy/pull/176) | **feat: `saas_infra` module for Railway multi-tenant provisioning** | 2026-02-05 |
| [#177](https://github.com/LuthienResearch/luthien-proxy/pull/177) | Railway Demo update | 2026-02-05 |
| [#212](https://github.com/LuthienResearch/luthien-proxy/pull/212) | fix: Railway deploy failures caused by PORT mismatch | 2026-02-19 |
| [#217](https://github.com/LuthienResearch/luthien-proxy/pull/217) | Railway demo update | 2026-02-19 |
| [#220](https://github.com/LuthienResearch/luthien-proxy/pull/220) | Update railway demo | 2026-02-19 |
| [#281](https://github.com/LuthienResearch/luthien-proxy/pull/281) | fix: remove hardcoded DB name from migration 008 | 2026-03-05 |
| [#334](https://github.com/LuthienResearch/luthien-proxy/pull/334) | Update railway | 2026-03-14 |

## Arc 2 — Peter Stoica (Mar–Apr 2026)

Scoping doc: [PR #434 draft: Railway cloud deployment scoping](https://github.com/LuthienResearch/luthien-proxy/pull/434).

| PR | Title | Merged |
|---|---|---|
| [#415](https://github.com/LuthienResearch/luthien-proxy/pull/415) | fix: Docker entrypoint breaks with SQLite DATABASE_URL | 2026-03-23 |
| [#416](https://github.com/LuthienResearch/luthien-proxy/pull/416) | fix: report all missing env vars at once on startup | 2026-03-23 |
| [#450](https://github.com/LuthienResearch/luthien-proxy/pull/450) | fix: auto-provision env var defaults for fresh PaaS deploys | 2026-03-26 |
| [#455](https://github.com/LuthienResearch/luthien-proxy/pull/455) | fix: local Docker build fallback when GHCR pull fails | 2026-04-01 |
| [#467](https://github.com/LuthienResearch/luthien-proxy/pull/467) | fix: prevent CDN caching of API responses on Railway/PaaS | 2026-03-30 |
| [**#497**](https://github.com/LuthienResearch/luthien-proxy/pull/497) | **feat: one-click Railway deploy (OAuth pass-through + default policies)** | 2026-04-09 |

## Adjacent / deploy-surface

Not pure Railway work, but touches the deploy surface and worth knowing.

| PR | Title | State |
|---|---|---|
| [#335](https://github.com/LuthienResearch/luthien-proxy/pull/335) | feat: integrate Sentry error tracking with two-layer data scrubbing | merged 2026-03-30 |
| [#531](https://github.com/LuthienResearch/luthien-proxy/pull/531) | fix: correct admin auth docs to match localhost bypass behavior | merged 2026-04-11 |
| [#515](https://github.com/LuthienResearch/luthien-proxy/pull/515) / [#516](https://github.com/LuthienResearch/luthien-proxy/pull/516) | feat: rich DB and Redis health checks on `/health` | open |
| [#517](https://github.com/LuthienResearch/luthien-proxy/pull/517) | feat: Prometheus `/metrics` endpoint | open |
| [#545](https://github.com/LuthienResearch/luthien-proxy/pull/545) | fix(cli): resolve `POLICY_CONFIG` to absolute path, populate empty config dir | open |
| [#550](https://github.com/LuthienResearch/luthien-proxy/pull/550) | fix(cli): skip `policy_config.yaml` write if file already exists | open |
| [#570](https://github.com/LuthienResearch/luthien-proxy/pull/570) | feat(health): report DB connectivity in `/health`, add `/ready` endpoint | open |

## Read order for getting up to speed

If you read exactly three: **#176**, **#497**, **#434**. That covers provisioning, the one-click flow, and the product framing. Everything else is texture.
