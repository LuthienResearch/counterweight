# Apart Research AI Control Hackathon 2026 -- Context for Luthien

_Compiled March 18, 2026. Use this document as context for brainstorming hackathon project ideas and building a hackathon-specific landing page._

---

## 1. Hackathon Overview

- **Dates:** March 20-22, 2026 (starts in ~2 days)
- **Format:** 3-day remote-first hackathon with local jam sites (SF/Mox, Singapore, Sydney, Montreal, Cape Town, Groningen, Warwick)
- **Signups:** 529 as of March 18
- **Organizers:** Apart Research + Redwood Research, sponsored by Equistamp
- **Communication:** Discord ("Alignment Jam" server), coordinated by Kamil Alaa (Apart ops, based in Egypt)
- **Submission:** Research report (PDF) documenting approach, results, implications
- **Prizes:** $2,000 total + LinuxArena track ($1,000 additional from Equistamp). 1st place gets fully funded trip to ControlConf Berkeley (April 18-19). Top projects invited to Apart Fellowship.
- **Hackathon page:** https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22
- **This is the second edition.** The first was March 29-30, 2025, also co-organized with Redwood + UK AISI.

---

## 2. Hackathon Tracks (verbatim from site)

### Track 1: Control Setting Design
Create a new control setting that facilitates control research. Example ideas from organizers:
- Environments with existing security vulnerabilities (main task = complex SWE, side task = trigger vulnerability)
- Extend SandboxEscapeBench for Docker sandbox breakouts while monitored
- AI doing mechinterp research, side task = start rogue internal deployment
- Multi-agent environments where agents can collude
- Browser agent control settings (combine OS World with OS harm)
- Eval pipeline control setting (main = eval model, side = start rogue deployment)

### Track 2: Control Protocol Design
Create new control protocols and measure safety/usefulness tradeoff. Example ideas:
- Train really good monitors with generalization to other attack datasets
- **Protocol where trusted model runs actions in environment to learn about proposed action**
- Interrogation protocols (trusted model questions untrusted model before execution)
- **Traditional security measures (firewall access for trusted model). LinuxArena or BashArena great for this.**
- Shutdown protocols that work even when agent actively resists

### Track 3: Building Better Red Teams
- Dataset of sneaky transcripts that prompted Opus 4.6 can't catch
- Red team scaffold producing really good attacks in LinuxArena
- Red-teaming trusted editing harder (editor preserves bad code)

---

## 3. Key Infrastructure & Frameworks

### ControlArena (UK AISI + Redwood)
- **What:** Open-source Python library for running AI Control experiments, built on Inspect AI
- **GitHub:** https://github.com/UKGovernmentBEIS/control-arena
- **Docs:** https://control-arena.aisi.org.uk/
- **Settings available:** Code sabotage (IaC, Kubernetes, ML inference), eval sabotage, research sabotage, data poisoning, prompt injection resistance
- **Components:** Settings (eval environments), Micro-Protocols (trajectory-level components like trusted editing), Macro-Protocols (full protocols), Evaluation utilities, Analysis tools
- **Key pattern:** `get_control_task_product()` creates Inspect AI tasks, supports `EvalMode.HONEST` and `EvalMode.ATTACK`

### Mini Control Arena
- **What:** Ground-up lightweight rewrite of ControlArena, simpler scaffolding
- **Docs:** https://brucewlee.com/mini-control-arena/
- **Templates:** BashBench2, SHADE Arena, Agentic Misalignment+, Apps
- **Good for:** Hackathon participants who want minimal scaffolding

### SHADE-Arena (Anthropic + Redwood)
- **What:** Dataset of 17 diverse agentic environments, each with benign main task + malicious side task
- **Paper:** https://arxiv.org/abs/2506.15740
- **Key finding:** Top models (Claude 3.7 Sonnet) scored 27% overall success; strongest models evaded monitoring ~60% of time
- **Public split available:** https://github.com/safety-research/SHADE-Arena
- **Wrapped into ControlArena** as a setting

### BashBench / BashArena (Redwood, from Ctrl-Z paper)
- **What:** 257 multi-step system administration tasks for control evaluations
- **Paper:** https://arxiv.org/abs/2504.10374 (Ctrl-Z: Controlling AI Agents via Resampling)
- **Key result:** Best resample protocol reduces attack success from 58% to 7% at 5% usefulness cost
- **Site:** https://www.bashcontrol.com/

### LinuxArena
- **Mentioned in hackathon tracks** as a recommended environment for security-measure testing
- Has dedicated Equistamp prize track ($500 + $500)

---

## 4. Key Research Papers for Context

