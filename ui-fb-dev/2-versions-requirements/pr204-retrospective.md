# PR #204 Retrospective: My Mistakes, and the Real Question

**Date:** 2026-02-19
**PR:** [#204 — Self-healing Anthropic request pipeline](https://github.com/LuthienResearch/luthien-proxy/pull/204)
**Status:** Rejected by Jai
**Related:** [#210](https://github.com/LuthienResearch/luthien-proxy/pull/210) (also rejected, same issues)

---

## Part 1: What I (Scott) Did Wrong

### Jai's feedback, distilled

Jai rejected this PR with two comments. The key points:

1. **"We do not impose additional changes to the client-server interaction that the user has not specifically requested."** Luthien is a transparent proxy. Absent a user-configured policy, it should be invisible.

2. **Passthrough-on-policy-failure is dangerous.** If a security policy fails, we do not silently forward content anyway. That defeats the entire purpose.

3. **The PR's root cause analysis was wrong.** It claimed "we have no request validation layer" and listed 5 bugs as evidence. But most of those bugs were format conversion issues, not missing validation. And it listed the PR itself as bug #5 — a sign the LLM had lost the plot.

4. **The "schema-aware middleware" claim was confabulated.** Claude cited LiteLLM and LangChain as precedent. Jai called it bullshit. Whether or not it's technically accurate, it was used to justify a design philosophy that's wrong for Luthien.

5. **"If you don't have a firm grasp on exactly what a PR is doing, don't submit it."**

---

### My mistakes, step by step

**Mistake 1: I let Claude escalate from bug fixes to architecture without checking with Jai.**

PRs #151, #167, #178, #201 were real bugs I found while dogfooding. Claude saw a pattern and proposed a sweeping "self-healing pipeline." That's a massive scope jump — from "fix this bug" to "redesign the request pipeline." I should have stopped and asked: "Jai, I keep finding similar bugs. Is there a structural fix you'd want, or should I keep filing individual fixes?"

> **Prevention:** Any PR that changes how the pipeline handles errors/failures requires a 1-sentence Slack to Jai before implementation. "I'm thinking about X — does that align with how you'd approach this?"

**Mistake 2: I didn't verify Claude's external claims.**

The PR cited LiteLLM and LangChain as industry precedent. I didn't check. Claude's confabulation became the justification for the design.

> **Prevention:** When Claude cites external projects to justify a design, treat it as unverified. Either check it yourself or flag it as "Claude claims X — I haven't verified" in the PR.

**Mistake 3: I trusted 11 auto-reviews that all said "Approve."**

Every single Claude bot review praised the code quality, test coverage, and documentation. Zero caught the fundamental design flaw. Auto-reviews check *how* the code is written, not *whether it should exist*.

> **Prevention:** Auto-reviews are for code quality only. Directional judgment — "should this change exist?" — is a human call. I need to make that call myself or get Jai's input.

**Mistake 4: I didn't understand "passthrough on failure" well enough to see the danger.**

"If the pipeline breaks, fall back to the original request" sounds reasonable for a web proxy. It's exactly wrong for a security proxy. If someone configures a policy and it fails, silently bypassing it means the user *thinks* they have protection when they don't.

> **Prevention:** Before submitting any PR, ask: "Does this change what happens when a policy fails?" If yes, full stop — discuss with Jai.

**Mistake 5: I was seduced by polish.**

The PR description was beautiful — COE analysis, design tenets table, user impact stories, 119 tests. It *felt* authoritative. Polished presentation is not the same as correct direction.

> **Prevention:** Recognize this pattern in myself. When Claude produces something that looks impressive, that's when I most need to slow down and ask "but is the premise right?"

---

### Summary of prevention mechanisms

| Mistake | Prevention | Trigger |
|---------|-----------|---------|
| Scope escalation | Slack Jai before any architectural PR | "This touches how the pipeline handles errors" |
| Confabulated claims | Verify or flag as unverified | Claude cites external projects |
| Trusting auto-reviews | Treat as code quality only | Any PR with auto-review approvals |
| Misunderstanding security implications | Ask "what happens when a policy fails?" | Any PR touching error handling |
| Seduced by polish | Slow down when output looks impressive | Claude produces a "beautiful" PR description |

---

### Salvageable pieces

Jai explicitly said some ideas were good — just not bundled this way:

- **Human-centered error messages** — welcome as a standalone PR
- **Flat error handling / untangling nested logic** — welcome as code quality PRs
- **Individual bug fixes** — keep as focused, single-concern PRs

---

## Part 2: The Real Question We Need to Discuss

Jai's principle is right: **absent a user-specified policy, Luthien should be invisible.** The PR was wrong to propose silently modifying requests and bypassing policies.

But here's what I'm running into as a dogfooder:

**I'm using Luthien without a policy, and it is almost certainly worse than direct API access.**

I'm finding bugs at a high rate per hour of dogfooding. Empty text blocks, orphaned tool results, format conversion issues — these are real failures that break my Claude Code sessions. Each one costs me accumulated context (code understanding, debugging state, partial implementations). When a session dies mid-flow, that's 30-60 minutes of context gone.

The bugs from PRs #151, #167, #178, #201 were all real. I hit them. They broke my sessions. If I were using the API directly without Luthien, I wouldn't have hit them.

So the question isn't "should we silently modify requests?" (answer: no). The question is:

### How do we live up to the principle "never worse than direct API access"?

Right now, we're not living up to it. The proxy introduces bugs that wouldn't exist without it. Every bug I find while dogfooding is evidence of this gap.

Some questions for Jai:

1. **Is "never worse than direct access" actually a principle we hold?** It seems like it should be a corollary of "invisible absent a policy." If the proxy is invisible, it can't be worse. But right now it's not invisible — it's introducing failures.

2. **What's the right response when the proxy's own pipeline creates a malformed request?** Not "silently fix it" (that's what #204 proposed and was rightly rejected). But also not "let it fail and blame the client" — the client's request was fine before the proxy touched it. Should we:
   - Fix the pipeline bug directly (individual PRs, which is what we've been doing)?
   - Add regression tests for known-bad patterns the proxy has historically produced?
   - Something else?

3. **How should we prioritize dogfooding bugs vs. feature work?** I'm finding these bugs because I'm actually using the product. That's valuable. But each bug fix is a separate PR, and if the rate stays high, that's a lot of Jai's review bandwidth spent on fixes rather than features. Is there a better workflow here?

4. **Is there a testing strategy that would catch these before I hit them?** Several of these bugs could have been caught by integration tests that send known-tricky requests through the proxy and verify the output matches direct API access. Would that be a valuable investment?

The irony of PR #204 is that it was trying to solve a real problem — Luthien is currently worse than direct access for some use cases — but it proposed the wrong solution in the wrong way. The problem still exists. I'd like to find the right solution together.
