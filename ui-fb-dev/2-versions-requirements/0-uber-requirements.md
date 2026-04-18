# Luthien Uber Requirements

**Date:** 2026-02-19 | **Updated:** 2026-02-25
**Method:** Musk's design process: make requirements less dumb, then delete, then simplify

Luthien is an open-source proxy that enforces safety policies on AI coding agents. We're in Seldon Labs (batch 1) with demo day on April 16. We have a working proxy, early design partners, and a growing feature set, but demos have been unreliable (75% success rate at EAG SF in February) and onboarding still requires hand-holding.

We reviewed the complete history of both repos (185 PRs + 27 issues in luthien-proxy; 73 PRs + 4 issues in luthien_control) and started with 14 candidate requirements. But these have competing priorities, generate bugs that undermine each other, and don't answer the fundamental question a developer asks before adopting any proxy: **what must be true for me to choose Luthien over a direct API call?**

Exactly three things. Everything else the proxy does is either a means to achieving one of these three, or work we should defer until these three are solid.

1. **Invisible Unless Needed**: don't break things
2. **Zero to Value in 10 Minutes**: be easy to adopt
3. **Policies You Can Trust**: be trustworthy when active

If we fail #1, nobody will adopt us. If we fail #2, they won't try. If we fail #3, they won't stay.

---

## Requirement 1: Invisible Unless Needed

**Target:** Using Luthien should never degrade from baseline direct API functionality. In the absence of a user-configured policy, the proxy must behave identically to a direct API call.

**Status: Red/Failing**

