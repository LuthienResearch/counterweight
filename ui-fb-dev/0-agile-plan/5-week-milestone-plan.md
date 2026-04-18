# Luthien Milestone Plan: March 12 → Demo Day (April 16)

**Key metric:** Total tokens through proxy from external users, trending up week-over-week
**Team:** Jai (surgeon/architect), Scott (copilot/BD), Peter (~10 hrs/wk, stability), Paolo (~25 hrs/wk, stability), Mike (~5 hrs/wk, content/UX)
**Constraint:** Scott out Thu Mar 13 – Mon Mar 17 (family). Jai fields trial calls during that window.

---

## Phase Framework

Three outreach phases, each informed by the previous, plus Demo Day as the milestone we're working backwards from.

### Phase 1: Live Handholding (Thu Mar 12) — WE ARE HERE

- Scott emails design partners with "book a call" link
- Scott and/or Jai sit with them 30 min, collect feedback from live call recording & transcript
- **Gate to Phase 2:** Clear onboarding communication + no showstopper bugs during a 30-min session

### Phase 2: Record Yourself (Wed Mar 18)

- Scott emails Wave 2 with improved instructions
- Users record their screen while setting up/using proxy on their own
- Incorporate feedback from recordings
- **Gate to Phase 3:** Need more telemetry with metrics to measure how users interact with the product when we're not on a live call or they're recording. Requires: (1) Scott & Jai define the most-important metrics in each user journey, and (2) Jai or other devs build that logging/telemetry into Luthien. Both must be 80% complete before moving to Phase 3.

### Phase 3: Free as a Bird / Beta Launch (TBD)

- Self-serve: users find us via landing page or GitHub, set up on their own
- Send launch announcement (strategy TBD: Signal + HN + email)
- Measure KPI (tokens through proxy) day-over-day and week-over-week
- In parallel: incorporate user feedback via [discord?/github?], update pitch deck (growth chart + user quotes + LOI)

### Demo Day (Apr 16) — Milestone, not a phase

- Graph of tokens through proxy going up and to the right + user quotes

---

## Phase 1: Live Handholding (Mar 12–17)

