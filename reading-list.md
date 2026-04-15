# Reading list

Recommended order for reading the `luthien-proxy` code. You don't need to read all of this before day 1 — but you'll want most of it before taking on Phase 1.

1. **[`deploy/README.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/deploy/README.md)** — user-facing one-click Railway flow. Updated in PR #497.
2. **[`railway.toml`](https://github.com/LuthienResearch/luthien-proxy/blob/main/railway.toml)** + Railway auto-detect block in `src/luthien_proxy/main.py` — how the server switches into Railway defaults when `RAILWAY_SERVICE_NAME` is present (PR #497).
3. **[`config/railway_policy_config.yaml`](https://github.com/LuthienResearch/luthien-proxy/blob/main/config/railway_policy_config.yaml)** — the default policy chain on Railway (DebugLoggingPolicy + SimpleLLMPolicy). PR #497.
4. **[`saas_infra/`](https://github.com/LuthienResearch/luthien-proxy/tree/main/saas_infra)** + its tests — Jai's Click CLI for multi-tenant Railway provisioning. Hybrid Railway-CLI / GraphQL architecture. PR #176. This is the foundation for Phase 2.
5. **[PR #434 scoping doc](https://github.com/LuthienResearch/luthien-proxy/pull/434)** — the original product framing for the one-click deploy.
6. **Fix PRs for the class of rough edges we've been hitting:** [#415](https://github.com/LuthienResearch/luthien-proxy/pull/415), [#416](https://github.com/LuthienResearch/luthien-proxy/pull/416), [#450](https://github.com/LuthienResearch/luthien-proxy/pull/450), [#455](https://github.com/LuthienResearch/luthien-proxy/pull/455), [#467](https://github.com/LuthienResearch/luthien-proxy/pull/467).
7. **[Root `AGENTS.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/AGENTS.md)** in luthien-proxy (PR #583) — invariants + anti-patterns for the codebase. Read this before opening a PR against luthien-proxy.

Also see:
- **[`CLAUDE.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/CLAUDE.md)** and **[`ARCHITECTURE.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/ARCHITECTURE.md)** for the fuller prose context
- **[`dev-README.md`](https://github.com/LuthienResearch/luthien-proxy/blob/main/dev-README.md)** for the dev loop (`./scripts/dev_checks.sh` runs format → type → test → complexity)
