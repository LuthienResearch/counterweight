# Onboarding Inspiration (2026-02-26)

Collected from Happy Coder and Notion. Focus: how to make first-time setup feel effortless, and mental models that make complex systems instantly understandable.

---

## 1. Happy Coder: "Type `happy` instead of `claude`"

### What it is
Happy Coder is a mobile client for Claude Code. It lets you control Claude Code sessions from your phone — approve permissions, send prompts, monitor progress — with end-to-end encryption.

### Why the onboarding is great

**The entire install is one line:**
```
npm i -g happy-coder && happy
```

**The entire quick start is 3 steps:**
1. Download mobile app
2. `npm install -g happy-coder`
3. Scan QR code

No signup. No account. No API keys. No config files. It piggybacks on your existing Claude Code subscription.

**The key UX innovation:** You type `happy` instead of `claude`. That's it. Everything else works identically — same tools, same permissions, same CLAUDE.md, same hooks. The wrapper is invisible.

### Could Luthien do this?

**The pattern:** Instead of asking users to configure a proxy URL, set env vars, and update their Claude Code config — what if they just typed `luthien` instead of `claude`?

```bash
# Current Luthien setup (multiple steps, error-prone)
export ANTHROPIC_BASE_URL=https://your-proxy.luthienresearch.org
export ANTHROPIC_API_KEY=sk-luthien-...
# Then configure Claude Code to use these...

# Dream state (Happy Coder pattern)
npm install -g luthien-cli
luthien   # wraps claude, routes through proxy automatically
```

**What the wrapper could do:**
- Auto-configure the proxy URL
- Handle auth (login once, token persists)
- Pass through everything else to Claude Code unchanged
- Show a small indicator that Luthien policies are active

**Trade-offs to consider:**
- Happy Coder wraps the CLI process; Luthien is a network proxy — different architecture
- A CLI wrapper might conflict with how Claude Code manages its own process
- Could offer BOTH: CLI wrapper for easy onboarding, proxy URL for advanced/enterprise users
- The wrapper could literally just set the right env vars and exec `claude` under the hood

### Mental models they use (steal these)

| Mental Model | How Happy Coder uses it | Luthien equivalent |
|---|---|---|
| **"Post office"** | The relay server is a post office passing sealed envelopes it can't open | Luthien proxy is a checkpoint — it reads the message, applies rules, then forwards it |
| **"Remote control"** | Your phone is a remote control for your Mac | Luthien is a safety net under the tightrope — the coder works normally, Luthien catches problems |
| **"Same session, two windows"** | Phone and desktop are equal views into one session | Could apply to Luthien's activity viewer — same session, but with an oversight lens |
| **"Extending reach, not replacing"** | Explicitly NOT a mobile IDE | Luthien explicitly does NOT slow you down or change your workflow |
| **Unix: "do one thing well"** | Just bridges phone ↔ desktop | Luthien does one thing: enforces safety policies on AI agent actions |

### Their anti-patterns (things they deliberately avoid)
- No account creation ("not a SaaS product")
- No cloud costs (your hardware)
- No lock-in (works with vanilla Claude Code)
- No data collection ("None. Zero. Nothing.")
- No complex config (QR code pairing vs. typing credentials)

---

## 2. Happy Coder: Full Onboarding Explanation (What Worked on Scott)

This explanation was given to Scott after he installed Happy Coder. He called it "pretty good" and asked to save it as inspiration. Key elements: mental model first, then day-to-day usage, then concrete example flow.

### The explanation that landed:

> **The mental model:** Your Mac is the engine, your phone is the remote control. Claude Code runs on your Mac like normal — Happy just encrypts the session and streams it to your phone.
>
> **Starting a session:**
> ```bash
> happy          # instead of 'claude'
> ```
> That's it. Everything else works the same — same tools, same permissions, same CLAUDE.md.
>
> **From your phone you can:**
> - Read responses as they stream in real-time
> - Send prompts — type or use voice input
> - Approve/deny tool calls — this is the killer feature. If Claude Code wants to edit a file or run a command, you get a push notification and can approve from your phone
> - Review history — scroll back even if terminal is closed
>
> **Example flow:**
> 1. At your desk: `happy` → "run dev_checks.sh and fix any failures"
> 2. Walk to kitchen, make coffee
> 3. Phone buzzes: "Claude wants to edit `src/foo.py`" → tap Approve
> 4. Phone buzzes: "Claude wants to run `uv run pytest`" → tap Approve
> 5. Come back to desk, work is done
>
> **Things to know:**
> - Sessions are encrypted end-to-end
> - Mac must be on — if your laptop sleeps, the session pauses
> - It's a wrapper, not a replacement — all your existing config still applies
> - Both phone and terminal see the same session

