# Antimemetic AI — Competitive Analysis

**Date:** 2026-04-01
**Source:** https://antimemeticai.com/d/pclqlt37c9r2hk
**Shared by:** Esben

## What they do

Antimemetic AI secures AI agent swarms by controlling how semantic content in code (comments, variable names, code structure) influences agent behavior. They treat harmful code patterns as "memetic" threats that propagate through codebases.

## Product: 4-stage platform

1. **Observe** — map how patterns spread through codebases
2. **Control** — remove harmful patterns, reinforce beneficial ones
3. **Vaccinate** — deploy defensive comments that neutralize attacks
4. **Amplify** — strengthen protective patterns

## Team and funding

- Rafael Irgolic (ex-Guardrails AI) and Jonathan Eicher (ex-Softmax)
- $2M pre-seed, 18 months runway

## Key research findings (Nanotown pilot)

- Naming conventions significantly influence agent behavior
- "secure_" prefix: agent spontaneously added password + bcrypt hashing
- "energetic_" prefix: highest cross-domain persistence (+54% decorators, asyncio)
- "lazy_" prefix: weakest propagation (47% signal decay)

## How it relates to Luthien

| | Luthien | Antimemetic |
|---|---|---|
| Where | API traffic (between agent and backend) | Codebase (what the agent reads) |
| When | Runtime (intercept requests/responses) | Pre-runtime (analyze/modify code patterns) |
| What | Block dangerous actions, verify honest behavior | Remove malicious code patterns, vaccinate codebases |
| How | Proxy + judge model | Semantic analysis of naming/comments |

## Assessment

**Complementary, not competitive.** They control inputs to the agent (codebase environment). Luthien controls outputs (actions and responses). A user could use both.

Potential partner or mutual referral. Rafael's Guardrails AI background is adjacent space.
