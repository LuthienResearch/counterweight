# UI Feedback and Development Tracker

**Purpose**: Track progress toward validated product-market fit using the [Learn More Faster](https://www.gv.com/research-sprint) methodology.

**Document owner**: Scott

---

## Goals Overview

| Goal | Description | Key Metric |
|------|-------------|------------|
| **Goal 1a** | Recruit design partners | 5 developers committed to biweekly calls despite bugs |
| **Goal 1b** | Dogfooding (paused til post-EAG) | Scott & Jai can use Luthien daily for real work |
| **Goal 2** | Unblock live external user trials | 3 external users successfully complete a guided session including seeing convo history and testing a policy |
| **Goal 3** | Unblock independent user trials | Users can try Luthien without hand-holding |

**Learn More Faster principle**: Each goal builds toward the next. We validate assumptions at each stage before investing in the next.

---

## Feedback Loop

Every piece of user feedback should flow through this pipeline:

```
Capture feedback → synthesize feedback → better requirements → better UI → repeat
```

Mapped to folders:
- **0-outreach4feedback/**: outreach planning, EAG workflow
- **1-feedback-synthesis/**: raw transcripts, quotes, theme synthesis
- **2-versions-requirements/**: consolidated requirements (policy config + value prop)
- **3-ui-mocks/**: UI specs and mockups that get updated based on requirements

### Raw feedback capture locations

- **Otter.ai transcripts:** Auto-generated from recorded calls. Search via `mcp__otter__otter_search`.
- **Google Docs (Gemini meeting notes):** Auto-generated for Google Meet calls. Live in `_User-Interview-Notes/` on Luthien Google Drive.
- **In-person notes:** Photos, sticky notes — filed in `1-feedback-synthesis/`.

### Full pipeline flow

```
Raw source (Otter/Gemini/notes) → 1-feedback-synthesis/ → 2-versions-requirements/ → 3-ui-mocks/ → code PRs
```

### More calls = faster loop

```
  1a:      1b:
OUTREACH  DOGFOODING
(calls,   (paused til
 demos)    post-EAG)
    │        │
    └───┬────┘
        │
        ▼
  CAPTURE FEEDBACK ──→ SYNTHESIZE FEEDBACK
        ▲                      │
        │                      ▼
    BETTER UI ◄──── BETTER REQUIREMENTS
```

More outreach = more calls = the loop spins faster. EAG SF is a chance to spin this loop 5-10x in one weekend. [Musk's 5-Step Design Process](https://modelthinkers.com/mental-model/musks-5-step-design-process) is how we get from raw feedback to better requirements: question every requirement, delete what you can, then simplify.

---

## Goal 1a: Recruit Design Partners

Find 5 developers willing to commit to biweekly calls despite bugs. These partners complete Goals 2 & 3 — they do the guided and external trials.

**Design partner criteria:**
- Uses AI coding agents daily
- Frustrated enough to tolerate early-stage software
- Willing to do biweekly 30-min calls for 3+ months

**Known adoption blockers:**
- **Windsurf** doesn't support custom proxy servers → blocks any Windsurf user from using Luthien. Quentin (Feb 10) blocked by this. Possibly intentional (protecting their context-building IP).

---

## Goal 1b: Dogfooding (paused until after EAG SF)

Blocked on backend bugs (Jai's bandwidth). Scott is pausing effort here until after EAG SF and focusing on outreach (Goals 2 + 3).

---

## Goal 2: External Guided Trial + Required Features

**Definition of done**: One external user can complete a guided 30-minute Luthien trial with Scott facilitating.

### User Journey (Guided Trial)

1. **Setup** (5 min): User has Luthien running locally
2. **First conversation** (10 min): User sends prompts through Luthien proxy
3. **View history** (5 min): User sees their conversation in `/history` UI
4. **Understand logging** (5 min): Overview of what's captured in the database
5. **[Future] Policy demo** (5 min): Show a simple policy in action

### Backlog

Prioritized feature list. Feedback drives reprioritization — raw feedback lives in [1-feedback-synthesis/3.1-policy-config-feedback.md](1-feedback-synthesis/3.1-policy-config-feedback.md). Sprint tasks live in [Trello](https://trello.com/b/ehoxykPf/luthien).

| Priority | Feature | Status | Source | Links |
|----------|---------|--------|--------|-------|
| P0 | Dynamic policy config forms | In progress | Zac: "overwhelming and hard to use" → simplify | [PR #175](https://github.com/LuthienResearch/luthien-proxy/pull/175) |
| P0 | Meaningful default policy (not AllCaps) | Not started | Zac: "AllCaps is not meaningful to me" | |
| P0 | Direct path from config → Claude Code | Not started | Zac: "It should say right here, here's how you can test with Claude Code" | |
| P1 | Surface results in terminal, not custom UI | Not started | Jack: "I would want to see something in Claude Code telling me what happened"; Zac: "if I have to visit a custom website, I might not" | |
| P1 | Pre-configured demo policy | Not started | Show value without config complexity | |
| P1 | Customizable destructive ops list | Not started | Jack: "edit what I think are destructive operations" | |
| P2 | Import rules from CLAUDE.md | Not started | Scott idea from Jack feedback — don't re-specify rules | |
| P2 | Rate-based spending alerts | Not started | Jack: "notify when churning through credits faster than normal" | |
| P2 | Policy-as-automated-QA | Not started | Zac: evaluate original prompt vs final agent message | |
| — | ~~Link from homepage to `/history`~~ | Done | — | PR #132 |
| — | ~~Session timestamps~~ | Done | — | PR #133 |
| — | ~~First user message as preview~~ | Done | — | PR #133 |
| — | ~~Policy config UI mockups~~ | Done | — | [Overview](https://github.com/LuthienResearch/luthien-org/blob/f481167/_UI_Specs/auto_retry_comparison.html), [A](https://github.com/LuthienResearch/luthien-org/blob/f481167/_UI_Specs/option-a-silent-retry.html), [B](https://github.com/LuthienResearch/luthien-org/blob/a75858e/_UI_Specs/policy_mockup.html), [C](https://github.com/LuthienResearch/luthien-org/blob/f481167/_UI_Specs/option-c-block-only.html) |

### Next milestones

- [ ] Complete first guided trial with external user
- [ ] Document learnings → reprioritize backlog

---

## Goal 3: Unblock Independent User Trials

**Definition of done**: A developer can try Luthien independently with <10 minutes of setup and clear next steps.

### North Star

```bash
# User types this in terminal:
luthien

# Luthien starts, auto-configures, and prompts for API key
# User immediately starts using Claude Code through Luthien
```
### 3 core things needed for Luthien (per Jai on Jan 20 2026)
1)	Luthien service w/ web interface 
2)	db 
3)	redis 

### Required Changes

#### Radical Onboarding Simplification

| Current State | Target State |
|---------------|--------------|
| Clone repo, install deps, configure .env | Single command install or setup working envir in the cloud|
| Read multiple docs to understand setup | Auto-configuration with sensible defaults |
| Manual Docker compose | Embedded database or cloud-hosted option |

#### Documentation Simplification

| Document | Current | Target |
|----------|---------|--------|
| Main README | Setup-heavy, multiple paths | "Getting Started" in 3 steps |
| luthienresearch.org | [Audit needed] | Mirror simplified README |

#### Telemetry for Learning

| Feature | Description | Privacy Consideration |
|---------|-------------|----------------------|
| Opt-in usage sharing | With user approval, share anonymized usage | Clear consent flow |
| Session metadata | Who, when, how long | No conversation content |
| Feature usage | Which UIs accessed | Help prioritize development |

**Learn More Faster note**: In early stages, most learning happens on calls with users. Telemetry becomes more valuable once we have enough users that we can't talk to all of them.

### Milestones

- [ ] Design simplified install flow
- [ ] Implement single-command setup
- [ ] Simplify README
- [ ] Update luthienresearch.org
- [ ] Add opt-in telemetry
- [ ] First independent user completes trial

---

## Scott's Prioritized Work Plan

**Core insight:** Goal 1a (outreach) spins the feedback loop. Goal 1b (dogfooding) is paused until after EAG SF. Scott's highest-leverage work right now is outreach → feedback → better requirements → better UI — this directly unblocks Goals 2 and 3.

### How outreach feeds the goals

| Activity | Supports | How |
|----------|----------|-----|
| Show README/landing page to new contacts | **Goal 3** | Tests whether value prop is clear enough for independent users |
| Show policy config mockups to developers | **Goal 2** | Validates toggle UI, default policies, terminal feedback before building |
| Guided trial with warm contacts | **Goal 2** | Tests the full user journey: setup → policy → see it work |
| Capture pain points from daily Claude Code users | **Goals 2+3** | Discovers what policies to ship as defaults, what setup friction to remove |
| Follow up and get people to try Luthien | **Goal 3** | Tests whether onboarding works without hand-holding |

### Current work cadence = the loop

1. **Capture feedback** (Goal 1a: outreach calls, demos) → 0-outreach4feedback/
2. **Synthesize feedback** (themes from raw notes) → 1-feedback-synthesis/
3. **Better requirements** (question & delete per [Musk 5-step](https://modelthinkers.com/mental-model/musks-5-step-design-process)) → 2-versions-requirements/
4. **Better UI** (update mocks when 3+ people say the same thing) → 3-ui-mocks/
5. **Ship code** when requirements are stable enough → luthien-proxy PRs

### Completed

- [x] Session viewer quick wins: homepage link, timestamps, first message preview (PRs #132, #133)
- [x] README v5 options (3 variations on `value-prop` branch)
- [x] Policy config mockups: Option A (current), Option B (terminal), Option C (browser UI)
- [x] PipBlockPolicy demo (live on `demo-pip-block` branch)
- [x] 4 user feedback sessions synthesized (Zac, Jack+Zac, Finn, Chris+Beth Anne+Bahar)

### Next up

- [ ] EAG SF outreach (Feb 14-16): Swapcard filtering, meeting invites, capture workflow
- [ ] Synthesize EAG feedback → update requirements → update UI
- [ ] Ship meaningful default policy (config change, not a feature)
- [ ] Ship toggle-based policy config UI (based on Jack's validated v3B)
- [ ] Terminal feedback when actions blocked (cross-cutting theme from all users)

---

## FAQs

### On Goal Prioritization

1. **"Why not fix blocking bugs yourself?"**
   - Some bugs may require deep backend knowledge
   - Risk of introducing new issues without code familiarity
   - Jai's review time might exceed fix time anyway

2. **"Why focus on UI before policies?"**
   - Conversation viewer is the "proof Luthien is working" moment
   - Easier to demo: "Look, all your conversations are logged"
   - Policies require more explanation and setup

3. **"Is Goal 3 premature?"**
   - Yes, it's aspirational. Goals 1a, 1b, and 2 will inform what "simple" actually means.
   - Including it now helps us make decisions that don't paint us into corners.

### On Technical Approach

4. **"Should we invest in better onboarding infra now?"**
   - Not yet. Manual onboarding with 1-3 users teaches us what matters.
   - Build infra after we've done it manually 5+ times.

5. **"What about authentication/multi-tenancy?"**
   - Out of scope for Goals 1-2 (single-user local setup)
   - May become relevant for Goal 3 if we host a shared instance

6. **"How does this relate to existing user stories?"**
   - Story 6 (Taylor) is the primary driver for Goals 2+3
   - Story 5 (Infrastructure) provides foundation for Goal 1b
   - Stories 1-4 inform future direction but aren't blockers

---

## Prioritization Summary

| Priority | Item | Goal | Rationale |
|----------|------|------|-----------|
| **NOW** | EAG SF outreach + feedback capture | 2, 3 | Highest-leverage activity while dogfooding is paused |
| **NOW** | README/value prop iteration based on feedback | 3 | Every conversation is a test of the landing page |
| P0 | Meaningful default policy | 2 | First impression must show real value |
| P0 | Toggle-based policy config UI | 2 | Jack validated v3B; replace dynamic forms (PR #175) |
| P1 | Surface results in terminal | 2 | Cross-cutting theme: don't make me visit a website |
| P1 | Fix dogfooding blockers | 1b | Jai's bandwidth — paused, not abandoned |
| P2 | Session sharing URLs | 2 | Enables async review workflow |
| P3 | Single-command install | 3 | Requires more infra investment |

---

## Links

- [User Stories README](README.md)
- [Story 6: Junior Developer](06-junior-developer-learning-with-guardrails.md)
- [UX Redesign Principles](https://github.com/LuthienResearch/luthien-proxy/blob/ux-exploration/dev/ux-exploration.md) *(on ux-exploration branch)*

---

## Changelog

- **2026-02-09**: Added feedback loop + outreach pipeline. Rewrote Scott's work plan: dogfooding paused, outreach supports Goals 2+3. Added EAG SF prep to priorities.
- **2026-02-08**: Added Phase 3 policy config UI feedback, mockup permalinks, and PR #175 tracking
- **2026-01-17**: Initial creation, merged plan of attack document, structured around Learn More Faster methodology
