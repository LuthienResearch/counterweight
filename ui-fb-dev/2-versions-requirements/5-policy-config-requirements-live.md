# Policy Interface - Live Requirements

**Owner:** Scott
**Last updated:** 2026-03-18
**Branch:** `policy-config-ux` ([PR #175](https://github.com/LuthienResearch/luthien-proxy/pull/175))
**Sprint task:** [Trello card](https://trello.com/c/eAmMvvbd)

---

## What this doc is

The **single source of truth** for what we're building in the policy config UI. Requirements come from user feedback and get questioned before entering the backlog.

**Feedback lives elsewhere** - this doc links to it but doesn't duplicate it:
- [../1-feedback-synthesis/3.1-policy-config-feedback.md](../1-feedback-synthesis/3.1-policy-config-feedback.md) - raw quotes from Zac (Jan 30) and Jack+Zac (Feb 3)
- [UI-feedback-dev-tracker.md](UI-feedback-dev-tracker.md) - Goal 2 backlog (this doc feeds into it)

---

## Every version of this interface

> **To view HTML mockups in browser:** GitHub Pages is enabled. All UI links below render at `https://luthienresearch.github.io/luthien-org/...`. You can also run `cd /Users/scottwofford/build/luthien-org && python3 -m http.server 8888` and use localhost URLs.

| Version | Date | What it was | Requirements / Spec | UI Permalink | PR | User Feedback |
|---------|------|-------------|--------------------|--------------|----|---------------|
| **v0: Static prototypes** | Jul 2025 | Interview props - 3 Claude prototypes + 1 GPT variant. Not functional, just screenshots for user research. | None (exploratory) | [A](https://luthienresearch.github.io/luthien-org/_User-Interview-Notes/Static%20Prototypes/claude-prototype-a.html), [B](https://luthienresearch.github.io/luthien-org/_User-Interview-Notes/Static%20Prototypes/claude-prototype-b.html), [C](https://luthienresearch.github.io/luthien-org/_User-Interview-Notes/Static%20Prototypes/claude-prototype-c.html), [GPT](https://luthienresearch.github.io/luthien-org/_User-Interview-Notes/Static%20Prototypes/gpt_v1.html) | - | None - never shown to users |
| **v1: Wizard (3-step)** | Nov 2025 | Guided wizard: Select Policy -> Enable & Test -> Try Out. 3 hardcoded policies, mock backend, copy-paste test prompt. | [Spec v1](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_spec.md) | [policy_config.html](https://luthienresearch.github.io/luthien-org/Scott%27s%20folder/Policy%20Configuration%20UI/v1/policy_config.html) | [PR #56](https://github.com/LuthienResearch/luthien-proxy/pull/56) (closed), [PR #66](https://github.com/LuthienResearch/luthien-proxy/pull/66) (merged Nov 19) | Jai (PR #123): (1) Can't go back or jump steps, (2) Forced flow even when user knows what they want, (3) Bespoke nav doesn't match other pages. -> Replaced by v2. [Rationale](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_spec.md#redesign-single-page-layout-pr-123-dec-2025) |
| **v2/v3: Single-page + auto-discovery** | Dec 2025 - Jan 30, 2026 | Replaced wizard with single-page layout. Policy list on left, config on right. Auto-discovered policies from codebase. Live test chat panel. Same code for v2 and v3 - v3 was just v2 configured with SimpleJudgePolicy for the Zac demo. | [Spec v1 addendum](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_spec.md#redesign-single-page-layout-pr-123-dec-2025) | [policy_config.html](https://github.com/LuthienResearch/luthien-proxy/blob/bc7336e/src/luthien_proxy/static/policy_config.html), [policy_config.js](https://github.com/LuthienResearch/luthien-proxy/blob/bc7336e/src/luthien_proxy/static/policy_config.js) (pinned to PR #123 merge) | [PR #123](https://github.com/LuthienResearch/luthien-proxy/pull/123) (merged Dec 29), [PR #125](https://github.com/LuthienResearch/luthien-proxy/pull/125) (closed) | Internal only until Jan 30. **Session 1** (Zac, Mox SF) - [Feedback](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai). "Overwhelming and hard to use", wants meaningful defaults, no custom website. [Recording](https://drive.google.com/file/d/1lrTtPLt-yQC1W4v-67qp0HGzXXjSfNkJ/view?usp=sharing) |
| **v3A: Silent Retry** | Feb 3, 2026 | Mockup: Luthien retries automatically, user sees final result only. "Run completed - all issues auto-resolved." | [Spec v2 draft](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_v2_spec.md) | [Overview](https://luthienresearch.github.io/luthien-org/_UI_Specs/auto_retry_comparison.html), [Detail](https://luthienresearch.github.io/luthien-org/_UI_Specs/option-a-silent-retry.html) | - | **Session 2** - [Feedback](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-option-a-silent-retry-detail-view). Jack: "I don't know what it blocked... I'd want to see a diff." |
| **v3B: Retry + Summary** | Feb 3, 2026 | Mockup: Full single-page flow - connect, toggles, blocked log, notifications. Auto-retry with visibility. | [Spec v2 draft](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_v2_spec.md) | [Detail](https://luthienresearch.github.io/luthien-org/_UI_Specs/policy_mockup.html) | - | **Session 2** - [Feedback](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-option-b-full-single-page-flow-connect--toggles--blocked-log--notifications). Jack: "I generally like little toggles", wants customizable rules. [Recording](https://drive.google.com/file/d/1VAOakpCoDfiiuYfD8uJChT8mvmDgdXA0/view), [Notes](https://docs.google.com/document/d/1PqigfX9RMftttop9DL6nYzXXc8F_LEwv9Fu_w7pLE7X8/edit?tab=t.5mg62yupqygy) |
| **v3C: Block Only** | Feb 3, 2026 | Mockup: Just block, no retry. Claude figures it out or doesn't. Simplest option. | [Spec v2 draft](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_config_ui_v2_spec.md) | [Detail](https://luthienresearch.github.io/luthien-org/_UI_Specs/option-c-block-only.html) | - | **Session 2** - [Feedback](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber). Zac: still prefers async. Jack: prefers terminal notifications via hooks. |
| **v4: Dynamic forms** | Feb 4-5, 2026 | Schema-driven config forms auto-generated from Pydantic models. Recursive renderer, discriminated unions, dynamic arrays, server-side validation. | [Dynamic forms design](https://github.com/LuthienResearch/luthien-proxy/blob/policy-config-ux/docs/plans/2026-02-04-dynamic-policy-config-forms-design.md) | Live on `policy-config-ux` branch (run locally to see) | [PR #175](https://github.com/LuthienResearch/luthien-proxy/pull/175) (open) | Not yet shown to users. **Key question:** Users asked for toggles and simplicity, not schema-driven forms. |
| **v5: N/A** | - | Skipped. | - | - | - | - |
| **v6: DeSlop default (3 options)** | Mar 18, 2026 | 3 browser mockups with DeSlop as default policy. Option A: Toggles + Blocked Log. Option B: Live Demo First. Option C: Status Board. Built against 5 surviving requirements from Round 2. | [Round 2 requirements](#current-requirements-round-2--march-2026) | [Landing](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/v6-landing.html), [A](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/v6-option-a-toggles.html), [B](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/v6-option-b-demo.html), [C](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/v6-option-c-status.html) | - | **Finn live trial (Mar 18):** Option B winner. [Post-mortem](../3-ui-mocks/3-policy-config/v6-postmortem.md): non-functional UI elements, value described instead of demonstrated, simple replacement not enough, multi-policy invisible. |
| **v7: 6 mockups (3 browser + 3 terminal)** | Mar 18, 2026 | Evolved from v6 based on Finn, Josh, and Scott feedback. Browser: DeSlop+Multi-Policy, LLM Judge Demo, Style Guide Policy. Terminal: Inline Feedback, Blocked+Retry, Session Summary. | [Round 2 requirements](#current-requirements-round-2--march-2026) | [Landing](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/v7-landing.html) | - | Not yet shown to users. |
| **v8: Inspiration-driven redesign (failed)** | Mar 18, 2026 | 3 concepts x 2 formats = 6 mockups + index. Stole from thermostat, ad blocker, car warning lights, Gmail filters. Concepts: Scoreboard (big number + feed), Diff Viewer (split-pane), Terminal Native (live mirror + full CLI). **Failed:** all 3 concepts organized around activity/history instead of policies. Wrong information hierarchy. | [Round 2 requirements](#current-requirements-round-2--march-2026), [Info hierarchy](#policy-config-information-hierarchy) | [Index](https://luthienresearch.github.io/luthien-org/ui-fb-dev/3-ui-mocks/3-policy-config/2026-03-18_v8-inspiration-redesign/index.html) | - | Internal review (Scott): wrong primitives. Led to [information hierarchy](#policy-config-information-hierarchy) section defining the right org: policy → default config → example. |

---

## Current Requirements (Round 2 - March 2026)

**5 requirements.** Derived from 17 (original) -> 8 (Feb 8 Round 1) -> 5 (this pass). See [Appendix B](#appendix-b-prior-requirements-versions) for the full derivation and [plans/policy-config-simplification.md](../plans/policy-config-simplification.md) for the 5 Whys analysis.

### Requirements

| # | Requirement (problem only) | Current state as of Wed Mar 18 | Key evidence |
|---|---------------------------|-----------|-------------|
| R1 | <u>Obvious first value.</u> The user's first experience trying a policy must make Luthien's value obvious. | Current defaults (AllCaps/NoOp) were chosen for implementation simplicity, not user value. | [Zac S1](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai): "AllCaps is not meaningful." [Finn S3](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-3-finn-metz-seldon-labs): $20/mo for em-dash removal. [Josh S8](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-8-josh-slack-feedback): "em dash example hard to see the difference." [Bahar S4](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-4-bahar-super-bowl-demo): "Handle fundamentals." |
| R2 | <u>Meet users where they work.</u> Users must be able to interact with policies from where they already work - terminal or browser. "Interact" means the full Nielsen set: visibility of status, control, feedback, error recovery. | Policy interaction currently requires context-switching to a web UI that terminal-first users don't visit. CLI has zero policy management after onboard. | [Jack S2](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber): "I don't think I would check this UI." [Zac S1](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai): "I might not visit a custom website." Jai: "UIs communicate faster." |
| R3 | <u>See and control what's active.</u> Users must see what policies are active and be able to turn them on or off. Where additional configuration is needed, use progressive disclosure: logical defaults first, expose details only after the user has decided to enable the policy. | Users are asked to configure policies before understanding what they do. Complexity is front-loaded instead of revealed progressively. | [Finn S3](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-3-finn-metz-seldon-labs): "It's still unclear what I would use this for." [Zac S1](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai): "hide what's not user-relevant." [Bahar S4](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-4-bahar-super-bowl-demo): "Handle fundamentals so I can focus on domain-specific." |
| R4 | <u>Customize for context.</u> Users must be able to customize policies for their context - modify existing, import from CLAUDE.md, or add their own. Multiple policies must be active simultaneously. Use progressive disclosure: don't require understanding internals to get value from built-in policies. | Generic policies produce false positives, which destroy trust. Policies are most valuable when users can specify what matters to their stack. Users assume only one policy can be active. | [Jack S2](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber): "edit what I think are destructive operations." [Quentin S5](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-5-quentin): PNPM not npm. [Josh S8](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-8-josh-slack-feedback): "can't have multiple policies active at the same time?" [Tyler S7](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-7-tyler-tracy): 60% FPR. [Beth Anne S6](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-6-beth-anne): "specific requirements." |
| R5 | <u>Verify policies are working.</u> Users must be able to verify that policies are working - did a policy fire? What did it do? (Includes both real-time and retrospective review.) | No feedback mechanism surfaces policy decisions to the user. Policies act invisibly in the proxy layer. | [Jack S2](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber): "I would want to see something in Claude Code telling me what happened." [Zac S1](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai): "I want to see what got rejected." |

---

## Policy Config Information Hierarchy

**Added 2026-03-18** after v8 mockup exploration (3 concepts x 2 formats). The v8 concepts (Scoreboard, Diff Viewer, Terminal Native) all failed because they organized around the wrong primitives — activity/history (conversation → turn → policy actions) instead of policies themselves.

### The right hierarchy for this page

A new user lands on the policy config page. They haven't used the system yet. They need:

1. **Policy** — what is this thing? Name and one-line description.
2. **Default configuration** — what does it do out of the box? (Not "configure it" — show what's already configured.)
3. **Example** — what would this catch? A before/after or "here's what this blocks." The example need not come from the user's history — it can be a canned demo.

### What doesn't belong on this page (at first glance)

- **Scoreboard / running counts** — premature. The user hasn't gone through a session yet. (v8 Concept 1 mistake.)
- **Diff viewer as primary view** — gets the hierarchy backwards. The diff is evidence *for* a policy, not the organizing unit. (v8 Concept 2 mistake.)
- **Live activity mirror** — duplicative of the existing history/activity view. (v8 Concept 3 browser version mistake.)
- **History-first feed** — the history view already covers conversation → turn → policy actions. The config page should be policy-first.

### What survived from v8

- **Counter / dashboard** as secondary element: tokens through the proxy, turns processed, policy actions taken. Useful as a "proof it's running" signal (ad blocker analogy), but not the hero.
- **Before/after examples per policy** (from Scoreboard and Diff Viewer): these are the right *content* organized under the wrong *hierarchy*. Move them under each policy card.
- **"Gmail filter from example"** pattern (from Diff Viewer): create/edit rules from observed events, not from scratch. Good for customization flow (R4), not for first-time landing.
- **Session summary on exit** (from terminal mockups): still a good R5 (verify policies working) pattern for the terminal surface.

### Implication for current UI

The current policy config page (v4/PR #175) already has the right top-level hierarchy (policy list → config panel) but overwhelms with:
- Internal/dev policies visible to users (NoOp, AllCaps, Debug, Sample, Multi*)
- Gateway settings front-loaded (inject policy context, dogfood mode)
- Test panel prominent before user understands what policies do
- Schema-driven forms instead of "here's what this does, toggle it on"

The simplification path: hide what doesn't help a new user, add examples to what remains.

---

## Appendix A: Design Principles

### Progressive disclosure

**Core idea:** Show only what's needed at each stage. Don't overwhelm upfront. Let users pull complexity when they're ready. ([Nielsen Norman Group](https://www.nngroup.com/articles/progressive-disclosure/))

How we apply this to Luthien's user journey:

| Stage | What they see | What's hidden |
|-------|--------------|---------------|
| **1. README / landing page** | Tagline, 2 env vars, "what it does" | How policies work, API payloads, config options |
| **2. Quick start (docker compose up)** | Health check, "it's running" | Policy internals, YAML config, admin API |
| **3. Policy config UI** | Toggles (on/off), what got blocked | Policy code, threshold tuning, judge model selection |
| **4. "What kinds of policies can I create?" (expandable)** | Concrete examples: block commands, clean output, enforce scope, LLM judge | Writing custom Python, API payload details |
| **5. Create your own policy** | Python examples, lifecycle hooks, SimplePolicy base class | Orchestration internals, streaming chunk logic |

### Progressive disclosure audit

**Where we currently violate progressive disclosure:**
- README shows everything at once (Quick Start through Architecture through Admin API)
- Policy config UI (v4/[PR #175](https://github.com/LuthienResearch/luthien-proxy/pull/175)) exposes schema-driven forms before users understand what policies do
- Activity Monitor shows raw streaming chunks as the primary view ([Finn](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-activity-monitor--history): "Why present the chunks?")

**Where we already follow it:**
- 2 env vars to get started (minimal setup)
- Toggles hide policy complexity behind on/off ([Jack](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-option-b-full-single-page-flow-connect--toggles--blocked-log--notifications): "I generally like little toggles")
- Blocked log shows outcomes, not internals

### Decision: Both terminal and UI

**Zac's insight:** Some users don't want to look at a browser window. Terminal-first.

**Jai's insight:** We're past peak terminal usage. UIs communicate information faster - humans learn best with pictures. ([Reference](https://drive.google.com/drive/folders/1XNESbS95jrNosEpVOGbFCkszbCrF18Wh))

**Resolution:** We can have both. Terminal is the primary interface (where users already are). Web UI is for visual communication - setup, status, and reviewing what happened. Not a replacement for terminal, but a complement.

**What this means for PR #175:** Dynamic schema-driven forms are over-engineered for this. Replace with simple toggles (what Jack asked for) + connection instructions (what Zac asked for). The UI should be a quick visual overview, not a configuration IDE.

### Policy mental model - two types

**Design note - progressive disclosure:** Don't front-load this on the README. Users don't need to know how policies work to get Luthien running (that's just 2 env vars). Surface it in the policy config UI when they're already thinking about rules. See [Design of Everyday Things](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things): the user's conceptual model should roughly mirror how the system works.

The question from the user's perspective isn't "what data does the API expose?" - it's **"what kinds of policies can I create?"** Answer with two categories:

**Universal good defaults** (ship these on - dangers every team faces):
- Block dangerous commands (`rm -rf`, `git push --force`)
- Enforce package standards (`pip install` -> `uv add`)
- Catch PII exposure (block responses that contain or request sensitive data)
- Flag unknown dependencies (is this package legit?)

**Custom policies for your use case** (anything you can define in Python):
- Clean AI output (remove em dashes, curly quotes)
- Enforce scope boundaries (only edit files you asked about)
- Domain-specific compliance (e.g., internal LLM tool advises customers - make sure it cites the actual policy instead of hallucinating guidance)
- Log everything for audit

For both types, surface metrics: what got blocked, how often, which policies fired. See also R7 + [3.2-failures-policy-ideas.md](../1-feedback-synthesis/3.2-failures-policy-ideas.md) for user-sourced policy ideas with specific quotes.

---

## Appendix B: Prior Requirements Versions

### Historical decisions (Feb 2026)

These decisions were made during the Feb 2026 sprint. Preserved for context, but the v6/v7 mockups have superseded the open questions below.

1. **Terminal feedback mechanism (R3): Injected streaming message.** Luthien injects a message into the streaming response when it blocks an action. No hooks dependency, works with any client. (Decided Feb 8, Scott + Jai sync. [Recording](https://drive.google.com/drive/folders/1XNESbS95jrNosEpVOGbFCkszbCrF18Wh))

2. **Web UI scope** was debated (build v3B now vs. mockup-first vs. terminal-only). We chose mockup-first, which led to v6 and then v7. The "skip web UI" option was ruled out because UIs communicate faster for setup and status review (Jai, Feb 8).

3. **"What kinds of policies?" placement** - resolved: the v7 mockups show this as progressive disclosure within the policy toggle cards.

### Round 1 Requirements (Feb 2026)

Applied Musk Steps 1-2 on 2026-02-08 with evidence from 2-3 sessions. Took 17 original requirements down to 8. Superseded by Round 2 (March 2026) which collapsed these to 5.

Started with [17 requirements](#original-17-requirements-feb-2026) gathered from user interviews ([Zac, Jan 30](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai); [Jack + Zac, Feb 3](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber)) and internal decisions (Scott/Jai). Applied [Musk's 5-Step Design Process](https://modelthinkers.com/mental-model/musks-5-step-design-process) - questioned every one, deleted 5, deferred 4, questioned 2 more. Six survived. Full audit below.

[Finn's session (Feb 6)](../1-feedback-synthesis/3.1-policy-config-feedback.md#session-3-finn-metz-seldon-labs) validated several existing requirements and added #4 below (mental model). His feedback also suggests future requirements not yet in this list - e.g., remove Docker dependency, LLM-powered judge for complex patterns, DeSlop as a demo policy.

| # | Requirement | Who asked | What "done" looks like |
|---|-------------|-----------|----------------------|
| R1 | **Meaningful default policy** | Zac | SimpleJudgePolicy (or similar) ships as default, not AllCaps/NoOp. Backend decision - not a UI requirement. |
| R2 | **Config -> Claude Code path** | Zac | 2-step setup instructions visible on policy page: set ANTHROPIC_BASE_URL, run `claude`. |
| R3 | **Results in terminal, not web UI** | Jack + Zac | Blocked actions appear in Claude Code output (hooks? streaming message?). #1 cross-cutting theme from both users. |
| R4 | **Customizable rules** | Jack | User can edit what gets blocked. Could be YAML config, CLAUDE.md, or UI toggles - doesn't need a web UI. |
| R5 | **Toggle switches** | Jack | Policies shown as on/off toggles, not complex forms. |
| R6 | **End-of-run summary** | Zac | Summary of blocked items shown after agent completes. Where? Terminal > web UI per both users. |
| R7 | **Support user-sourced policy types** | Quentin, Nico, Beth Anne, Jack, Tyler | Implement policies described in [3.2-failures-policy-ideas.md](../1-feedback-synthesis/3.2-failures-policy-ideas.md): backward compat detection (Tyler: 60% FPR on cursor rules), plan abandonment, DRY enforcement, package manager standards, suspicious package flagging, silent failure detection, unnecessary code changes, enforce team utility usage (Tyler), require proof of testing in PRs (Tyler). Each idea has named sources + quotes. |
| R8 | **Allow users to modify/customize existing policies** | Quentin, Beth Anne | Users don't want generic built-in policies; they want to customize parameters for their stack. Quentin: pnpm not npm ("I'm always using PNPM instead of npm"). Beth Anne: "I have specific requirements on how and what to install." Beyond toggles (R5): once a policy is on, let users change what it enforces. Could be: editable config fields in UI, YAML editing, or CLI flags. See [cross-cutting note in 3.1](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-policies-ranked-by-his-interest) and [customization angle in 3.2](../1-feedback-synthesis/3.2-failures-policy-ideas.md#enforce-package-manager-standards). |

#### Round 1 Step 3: Simplify and optimize

The 8 surviving requirements collapsed into **4 things to build:**

| # | What to build | Why | Simplest version | Owner |
|---|---------------|-----|------------------|-------|
| 1 | **Ship meaningful default policy** | Zac: "AllCaps is not meaningful. 'Block jailbreaks' is meaningful." (R1) | Set SimpleJudgePolicy as default in `policy_config.yaml`. Config change, not a feature. | Scott (config) |
| 2 | **Web UI: toggles + connect + blocked log** | Jack: "I like toggles." Zac: "Show me how to test in Claude Code." (R2, R5, R6) | One page. Toggle policies on/off, 2-step Claude Code setup instructions, log of what got blocked. Basically v3B - Jack already liked it. | Scott (mockup -> validate -> build) |
| 3 | **Terminal feedback when actions blocked** | Jack + Zac both want results in terminal, not a browser. #1 cross-cutting theme. (R3, R4, R6) | Blocked actions appear in Claude Code output. Customizable rules = the toggles ARE the customization (on = enforced, off = not). | Scott (UX design) -> Jai (implementation) |
| 4 | **Show users what kinds of policies they can create - framed as two types** | [Finn](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-policies): "It's still unclear what I would use this for." Super Bowl demos (Feb 8): users can't imagine policies because they don't know what's possible. [Bahar](../1-feedback-synthesis/3.1-policy-config-feedback.md#feedback-on-universal-vs-custom-policies): "Handle fundamentals so I can focus on domain-specific." | Expandable "What kinds of policies can I create?" section showing two categories: (1) **Universal good defaults** - dangers every team faces (rm -rf, wrong package manager, secrets in code). Ship these on. (2) **Custom policies for your use case** - domain-specific rules in Python (clean AI slop, enforce scope, compliance). Include concrete examples per category. Surface metrics where available (what was blocked, how often). See R7 + [3.2-failures-policy-ideas.md](../1-feedback-synthesis/3.2-failures-policy-ideas.md) for specific policy ideas from users. | Scott (UX design) |

**What got simplified away:**
- Dynamic schema-driven forms -> toggles
- Separate "customizable rules" feature -> toggles ARE the customization
- Separate "end-of-run summary" -> same as terminal feedback + blocked log in UI
- Config -> Claude Code as its own feature -> it's just 2 lines on the toggle page

### Original 17 requirements (Feb 2026)

All 17 requirements questioned. Every requirement must have a **named person** who asked for it.

| # | Requirement | Who said it | Evidence | Verdict |
|---|-------------|-------------|----------|---------|
| 1 | **Web UI for policy config** | Scott/Jai (internal) | No user asked for this. Zac: "if I have to visit a custom website, I might not visit that." Jack: "I would want to see something in Claude Code." | **QUESTION** - both users push toward terminal/GitHub. May only be useful for setup + demo. |
| 2 | **Dynamic schema-driven forms** | Scott/Jai (internal) | PR #175 - auto-generate forms from Pydantic models | **QUESTION** - users want toggles and simplicity, not schema-driven forms. Over-engineered for current policies. |
| 3 | **Meaningful default policy** | Zac | "AllCaps is not meaningful to me. 'Block jailbreaks' is meaningful." | **KEEP** |
| 4 | **Direct path: config -> Claude Code** | Zac | "It should say right here, here's how you can test with Claude Code" | **KEEP** |
| 5 | **Surface results in terminal, not web UI** | Jack + Zac | Jack: "I would want to see something in Claude Code telling me what happened." Zac: "if I have to visit a custom website, I might not." | **KEEP** |
| 6 | **Customizable destructive ops list** | Jack | "edit what I think are destructive operations, or just things I don't want it to do ever" | **KEEP** |
| 7 | **Import rules from CLAUDE.md** | Scott (idea) | Triggered by Jack's feedback, but Jack didn't ask for this | **DELETED** - Scott's inference, not a user request |
| 8 | **Rate-based spending alerts** | Jack | "notify when churning through credits faster than normal" | **DEFERRED** - real need, separate feature |
| 9 | **Policy-as-automated-QA** | Zac | "evaluate original prompt vs final agent message" | **DEFERRED** - policy type to build, not UI |
| 10 | **Auto-retry on blocked actions** | Zac | "wants Claude to automatically retry when blocked" | **DEFERRED** - backend behavior, not UI |
| 11 | **Wizard flow (3 steps)** | Scott/Jai (internal) | Spec v1, Nov 2025 | **DELETED** - already replaced in PR #123 |
| 12 | **Test chat panel in web UI** | Scott/Jai (internal) | Spec v1 & v2 | **DELETED** - Zac: "This is good for you guys as a debugging thing." |
| 13 | **Global status bar** | Scott (v2 spec) | No user asked for this | **DELETED** - over-engineering |
| 14 | **Database overview UI** | Scott (tracker) | No user asked for this | **DELETED** - no evidence anyone wants this |
| 15 | **Notifications (email/Slack)** | Zac + Jack | Zac: email/Slack. Jack: terminal ping via hooks. | **DEFERRED** - separate from policy config |
| 16 | **Policy toggle switches** | Jack | "I generally like little toggles" | **KEEP** |
| 17 | **Show what got blocked (end-of-run summary)** | Zac | "When it's finished... that's when I want to see what got rejected" | **KEEP** |
| 18 | **Policy metrics / measurement at scale** | [Bahar](../1-feedback-synthesis/3.1-policy-config-feedback.md#testing-and-metrics-at-scale) | "Testing is a HUGE problem." Policy creation is 3 parts: knowledge, detection, enforcement - but without measurement you can't improve any of them. Need: what got blocked (already stored in Postgres), false positive rates, edge case detection. Future: QA-as-seeds -> synthetic perturbations -> active learning loop. "Detecting that 0.01% is very hard." Even for individual users, basic metrics matter - "how many times did this policy fire today?" is the difference between trust and guessing. | **DEFERRED** - coming soon. Basic metrics (block count, policy fire rate) are low-hanging fruit from existing data. Advanced metrics (false positive rate, synthetic testing) require labeled data and are further out. |

#### Deleted (5) - should not exist
- #7 Import rules from CLAUDE.md - premature, Scott's inference
- #11 Wizard flow - already dead
- #12 Test chat panel - internal tool, not user-facing
- #13 Global status bar - no user asked
- #14 Database overview UI - no user asked

#### Deferred (6) - real needs, wrong workstream
- #8 Rate-based spending alerts -> separate feature
- #9 Policy-as-automated-QA -> new policy type
- #10 Auto-retry on blocked actions -> backend behavior
- #15 Notifications email/Slack -> separate feature
- #18 Policy metrics / measurement at scale -> coming soon. Basic metrics (block count, fire rate) from existing Postgres data are low-hanging fruit. Advanced metrics (false positive rate, synthetic testing, active learning) further out. Bahar: "If you're thinking about AI safety, [testing] has to be part of the conversation."
- #19 **Plan abandonment detection** -> new policy type. Quentin (Feb 10): AI silently switched from Kubernetes to Terraform mid-task. "AIs HATE FAILURE." Wants: detect when AI changes plans, force stop and ask. See [3.2-failures-policy-ideas.md](../1-feedback-synthesis/3.2-failures-policy-ideas.md#detect-plan-abandonment--short-circuiting).

---

## Changelog

- **2026-02-08**: Created. Applied Musk Steps 1-2 to all 17 requirements. Deleted 5, deferred 4, kept 6. Moved full audit to appendix.
- **2026-02-08**: Added S4 (mental model for policies) based on Super Bowl demo observation. Added progressive disclosure design principle section.
- **2026-02-08**: Added #18 (policy metrics / measurement at scale) from Bahar's Super Bowl feedback. Deferred but flagged as coming soon - important for any team use case.
- **2026-02-08**: Incorporated Bahar's full policy config feedback. Updated #4 to frame policy examples as two types (universal defaults + custom). Enriched #18 with basic vs advanced metrics distinction. Updated design note examples to show two-category framing with metrics reference. Added Bahar to ../1-feedback-synthesis/3.1-policy-config-feedback.md as Session 4.
- **2026-02-10**: Renumbered requirements from legacy audit numbers (3,4,5,6,16,17) to R1-R6. Added R7: support user-sourced policy types (links to 3.2-failures-policy-ideas.md). Updated all internal cross-references. Added debrief transcript links to 3.2-failures-policy-ideas.md sources.
- **2026-02-10**: Added R8: allow users to modify/customize existing policies. Sourced from Quentin (pnpm vs npm customization) and Beth Anne (specific install requirements). Updated 3.1 feedback synthesis with cross-cutting observation, 3.2 with customization angle. Created 3 UI option mockups in ui-fb-dev/3-ui-mocks/3-policy-config/.
- **2026-02-10**: Added Tyler Tracy (Session 7) to 3.1 feedback synthesis. Added 3 pain points as policy ideas to R7 + 3.2: backward compat (60% FPR signal), enforce team utility usage (new), require proof of testing in PRs (new). Updated cross-cutting themes table.
- **2026-03-18**: Round 2 simplification - 5 Whys on all 8 requirements with 12 sessions of evidence. Collapsed R4+R7+R8 into R4 (customization for context accuracy), R6 into R3 (both are policy visibility), reframed R5 (progressive disclosure, not toggle switches). 8 -> 5 requirements. Round 1 requirements preserved as historical record. Full analysis: [plans/policy-config-simplification.md](../plans/policy-config-simplification.md).
- **2026-03-18**: Doc cleanup - added v6+v7 to version table with GitHub Pages permalinks. Removed "What got collapsed" explainer from requirements section (one-line appendix link instead). Moved decisions made/open decisions to Appendix B as historical. Top of doc is now: version table -> 5 requirements -> done.
- **2026-03-18**: v8 inspiration-driven redesign attempted and failed. Added "Policy Config Information Hierarchy" section capturing what we learned: the right hierarchy is policy → default config → example, not activity → turn → policy action. v8 mockups (Scoreboard, Diff Viewer, Terminal Native) all organized around the wrong primitives. Key salvage: before/after examples belong under each policy card, counter as secondary "proof it's running" element, session summary for terminal R5.
