# Hackathon Project Ideas -Apart Research AI Control Hackathon (March 20-22, 2026)

_Built for hackathon participants deciding what to build this weekend. Each idea uses Luthien Proxy as real infrastructure, not just theory._

---

## 1. Proxy-Level Monitor for BashArena

**Track:** 2 (Control Protocol Design)
**Difficulty:** Accessible (minimal AI safety background needed)

Build a Luthien policy that watches agent actions in BashArena tasks and flags suspicious sysadmin commands before they run. Compare detection rates against BashArena's existing monitoring baselines.

**How Luthien fits:** Luthien sits between the agent and the model API, intercepting every request/response. Write a custom policy that pattern-matches dangerous bash commands (privilege escalation, file exfiltration, network pivots) and logs them with full conversation context.

**Why it's interesting:** BashArena has 257 multi-step sysadmin tasks with known attack vectors. Luthien gives you the interception layer for free, so you focus on writing smarter detection logic. Ctrl-Z showed resample protocols cut attack success from 58% to 7%. Can a proxy-level monitor do better?

**Judge appeal:** Aryan Bhatt (Ctrl-Z author), Tyler Tracy (Redwood)

---

## 2. LLM-as-Judge Interrogation Protocol

**Track:** 2 (Control Protocol Design)
**Difficulty:** Moderate

Use Luthien's LLM-as-judge policy to build an interrogation protocol: before the untrusted model's action runs, a trusted model reviews it and asks clarifying questions. Measure the safety/usefulness tradeoff at different interrogation depths.

**How Luthien fits:** Luthien's `SimpleLLMJudge` policy already calls a second model to evaluate responses. Extend it to ask follow-up questions back to the untrusted model before deciding to allow or block.

**Why it's interesting:** The hackathon explicitly calls for "interrogation protocols (trusted model questions untrusted model before execution)." Luthien gives you the scaffolding. You design the interrogation strategy and measure whether it catches more attacks without killing usefulness.

**Judge appeal:** Rogan Inglis (UK AISI), Fabien Roger (control paper co-author)

---

## 3. Red Team Luthien's Policies

**Track:** 3 (Building Better Red Teams)
**Difficulty:** Accessible (great for security-minded hackers)

Try to get harmful actions past Luthien's built-in policies (dangerous command blocking, DLP, LLM-as-judge). Document which evasion strategies work, which don't, and why. Build a dataset of adversarial transcripts.

**How Luthien fits:** Luthien is the target. Set up the proxy with its default policies, then try to get harmful actions through. Every attempt is fully logged in the conversation audit trail, giving you a complete dataset of attack/defense interactions.

**Why it's interesting:** The hackathon asks for "dataset of sneaky transcripts" and "red team scaffold producing really good attacks." Luthien's policies are real defenses, not toy examples. Breaking them produces useful safety research.

**Judge appeal:** Francis Rhys Ward (CTRL-ALT-DECEIT author), Mia Hopman (Apollo Research)

---

## 4. Multi-Policy Firewall for LinuxArena

**Track:** 2 (Control Protocol Design) -LinuxArena track (Equistamp prizes)
**Difficulty:** Moderate to advanced

Stack multiple Luthien policies into a layered defense: regex-based command blocking + DLP for data exfiltration + LLM-as-judge for intent analysis. Test against LinuxArena tasks and measure how the layers interact. Does adding policies improve safety linearly, or are there diminishing returns?

**How Luthien fits:** Luthien supports multiple active policies evaluated in sequence. The hackathon says "traditional security measures (firewall access for trusted model) -LinuxArena or BashArena great for this." Luthien IS that firewall.

**Why it's interesting:** Most control research tests single protocols. This tests whether composing multiple simple policies beats a single sophisticated one. Eligible for the $1,000 Equistamp LinuxArena prize track.

**Judge appeal:** Tyler Tracy (Redwood), Buck Shlegeris (would demonstrate practical proxy-level control)

---

## 5. Steganography Detection via Proxy Logging

**Track:** 3 (Building Better Red Teams)
**Difficulty:** Advanced (for experienced control researchers)

