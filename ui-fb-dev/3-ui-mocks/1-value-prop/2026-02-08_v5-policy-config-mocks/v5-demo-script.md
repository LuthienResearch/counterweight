# Super Bowl Demo Script

**Time:** 5-10 min per person | **Have this on your phone**

---

## Setup Checklist

- [ ] HTTP server running on 8888
- [ ] Luthien gateway running on 8000 (docker compose)
- [ ] Logged into localhost:8000 (password: `admin-dev-key`)
- [ ] All tabs open and loaded (see below)
- [ ] Phone ready to take notes

### Tabs to open

| Tab | URL | What |
|-----|-----|------|
| 1 | [README Option A](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-a-problem-first.md) | Landing: Problem-First |
| 2 | [README Option B](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-b-visual-flow.md) | Landing: Visual Flow |
| 3 | [README Option C](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-c-use-case-first.md) | Landing: Use-Case-First |
| 4 | [Policy: Terminal](http://localhost:8888/_UI_Specs/v5-option-a-terminal.html) | Policy config: terminal-only |
| 5 | [Policy: Web Dashboard](http://localhost:8888/_UI_Specs/v5-option-b-web-ui.html) | Policy config: web UI |
| 6 | [Policy: Hybrid](http://localhost:8888/_UI_Specs/v5-option-c-hybrid.html) | Policy config: both |
| 7 | [DeSlop Demo](http://localhost:8888/_UI_Specs/v5-deslop-demo.html) | Interactive: clean AI slop |
| 8 | [Live UI](http://localhost:8000/policy-config) | Bonus: Jai's dynamic forms |

---

## The pitch (30 sec)

> "AI coding agents write most of the code now. But they do dumb stuff — delete files, ignore your rules, go off-task. We built a proxy that enforces rules on the AI. Like a bouncer for your codebase."

---

## For NON-TECHNICAL friends: start with DeSlop (Tab 7)

> "You know how AI writes with those annoying em dashes everywhere? This cleans that up automatically."

**Do:** Click "Clean It" on the LinkedIn sample. Show the count. Try code comment sample.

**Ask:** "Does that make sense? What other annoying things would you want fixed?"

Then show Landing Page options (Tabs 1-3) and ask which one is clearest.

---

## For TECHNICAL friends: full flow

### 1. Landing Page (Tabs 1-3) — "which makes you want to try it?"

| Tab | Say |
|-----|-----|
| A | "Leads with the pain — here's what agents do wrong." |
| B | "More visual — before/after, flow diagram." |
| C | "Leads with 'pick your policy' — code examples up front." |

**Ask:** Which makes you want to try it? What's confusing? Does "two env vars" land?

### 2. Policy Config (Tabs 4-6) — "how should you configure rules?"

| Tab | Say |
|-----|-----|
| A | "Everything in terminal. Blocks show inline." |
| B | "Web dashboard. Toggles, blocked log." |
| C | "Both. Terminal for real-time, dashboard for config." |

**Ask:** Which would you actually use? Would you open a browser for this?

### 3. Bonus: Live UI (Tab 8)

> "This is what my co-founder built. Auto-generates forms from code. More powerful but more complex."

**Ask:** Overwhelming or useful? This or the toggles?

---

## Key questions (pick 2-3, don't interrogate)

1. "Which would you **actually use**?" (not which looks coolest)
2. "What's **confusing**?" (watch their face)
3. "What's **missing**?"
4. "Would you **pay** for this?" (only if engaged)

---

## After each person — note on phone

```
Name:
Technical? Y/N
Landing page: A / B / C / none
Policy config: A / B / C / none
Key quote:
Confused by:
```
