# Plan: v7 Policy Config Mockups (3 Browser + 3 Terminal)

**Date:** 2026-03-18
**Author:** Scott (executed by Claude Code)
**Scope:** Musk Step 3 - design the simplified UIs. Step 1 (question requirements) was done in [policy-config-simplification.md](policy-config-simplification.md). Step 2 (delete) happened implicitly during Step 1.
**Status:** Implemented

---

## Context

v6 mockups were tested with Finn (Mar 18). Option B (live demo) won. Options A and C failed. [Post-mortem](../3-ui-mocks/3-policy-config/v6-postmortem.md) identified four root causes: non-functional interactions, value described instead of demonstrated, simple replacement not enough for power users, multi-policy invisible.

This plan produces 6 mockups that address the v6 failures while staying within the [5 surviving requirements](../2-versions-requirements/5-policy-config-requirements-live.md#requirements).

## Feedback driving this iteration

Sources: [3.1 feedback synthesis](../1-feedback-synthesis/3.1-policy-config-feedback.md), Trello cards for Josh and Scott testing notes.

- **Finn (Mar 18):** Option B winner. Simple find-and-replace is not enough - wants LLM judge + auto-retry against a style guide. "Those two M dashes kill the piece entirely."
- **Josh (Slack, Mar 12):** "Can't have multiple policies active at the same time?" Em-dash example hard to see the difference.
- **Scott (testing):** SimpleLLMPolicy didn't block rm command - default policy must actually work.

## The 6 mockups

### Browser (3)

**B1: DeSlop Hero + Multi-Policy.** Demo-first layout (v6 Option B pattern). Key difference from v6: multiple policies shown active simultaneously. Addresses Josh's multi-policy question and his "hard to see the difference" feedback by using more obvious sample text.

**B2: LLM Judge Demo.** Shows what an LLM-based policy does - blocking a dangerous command (`rm -rf`) with reasoning and auto-retry. Addresses Finn's "I need another LLM to rephrase" and the gap between string replacement and real safety policies.

**B3: Style Guide Policy.** Finn's actual use case: paste a style guide, LLM judge scores responses for authenticity, auto-retries if below threshold. Shows the "custom policy" tier with user-provided rules.

### Terminal (3)

All styled as HTML pages that look like terminal windows.

**T1: Real-Time Inline Feedback.** What happens DURING a Claude Code session when policies fire. `[Luthien]` messages injected into the response stream. Addresses Jack's "something in Claude Code telling me what happened."

**T2: Blocked Action + Auto-Retry.** What happens when a policy BLOCKS something. Block reason, auto-retry with constraint injection, success confirmation. Addresses Finn's auto-retry loop and Zac's retrospective review need.

**T3: Session Summary + luthien status.** End-of-session summary at `/exit` with per-policy counts. `luthien status` for details. Shows multi-policy, metrics (Finn liked the KPIs), and retrospective review.

## Files created

All in `ui-fb-dev/3-ui-mocks/3-policy-config/`:

| File | Type | Requirements addressed |
|------|------|----------------------|
| `v7-landing.html` | Landing page | Links to all 6 |
| `v7-b1-deslop-multi.html` | Browser | R1, R2, R4, R5 |
| `v7-b2-judge-demo.html` | Browser | R1, R3, R5 |
| `v7-b3-style-guide.html` | Browser | R1, R3, R4 |
| `v7-t1-inline-feedback.html` | Terminal | R2, R3 |
| `v7-t2-blocked-retry.html` | Terminal | R2, R3, R4 |
| `v7-t3-session-summary.html` | Terminal | R2, R3, R5 |

## How v7 addresses v6 failures

| v6 failure ([post-mortem](../3-ui-mocks/3-policy-config/v6-postmortem.md)) | v7 response |
|---|---|
| Non-functional interactions (configure button dead) | All interactive elements have working JavaScript |
| Value described, not demonstrated | B1 and B2 show before/after and block/retry demos |
| Simple replacement not enough | B2 (LLM judge) and B3 (style guide) show advanced policies |
| Multi-policy invisible | B1 defaults to 2 policies ON; T3 shows 3 policies in summary |

## What's next

- Show v7 mockups to 1-2 users (Finn again, or new user)
- Pick winning pattern(s) from the 6
- Musk Step 4: accelerate - build the winner as real code
