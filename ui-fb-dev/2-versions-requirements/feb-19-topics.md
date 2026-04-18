# Feb 19 Topics: Reliability, PR Process, and Uber Requirements

**Date:** 2026-02-19

**Author:** Scott Wofford

**For Discussion with:** Jai, Esben & Finn

**Sources:** [uber-requirements.md](uber-requirements.md), [pr204-retrospective.md](pr204-retrospective.md)

---

We are improving. Our first live demos in October 2025 with [Lee Wall](https://www.google.com/search?q=Lee+Wall+EA) (Oct 24) and [Jack Wittmayer](https://www.google.com/search?q=Jack+Wittmayer+Counterweight) (Oct 27) had low success rates. At EAG SF last weekend (Feb 13-15, 2026), our all-caps demo policy worked about 75% of the time. However, I was still not able to demo a truly useful policy, and 75% is not good enough to leave running unsupervised. We agree that absent a user-configured policy, Luthien should be invisible. The proxy helps teams get more upside and less downside from AI tooling (Claude Code today; enterprise adoption of multi-agent workflows like [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) and [OpenClaw](https://github.com/openclaw/openclaw) tomorrow). 

The proxy is not currently invisible. The default configuration runs a NoOpPolicy (pass-through, no rules enforced). Since the Anthropic/OpenAI pipeline split ([#169](https://github.com/LuthienResearch/luthien-proxy/pull/169)), I have dogfooded less than 3 hours total, and I keep hitting proxy-introduced bugs: empty text blocks ([#201](https://github.com/LuthienResearch/luthien-proxy/pull/201)), cache_control forwarding ([#178](https://github.com/LuthienResearch/luthien-proxy/pull/178)), auth mode confusion ([#205](https://github.com/LuthienResearch/luthien-proxy/issues/205)), duplicate tools ([#208](https://github.com/LuthienResearch/luthien-proxy/pull/208)). I tried to fix this structurally in [PR #204](https://github.com/LuthienResearch/luthien-proxy/pull/204), a Claude Code-driven PR that attempted to redesign the request pipeline to handle all these bugs at once. Jai correctly rejected it: the implementation silently modified requests and bypassed policies on failure, which is the opposite of what we want. I learned a lot from this mistake (see [Appendix A: What I Learned From PR #204](#what-i-learned-from-pr-204)).

**Central questions:** How might we live up to our "invisible unless needed" aspiration? What should we focus on next to get there?

**Scott's Tentative Answer (for discussion):** Three uber requirements, in priority order:
1. **Better than no proxy**: using Luthien should never be worse than a direct API call
2. **Frictionless Onboarding**: Beginner experiences value within ~10 minutes
3. **Policies are reliable**: defined as good performance metrics (recall, precision, etc.), low failure rate, and loud failures

Our first priority should be solving for the first requirement. I also think we should prioritize Anthropic path reliability before investing more in OpenAI compatibility.

---

## 1. Better Than No Proxy

Using Luthien must be better than no proxy (our baseline), not worse. On the default NoOpPolicy, most (99.9%) requests that works without Luthien should also work  with Luthien. Users may tolerate a very low failure rate (0.1%) if the value is high, but right now the failure rate is not low and we are not yet delivering enough value to offset it.

**Status: Failing.** Post-pipeline-split we've found bugs where the proxy caused bugs on the default NoOpPolicy:

| What broke | Root cause | PR/Issue |
|-----------|------------|----------|
| 400: `cache_control` on tools rejected by Anthropic | Pipeline preserves fields the API rejects | [#178](https://github.com/LuthienResearch/luthien-proxy/pull/178) |
| 400: empty text content blocks | Pipeline produces empty content blocks | [#201](https://github.com/LuthienResearch/luthien-proxy/pull/201) |
| 401: Claude Code auth failure with Claude Max relay | Auth mode defaults wrong | [#205](https://github.com/LuthienResearch/luthien-proxy/issues/205) |
| `/compact` fails: "Tool names must be unique" | Duplicate tool definitions forwarded | [#208](https://github.com/LuthienResearch/luthien-proxy/pull/208) |

A developer who hits a bug will bypass the proxy next time.

**Goal:** By [date TBD], complete 8 hours of real Claude Code work through the proxy on NoOpPolicy with zero proxy-caused failures. Measured by dogfooding sessions with session logs.

**Status: Red.** We're experiencing several bugs post-pipeline-split (examples in table above). Each one was discovered during dogfooding, not caught by tests.

**Tentatively Proposed Path to green:**
1. Fix all known NoOpPolicy and no policy bugs (Owner: TBD - Jai?)
2. Add regression tests that replay known-tricky requests through the proxy (Owner: TBD - Jai?)
3. Complete an 8-hour dogfooding session with zero proxy-caused failures (Owner: TBD - Scott?)

## 2. Quick Time-to-Value for New Users

A developer goes from "what is Luthien?" to a successful proxied API call in [~10] minutes, unassisted. 10 minutes is a placeholder; lower is better. We should measure this and drive it down over time.

**Goal:** By [date TBD], a senior developer can go from "What is Luthien?" to a useful policy enforcement action via Luthien proxy (can be user attempting to trigger) in under 10 minutes with no assistance. Measured by timed walkthroughs with 3+ new, external developers.

**Status: Yellow.** Setup works end-to-end but is fragile. Known blockers:
- Landing page does not lead with value prop (Tyler, Zac, Ram feedback)
- Setup footguns (easy to misconfigure on first run)
- Auth confusion (which mode, which key)

**Path to green:**
1. Document all user onboarding frictions post EAG SF (owner: Scott) 
2. Fix the top 3 onboarding friction points identified in user walkthroughs (owner: Jai)
3. Landing page rewrite: lead with what Luthien does for you, not what it is (owner: Scott; goal is Jai's approval of PR)
4. Run 3 timed walkthroughs with external devs and measure time-to-first-call (owner: Scott)

## 3. Policies That Work When Configured

When a policy is configured, it should do its job. If it fails, the failure should be visible, not silent. 

**Goal:** A configured policy reliably enforces its rules across both streaming and non-streaming paths. Misconfiguration produces a clear error, not silent passthrough. Measured by intentional break tests.

**Status: Yellow.** Core system works reliably. Known gaps:
- Policy authoring is error-prone (wrong inheritance crashes gateway)
- Streaming/non-streaming behavior gaps
- Previously had a silent fallback bug where a misconfigured policy would quietly revert to NoOpPolicy instead of raising an error (fixed, but it shows the kind of thing we need to watch for)
- We have no metrics; we need: performance metrics (recall, precision, etc.), loud failures and failure rate metrics
- Once we have metrics the performance needs to be good enough that it's not super frustrating for the user. As a current user, I don't use policies because if the underlying proxy + NoOp policy keeps causing bugs, I don't want to add the complexity of an actually-useful policy. 

**Path to green:**
1. Define metrics (owner: Scott, goal: Jai's approval)
2. Build data pipeline to capture metrics (owner: Jai)
3. Add integration tests for intentional policy misconfiguration (expect clear errors, not passthrough) (Owner: Jai?)
4. Document policy authoring with examples that cover common mistakes (Owner: Jai?)
5. Are there any remaining streaming/non-streaming parity gaps? (owner: Jai)

---

## Decisions Needed

1. **Do we agree "better than no proxy" is the bar?**
   Our baseline is a direct API call. If using Luthien is worse than that baseline, we have a problem. Right now my assessment is that it is worse.

2. **Reliability sprint?**
   Should we pause features and focus on making the NoOpPolicy path bulletproof? Hard to sell new capabilities if the baseline experience is broken.

3. **Regression testing strategy?**
   CI tests that send known-tricky requests through the proxy and compare to direct API. Would this improve the rate at which we catch these before dogfooding?

5. **Dogfooding bug workflow?**
   I am finding real bugs, but each one is a separate PR and costs review bandwidth. Is there a better process? Hire a QA contractor for $25-$50/hr? ([draft Upwork posting](https://www.upwork.com/freelance-jobs/apply/Engineer-Find-Bugs-Fix-Them-Improve-Our-Safety-Dev-Tool-Python-CLI_~022018698581455602230/))


---

## Appendix A: What Scott Learned From PR #204

After the "thinking blocks in streaming" bug ([PR #134](https://github.com/LuthienResearch/luthien-proxy/pull/134)) in early January, Jai encouraged me to always try to fix bugs when I find them. Esben said something similar: "the models have gotten much better in the past few months, you can rely on them more." This encouragement gave me more confidence to push PRs I did not fully understand.

I overcorrected. I optimized for fixing bugs quickly and went too far on the "vibe coding" end of the spectrum. Claude escalated from individual bug fixes to a full pipeline redesign. I Slacked Jai about #204 before merging but did not hear back and pushed ahead anyway. Five mistakes:

| Mistake | What happened | Prevention |
|---------|--------------|------------|
| Scope escalation | "Fix 400 errors" became "redesign the pipeline" | 1-sentence Slack to Jai before any architectural PR (sent yesterday) + Jai replies |
| Unverified claims | Claude cited LiteLLM/LangChain as precedent; I did not check | Flag Claude's external claims as unverified |
| Trusted auto-reviews | 11 approvals, zero caught the directional flaw | Auto-reviews check code quality only, not direction |
| Missed security implication | "Passthrough on failure" silently bypasses policies | Ask "what happens when a policy fails?" on every PR |
| Seduced by polish | Beautiful PR description, wrong premise | When the output looks impressive, slow down and check the premise |

### Jai's Feedback on PR #204 (direct quotes)

On the core premise ("default path is passthrough, fall back to unmodified request on failure"):

> Absolutely not. If a security policy fails, we do not fallback to doing nothing and forwarding content anyway. [...] We are NOT making it the default.

On Claude's claim that "LiteLLM and LangChain both treat LLM proxies as schema-aware middleware":

> Bullshit. We're not shipping a PR built on obvious confabulation.

On the overall PR:

> Rejected with prejudice. This is a central example of a slop PR and I generally don't want to see them. If you don't have a firm grasp on exactly what a PR is doing, don't submit it.

On the PR's claim that "we have no request validation layer" behind 5 bugs:

> This is an impressive concentration of completely untrue statements in relatively few words. First of all, it lists *this PR* as the 5th bug, which is a good sign the LLM has wandered off into crazytown. Second, most of the actual bugs listed were a consequence of converting between Anthropic and OpenAI formats, not a lack of validation.

What Jai said was welcome as standalone PRs: human-centered error messages, flat error handling (untangle nested try/except), individual bug fixes (one per PR).

I need help recalibrating. Where should I be on the "vibe vs. understand the details" spectrum? This is also a real Luthien use case, exactly [User Story #6: Junior Developer Learning with Guardrails](https://github.com/LuthienResearch/luthien-proxy/blob/main/dev/user-stories/06-junior-developer-learning-with-guardrails.md).

**Salvageable pieces** (Jai said these are welcome as standalone PRs): which I (Scott) can own: 
(A) human-centered error messages
(B) flat error handling
(C)  individual bug fixes (one per PR).