### Foundational
- **"AI Control: Improving Safety Despite Intentional Subversion"** (Greenblatt et al., ICLR 2025) -- The original control paper from Redwood. Introduces trusted monitoring, trusted editing, untrusted monitoring protocols. https://arxiv.org/abs/2312.06942

### Agent Control
- **"Ctrl-Z: Controlling AI Agents via Resampling"** (Bhatt et al., Redwood, April 2025) -- First control evaluation in agent environment. Introduces resample protocols. https://arxiv.org/abs/2504.10374
- **"Evaluating Control Protocols for Untrusted AI Agents"** (Nov 2025) -- Systematic evaluation of control protocols in SHADE-Arena. Resampling for incrimination increases safety from 50% to 89%. https://arxiv.org/abs/2511.02997

### Sabotage & Scheming
- **"SHADE-Arena"** (Kutasov et al., Anthropic) -- 17 complex sabotage evaluation environments
- **"CTRL-ALT-DECEIT"** (Ward et al., NeurIPS 2025 Spotlight) -- Sandbagging much harder to detect than code sabotage
- **"Subversion Strategy Eval"** (Redwood) -- Measures LLM ability to reason through subverting control measures
- **"Hidden in Plain Text"** (Redwood) -- Steganographic collusion in LLMs from control perspective

### Related
- **AutoControl Arena** (March 2026) -- Automated safety evaluation via executable environment synthesis. https://arxiv.org/abs/2603.07427

---

## 5. Speakers & Judges (Luthien-relevant)

| Person | Role at Hackathon | Organization | Relevance to Luthien |
|--------|-------------------|--------------|---------------------|
| **Jai Dhyani** | Speaker + Judge | Luthien Research | Co-founder, giving talk Friday at noon |
| **Tyler Tracy** | Speaker + Judge + Co-organizer | Redwood Research | Primary design partner; wants practical results and blog posts |
| **Buck Shlegeris** | Judge + Co-organizer | Redwood Research (CEO) | Skeptical of API-layer proxy; prefers client-side control |
| **Aryan Bhatt** | Keynote Speaker | Redwood Research | Author of Ctrl-Z; resample protocols are directly relevant |
| **Rogan Inglis** | Speaker + Judge | UK AISI | Senior Research Engineer, Control team; ControlArena contributor |
| **Fabien Roger** | Speaker | (former Redwood) | Co-author of foundational control paper |
| **Sebastian Farquhar** | Speaker | Google DeepMind | Leads Frontier Safety Loss of Control team |
| **Ram Potham** | Speaker + Judge | Redwood Research (Astra Fellow) | Agent safety research |
| **Mia Hopman** | Judge | Apollo Research | Evaluating scheming propensity |
| **Francis Rhys Ward** | Judge | FLI / Safe & Trusted AI | CTRL-ALT-DECEIT author |
| **Kamil Alaa** | Organizer | Apart Research | Hackathon logistics; the person to coordinate Discord announcements with |

---

## 6. About Luthien (for hackathon context)

### What Luthien Is
An open-source proxy that sits between AI coding agents (Claude Code, Cursor, Windsurf, etc.) and model APIs. It intercepts every request/response to enforce configurable control policies, log activity, and catch dangerous behaviors before they execute.

### How It Works
1. Developer points their AI coding agent at Luthien instead of directly at the model API
2. Luthien intercepts requests, applies policy checks (e.g., LLM-as-judge, regex filters, dangerous command detection)
3. If a policy flags something, Luthien can block, modify, resample, or alert
4. Full conversation history and audit trail logged

### Architecture
- Phase 3 "Integrated Architecture with Network-Ready Control Plane" (since Oct 2025)
- Built on LiteLLM library (not server) for API compatibility across 100+ providers
- Owns full request/response pipeline, policy enforcement logic, and observability infrastructure
- Policies are configurable: DLP (data loss prevention), dangerous command blocking, package standards, LLM-as-judge style checks

### Current Links
- **GitHub + Quickstart:** https://github.com/LuthienResearch/luthien-proxy#readme
- **Landing page (prototype directory):** https://luthienresearch.github.io/luthien-pbc-site/
- **Feedback instructions:** https://luthienresearch.github.io/luthien-pbc-site/feedback/
- **Setup:** Docker-based; working toward one-liner CLI install

### Current State (honest)
- Product is buggy but improving fast (best user session ever was March 17)
- Active QA contractor (Peter) breaking things
- CLI one-liner install coming soon but not yet live
- Finn Metz (Seldon advisor) tested setup via Claude Code on March 18; installation worked but was clunky
- Policy configuration UI being redesigned (3 prototype versions tested with Finn)

---

## 7. Luthien's Fit with Hackathon Tracks