**Jai:**
- [CLI works: luthien-cli installable via pipx, runs setup, starts proxy](https://trello.com/c/hnF5IUh0) (Due: 3/12)
- [Implement 'luthien onboard' CLI (spin up server, get plain English command, start Claude running through proxy)](https://trello.com/c/5kVrFJXG) (Due: 3/12)
- [Document OAuth passthrough, make it default, make API usage obvious](https://trello.com/c/p9iKOQFy) (Due: 3/12)
- [Sign RSPAs + incorporation docs (waiting on Virgil to update)](https://trello.com/c/lJemdpCO) (Due: 3/14)
- [Book March flights for retreat](https://trello.com/c/p3IooZXu) (Due: 3/17)

**Scott:**
- [MILESTONE: March 12: Scott schedule send design partners emails; Wave 1 (handholding OK)](https://trello.com/c/ZNZTvue6) (Due: 3/12)
- [Action Jai's feedback on: instructions, landing page & readme](https://trello.com/c/KDFJNGHO) (Due: 3/12)
- [Get luthiencontrol.ai and luthienproxy.ai domains, redirect .org](https://trello.com/c/4yHLpDsS) (Due: 3/12)
- [Email angel investor pitch to friends](https://trello.com/c/y6yzcB6t) (Due: 3/12)
- [Sign RSPAs + incorporation docs (waiting on Virgil to update)](https://trello.com/c/Alall3uS) (Due: 3/12)
- [Book March flights for retreat](https://trello.com/c/xwCSZC5d) (Due: 3/11)
- [Add Bash Arena benchmark to agenda with Josh](https://trello.com/c/v06C2FdS) (Due: 3/19)

**Peter:**
- [Graceful failure handling](https://trello.com/c/YrsPj7kw) (Due: 3/14)
- [Surface upstream billing mode to prevent unexpected API charges (PR #311)](https://trello.com/c/0KbX3gHS) (Due: 3/14)
- [Triage & close Scott's stale draft PRs (#242, #233)](https://trello.com/c/9XrriEhc) (Due: 3/14)

**Mike:**
- [Book next Scott/Mike check-in for Tuesday or Wednesday of next week](https://trello.com/c/sH0FQv6w) (Due: 3/12)

### Phase 1 Blockers

- CLI delivery is the single gating item for Wave 1 emails and all trials
- If CLI slips, fall back to Docker quick_start.sh for Wave 1 (hand-held = acceptable)

### Phase 1 Success Criteria

- 5 design partner emails sent
- 3+ trials completed (even with hand-holding)
- CLI installable and working end-to-end
- First external tokens recorded

### Phase 1 Token Target

**50K tokens from 3+ external users** (hand-held sessions, ~20K tokens each)

---

## Phase 2: Record Yourself (Mar 18–19)

**Scott:**
- [MILESTONE: Schedule send Wave 2 design partner emails](https://trello.com/c/KSsm1WW6) (Due: 3/18)
- [Prep for Yoeri meeting Wed — include LOI discussion and partnership framing](https://trello.com/c/aQEFB0Qv) (Due: 3/18)
- [Draft newsletter to communicate our transition to PBC](https://trello.com/c/Zq9V4Vkz) (Due: 3/17, with Jai)
- [Cleanup people database rows 243+](https://trello.com/c/tH2S005D) (Due: 3/17)
- [Apply for ControlConf 2026 (+ workshop)](https://trello.com/c/XgJkF3ZT) (Due: 3/18)
- [Send Mike an audio message with context on the About section](https://trello.com/c/MNNeWGV5) (Due: 3/14)
- [Disable auth requirement when accessing from localhost by default](https://trello.com/c/hTmxXQDM) (Due: 3/19, with Paolo)

**Jai:**
- [Telemetry: total tokens through proxy (external users only)](https://trello.com/c/RnlApreP) (Due: 3/14)
- [Generate policy from claude.md](https://trello.com/c/j9DbbAaC) (Due: 3/18)
- [Implement default demo policies: logging URL + English language rules](https://trello.com/c/EPxaYuyD)
- [Cut everything below 'What You Get' in README.md, link to new dev-README.md / Rewrite quickstart](https://trello.com/c/BEZZRjmV)
- [Cloud offering setup (free tier for onboarding) [STRETCH]](https://trello.com/c/inDQOX5D) (Due: 3/19)
- [Implement one-click cloud deploy (Railway + OAuth pass-through)](https://trello.com/c/NLrSCTEK) (Due: 3/19)
- [Remove Codex support](https://trello.com/c/yxI4zALL)

**Peter:**
- [Add shellcheck --shell=bash to dev_checks.sh](https://trello.com/c/sz7MSkS0) (Due: 3/18)
- [Add bash 3 shebang comment convention to all scripts](https://trello.com/c/JFbhinBV) (Due: 3/18)
- [Bug: /compact fails with 'Tool names must be unique' error](https://trello.com/c/OUujiOqI) (Due: 3/18)
- [UX: Policy config page shows 'Reactivate' instead of 'Deactivate' for active policy](https://trello.com/c/lCyFZvyZ) (Due: 3/14)
- [Ship billing mode visibility PR with at least unambiguous ones](https://trello.com/c/TD5qZPbl) (Due: 3/19)
- [Error handling for insufficient cloud usage/credits](https://trello.com/c/Gr2XnN82) (Due: 3/18)
- [Review Paolo's 5 open PRs (#312-#316) and leave comments](https://trello.com/c/tkHGan83) (Due: 3/14)
- [Simplify timeout PR #310 — remove explicit packet timeout, keep logging and error handling](https://trello.com/c/X2eKWz0P) (Due: 3/14)

**Mike:**
- [Provide written feedback on what changed between v10.6 and v10.7 landing page copy](https://trello.com/c/vr0GPdfj) (Due: 3/14)
- [Install Claude Code and explain the difference between a PR, push, commit, merge, and a PR bot](https://trello.com/c/fVONgR6R) (Due: 3/18)
- [Review CodeRabbit, Qodo, Arch, and batch-mate websites and deliver a summary of positioning patterns Luthien should steal or avoid](https://trello.com/c/4yVUFzYU) (Due: 3/18)
- [Build a "Has this ever happened to you?" section on the landing page and recommend whether to test it with users or kill it](https://trello.com/c/RyZ5sv6U) (Due: 3/18)
- [Create a testable version of the landing page with AI safety mission higher, or explain why it's not worth testing](https://trello.com/c/tyBnuTKj) (Due: 3/18)
- [Answer whether an "About" section is worth building, relative to other landing page priorities](https://trello.com/c/5zmfQXgc) (Due: 3/18)
- [Decide whether the easter egg empathy concept is worth iterating on, and if yes, propose a non-tacky approach](https://trello.com/c/LmYNv2AT) (Due: 3/18)

**Paolo:**
- [UX: /history page shows sessions, not conversations — confusing first impression](https://trello.com/c/FR6FimBc) (Due: 3/18)

**Unassigned:**
- [Simplify quick start to 'ask Claude to do it'](https://trello.com/c/Tbtve4Jb)
- [Trial doc generic version for cold sends](https://trello.com/c/yQ0AMDNb)
- [Landing page: redesign concerns/objections section for cold engineers](https://trello.com/c/xrjkJY4t) (Due: 3/18)

### Phase 2 Success Criteria

- Improved install path that doesn't require hand-holding
- Wave 2 emails sent
- Telemetry counting tokens from external users
- One person completes self-serve install cold (no Slack, no hand-holding)

### Phase 2 Token Target

**200K tokens from 10+ external users** (mix of hand-held + early self-serve)

---

## Phase 3: Free as a Bird / Beta Launch (after Mar 19)

*This phase is almost entirely shaped by feedback from Phases 1 and 2. Items below are known anchors — everything else will be prioritized based on what we learn.*

- [Bash Arena benchmark: before/after Luthien safety + utility metrics](https://trello.com/c/87seMBXH) (Owner: Jai)
- [[HIGH] Integrate Sentry for error tracking](https://trello.com/c/BGMs38T6) (Owner: Peter, Due: 4/1)
- [[HIGH] Add Prometheus metrics endpoint](https://trello.com/c/O8DH9KOr) (Owner: Paolo, Due: 4/1)
- [[HIGH] Custom LLM metrics + Grafana dashboards](https://trello.com/c/yrFjc5GE) (Owner: Paolo, Due: 4/8)
- [Get credible quote for landing page (Fabian, OpenAI, etc.)](https://trello.com/c/NdXvs2vc) (Owner: Scott, Due: 3/20)
- [Video tutorial for README](https://trello.com/c/nG64tPrk)
- [Ask Marius who at Apollo is closest to lab conversations on control](https://trello.com/c/wLVme43P) (Owner: Scott, Due: 3/20)
- [Docker-free install path with SQLite support](https://trello.com/c/ZiJMNMAy) (if needed based on user feedback)
- [Metrics/bar chart -- nothing -> prompting -> Luthien](https://trello.com/c/TBSszp8Y)
- [Architecture diagram bigger on landing page](https://trello.com/c/IQZeyAcR)
- [Page flow restructure -- 'story down the page'](https://trello.com/c/Qcj0VCiB)

---

## Demo Day (Apr 16)

[MILESTONE: April 16 — Demo Day (tokens up-and-to-right)](https://trello.com/c/IYWrftZ4)

**Success criteria (from Finn/Esben):**
- Week-over-week token growth chart
- 2+ non-friend testimonials
- Self-serve onboarding works from landing page
- Horizontal tool story clear

---

## Token Growth Targets (aspirational)

| Phase | Target Tokens | Target Users | Milestone |
|-------|--------------|-------------|-----------|
| Phase 1 (Mar 12–17) | 50K | 3+ | First external tokens (hand-held) |
| Phase 2 (Mar 18–19) | 200K | 10+ | Record yourself — self-serve works |
| Phase 3 (Mar 20 – Apr 15) | 500K → 2M | 20+ → 50+ | Beta launch + repeat usage |
| Demo Day (Apr 16) | 2M+ | 50+ | Graph goes up and to the right |

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| CLI doesn't ship by Thu 3/12 | Delays Wave 1 emails | Fall back to Docker quick_start.sh for hand-held trials |
| Design partners don't respond to emails | No tokens, no growth | Scott does personal 1:1 outreach + live pairing sessions |
| Token growth is flat after Phase 2 | Weak Demo Day story | Pivot to live pairing sessions (generate tokens + testimonials simultaneously) |
| Showstopper bugs surface during trials | Users churn, bad word-of-mouth | Peter + Paolo on standby; Jai triages within 24 hrs |

---

*Created: 2026-03-11 | Updated: 2026-03-11 | Sources: Trello board state, design-sprint-part2-plan.md, mar05-demo-day-top10.md*
