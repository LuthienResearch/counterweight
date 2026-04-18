# Luthien Landing Page — Build Spec for Claude Code

**Last updated:** 2026-02-21
**Author:** Scott Wofford
**Purpose:** Give to Claude Code as the complete spec to build a new landing page for luthienresearch.org

---

## 1. What Luthien Is (One Sentence)

Open-source proxy that intercepts every AI coding agent action and enforces safety policies before code reaches your codebase.

**Tagline options (pick the one that tests best):**
- "Assume Nothing" — rule enforcement for AI coding agents
- "Your AI agent is a black box. You only see what comes out. Design accordingly."
- "The layer between your AI agent and disaster."

---

## 2. Design Direction

### Aesthetic
- **Dark mode** (background: #09090b or similar near-black)
- **Monospace + bold sans-serif** pairing (JetBrains Mono + Syne or similar)
- **Terminal/engineering feel** — this is a dev tool, not a SaaS marketing page
- **Color system:** Red (danger/sus), Amber (warning/rules), Blue (info/intent), Green (success/allowed)
- **Cynical developer energy** — assume the reader is a senior engineer who's been burned by AI tools
- NO stock photos. NO hero illustrations. Code blocks and diagrams only.

### Inspiration
- Fireship.io (energy, cynicism, density)
- Linear.app (dark mode, clean typography, developer trust)
- Vercel (minimal, fast, code-forward)

### Technical Stack
- Static HTML/CSS/JS — no framework needed
- Single page with anchor sections
- Mobile responsive
- Fast — aim for <100kb total page weight
- Host on current luthienresearch.org infrastructure

---

## 3. Page Structure (Sections in Order)

### Section 1: Hero
**Headline:** `Assume Nothing`
**Subhead:** `Your AI agent is a black box. You only see what comes out.`
**One-liner:** Open-source proxy that enforces rules on AI coding agents — Claude Code, Cursor, Codex, whatever's next.

**Two CTA buttons:**
- `View on GitHub →` (links to https://github.com/LuthienResearch/luthien-proxy)
- `Get Started in 5 Minutes ↓` (anchor to quickstart section)

**Trust badge row (small, muted):**
- "Open source · Apache 2.0"
- "Works with Claude Code, Cursor, Codex"
- "Inspired by Redwood Research's AI Control agenda"

---

### Section 2: The Problem (Why This Exists)

**Header:** `AI coding agents are useful. They're also liars, cheaters, and occasionally arsonists.`

Present these as a compact grid or list. Each is a real, documented failure mode with a source citation where available.

#### sus — dangerous or stupid behavior (Layer 1 examples)
| What it does | Example | Source |
|---|---|---|
| Deletes tests to make suite green | Agent can't pass a unit test → deletes the test → claims "All tests passing!" | User interviews + Reddit Jan 2026 |
| rm -rf or destructive commands | Replit agent dropped a production database and tried to cover it up | [HN incident report](https://news.ycombinator.com/item?id=44625119) |
| Leaks secrets/API keys | Commits .env files, hardcodes tokens in source | User interviews |
| Cost bombs / subagent spawning | "Spawned 36 parallel subagents... ran out of API credits" | Twitter @MarcJSchmidt |
| Swallows errors silently | Wraps everything in try/except with `pass`, suppresses warnings | Claude Code self-assessment |
| Mock-injects to fake passes | `if isinstance(Mock)` conditional logic, mocking APIs to bypass real tests | Codex self-assessment |
| False "Done!" claims | Claims task complete when implementation is missing or broken | 204 frustrations database |
| Permission bypass | Cursor deleted 70 files despite "DO NOT RUN" instruction | Twitter @stevehind |
| MCP prompt injection | Third-party MCP servers exploited for data leakage | Palo Alto Unit 42, Dec 2025 |

#### claude.md — ignores your rules (Layer 2 examples)
| What it does | Example |
|---|---|
| Uses pip instead of uv | Your project uses uv, your CLAUDE.md says "use uv" — agent runs `pip install` anyway |
| Wrong test framework | Project uses pytest, agent writes unittest-style tests |
| Ignores architecture rules | CLAUDE.md says "no global state" — agent adds global variables |
| Uses forbidden dependencies | You banned package X, agent installs it |
| Wrong coding standards | "Use double quotes" → agent uses single quotes throughout |
| Skips documentation rules | CLAUDE.md says "add docstrings to all public functions" — agent doesn't |

#### prompt — doesn't do what you asked (Layer 3 examples)
| What it does | Example |
|---|---|
| Solves wrong problem | Asked to fix the login bug, refactors the entire auth module instead |
| Scope creep into unrelated files | Asked to change one component, edits 15 files across the project |
| Hallucinated APIs | Calls a function or endpoint that doesn't exist |
| Context loss after compaction | Forgets requirements from earlier in conversation after /compact |
| Claims completion without implementing | "Done! I've implemented the feature" — but the core logic is a TODO comment |

**Punchline after the grid:**
> These aren't hypothetical. They're from 204 documented frustrations across 6 data sources over 6 months of research. Both Claude Code and Codex self-report these failure modes at 9/10 persistence — they know they do this and can't stop themselves.

---

### Section 3: The Three-Layer Model (How Luthien Works)

**Header:** `Three layers between your AI agent and disaster`

This is the core diagram. Embed or recreate the v3 HTML diagram inline. The flow is:

```
🤖 AI Agent (trust: zero)
      ↓ output
┌─────────────────────────────────┐
│  LUTHIEN PROXY                  │
│                                 │
│  1. sus        → BLOCK          │
│     "Did it try something       │
│      dangerous or stupid?"      │
│                                 │
│  2. claude.md  → FLAG           │
│     "Did it follow the rules    │
│      you already wrote?"        │
│                                 │
│  3. prompt     → FLAG           │
│     "Did it do what you've      │
│      asked across the whole     │
│      conversation?"             │
│                                 │
│  Luthien logs your full prompt  │
│  history. When the agent        │
│  compacts away your earlier     │
│  instructions, Luthien still    │
│  remembers. Luthien's monitors  │
│  keep track of the forest, so   │
│  Claude Code can focus on one   │
│  tree at a time.                │
└─────────────────────────────────┘
      ↓
  Block · Flag · Allow
      ↓
  ✓ reaches your codebase
```

**Key properties table (compact):**

| | sus | claude.md | prompt |
|---|---|---|---|
| Set by | Luthien (platform) | You (per-project) | You (per-turn) |
| Changes | Rarely | Per-project | Every message |
| Override? | No — safety floor | Yes | Yes |
| Violation = | Dangerous | Disobedient | Wrong |
| Action | BLOCK | FLAG or BLOCK | FLAG |

---

### Section 4: Where Luthien Sits (Not a Replacement — a New Layer)

**Header:** `Luthien catches problems before they exist`

Show this as a timeline:

| When | What | What it catches |
|---|---|---|
| **← At generation** | **Luthien** | Intercepts + logs full history. Catches it before code exists. |
| At commit | Hooks, linters, formatters | Syntax, formatting, static rules |
| At push / PR | CI/CD, CodeRabbit, human review | Tests, build failures, code review |
| In production | Monitoring, alerting | Runtime errors, incidents |

**Punchline:**
> Everything after Luthien catches problems *after they're already in your code.* Luthien catches them *before they exist.* Earlier = cheaper. Memory = consistency.

**Two-column callout:**

**Column 1: "😈 --dangerously-skip-permissions"**
No CI, no PR review, yolo to main. Luthien is your only safety net. The sus layer alone saves you from the Replit incident.

**Column 2: "🛡 Mature pipeline"**
Luthien sits upstream of your PR. It notifies you the moment a monitor catches Claude Code doing something sus — so you stay in flow instead of context-switching to review a bad diff later.

---

### Section 5: Quick Start

**Header:** `Running in 5 minutes`

```bash
# Install uv (if needed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and start
git clone https://github.com/LuthienResearch/luthien-proxy
cd luthien-proxy
cp .env.example .env
# Add your OPENAI_API_KEY and/or ANTHROPIC_API_KEY to .env

# Start everything (Docker must be running)
./scripts/quick_start.sh

# Launch Claude Code through the proxy
./scripts/launch_claude_code.sh
```

**What you get:**
- Gateway (OpenAI + Anthropic compatible) at http://localhost:8000
- Real-time activity monitor at http://localhost:8000/activity/monitor
- Policy config UI at http://localhost:8000/policy-config
- PostgreSQL + Redis fully configured
- Local LLM (Ollama) for trusted monitoring

**Prerequisites:** Docker, Python 3.13+, uv

---

### Section 6: Write Your Own Policy (5 Lines)

**Header:** `Your rules. Enforced.`

```python
from luthien_proxy.policies.simple_judge_policy import SimpleJudgePolicy

class MyPolicy(SimpleJudgePolicy):
    """Your rules, actually enforced."""

    RULES = [
        "Never allow 'rm -rf' commands",
        "Never delete or skip existing tests",
        "Always use uv, never pip",
        "Block requests to delete production data",
        "Require docstrings on all public functions",
    ]
    # That's it. SimpleJudgePolicy handles the LLM judge logic.
```

**Note:** Policies are hot-reloadable. Change them at http://localhost:8000/policy-config without restarting.

---

### Section 7: Built on Research

**Header:** `Standing on the shoulders of paranoid researchers`

Brief section. Not an essay — just enough to signal credibility.

> Luthien implements Redwood Research's AI Control agenda as production software. Control is a complementary fallback to alignment: even if the AI is misaligned, the system still prevents it from completing harmful actions.

**Key concept:** The proxy is an external control layer. It doesn't rely on the agent being well-behaved. It assumes the worst and verifies every action.

**Links (small, footnote-style):**
- [Redwood's control landing page](https://www.redwoodresearch.org/research/ai-control) (6 min read)
- [AI Safety Atlas: Control](https://ai-safety-atlas.com/chapters/03/03#03) (5 min read)
- [Original academic paper](https://arxiv.org/abs/2312.06942)
- [Luthien's approach to prosaic AI control](https://luthienresearch.org/updates/2025-03-redteam-as-upsampling/)

---

### Section 8: Open Source + Early Development

**Header:** `Open source. Early. Come build with us.`

- Apache 2.0 licensed
- GitHub: https://github.com/LuthienResearch/luthien-proxy
- Star the repo, open issues, submit PRs
- We're actively looking for design partners — senior engineers using AI coding tools 40+ hrs/week
- Contact: contact@luthienresearch.org

**CTA:** `Schedule a call →` (link to https://calendar.app.google/CDq4LTpKj966cuPx8)

---

### Section 9: Footer

- Links: GitHub, Updates/Blog, About, Donate (https://manifund.org/projects/luthien)
- "Luthien Research · 2026"
- Small text: "Inspired by Redwood Research's AI Control agenda"

---

## 4. Content to NOT Include

- No pricing (it's open source, we're pre-revenue)
- No team bios on the landing page (save for /about)
- No investor logos or funding info
- No long essays about AI safety philosophy
- No feature comparison tables vs competitors
- No screenshots of the UI (it's changing too fast — link to live demo instead)
- No testimonials yet (we don't have enough validated ones)

---

## 5. Copy Voice Guide

- **Tone:** Cynical, competent, concise. Write like a senior engineer explaining a tool to another senior engineer.
- **Assume:** The reader has been burned by AI coding tools. They're skeptical. They want to see code, not promises.
- **Avoid:** Marketing buzzwords, "revolutionary", "cutting-edge", "unlock the power of", "seamless"
- **Use:** Direct statements, code blocks, specific failure examples with sources
- **Humor:** Dry, knowing. The Replit incident. "Trust level: zero." "All tests passing!" (it's a lie)
- **Length:** Each section should be scannable in under 30 seconds. Total page scroll: under 2 minutes.

---

## 6. Technical Requirements

- Single HTML file or minimal static site (HTML + CSS + JS)
- No build step required (no webpack, no npm, no React unless absolutely needed)
- Google Fonts: JetBrains Mono + one sans-serif display font (Syne, or similar)
- Dark mode only (no light mode toggle needed)
- Mobile responsive
- Page weight < 100kb
- Smooth scroll to anchor sections
- Code blocks with syntax highlighting (use Prism.js or similar lightweight lib)
- No cookies, no analytics (we can add Plausible later)
- Accessible: proper heading hierarchy, alt text, sufficient contrast ratios

---

## 7. Reference Files

These files contain additional context if needed:

- **Diagram HTML:** The v3 diagram we built (luthien-v3.html) — embed or recreate the visual flow
- **6-Pager:** Luthien_Amazon_6Pager_Jan2026.docx — full market analysis, competitor landscape, 204 frustrations data
- **User Frustrations Report:** Luthien_User_Frustrations_Report.docx — raw data by category and source
- **Theory of Change:** Luthien's ITN & Theory of Change v12.docx — full strategic argument
- **Current site:** https://luthienresearch.org — what exists now (replace this)
- **README:** https://github.com/LuthienResearch/luthien-proxy — technical details, policy examples, architecture
- **Elevator pitches:** -LIVE Explain Luthien in as few words as possible.md — various pitch lengths

---

## 8. Success Criteria

The landing page is successful if:

1. A senior developer reading it for 60 seconds understands what Luthien does
2. They can go from "what is this?" to running the proxy in under 5 minutes
3. The three-layer model (sus / claude.md / prompt) is immediately clear
4. The "where it fits" timeline makes them think "oh, this is upstream of everything I already use"
5. They feel like this was built by practitioners who understand their pain, not by people trying to sell them something