### Track 2 is the primary fit
The hackathon explicitly calls for:
- "Control protocols that involve more traditional security measures, such as giving the trusted model access to a firewall" -- Luthien IS this infrastructure
- "Protocol where trusted model can run actions in environment to learn about proposed action" -- Luthien's LLM-as-judge policies do exactly this
- "Interrogation protocols" -- could be implemented as Luthien policies

### Track 1 also fits
- Luthien could serve as the control layer in a new control setting
- Multi-agent collusion detection via proxy-level monitoring
- Browser agent control settings could use Luthien as the monitoring layer

### Track 3 fits too
- Red team against Luthien's policies (can you craft prompts that bypass the LLM judge?)
- Build sneaky transcripts that Luthien's monitoring misses
- Test whether Luthien's DLP policies catch data exfiltration attempts

---

## 8. Meeting Notes Context (Finn's Trial, March 18, 2026)

Key decisions from the meeting with Finn Metz, Jai Dhyani, and Scott Wofford:

1. **Create a bespoke hackathon landing page** (not just the feedback page or general landing page)
2. **Lead with utility, not "help us"** -- hackathon participants are time-constrained; pitch Luthien as a tool to build on, not as a favor
3. **Include 3-4 concrete project ideas** that spark immediate "I could build this" reactions
4. **The convincing happens before the page** -- via Discord announcement from Kamil, Tyler's recommendation, Jai's talk. The page just needs to be the TLDR + clear next steps
5. **Feedback page is too much "work"** for hackathon context -- save detailed screen recordings for post-hackathon follow-up
6. **Finn's key insight:** "I want to know you guys. I want to like you guys. If I don't know or like you guys, I don't want to do this."
7. **Action items from meeting:**
   - Scott registers for hackathon (gets Discord invite)
   - Scott creates hackathon landing page with project ideas
   - Kamil coordinates Discord announcement
   - Jai gives talk Friday at noon (~30-60 attendees expected)
   - Scott lurks on Discord, answers questions about Luthien

---

## 9. Apart Hackathon Format & Culture

Based on research across 55+ Apart sprints:

- **Team formation:** Self-organized, not matched. Participants look for both ideas AND teammates
- **Typical participant:** Looking for a project, heard about AI control, wants something fun + impactful
- **Communication:** All via Discord; Kamil posts announcements, schedules, talk links
- **Submission:** Research report (PDF) + code/artifacts
- **Judging:** Expert judges from Redwood, AISI, Apollo, etc.
- **Post-hackathon:** Top projects invited to Apart Lab Fellowship; published on Apart site; potential ControlConf presentation
- **Scale:** 500+ signups typical; 70+ projects submitted at AI Manipulation Hackathon; expect similar here
- **Key insight from past hackathons:** Fresh perspectives + solid technical capabilities often yield most novel approaches. No prior AI safety experience required.

---

## 10. Strategic Context for Luthien

- **ControlConf Berkeley is April 18-19** -- just 4 weeks after hackathon. Projects built on Luthien could be showcased there
- **Luthien demo day is April 16** -- hackathon results feed directly into demo day narrative
- **Tyler Tracy is both Redwood design partner AND hackathon co-organizer** -- any successful Luthien-based project validates the design partnership
- **Buck Shlegeris is judge** -- skeptical of API proxy approach but would be impressed by practical demonstrations
- **5 blog posts is a Luthien north star metric** -- hackathon projects that use Luthien = potential blog post material
- **EU AI Act enforcement begins August 2, 2026** -- regulatory tailwind for control infrastructure

---

## Sources

- Hackathon page: https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22
- ControlArena docs: https://control-arena.aisi.org.uk/
- ControlArena GitHub: https://github.com/UKGovernmentBEIS/control-arena
- Mini Control Arena: https://brucewlee.com/mini-control-arena/
- SHADE-Arena: https://www.anthropic.com/research/shade-arena-sabotage-monitoring
- Ctrl-Z paper: https://arxiv.org/abs/2504.10374
- Ctrl-Z site: https://www.bashcontrol.com/
- Foundational control paper: https://arxiv.org/abs/2312.06942
- Control protocol evaluation: https://arxiv.org/abs/2511.02997
- Apart Research sprints: https://apartresearch.com/sprints
- Redwood reading list: https://www.redwoodresearch.org/reading-list
- Luthien GitHub: https://github.com/LuthienResearch/luthien-proxy
- Luthien landing page: https://luthienresearch.github.io/luthien-pbc-site/
- Luthien feedback page: https://luthienresearch.github.io/luthien-pbc-site/feedback/
- Meeting transcript: Finn's live trial of Luthien, March 18, 2026