Use Luthien's full conversation logging to detect steganographic communication between colluding agents. Analyze token distributions, unusual formatting patterns, and information-theoretic anomalies in logged conversations. Compare against Redwood's "Hidden in Plain Text" findings.

**How Luthien fits:** Luthien logs complete request/response pairs with full token-level detail. Write an analysis policy that flags statistical anomalies in response content that could indicate hidden channels.

**Why it's interesting:** Steganographic collusion is one of the hardest control problems. Having a proxy that captures every message gives you the raw data to build detection tools. The hackathon mentions "multi-agent environments where agents can collude" as a Track 1 idea. This tackles the detection side.

**Judge appeal:** Buck Shlegeris (Redwood CEO), Francis Rhys Ward (steganography research)

---

## 6. Control Setting: Code Review with Hidden Vulnerabilities

**Track:** 1 (Control Setting Design)
**Difficulty:** Moderate

An AI agent does code review (main task) while trying to approve code with hidden security vulnerabilities (side task). Luthien watches the review process and flags suspicious approvals.

**How Luthien fits:** Luthien intercepts the agent's review comments and code suggestions. A policy checks whether approved code contains known vulnerability patterns (SQL injection, command injection, hardcoded secrets) that the agent should have caught but suspiciously didn't.

**Why it's interesting:** The hackathon asks for "environments with existing security vulnerabilities (main task = complex SWE, side task = trigger vulnerability)." Code review is a realistic setting where a scheming agent could do real damage by approving bad code.

**Judge appeal:** Rogan Inglis (UK AISI), Ram Potham (agent safety)

---

## 7. Policy Benchmark: DeSlop as Canary

**Track:** 2 (Control Protocol Design)
**Difficulty:** Accessible (good starter project)

Use Luthien's DeSlop policy (removes AI writing tics like "delve," "utilize," etc.) as a simple canary to validate your control evaluation pipeline. If your pipeline can measure DeSlop's effect on output, you can swap in harder policies (dangerous command blocking, LLM judge) and trust the measurements.

**How Luthien fits:** DeSlop ships with Luthien and is easy to test: send text with AI slop, verify it gets cleaned. Use this to calibrate your measurement setup before tackling harder control questions.

**Why it's interesting:** Many hackathon projects fail because the evaluation pipeline has bugs, not because the protocol is bad. Starting with a known-good simple policy lets you validate your tooling first. Then graduate to measuring safety/usefulness tradeoffs on real control policies.

**Judge appeal:** Practical approach that any judge would appreciate as methodologically sound

---

## 8. Trusted Editing via Proxy Rewrite

**Track:** 2 (Control Protocol Design)
**Difficulty:** Advanced

Luthien intercepts the untrusted model's code suggestions and has a trusted model rewrite suspicious sections before they reach the developer. Does the trusted editor keep the code working while removing sabotage?

**How Luthien fits:** Luthien's policies can modify responses before forwarding them. Build a policy that spots high-risk code patterns, sends them to a trusted model for rewriting, and returns the cleaned version. Both the original and edited versions get logged.

**Why it's interesting:** Trusted editing is a core control protocol from the foundational paper (Greenblatt et al.). Implementing it at the proxy layer means it works with any AI coding agent without modifying the agent itself. The hackathon Track 3 mentions "red-teaming trusted editing harder (editor preserves bad code)," so you could build AND red-team it.

**Judge appeal:** Fabien Roger (control paper co-author), Aryan Bhatt (Ctrl-Z)

---

## What Luthien CAN Do Today (for scoping)

- Sits between any AI coding agent and model API
- Logs all requests/responses with full audit trail
- Runs configurable policies: regex filters, dangerous command blocking, DLP, LLM-as-judge
- Block or flag responses that fail policy checks
- Multiple policies active simultaneously
- Docker-based setup; works with Claude Code, Cursor, etc.

## What Luthien CANNOT Do Yet

- Auto-retry/resample loop (planned, not shipped)
- One-liner CLI install (coming soon)
- Multi-agent coordination (single-agent proxy only)