### Why this worked (onboarding design takeaways):
1. **Mental model FIRST** ("engine + remote control") before any features
2. **One-line start command** — shows how little changes
3. **Concrete scenario** (desk → kitchen → phone approval → done) makes it tangible
4. **"Things to know"** section sets expectations without overwhelming

---

## 3. Notion: Guided First Steps Modal

**Screenshot:** `notion-onboarding-modal.png` (if available in this folder — otherwise see conversation from 2026-02-26)

### What it does
When you first open Notion, a modal pops up: **"Get extra help on your first steps in Notion"** with the subtext: "Confused by Notion? Book a quick, friendly session with a consultant who can show you the ropes."

**Three illustrated action cards:**
- "set up a database" (with database icon)
- "manage projects" (with project icon)
- "create workflows" (with workflow icon)

**CTA:** "Get started" button

### Why this is interesting for Luthien
- **Acknowledges confusion is normal** — "Confused by Notion?" normalizes the feeling
- **Offers human help, not just docs** — "Book a session with a consultant"
- **Task-oriented options** — not "learn about features" but "set up a database" (the thing you actually want to DO)
- **Illustrated, friendly, low-pressure** — cartoon people, warm tone, easy to dismiss (X button)

### Luthien equivalent ideas
- First-time user opens Activity Viewer: modal with "What do you want to protect against?"
  - "Block dangerous commands" (with shield icon)
  - "Monitor what agents are doing" (with eye icon)
  - "Set cost limits" (with dollar icon)
- Or: first `luthien` CLI run shows: "What kind of policies do you want?"
  - Quick presets: "Safety basics", "Full monitoring", "Custom"
- The human help angle: "Want a 15-min setup call? We'll configure policies for your team's workflow"

---

## 4. Happy Coder: Detailed Product Docs (Reference)

### Landing page positioning
- **Headline:** "Claude Code Anywhere"
- **Subhead:** "Spawn and control multiple Claude Codes in parallel. Happy Coder runs on your hardware, works from your phone and desktop, and costs nothing. Open source."
- Install command front and center on the page

### How they explain the architecture (3 parts)
1. **CLI Program (`happy`)** — Runs on your computer. Starts Claude Code and watches what it does. Encrypts and sends to server.
2. **Mobile App** — Runs on your phone. Gets encrypted data, shows what Claude Code is doing.
3. **Relay Server** — Connects computer and phone. Passes encrypted messages. Can't read your data. Just moves encrypted blobs.

### Why the relay server exists (firewall mental model)
> "The server solves a simple problem: firewalls. Your phone and computer are usually on different networks. They can't talk directly. The server acts like a post office. Both devices connect OUT to the server. This works because firewalls usually allow outgoing connections."

### Their "zero trust" pitch
> "You might wonder: 'The developers run the server. Why should I trust them?' Good question! You don't have to trust us."
- Phone and computer share a secret key through QR code. Server never sees it.
- Before sending data, computer encrypts with this key.
- Server only sees encrypted blobs.

### Voice agent
Not just dictation — an AI intermediary (Claude Sonnet) that converts "rubber duck planning" into concrete Claude Code requests. Speaks back results via Eleven Labs TTS.

### Permission system on mobile
- Intercepts MCP tool calls and file edits
- Shows exactly what Claude wants to do before it happens
- Allow/Deny buttons on mobile
- "Remember for this session" option

### Their philosophy on mobile coding
> "Happy Coder is not designed for writing code directly on phones. Instead, it extends reach to development machines with one core principle: working with Claude Code from anywhere in the same session without friction."

> "Programming involves thinking that doesn't always happen at desks. Best insights often occur during walks, lunch, or quiet moments before sleep."

### Their FAQ gold
- **"What justifies your claim that Happy Coder is simple?"** — No signup, cross-platform, "it just works", smart error handling, Unix philosophy
- **"Is Happy Coder free?"** — "Yes, completely free. No catches. No usage limits. No user limits. Open source (MIT)."
- **"Am I locked in?"** — "No lock-in whatsoever. Works with vanilla Claude Code — not a proprietary wrapper."
- **Latency:** ~300ms typical
- **Data collected:** "None. Zero. Nothing."

---

## Key Takeaways for Luthien Onboarding

1. **One command to start** — `happy` instead of `claude`. Can Luthien do `luthien` instead of `claude`?
2. **Mental model before features** — Explain WHAT it is in one sentence before listing what it does
3. **Concrete scenario** — Show the user's actual day, not abstract feature lists
4. **Acknowledge confusion** (Notion) — "Confused? That's normal. Here's help."
5. **Task-oriented first steps** (Notion) — "What do you want to DO?" not "Here are our features"
6. **No signup friction** (Happy) — Can Luthien offer a no-account trial?
7. **Security as a feature, explained simply** (Happy) — "Post office with sealed envelopes"
8. **Philosophy statement** — Both Happy and Notion are clear about what they ARE and AREN'T
