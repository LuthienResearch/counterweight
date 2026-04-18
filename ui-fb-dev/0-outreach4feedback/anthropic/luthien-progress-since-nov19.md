# Luthien Progress Briefing: Nov 19, 2025 → March 23, 2026

**For:** April 1 call with Fabien Rogers (Anthropic alignment researcher)
**Scale:** 254 merged PRs, 316 commits, 4 contributors

---

## Mapped to Fabien's Three Contribution Paths

### 1. Training Data for Safety Monitors

**What we have:**
- Full request/response logging infrastructure — every proxied conversation is stored with timestamps, session IDs, policy decisions, and annotations
- Conversation history viewer UI (`/history`) with filters, search, markdown export
- Policy intervention annotations inline on turns that triggered policies
- Session-based tracking (extracts session ID from Claude Code metadata)
- Debug API for querying conversation events programmatically

**What we DON'T have yet (gap):**
- No automated dataset generation pipeline from logged interactions
- No export-to-training-format tooling
- No synthetic evaluation harness
- No labeled dataset of safety violations vs. benign behavior

**The opportunity:** We're sitting on real-world logged AI agent sessions with policy intervention labels. This is raw material for training data, but needs a pipeline to extract/label/format it.

---

### 2. Evaluations for Prosaic Misalignment

**What we've built — this is our strongest area:**

- **LLM Judge Infrastructure** — `ToolCallJudgePolicy` evaluates tool calls with configurable probability thresholds and explanations; `SimpleLLMPolicy` evaluates and transforms response content blocks
- **Policy Composition** — `MultiSerialPolicy` (sequential chains) and `MultiParallelPolicy` with 5 consolidation strategies: `first_block`, `most_restrictive`, `unanimous_pass`, `majority_pass`, `designated`
- **7 preset policy demos** with auto-discovery: block dangerous commands, block sensitive file writes, block web requests, enforce package manager standards, etc.
- **Mock E2E testing framework** (#307) — real HTTP requests against fake backend, zero API cost
- **Overseer multi-turn E2E test harness** (#266) — tests multi-turn agent sessions
- **DogfoodSafetyPolicy** — regex-based blocking for self-destructive agent behavior (agent killing its own proxy)

**Concrete prosaic failure stories from user research:**
1. **False success claims** — Nathan: "Claude comments out failing tests and declares success" (test-cheating)
2. **Plan abandonment** — Quentin: "AI switched from Kubernetes to Terraform without asking"
3. **Silent failures** — Nico: code appears to work but silently drops errors
4. **Backward compatibility hacks** — Tyler (Redwood): 60% false positive rate on pattern matching detection
5. **Unrequested functionality** — Nathan, Nico: agent adds features nobody asked for
6. **Self-destruction** — Dogfooding: agent ran `docker compose down` and severed its own API connection

**Planned but not yet built:**
- User Story 3: Multi-Reviewer Evaluation Pipeline (ensemble safety evaluation with specialized reviewers, reviewer disagreement detection)
- User Story 4: Human-in-the-Loop approval workflow (pause/resume with approval UI)

---

### 3. UX Exploration for Classifier Integration

**What we've built:**
- **Auto-discovering Policy Config UI** — generates form fields from policy constructor signatures using type hints; hot-reload without restart
- **Policy context injection** (#355) — injects system message informing the LLM about active policies, preventing model confusion when policies modify output
- **Chain-first configuration UX** — users configure policy chains rather than individual policies
- **Warning injection on judge failure** — instead of silent pass-through, inject visible warning when SimpleLLMPolicy judge fails
- **7 SimpleLLMPolicy presets** — one-click activation of pre-built safety rules
- **Conversation live view with diff display** — see policy modifications in real-time

**Key UX findings from user trials:**
- Tyler (Redwood Research — **strongest design partner**): installed live on call, "smoothest user trial ever," wants benchmark data (Control Arena), will distribute to 10-person team
- Nico (4th session): pip-to-uv preset "resonated immediately," history view "superior to Langsmith," requested: run as service, share rules via VCS
- Zac (Counterweight): "Policy config is overwhelming and hard to use" — led to simplification work
- Jack (Counterweight): wants notifications in Claude Code, not a separate UI
- Peter (QADNA): comprehensive QA trial found 9 issues, stability improving
- **Demo reliability was 75% at EAG SF (Feb 2026)**, now improving rapidly

---

## Top 3 Most Significant Accomplishments

1. **Real policy composition system** — serial/parallel chains with LLM judges, configurable consolidation strategies, and 7 preset demos. This is the infrastructure for running classifiers on live agent traffic.

2. **Dramatically lowered onboarding barrier** — from "clone repo + Docker Compose" to `pip install luthien-cli && luthien onboard` with SQLite, no Docker needed. Senior dev can get proxied in ~10 min.

3. **Concrete prosaic failure catalog from real users** — false success claims (test-cheating), plan abandonment, self-destruction, silent failures. These are real stories from developers using AI agents 40+ hours/week.

---

## What's Demoable on April 1 (5 minutes)

| Demo | Time | Status |
|------|------|--------|
| `pip install luthien-cli && luthien onboard` → proxied Claude Code in <5 min | 2 min | Working |
| Hot-swap a policy (e.g., `prefer_uv` or `block_dangerous_commands`) and see it take effect on next Claude Code message | 1 min | Working |
| Conversation history viewer — show policy interventions inline on real sessions | 1 min | Working |
| Policy diff viewer — show before/after of policy modifications on a real call | 1 min | Working |

**Best concrete prosaic failure story for the call:**
> "During dogfooding, the AI agent ran `docker compose down` and killed the proxy it was communicating through — severing its own connection mid-session. This led us to build DogfoodSafetyPolicy, a zero-latency regex blocker. But the deeper insight is: **we now have infrastructure to run ANY classifier on live agent traffic** — tool calls, response content, or full conversation context — with serial/parallel composition and configurable consolidation strategies."

---

## Needs More Context (Flag for Scott/Jai)

- **Training data pipeline**: Has Jai discussed any plans for exporting logged sessions as labeled training data? This is the clearest gap relative to Fabien's interest.
- **Control Arena / benchmark integration**: Tyler (Redwood) specifically asked for benchmark data. Is there a plan to integrate with Control Arena or similar evals?

---

## Quick Reference: Key Numbers

| Metric | Value |
|--------|-------|
| Merged PRs since Nov 19 | 254 |
| Total commits | 316 |
| Contributors | 4 (Jai, Scott, Peter, Paolo) |
| User interviews/trials | 15+ people |
| Policy presets shipping | 7 |
| Stability score (latest) | 65-88/100 (up from 20-50) |
| Unit test coverage | 90% |
| Strongest design partner | Tyler Tracy (Redwood Research) |
| Enterprise prospect | Kushal/Relativity (3,500 engineers) |
