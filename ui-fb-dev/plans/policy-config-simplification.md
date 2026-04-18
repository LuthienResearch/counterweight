# Radical Simplification: Policy Config UIs

**Date:** 2026-03-18
**Author:** Scott
**Scope:** Musk Step 1 only — question requirements. Design comes after.

---

## Context

The [policy config requirements doc](../2-versions-requirements/5-policy-config-requirements-live.md) applied Musk Steps 1-2 on Feb 8 with evidence from 2-3 sessions (Zac, Jack+Zac, Finn). That pass took 17 requirements down to 8 (R1-R8).

Now we have **12 sessions** of evidence. Time to challenge R1-R8 again. **This plan is Step 1 only** — question requirements. Design comes after.

---

## Musk Step 1 (Round 2): 5 Whys on R1-R8

### R1: Meaningful default policy

**5 Whys:**
1. Why does the default need to be meaningful? → Users try Luthien once and decide if it's worth continuing
2. Why do they decide quickly? → Many tools compete for their attention; setup takes effort
3. Why does setup effort matter? → If the first experience is neutral/confusing, they won't invest more time
4. Why would the first experience be neutral? → Because the current default (AllCaps/NoOp) doesn't do anything a user would notice or care about
5. Why doesn't it do anything noticeable? → It was chosen for implementation simplicity, not user value

**Root problem:** Users decide in one session whether Luthien is worth their time. If the first experience doesn't demonstrate obvious value, they leave.

**Evidence:** Zac (Jan 30): "AllCaps is not meaningful to me. 'Block jailbreaks' is meaningful." Finn (Feb 6): would pay $20/mo for em-dash removal alone — visible on first request. Bahar (Feb 8): "Handle fundamentals so I can focus on domain-specific."

**Verdict: KEEP.** Requirement = "The first experience must make Luthien's value obvious."

### R2: Config → Claude Code path

**5 Whys:**
1. Why do users need a path from config to use? → They get stuck after configuring a policy
2. Why do they get stuck? → Configuring is disconnected from using — different context (browser vs terminal)
3. Why is it disconnected? → Policy config happens in a web UI, but the proxy intercepts API calls from a terminal tool
4. Why does that gap matter? → The time between "I configured something" and "I see it working" creates uncertainty
5. Why is uncertainty bad? → Users can't tell if they did it right, so they don't trust the system and may abandon it

**Root problem:** There's a gap between configuring a policy and experiencing it work. That gap creates uncertainty and erodes trust.

**Evidence:** Zac (Jan 30): "It should say right here, here's how you can test with Claude Code." Finn (Feb 25): copied entire README into Claude Code to set up — gap between "reading config" and "seeing it work" was too wide.

**Verdict: KEEP.** Requirement = "The gap between configuring a policy and experiencing it must be minimal."

### R3: Results visibility

**5 Whys:**
1. Why do blocked actions need to be visible? → Users don't know what Luthien is doing
2. Why don't they know? → Policy actions happen silently in the proxy layer
3. Why silently? → The proxy modifies/blocks API responses without surfacing the decision to the user
4. Why not surface it? → There's no feedback mechanism back to the user's working context
5. Why does that matter? → Invisible control creates no trust. Users need to verify the system works before relying on it.

**Root problem:** Users can't verify that policies are working. Without visibility, there's no trust, and without trust, they disable or ignore the system.

**Evidence:** Jack (Feb 3): "I don't think I would check this UI... I would want to see something in Claude Code telling me what happened." Zac (Jan 30): "I want to see what got rejected." Jai (Feb 8): "UIs communicate information faster — humans learn best with pictures."

**Verdict: KEEP.** Requirement = "Users must be able to verify that policies are working."

### R4 + R7 + R8: Customizable rules / user-sourced policies / customize params

**5 Whys:**
1. Why do policies need to be customizable? → Generic rules don't fit real-world stacks
2. Why don't they fit? → Each team uses different tools, conventions, and definitions of "dangerous"
3. Why does that matter? → A policy that blocks the wrong thing (false positive) is worse than no policy
4. Why are false positives worse? → They train users to ignore or disable the system entirely
5. Why would they disable it? → Because trust requires accuracy for the user's specific context, and a system that's wrong too often gets turned off

**Root problem:** Generic policies produce false positives, which destroy trust and lead users to disable the system. Policies must be accurate for the user's specific context.

**Evidence:** Jack (Feb 3): "edit what I think are destructive operations." Quentin (Feb 10): "I'm always using PNPM instead of npm... I'd want to customize what this policy enforces." Beth Anne (Feb 8): "I have specific requirements on how and what to install." Tyler (Feb 10): backward compat detection has 60% false positive rate on cursor rules. Nico (Feb 10): catches backward compat in every PR review.

