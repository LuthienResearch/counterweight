# Gateway Landing Page — Live Requirements

**Owner:** Scott
**Last updated:** 2026-03-19
**Feedback source:** Internal review (no user sessions yet)

---

## What this doc is

The **single source of truth** for what we're building on the gateway landing page (`/`). Requirements come from user feedback and get questioned before entering the backlog.

**Feedback lives elsewhere** — this doc links to it but doesn't duplicate it:
- [3.1-policy-config-feedback.md](../1-feedback-synthesis/3.1-policy-config-feedback.md) — overlapping feedback on first impressions and discoverability
- Policy config requirements doc has related info hierarchy analysis: [5-policy-config-requirements-live.md](5-policy-config-requirements-live.md#policy-config-information-hierarchy)

---

## Every version of this page

| Version | Date | What it was | UI Permalink | PR | Feedback |
|---------|------|-------------|-------------|-----|----------|
| **v0: Link directory** | Pre-Mar 2026 | Quick Start box + endpoint list with green left-border cards. Lists every endpoint (GET /health, POST /v1/messages, etc.) on the landing page. Developer-facing, no live data. | [index.html (pinned to 9220c0f)](https://github.com/LuthienResearch/luthien-proxy/blob/9220c0f7b99d53742a268804c54204b17987d41a/src/luthien_proxy/static/index.html) | - | No user feedback collected. Internal: "looks like a Swagger page, not a product." |
| **v1: Progressive disclosure** | Mar 2026 | Page cards with title + description + path. Collapsible Developer Reference. Inter + JetBrains Mono. Zinc palette, frosted-glass nav. | [index.html (pinned to 2ed7131)](https://github.com/LuthienResearch/luthien-proxy/blob/2ed71311311e6c6a6109f7ad0693c584a0302c5c/src/luthien_proxy/static/index.html) | [PR #379](https://github.com/LuthienResearch/luthien-proxy/pull/379) | Internal review only. Better hierarchy than v0, but still a link directory — no live data, no sense of "the proxy is running and doing things." |
| **v2: Dashboard with KPI scorecard** | Mar 19, 2026 | PBC-style sections (Activity / History / Policies / Developer). KPI cards (tokens, active policy, sessions, requests) powered by `GET /api/admin/stats`. Anchor nav on landing page. 2x2 card grid for Policies. Collapsible developer reference. | [index.html (pinned to 7e5b028)](https://github.com/LuthienResearch/luthien-proxy/blob/7e5b02897360fec01b76adb3f36a892515b6bb80/src/luthien_proxy/static/index.html) | [PR #387](https://github.com/LuthienResearch/luthien-proxy/pull/387) (closed, exploratory) | Internal review only. Better "proof it's running" feel. Open questions: KPI cards show "—" when unauthenticated — is that confusing? Should health/status be the hero instead? |
| **v3: Screenshots + human copy** | Mar 19, 2026 | Users see a preview of each page before clicking so they know what to expect. Copy tells users what they can do, not how the system works internally. Setup tasks (credentials, client config) separated from daily-use tools. Visual style matches public site per [design system](../design-system.md#cross-surface-consistency). | TBD | TBD | R1: status signal. R2: screenshots give users a map of what's available. R3/R4: admin vs non-admin access clarity. |

---

## Requirements

Gathered from internal review and adjacent user feedback (policy config sessions, onboarding). Not yet validated with users on this specific page. See also [0-uber-requirements.md](0-uber-requirements.md) and [README.md](README.md) for how to write requirements and design principles.

### Requirements

| # | Requirement (problem only) | Current state as of Wed Mar 19 | Key evidence |
|---|---------------------------|-------------------------------|-------------|
| R1 | <u>Proof of life.</u> Users should be able to tell whether the proxy is running. The proxy sits invisibly between the client and the API. Users need a signal that says "this is alive and working." | Gateway landing page is static. No live data, no health indicator, no request counts. | Policy config info hierarchy analysis (Mar 18): counters are "useful as a 'proof it's running' signal." [UX exploration](../ux-exploration.md): visibility of system status rated as primary gap. |
| R2 | <u>Feature discovery.</u> Users should understand what features are available to them once the proxy is running. The gateway has pages for monitoring, reviewing history, configuring policies, and viewing diffs, but users have no map. They either guess URLs or never find them. | Landing page lists page names and paths but gives no preview of what each page looks like or does. | Users bookmark subpages they've been shown but never discover pages on their own. [UX exploration](../ux-exploration.md) H6: recognition rather than recall rated "poor." |
| R3 | <u>Admin access.</u> As an admin, I should be able to access and configure all applicable pages from the gateway. Admin users need a single place to find every tool available to them, including setup and configuration tasks. | Admin features (credentials, client setup) are separate page cards at the same level as daily-use features. No admin-specific grouping. | Internal: admin features scattered across pages with no single entry point. |
| R4 | <u>Auth is opt-in.</u> Users should be able to use all gateway features without logging in when running locally. Authentication should be available as an opt-in feature, not a default gate. Luthien currently only runs locally, so requiring login creates friction with zero security benefit. | Login page takes over when clicking any authenticated page. No way to disable it. All local users are effectively admins. | Internal: Scott hates the login takeover pattern for local-only deployments. When Luthien supports shared/remote deployments, auth becomes relevant, but it should never be the default for local use. |

**Note:** "Technical details get in my way" (previously R3) was moved to design principles. It describes *how* to organize pages (progressive disclosure, developer reference subordinate), not a user problem. See [README.md](README.md#luthien-specific-design-principles).

### Questioning the requirements

**Not yet validated with external users.** Key questions to answer:

1. **Do users ever visit the landing page?** If they bookmark subpages directly, this page may not matter. Need to check with Finn and Josh.
2. **Is R1 real or assumed?** No user has said "I didn't know if the proxy was working." The closest evidence is from the policy config info hierarchy analysis, which was about a different page.
3. **Is R4 a real scenario?** How many deployments have unauthenticated visitors landing on `/`? If the answer is "basically none," R3 and R4 collapse into one requirement.

---

## Appendix A: 5 Whys — How we arrived at these requirements

1. **I just set up the proxy. Now what?** Setup finishes, Claude Code connects, but nothing tells me what to do next.
2. **Why not?** The proxy sits between my client and the API. It works silently. There's no feedback telling me it's running.
3. **Why does that matter?** I can't tell "working silently" from "broken silently." Without a signal, I don't trust it.
4. **Why can't I just check?** The gateway has tools for monitoring, history, policy config, and diffs, but I don't know they exist or where to find them.
5. **Root problem:** When I land on the gateway, I have no way to confirm the proxy is alive, understand what it's doing, or discover the tools available to me.