Known issues from dogfooding and repo history (15+ proxy-introduced bugs):
- Images crash the gateway, then Claude sees wrong image (#94, #103, #108)
- Streaming stuck repeating message_start events (#59)
- Thinking blocks stripped or lost in streaming (#128, #129)
- Client parameters forwarded to API causing 400 errors (#151, #178, #201)
- Auth mode defaults wrong, causing 401s (#43, #205)

The root cause pattern is consistent: format conversion between OpenAI and Anthropic representations introduces bugs at every content type boundary (images, thinking blocks, tool calls, cache control).

**Acceptance test:** Run any AI coding agent (Claude Code, Codex, Cursor) through the proxy with no policy for 8 hours of real work. Zero proxy-caused failures.

**Path forward:**
- Fix known NoOpPolicy bugs
- Add regression tests for each previously broken request type
- Complete dogfooding validation (8-hour session)
- Evaluate whether OpenAI compatibility layer is worth the bug surface area, or go Anthropic-native-first

---

## Requirement 2: Zero to Value in 10 Minutes

**Target:** A developer who has never seen Luthien understands the value prop (2 min), installs and runs the proxy (5 min), and sees it working with their existing AI tool (3 min).

**Status: Yellow/Partial**

Known blockers:
- README buries the value prop under implementation details (feedback from Tyler #179, Zac and Ram #144, #154)
- Migrations fail silently; gateway runs but nothing persists (#109)
- Auth configuration confusing with multiple modes and wrong defaults (#43, #205)
- Docker build failures on first attempt (#36)

User trial friction (Feb 2026):
- Peter/QADNA (Feb 25): Python 3.10 installed, project requires 3.13+ — `quick_start.sh` should check version and warn. README implies API key is the only option — needs Claude Pro/Max subscription guidance. Stale/expired API key returns nested JSON error instead of clear "your API key is invalid" message.
- Tyler/Redwood (Feb 10): `quick_start.sh` health check fails without Grafana. `quick_start.sh` vs `docker compose up` confusion. Pre-built Docker images needed for team deployment.

If setup takes longer than the time a developer would spend evaluating whether to try it, they won't try it.

**Acceptance test:** Hand a senior developer the landing page URL. Time them from first click to first successful proxied API call. Must be under 10 minutes with no help.

**Path forward:**
- Rewrite landing page to lead with user benefit, not technical architecture
- Address top 3 onboarding friction points identified in user walkthroughs
- Add clear error messages for common misconfigurations (wrong auth mode, missing DB)
- Conduct timed walkthroughs with external developers

---

## Requirement 3: Policies You Can Trust

**Target:** Configured policies reliably enforce rules. Failures are visible, never silent passthrough. The user chose to have a policy; the system must honor that choice loudly.

**Status: Yellow/Partial**

Known gaps:
- AllCapsPolicy crashed on streaming because of missing required methods (#53)
- ToolCallJudgePolicy wrong inheritance prevented gateway from starting (#60, #62)
- SimplePolicy only worked in streaming mode, not non-streaming (#147)
- Anthropic/OpenAI path unification made policy writing harder (#169)
- No silent-passthrough protection; if a policy errors, the request passes through unchecked
- No systematic failure rate tracking or performance metrics (recall, precision)

A policy author must understand streaming vs. non-streaming, Anthropic vs. OpenAI formats, and multiple inheritance paths. That's too much surface area for what should be "evaluate this request/response."

**Acceptance test:** Configure a simple blocking policy. Attempt to bypass it 10 different ways. It blocks every time. Then break the policy config intentionally. The system shows a clear error, not silent passthrough.

**Path forward:**
- Define measurable policy performance metrics
- Add integration tests for misconfiguration scenarios (policy errors should block, not pass through)
- Document policy authoring with common mistake examples
- Verify streaming/non-streaming parity for all policy types

---

## Key Decisions Needed

1. **Confirm baseline:** Agree that "better than no proxy" (Requirement 1) is the existential bar. If we fail this, nothing else matters
2. **Reliability sprint:** Pause feature work to solidify the NoOpPolicy path?
3. **OpenAI compatibility:** Is the OpenAI format layer worth the bug surface area, or should we go Anthropic-native-first and add OpenAI later when it's rock-solid?
4. **CI testing strategy:** Implement regression tests comparing proxy behavior against direct API calls?
5. **Bug triage process:** Establish workflow for finding and fixing bugs discovered through dogfooding

---

## How We Got From 14 to 3

The repo review produced 14 candidate requirements. We applied a deletion pass. If we deleted the requirement, would anyone actually notice? Auth flexibility (three modes caused more bugs than it solved), policy composition (zero users have asked for it), database optionality (every deployment has a DB), and format conversion as a standalone goal (it's a means to Requirement 1, not an end) were all deleted or subsumed.

The remaining requirements collapsed into three groups. "Don't break requests" + "handle all content types" + "support streaming" + "forward errors accurately" are all the same requirement: the proxy must be invisible. "Easy to set up" + "migrations don't fail" + "landing page communicates value" are all: zero to value in 10 minutes. "Policies easy to write" + "see what the proxy is doing" are: policies you can trust.

**Our users** (per Jai, 2026-02-19) fall into two roles: the "accelerate AI tooling" person who maximizes upside of agentic systems, and the "keep AI tooling safe" person who applies company policies and minimizes downside. Daily Claude Code usage is the wedge. Once people use Luthien all day for coding, they'll naturally extend it to agents in production.

---

## Appendix: Evidence by Category

### A. Proxy breaks working requests (supports Requirement 1)

| Issue | What broke | Root cause |
|-------|-----------|------------|
| #94, #103, #108 | Images crash gateway, Claude sees wrong image | LiteLLM multimodal routing, format conversion |
| #59 | Streaming stuck repeating message_start events | Pipeline buffering bug |
| #61 | Codex shows every token twice | Streaming duplication in OpenAI path |
| #128, #129 | Thinking blocks stripped (500s) or lost in streaming | Format conversion drops thinking blocks |
| #151 | `context_management` forwarded to Anthropic (400) | Client params not filtered before API call |
| #167 | Orphaned tool_results after /compact (400) | Pipeline doesn't clean up dangling references |
| #178 | `cache_control` on tools causes 400 | Format conversion preserves fields API rejects |
| #201 | Empty text blocks cause 400 | Pipeline produces empty content blocks |
| #205 | Claude Code 401 with Claude Max relay | Auth mode defaults wrong |
| #43 | Claude Code 401 | Proxy key vs API key mismatch |
| #1 (control) | Brotli decoding error with OpenAI backend | httpx encoding issue |

### B. Setup and onboarding friction (supports Requirement 2)

| Issue | What happened |
|-------|--------------|
| #78 | Migration footgun: existing DB users can't add new tables |
| #109 | DB schema mismatch fails silently; gateway runs but nothing persists |
| #36 | Docker build fails on local-llm container |
| #43, #205 | Auth configuration confusing; multiple modes, wrong defaults |
| #64 (control) | Poetry can't find luthien_control in path |
| PRs #144, #154 | Onboarding feedback from Zac, Ram; README buries value prop |
| PR #179 | Tyler's feedback; README doesn't lead with user benefit |

### C. Policy authoring gaps (supports Requirement 3)

| Issue | What happened |
|-------|--------------|
| #53 | AllCapsPolicy missing required methods; crashes on streaming |
| #60, #62 | ToolCallJudgePolicy wrong inheritance; gateway won't start |
| #136, #137 | Policy Config UI doesn't show judge results or link to diff viewer |
| PR #147 | SimplePolicy only worked streaming, not non-streaming |
| PR #169 | Anthropic/OpenAI path unification made policy writing harder |

### D. Observability gaps (supports Requirement 3)

| Issue | What happened |
|-------|--------------|
| #27 | Telemetry/logging solution needed (original issue) |
| #11 | Get rid of DebugLogWriter |
| PR #107 | Structured span hierarchy needed for pipeline visibility |
| PR #67 | Sink-based observability architecture |
| PR #186 | Conversation live view with diff display |