**Verdict: COLLAPSE R4+R7+R8 into one.** Requirement = "Policies must be accurate for the user's specific context."

### R5: Toggle switches

**5 Whys:**
1. Why do users want simple controls? → They don't check complex UIs
2. Why don't they check? → They're in their terminal working, not in a browser managing policies
3. Why are they in their terminal? → That's where they write code — context switching to a browser is costly
4. Why is context switching costly? → They lose flow state and it interrupts their primary task (building software)
5. Why does that matter? → Policy management is a supporting activity, not the user's primary job. If it demands too much attention, it gets skipped.

**Root problem:** Policy management competes with the user's primary job (writing software). If it demands more attention than it saves, users skip it.

**Evidence:** Jack (Feb 3): "I don't think I would check this UI." Zac (Jan 30): "hide what's not user-relevant... show only what the user needs to decide." Finn (Feb 6): "It's still unclear what I would use this for." Bahar (Feb 8): "Handle fundamentals so I can focus on domain-specific."

**Verdict: REFRAME.** Requirement = "Policy management must not compete with the user's primary work."

### R6: End-of-run summary

**5 Whys:**
1. Why do users want a summary at the end? → They want to know what happened during a long run
2. Why don't they know what happened? → Because they let the agent run autonomously and can't observe every action
3. Why can't they observe every action? → Because the value of autonomous agents is NOT watching them constantly
4. Why does that matter? → Because the "check at the end" workflow is how most users operate — Zac: "let it run, then show me what got rejected"
5. Why is this different from R3 (visibility)? → R3 is real-time visibility. This is retrospective review — a different mode of interaction.

**Root problem:** Users who run agents autonomously need a way to review what happened without having watched in real-time.

**Evidence:** Zac (Jan 30): "I want to run Claude Code by itself and just let it run. When it's finished, that's when I want to see what got rejected." Jack (Feb 3): "I'd want to see a diff or a summary."

**Verdict: COLLAPSE into R3.** R3 and R6 are both about "did a policy work?" Whether real-time or retrospective, it's visibility of system status.

---

## Surviving Requirements (post Round 2)

| # | Requirement (problem only) | Root cause | Key evidence |
|---|---------------------------|-----------|-------------|
| R1 | The user's first experience trying a policy must make Luthien's value obvious. | Current defaults (AllCaps/NoOp) were chosen for implementation simplicity, not user value. | Zac: "AllCaps is not meaningful." Finn: $20/mo for em-dash removal. Bahar: "Handle fundamentals." |
| R2 | Users must be able to interact with policies from where they already work — terminal or browser. "Interact" means the full Nielsen set: visibility of status, control, feedback, error recovery. | Policy interaction currently requires context-switching to a web UI that terminal-first users don't visit. CLI has zero policy management after onboard. | Jack: "I don't think I would check this UI." Zac: "I might not visit a custom website." Jai: "UIs communicate faster." |
| R3 | Users must be able to verify that policies are working — did a policy fire? What did it do? | No feedback mechanism surfaces policy decisions to the user. Policies act invisibly in the proxy layer. | Jack: "I would want to see something in Claude Code telling me what happened." Zac: "I want to see what got rejected." |
| R4 | Users must be able to customize policies for their context — modify existing, import from CLAUDE.md, or add their own. Use progressive disclosure: don't require understanding internals to get value from built-in policies. | Generic policies produce false positives, which destroy trust. Policies are most valuable when users can specify what matters to their stack. | Jack: "edit what I think are destructive operations." Quentin: PNPM not npm. Tyler: 60% false positive rate. Beth Anne: "specific requirements." |
| R5 | Users must see what policies are active and be able to turn them on or off. Where additional configuration is needed, use progressive disclosure: logical defaults first, expose details only after the user has decided to enable the policy. | Users are asked to configure policies before understanding what they do. Complexity is front-loaded instead of revealed progressively. | Finn: "It's still unclear what I would use this for." Zac: "hide what's not user-relevant." Bahar: "Handle fundamentals so I can focus on domain-specific." |

**5 requirements.** Down from 17 (original) → 8 (Feb 8 pass) → 5 (this pass).

**What got collapsed:**
- R7 (user-sourced policies) + R8 (customize params) → collapsed into R4
- R6 (end-of-run summary) → collapsed into R3. Both are about the same thing: "did a policy work?" Whether real-time or retrospective, it's visibility of system status.
- Old R5 (toggle switches) → reframed as R5 (visibility + control with progressive disclosure). The underlying need isn't a specific UI pattern, it's seeing what's active and controlling it without front-loaded complexity.

---

## What's Next (NOT in this plan)

This plan is **requirements simplification only** (Musk Step 1). Next steps:
1. **Musk Step 2** (what to delete) as a separate pass
2. **Musk Step 3** (design the simplified UIs) as a separate planning pass
3. **Then:** Implement
