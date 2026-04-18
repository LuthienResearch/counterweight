# TLDR: User Interview Takeaways

Quick-reference summary of key takeaways from each user interview. For full quotes and context, see the numbered feedback files in this folder.

---

## Quentin Feuillade-Montixi (Feb 10, 2026)

**Background:** Senior engineer, founder of WeaveMind.ai. Seldon batch 2 peer. Uses Windsurf + Claude. Builds control infrastructure for general AI workflows.

**Source:**
- Google Drive folder: https://drive.google.com/drive/folders/1Aav0TjriwH7aGpmL4jGODGRuhNtMIBUH
- Gemini notes + Scott's handwritten discovery call notes in luth-gdrive-clone

**Outcome: NOT a design partner.** Blocker: Uses Windsurf, which doesn't support custom proxy servers (likely to protect their context-building IP). Can't route through Luthien.

### Key Takeaways

**1. Policy enforcement is NOT his top priority**
- "Enforcing policies not as big for me" — his "Working with Me" file already gets ~90% compliance with memories
- pnpm vs npm enforcement: "Not as frustrating because I can just block it"
- Policy compliance is dynamic and hard to predict in advance: "Hard to know in advance what policies you're going to need"

**2. TOP PRIORITY: Knowledge/context management across sessions & users**
- **Most common failure:** Context management — "I have to repeat myself"
- **Would pay for:** "Something that's helping me build context" + "Knowledge base across people"
- **Time savings:** Could save ~1hr/day not repeating context
- Current pain: manually scrolling back to find previous design conversations, copy/pasting context back in (Windsurf is especially bad at this)
- Vision: common knowledge for all employees, cross-session + cross-user context sharing

**3. HIGH PRIORITY: Detect when AI gives up and changes plan**
- **Specific pain:** AI tried to implement everything in Terraform when he requested Kubernetes + Cloud Run — silently switched plans without telling him
- "AIs HATE FAILURE" — they avoid admitting failure and seek quick solutions over robust ones
- **Feature request:** Detect when AI changes plans mid-execution, make it stop and ask the user
- His "Working with Me" already has patterns for this ("wait... this feels like a shortcut") but compliance degrades with long context

**4. History/conversation logging got strong reaction**
- Lost an hour of feature design conversation on Claude recently
- "Excited about" the PostgreSQL database storage of all conversations and tool calls
- Sees B2B value in context reconstruction and injection (debug issues by reproducing bugs with shared conversation history)

**5. Other observations**
- Compliance rates: early in conversation = high, degrades with context length ("context rot")
- Memories (project-specific) dramatically improve compliance: 10% → 90%
- Rust gets cleaner code from AI than Python (possibly due to pretraining differences)
- Spends 0.5-2 days periodically cleaning up AI-generated code duplication
- SOC 2 compliance would encourage proxy adoption; main security concern is data transmission + encryption at rest

### Policies Quentin discussed (ranked by his interest)
1. **Detect plan abandonment** — HIGH (biggest pain point)
2. **Cross-session context injection** — HIGH (would pay for this)
3. **Backward compatibility cleanup** — MEDIUM (70% compliance currently)
4. **DRY enforcement** — MEDIUM
5. **Prohibited strings (em dashes, preamble)** — LOW (context rot is real cause)
6. **Code style (imports, function patterns)** — LOW (98% for Python already)
7. **pnpm vs npm** — LOW ("can just block it")

### Action Items
- [x] Add "knowledge/context management" feature to product backlog → [4-history-and-context-requirements-live.md](../2-versions-requirements/4-history-and-context-requirements-live.md)
- [x] Add "plan abandonment detection" policy to product backlog → [5-policy-config-requirements-live.md #19](../2-versions-requirements/5-policy-config-requirements-live.md) + [3.2-failures-policy-ideas.md](3.2-failures-policy-ideas.md#detect-plan-abandonment--short-circuiting)
- [x] Note Windsurf support gap as adoption barrier → [UI-feedback-dev-tracker.md](../UI-feedback-dev-tracker.md#goal-1a-recruit-design-partners)
- [ ] Consider: Quentin open to partnership in niche areas (logging, policy, monitoring) even if not design partner

---

## Tyler Tracy — Redwood Research (Feb 10 + Mar 3, 2026)

**Background:** Senior engineer at Redwood Research. Team of ~10 engineers. Uses Cursor + Claude Code. Building AI safety research tooling (Linux Arena). Weekly office hours with Luthien since mid-2025.

**Source:**
- Feb 10: [Office Hours notes](https://docs.google.com/document/d/1Qo2D5zrtuHO2MF6wJX4v86sJPm-YAmCNwKWPJTcFJvM/edit?tab=t.0), [Gemini transcript](https://docs.google.com/document/d/1lRX5U7_2Ig1oOw775xm9uoGGK6yJx2gip8N2BlAA0JQ/edit?tab=t.fp5fl2phgglm)
- Mar 3: Google Doc `1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI` (Gemini notes)
- Policy feedback also in [3.1-policy-config-feedback.md, Session 7](3.1-policy-config-feedback.md#session-7-tyler-tracy-redwood-research)
- Value-prop feedback: [1-value-prop-feedback.md, Session 4](1-value-prop-feedback.md#session-4-tyler-tracy-redwood-research--live-install) (Feb 10) + [Session 12](1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback) (Mar 3)

**CX version:** [readme-v6.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v6.md) -- had "Who it's for" section, colored side-by-side comparison cards (not SVG terminals), "Policies" section with built-in common failure modes + custom policies, "Claude Code (or Codex)" in intro. Substantially different from current PR #179 state.

**Outcome: STRONGEST design partner candidate.** Installed Luthien live on first attempt. Said "maybe I should just tell them to use this" about deploying to his 10-person team. 5/5 across all design partner criteria.

### Key Takeaways

**1. Installed live on the call -- "smoothest user trial ever" (Jai)**
- Used [readme-v6](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v6.md) to install. Docker compose up worked. Activity monitor showed requests. Curl test passed.
- Blocker to team deployment: Docker images built locally (slow). Pre-built images needed for team self-service.

**2. Install friction: quick_start.sh vs docker compose up**
- `quick_start.sh` health check fails when Grafana hasn't been launched yet (known bug, Jai: "I've been meaning to fix forever")
- Confusion about whether to use `quick_start.sh` or `docker compose up` -- resolved in README v7 (users get `docker compose up`, devs get `quick_start.sh`)

**3. Backward compat code is a 60% false positive problem**
- Has cursor rules to prevent backward compatibility code
- False positive rate is 60% -- pattern matching catches too many legitimate cases
- "Most of the time not back [compat needed]. Prompt me if 10% of times it thinks it's right."
- Main reason it doesn't work: AUTO mode (auto-apply bypasses human checkpoint)

**4. AI ignores team utilities / CLI / MCP server**
- Team has a CLI for their project (Linux Arena) -- launch evals, list properties, automated Claude Code agents
- AI won't use the MCP server. Writes its own implementations instead.
- "All of our docs are documented using that CLI"
- Validates same pain as other users re: AI not following team conventions

**5. AI PRs don't show proof of testing -- "biggest frustration with AI PRs"**
- "People don't prove their change, how to make work easy to verify?"
- "Just skip it; easy path to go down"
- Uses GitHub PR template and status checks. Pretty happy with Cursor bug bot.
- PR reviewers don't have access to the same context the author had

**6. Distinction: bug detection (automatable) vs research taste (human)**
- "What is point of AI control; prior of what you're looking for is much better. TPR, safety metric."
- "Check if there are bugs, not if logic wrt research is correct."
- "I want them to have research taste" -- what PR reviewers need from context that AI control can't provide
- Control should focus on catching objective errors, not subjective research quality

**7. Workflow context (from raw notes)**
- Spends 10-40% of time on tech things. Large codebase, 10-person team, all remote.
- Uses Cursor or shell. "Sucks transition between main workflow and web-based UIs." Claude code .com is "buggy overall" -- no worktrees.
- Uses `claude.md` / `agent.md` symlink for interoperability between Claude Code and Cursor. "Docs made for humans and AIs." Issue: docs aren't up to date.
- "Hard to write docs for humans and AIs" -- the dual-audience documentation problem.
- Tyler's idea for PR proof of testing: "upload to website, link run on PR, after run, show field on data change." Sub-agent hack could also work.
- "Pretty happy with cursor bug bot -- I trust there aren't bugs" -- existing tooling he trusts.
- "Other 60% if I had all these meeting notes, pull my..." -- sees value in meeting notes aggregation across sessions.

**8. Mar 3: Benchmark data is the #1 trust-builder for Tyler's persona**
- "There are a lot of things that are trying to do this... I don't have any data to know that yours is better or like actually works."
- Wants a 2D frontier graph (safety metric vs utility metric). Specifically recommends **Bash Arena (Control Arena)**: "Before Luthien the database is deleted 10% of the time, after Luthien 0% of the time."
- Converges with Josh on needing quantitative evidence, but Tyler is much more specific about which benchmark.

**9. Mar 3: Trial doc unclear for cold sends — "not necessarily clear what this is"**
- Tyler wants to forward Luthien to his team and contractors, but current docs assume context cold readers don't have.
- Fictional class names in YAML examples undermine trust: "If a developer tries to use them, they'll fail."
- "Cloud account" mentioned but unexplained — creates confusion.

**10. Mar 3: Video > text for trust**
- "GitHub repos that have a video at the beginning... would make me trust it a bit more."
- References Fire Ship, coding YouTubers as discovery channels.
- Quotes have limited impact on Tyler: "Guy from Amazon, I wouldn't care as much. Someone from OpenAI, maybe a bit more."

### Action Items
- [x] Capture policy pain points -> [3.1-policy-config-feedback.md](3.1-policy-config-feedback.md#session-7-tyler-tracy-redwood-research), [3.2-failures-policy-ideas.md](3.2-failures-policy-ideas.md)
- [x] Capture install/onboarding friction -> [dev/TODO.md](https://github.com/LuthienResearch/luthien-proxy/blob/main/dev/TODO.md) (Onboarding & Install section)
- [x] Capture Mar 3 README feedback → [1-value-prop-feedback.md, Session 12](1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback)
- [ ] Push pre-built Docker images to Docker Hub (blocker for team deployment)
- [ ] Fix quick_start.sh Grafana/gateway health check bug
- [ ] Create benchmark data using Bash Arena / Control Arena (Tyler's #1 ask)
- [ ] Create cold-send-friendly trial doc for Tyler to distribute to team

---

## Jai Dhyani — PR #179 README Review (Feb 12, 2026)

**Background:** Co-founder & CTO at Luthien. Reviewed PR #179 (value-prop README rewrite) and discussed product strategy during weekly debrief.

**Source:**
- Gemini transcript: `scott_jai debrief seldon wkly - 2026_02_12 17_28 PST - Notes by Gemini.md`
- Session context: Preparing for EASF weekend (Scott meeting potential users)

**Outcome: Actionable README feedback.** Clear direction for PR #179 restructuring + deployment strategy decisions.

### Key Takeaways

**1. One-click frictionless deploy is THE priority**
- "The main thing is creating frictionless useful product experience right now"
- One-click deploy with English language rules description working out of the box
- OAuth pass-through simplifies everything: user brings own Claude subscription, just set one env var (backend URL)
- "Don't worry about auth — just do straight pass-through and flag auth as a thing to figure out later"

**2. README structure: value prop → examples → visual diagram → setup details**
- "Adding a thing at the very start of the readme" — keep it short: "a few sentences and maybe one or two pictures"
- Before/after comparison format validated: "Yes, that's great"
- Add "across your org" to the intro sentence — half-sentence addition
- Flow: value prop → specific examples → how it's implemented (visual diagram) → "the nerd stuff" (setup)

**3. Cut "Who it's for" section**
- "This is implicit in everything else. We don't need to make it more explicit."
- "That filter holds is how we're funneling people towards this point"

**4. Rename "What policies can do" → "Example use cases"**
- "Instead of trying to describe the principle of how it works, just showing examples of people getting utility out of it"
- Each example should ideally link to how to activate that policy (future)
- "The purpose is to demonstrate utility, not explain mechanics"

**5. Don't show unimplemented features**
- "Until we've actually done that reliably, we don't put it in"
- Reliability = Jai is daily-driving it with a rule that works
- Current state: "ones that meet reliability don't meet utility — we need one that meets both"

**6. Visual diagram: You → Luthien → Anthropic**
- "Luthien enforces your policies on everything that goes into or comes out of the backend"
- Actions: can replace file edits that violate rules, generate easy-to-read log of everything agent does
- Monitors, blocks, or changes requests/responses

**7. Default demo policies for EASF weekend**
- Logging URL policy: inserts a URL at conversation start that links to a live-updating full log
- English language rules policy: convert natural language rules to enforcement
- "These are basically two policies to implement"

### Action Items
- [ ] Restructure PR #179: value prop → example use cases → visual diagram → quick start → existing setup details
- [ ] Add "across your org" to intro sentence
- [ ] Cut "Who it's for" section
- [ ] Replace "What policies can do" with "Example use cases" — show utility, not mechanics
- [ ] Only show features that are reliably implemented
- [ ] Add visual diagram (You → Luthien → Anthropic with monitor/block/change annotations)

---

## Nicolás "Nico" Mesa (Feb 9, 2026)

**Background:** Senior engineer, co-founder of Veleiro ([app.veleiro.ai](https://app.veleiro.ai)). Ex-Amazon SDE 3. Scott's personal friend from Amazon. Builds AI-powered Salesforce implementation tool. Team of 3 engineers. Uses Claude Code exclusively.

**Source:**
- Google Drive folder: luth-gdrive-clone/_User-Interview-Notes/Nico/
- Gemini transcript: `Scott (Nicolás Mesa) - 2026_02_09 10_28 PST - Notes by Gemini.md`
- Nico's rules + CLAUDE.md: [Google Doc](https://docs.google.com/document/d/1xTGh4_eNoK9zrCARg7ehhZTbFaLYkjR5x3sI9wJkxI4/edit?tab=t.0), also in luth-gdrive-clone as `Nicolas_Luthien.md`

**Outcome: POTENTIAL design partner.** Uses Claude Code (can route through Luthien). Open to another call. Scott asked for repo read access.

### Key Takeaways

**1. Built a Claude-Code-like virtual file system for their agents**
- Evolved through 3 iterations: "rewrite whole document" → "specific tools" → "virtual file system" (like Claude Code)
- Agents see folders, can run bash commands, edit specific parts of files
- Progressive discovery via README files in each folder (similar to Claude Code skills)
- Scratch folder for agent's intermediate work (user doesn't see it)

**2. AI is "too scared of failure" — should fail hard, not silently continue**
- "At Amazon, I was like, 'No, if there's something wrong, we fail.' It's wrong. Don't be scared to show a user a message."
- Silent failures are worse than visible errors — users think everything went fine when it didn't
- Their #1 review pattern: checking for swallowed errors in AI-generated PRs

**3. Backward compatibility code is a recurring frustration**
- "F*** backwards compatibility. You are in charge here. I grade everything."
- AI keeps old code around "for backward compatibility" instead of migrating everything
- Nico reviews PRs from 2 other engineers and constantly catches this pattern
- Same frustration as Quentin — validates this as a cross-user policy idea

**4. Sonnet 4.5 stops mid-task**
- "Okay, I'm going to do blah." And stops. "Okay, do it." "Okay, I'm going to do it." And stops.
- Anthropic-internal header exists to disable adaptive context stopping, but it's not public
- Related to how the model was trained to save context when context is running low

**5. Customer problem: AI generates too much text**
- Users don't read AI output → miss errors → discover mistakes late
- Solved partially with version history + diff comparison: "if they read it once and then ask for changes, they can see only what changed"
- Still not fully solved for very long documents

**6. Strong validation + good error messages are their #1 agent improvement**
- "Error messages are very very important — not only the error but also alternatives or how to fix it"
- Their virtual file system validates after every agent edit (like an IDE showing squiggly lines)
- Agent self-corrects when given good error messages — "it corrected itself before the user even noticed"

**7. CLAUDE.md management patterns**
- CLAUDE.md got too big → Claude Code said "this is too big"
- Split into topic files (testing.md, etc.) + use `@file` references in prompts
- Another engineer uses slash commands/skills for common patterns (UX, security, Sentry fix)
- Sentry integration: `/sentry-fix <issue-URL>` — Claude Code reads logs, proposes fix

**8. Getting real customer traction now**
- Small but active user group giving feedback
- "At least we're getting feedback instead of guessing what people want"
- Concern about overfitting to small user base

### Policies from Nico's Rules + CLAUDE.md (ranked by how much he discussed them)
1. **Don't swallow errors / fail hard** — HIGH (his #1 review pattern, Amazon philosophy)
2. **No backward compatibility code** — HIGH (catches this in every PR review)
3. **Package manager enforcement (uv)** — MEDIUM (in rules, same as Quentin's pnpm)
4. **Guard clauses over nested if/else** — MEDIUM (explicit in CLAUDE.md)
5. **Imports at top of file** — LOW (standard, in rules)
6. **Don't change unnecessary code** — LOW (standard, in rules)
7. **Pydantic over dicts/dataclasses** — LOW (tech-specific preference)
8. **Deterministic tests (no conditional pass/fail)** — LOW (in CLAUDE.md, very specific)

### Action Items
- [x] Add policy ideas to backlog → [3.2-failures-policy-ideas.md](3.2-failures-policy-ideas.md)
- [x] Add version history/diff feedback to history synthesis → [2-history-and-context-feedback.md](2-history-and-context-feedback.md)
- [x] Save Veleiro UI screenshot as /history inspiration → [3-ui-mocks/2-history-and-context/](../3-ui-mocks/2-history-and-context/)
- [ ] Schedule follow-up call after Scott's trip — show Luthien concepts
- [ ] Get read access to Veleiro GitHub repo
- [ ] Consider: Sentry-like integration for Luthien (slash command for bug investigation)

---

## Paolo Calvi (Mar 3, 2026)

**Background:** Airbus engineer (not 40-hour contract — has ~25 hours/week freelance capacity). Active contributor to Agent Zero (fixing bugs, developing guard plugin). Pythonist — "Zen of Python is my religion." Based in Germany. Two kids (ages 8 and 2.5). Paying personally for Luthien engagement (not Airbus-funded).

**Source:**
- Voice memo transcript: `~/Downloads/paolo-scott-march-3-transcript.md`
- Gemini notes: Google Drive folder `1MPmvqqIXWp3M03yUCCukEKpiNr4u8kNs` (Scott (Paolo Calvi) - 2026/03/03)
- Claude Desktop support log: OpenCode/Agent Zero/Cisco compatibility research (pasted in session)

**Outcome: ENTHUSIASTIC early adopter + contractor.** Power user persona — "he needs it so f***ing much" that he'll debug and fix bugs himself. Wants both cash + equity arrangement. Started Agent Zero guard plugin work independently before discovering Luthien. Sees Luthien as the perfect backend for the guard system he was already trying to build.

### Key Takeaways

**1. "Guard proxy" — "proxy" undersells the product**
- "A proxy, somebody will imagine something that just passes through blindly things."
- "You should basically call it a guard proxy... highlighting that it's not just [a proxy], because a proxy, you think about caching, you think about squid, and you're not really thinking about filtering."
- Naming feedback converges with R1 messaging requirements — the word "proxy" doesn't communicate control/filtering.

**2. Agent Zero plugin as distribution channel**
- Already building a guard plugin for Agent Zero. Luthien is the perfect backend.
- "The best way to go ahead, and even to popularize the proxy, is to say to people using Agent Zero — here you go. You have a really ready to go solution."
- Agent Zero's plugin architecture creates hooks for guard systems — Luthien can slot in as a provider.
- OpenCode is another vector: "Open Code, and Agent Zero. These are two main projects that I follow intensively."

**3. Cisco AI Defense as complementary, not competing**
- Built a Cisco AI Defense plugin for Agent Zero (prompt injection firewall). Found it free and useful.
- Sees Cisco and Luthien as complementary layers: Cisco for prompt injection detection, Luthien for broader proxy/control.
- "You're doing what I'm trying to do and actually doing it."

**4. Parental content control as use case**
- Building a home lab to control kids' content consumption with AI-supervised filtering.
- "I want the filtering on videos done by AI. I want to freaking own it."
- "I don't want to be finding out one day that somebody injected a prompt, and everything poof, goes into oblivion."
- Prompt injection prevention is personal, not just professional.

**5. Power user persona — will debug and contribute**
- "He needs it so f***ing much" — not a passive evaluator. Will fix bugs, submit PRs, daily-drive the product.
- Recommended PR-Agent (Qodo) for AI-assisted PR review to handle contribution volume.
- Red-blue strategy: "two different models one against each other" — understands the LLM-as-judge concept intuitively.

**6. Cultural alignment — Trust, Speak Up, Respect, Zen of Python**
- "Speak up culture" from Airbus — if something isn't right, escalate. "You have to stand up and say, I'm not sure that this is a good shortcut."
- Co-defined cultural values during the call: Trust, Speak Up, Respect, Zen of Python.
- "Import this" — wants the project managed with Python's philosophy.

**7. Tweakable/adaptable rules are imperative**
- "It's absolutely imperative to be tweakable and adaptable."
- Prompt injection as first policy use case: "I want to be super confident when I use agentic [AI]."
- Converges with other users on customizability being key (Quentin, Beth Anne, Tyler).

### Action Items
- [ ] Explore Agent Zero guard plugin integration (dev item — `dev/TODO.md`)
- [ ] Set up PR-Agent (Qodo) for luthien-proxy repo (dev item — `dev/TODO.md`)
- [ ] Contact Alessandro Frau on Discord (Agent Zero admin) — operational item for Trello
- [ ] Schedule follow-up after Paolo's first week of usage

---

## Scott Wofford — Dogfooding COE (Feb 24, 2026)

**Background:** Luthien co-founder. Using Claude.ai with browser tools to update Substack settings. Not a coding session — general AI assistant usage that surfaced a controllable failure mode.

**Source:**
- Claude.ai session (Feb 24, 2026)
- External quotes collected same session: Medium/@elliotJL, Scott Spence blog

**Outcome: New policy idea + landing page copy direction.** The frustration of being confidently misled by an AI that had tools available but didn't use them directly informed R9 (funny/relatable landing page copy) and a new policy idea (require verification before factual instructions).

### Key Takeaways

**1. AI gives wrong instructions with full confidence when verification tools are available**
- Claude gave wrong Substack navigation instructions 3x
- Had screenshot tools AND web search available — never used them
- Only got correct answer when forced to search docs
- This is the exact failure mode Luthien's control policies address

**2. The experience is emotionally resonant — and funny in hindsight**
- "I'm a product manager for a stochastic parrot" captures this perfectly
- The absurdity of an AI confidently giving wrong directions while having a map is relatable to every developer
- Led to R9: landing page copy should use this humor

**3. Maps to a concrete policy: "no factual claims without tool verification"**
- Detectable at proxy level: response contains step-by-step instructions but no tool_use block preceded it
- Could be prompt-layer (inject "always verify before instructing") or sus-layer (output classifier)

### Action Items
- [x] Added policy idea to 3.2-failures-policy-ideas.md
- [x] Added R9 to requirements (funny/relatable copy)
- [x] Added developer quotes to 1-value-prop-feedback.md
- [ ] Generate landing page prototypes exploring humor angle (this session)

---

## Peter Teodosiu — QADNA QA Trial (Feb 25, 2026)

**Background:** CTO of QADNA (Bucharest). Ex-Google. Runs 14 Claude Code instances daily building AI-driven QA SaaS platform. Plans to give agents internal API access to their platform.

**Source:**
- QA trial + video transcript + [QA Trial Report](https://docs.google.com/document/d/1xugPuJjtfxXw3ale54rdhqAlsH5wcvo31RtPVPJLgz4/edit)
- Session log: `luthien-private-session-logs/2026-02-25_peter-qadna-trial.csv`

**Outcome: STRONG design partner candidate.** Plans to continue toward Aprimo day. Validated Luthien concept — "I haven't seen something like this before... this is something that should exist."

### Key Takeaways

**1. Destructive agent actions with API access (~10/10 severity)**
- "You're playing a bit with fire, as much as you want to guard on it."
- Building a platform where agents will have internal API access to manage test cases — very concerned about destructive actions (e.g., mass-deleting test cases from an ambiguous user instruction)
- This is his #1 motivation for Luthien: guardrails against destructive actions that can't be fully prevented by application-level confirmation dialogs

**2. Unsupervised agent drift (8-9/10)**
- "If you leave them unattended and unsupervised, they will just go to a very comfortable place... the end prompts were so conservative that they weren't really doing anything. They were just saving up on the tokens, doing minimal stuff for the easiest tests."
- Agents self-optimize for token savings, become overly conservative, stop doing useful work

**3. Context loss after compacting**
- "Especially after compacting, where that's not something you can actually control how well it compacts and how much it actually keeps around."
- Repeatedly-stated instructions forgotten after compaction events

**4. Strong positive reaction to Luthien**
- "This looks like something really cool and I would love to try it."
- "I haven't seen something like this before... this is something that should exist."
- "I don't find this confusing at all. It's very well simplified."
- On the architecture diagram: "Pretty much you have a bit of middleware in it that you're logging every request and response, arbitrary rules and policies to calls and responses."

**5. Landing page feedback**
- "Very clear," "love how it looks," dark mode appreciated
- Notes it reads as a dev tool — non-technical users wouldn't understand it (fine for our ICP)
- Latency concern: curious how fast the proxy would be, especially when calling another LLM for subjective policy checks

**6. Onboarding friction**
- Python 3.10 installed, project requires 3.13+ — `quick_start.sh` should check and warn
- README implies API key is the only option — needs Claude Pro/Max subscription guidance
- Stale/expired API key returns nested JSON error instead of clear message

**7. Bugs found during trial**
- DeSlop policy activation error
- SamplePydanticPolicy unimplemented — causes all requests to fail when selected
- No clear feedback when API key is invalid/expired

### Action Items
- [x] Added 8 bugs to `dev/TODO.md` (PR #242)
- [x] Frustrations #55-59 documented
- [ ] Add frustrations to Frustrations DB spreadsheet
- [ ] Schedule follow-up call toward Aprimo day
- [ ] Fix Python version check in `quick_start.sh`

---

## Maria Paula Mendieta (Feb 26, 2026)

**Background:** Director of Product at Carbon Direct. Ex-economist/data scientist. Strong product/UX instincts. Not a developer.

**Source:**
- Otter.ai transcript: `/Users/scottwofford/Downloads/Maria's feedback on Luthien landing_readme v8_otter_ai.txt`

**CX version:** landing_v8 (current landing page prototypes) + README

**Outcome: NOT a design partner** (not ICP — not a developer, doesn't use Claude Code). But strong structural/UX feedback from a product perspective.

### Key Takeaways

**1. Reorder: value prop first, quotes at the bottom**
- "I would put the quotes at the bottom, not at the top, because it's almost like testimonial type so you have you want the what it does at the top, so that the quotes makes sense."
- Important note: current quotes are evidence of pain (developer frustrations), NOT testimonials. Maria's reorder suggestion still valid for structure — value prop → demo → evidence of pain — but the framing matters.

**2. Punchier value prop — lead with user action, not architecture**
- "enforce rules and block dangerous operations, but with Luthien coma as a proxy that sits between or something along those lines, yeah, so that they enforce rules and block dangerous operations is like at the very beginning"
- "I would add a punchier version of this at the top"
- Start with what the user will DO (enforce rules), not what Luthien IS (a proxy)

**3. Visual identity: Luthien needs its own avatar/icon**
- "if you had your own, like Avatar, it would be more visible. What is, what is Claude, and what is you?"
- Claude has its visual identity (the Claude icon). Luthien blends into the code. An avatar/icon (parrot, magnifying glass, spy) would make Luthien's interventions visually distinct.

**4. Emotional overlays on the demo (post-it sketch)**
- Maria sketched on paper ([photo](maria-sticky-notes-feb26.jpeg)): realistic terminal view with thought bubble overlays showing user frustration escalating
- "it's clearly not part of the UI, but you're clearly [drawing] the eyes and, like, look at what's happening, and it's getting worse and worse and worse"
- The overlay shows the emotional experience the code doesn't capture

**5. "AI coding agent" confusing and redundant with LLM — say "Claude Code"**
- "I don't interpret this as a coding agent... to me, this is an interface"
- "no, because it sounds redundant with... LLM"
- Decision: remove "agent" terminology from landing page. Say "Claude Code" (specific, recognizable) instead of "AI coding agent" (jargon, confusing)

**6. Policy examples too vague — show actual rule text**
- "I think your example. Too vague, like popular MD policy, but what did the policy say? Which policy"
- When showing a block, include the actual policy rule that triggered it (e.g., "blocked per policy: never use pip")

**7. Marketing structure: value prop → preview → use cases → quotes**
- "What is it structure? What's the value prop? Preview of the tool? Like a GIF?"
- "what you're missing here is a puncher storytelling of like, why should you use me?"
- De-emphasize install in the demo section — install ≠ demo. "you don't need to tell them how to install it. If they're excited about this, you can have a value prop that it's easy to install"

### Action Items
- [ ] Update R1 evidence with Maria (6th independent user on reorder) → [1-value-prop-requirements-live.md](../2-versions-requirements/1-value-prop-requirements-live.md)
- [ ] Update R2 evidence with Maria quotes on punchier value prop + "agent" terminology → requirements
- [ ] Update R3 evidence with Maria on use case storytelling → requirements
- [ ] Update R4 evidence with Maria on showing actual policy text → requirements
- [ ] Update R5 design note on de-emphasizing install → requirements
- [ ] Consider: visual identity / avatar for Luthien (new item for backlog)
- [ ] Consider: emotional overlay concept for demo section

---

## Josh Levy (Feb 25, 2026)

**Background:** AI safety researcher. Previously worked on debate and control research related to persuasion (FAR grant, ending March 11). Based in Seattle. Deep understanding of AI control, evaluations, and AI safety landscape. Potential Luthien hire if funding is secured.

**Source:**
- Gemini notes: [Google Doc](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw/edit)
- Recording: [Google Drive](https://drive.google.com/file/d/15uU7Kc-XvXLajt2GeYsEbsN4WqU1r1TO/view)

**CX version:** Landing page prototypes (Round 4b) + README quick start (PR on `value-prop` branch)

**Outcome: Not a design partner** (researcher, not daily Claude Code user), but high-signal feedback on value prop differentiation and metrics. Potential future hire for research role.

### Key Takeaways

**1. "Meanwhile" section is corny — remove it**
- "Meanwhile, I would get rid of that meanwhile thing... seems corny. Like too corny"
- Tone miscalibration for the target audience

**2. Scrolling > clicking for incident examples**
- "How about instead of maybe just have multiple of these scrolling through so it's easier to... latch on to one"
- "the nice thing about the scrolling is you have the best of both worlds. Like cuz you have multiple and so that way people can just like see which one"
- Current click-to-advance behavior also has a bug (unexpected behavior on click)

**3. Block phrasing: remove colon, use active verb + policy name**
- "blocked pip install. Um, like the phrasing is a little weird... it could be like blocking pip install per [policy]. Like I don't think you need the colon... the colon's weird."
- Converges with Maria on showing which policy triggered the block

**4. Emojis in terminal confusing — LLMs use emojis too**
- "it's a little confusing because um like the LLMs use a lot of emojis"
- Unclear whether the emoji is from the LLM, the user, or Luthien's annotation
- Also: "I get rid of the nice. I'd get rid of... do I need all caps — just make it as tight and succinct as possible"

**5. Architecture section too detailed for landing page**
- "all of the above stuff is super clear and I think very good. It's just this cloud thing here."
- "I don't know what the cloud is either."
- "it's a lot of words for something that I think is ancillary relative to like the main stuff"
- Solution: "I think you could have another tab below which is like 'how it works' if you want to include that."

**6. CTA: "book a call" is anti-pattern for engineers**
- "if I ever see as an engineer like book a call, I'm just like next like this is marketing BS."
- "make it clear on the landing page like try it yourself and then just link over to GitHub"
- Include a bug warning: "just include a warning... only highly motivated people are going to be here"

**7. VALUE PROP GAP: What does Luthien do that a system prompt can't?**
- "what Luthian is doing special here that can't just be like literally you have a set of instructions that are just getting passed to the prompt"
- "if I took these rules and literally just passed them as a prompt, they'd probably get followed most of the time"
- "you need to be comparing the effectiveness of Lucian relative to that baseline"
- This is the most strategically important feedback point — landing page must answer this question.

**8. Luthien's sweet spot: context rot and large codebases**
- "Lucian will be maybe most effective like in a context rot scenario or where there's like a huge amount of files"
- Context rot = instructions in CLAUDE.md get forgotten over long sessions. This is exactly where a proxy adds value over a system prompt.

**9. Landing page needs metrics (bar chart: nothing → prompting → Luthien)**
- "what's kind of missing here is like some metrics"
- "a little bar chart with like nothing, just prompting, and then Luthien and you're improving like probably 15% or whatever it is"
- Also: adversarial experiments — "you might even create one where you do have an adversarial agent"

**10. Overall positive — loves the Claude Code use case**
- "this is great progress. Like I think it looks really good."
- "I love the use case of cloud code. So, good job like figuring that out."

### Action Items
- [ ] Update R1 evidence with Josh (demo section: tight and succinct, scrolling > clicking) → [1-value-prop-requirements-live.md](../2-versions-requirements/1-value-prop-requirements-live.md)
- [ ] Update R2 evidence with Josh on value prop differentiation vs system prompt baseline → requirements
- [ ] Update R4 evidence with Josh on block phrasing (remove colon, active verb + policy) → requirements
- [ ] Update R5 evidence with Josh on CTA ("try it yourself" + GitHub, not "book a call") → requirements
- [ ] Update R9 evidence with Josh on tone ("Meanwhile" too corny) → requirements
- [ ] Consider: new requirement for metrics/benchmarks on landing page (Josh: bar chart comparing nothing → prompting → Luthien)
- [ ] Consider: context rot as the key differentiator messaging angle
- [ ] Consider: adversarial demo experiment (YouTube video idea discussed)

---

## Finn Metz — Landing Page Review (Feb 25, 2026)

**Background:** Co-founder of Seldon Labs (AI safety accelerator, SF/Berkeley). Runs accelerator batches. Daily Claude Code user. Known for hating AI slop, especially em dashes. Previously reviewed Luthien policies on Feb 6 (policy config session).

**Source:**
- [Gemini notes + transcript](https://docs.google.com/document/d/1Foi5Qjcyyn0vxCOXgqooV2EXdE5b3806kYXguS9xz1w/edit)
- [Recording](https://drive.google.com/file/d/1fnGINriZOC6IRj25GaJFmuRxdDQSFw6N/view)

**CX version:** Landing page prototypes (Round 4b) + README quick start on GitHub

**Outcome: Ongoing Seldon relationship.** Not ICP (accelerator operator, not daily production user), but high-signal feedback from someone who understands developer tooling and runs a community of AI safety startups. Hosts co-founder matching events — potential distribution channel.

### Key Takeaways

**1. Cards spin too fast — can't read them**
- "Why does it go so fast? I'm a product manager for a stoastic parrot. I can't read this."
- Same feedback as Josh (same day, independently). Now the most-reproduced UX bug.

**2. Before/after demo section is too dense and confusing**
- "I get very confused by this. Like, it's just too much."
- "Hard for me to tell what is before and what is after."
- Would have skipped the entire section. Needs simpler version with clearer headings.

**3. Emotional arc of Claude frustration resonates**
- "I do definitely get the emotional arc. So, I've been here where like I've gotten frustrated at Claude."
- The story works; the current presentation doesn't communicate it clearly enough.

**4. Architecture diagram should be bigger**
- "This is great. I think this should be bigger."
- Contrast with Josh (wants it hidden). Solution: `<details>` collapse (v9 approach).

**5. "Who are you guys?" — needs an about section**
- "The main thing I'm wondering is like, who are you guys?"
- First explicit request for team identity on the landing page. Wants faces, GitHub links, location.

**6. Incident cards are cool as proof, but expected incident → fix mapping**
- Interpreted the collection as a potential incident database
- "In those cases I would love to see like how Lucian then fixed it or something."
- Opportunity: pair incidents with "how Luthien handles this"

**7. LLM-as-judge policy is "really cool"**
- "I haven't seen this before being like implemented in an easy and like whatever manner."
- Asked if it's a separate instance — right technical question.

**8. Quick start: "Just ask Claude to do it"**
- Copied entire README into Claude Code: "Yo, do this. Let me know what you need."
- Scott: "That's brilliant. I don't know why I didn't think of simplifying this."
- Modern developer onboarding = delegate to the AI.

**9. DeSlop policy attempt failed**
- Tried to activate em-dash removal via Claude Code — didn't work (likely same bug Peter hit)
- "I want the policy, but don't want to use a s***** interface. I want to just tell you to fix."

### Action Items
- [x] Add Session 8 to value-prop-feedback.md
- [x] Add TLDR entry
- [x] Map feedback to R# requirements (R1, R5, R9)
- [ ] Add "about section" to landing page backlog
- [ ] Investigate DeSlop policy activation bug (also hit by Peter)
- [ ] Consider: "just ask Claude to set up Luthien" as primary quick start path

---

## Mike Mantell (Mar 4 + Mar 11, 2026)

**Background:** UX design contractor. Professional UX/copy review perspective, not a developer. Not a Claude Code user. Working part-time (~5 hrs/wk) on Luthien landing page copy and positioning.

**Source:**
- Mar 4 Otter.ai transcript: `Rxaj9ooSUMjjDZneNmn34QoXHEk`
- Mar 4 Gemini notes: GDrive `Scott (Mike Mantell) - 2026/03/04 15:00 PST`
- Mar 11 Gemini notes: GDrive `Scott (Mike Mantell) - 2026/03/11 15:29 PDT`
- Mar 11 debrief: `luth-gdrive-clone/_Seldon_labs/Mike Mantell/2026-03-11_mike-debrief-proposed-cards.md`

**CX version:** Mar 4: v10 on `main`. Mar 11: v10.6/v10.7, reviewing V11 draft.

**Outcome: NOT a design partner.** UX contractor, not ICP. High-signal UX/copy feedback from a professional design perspective.

### Key Takeaways (Mar 4)

**1. "Enforces your rules" = best hook — "that's active"**
- Singled out "enforces your rules" as the strongest phrase on the page
- Active verb conveys agency — Luthien does something, not just describes what it is
- 14th user confirming lead-with-value (R2)

**2. Problem section overwhelms — "I don't want to read all this shit"**
- The numbered categories (70, 15, 19, 20) create information overload
- 4th reviewer flagging problem section density (after Maria, Finn, Darren)

**3. CTA needs a transition — gym trainer analogy**
- Page jumps to "sign up" without building a bridge
- Need "one more step" between showing value and asking for action
- CTA placement issue, not just content

**4. "Suspicious stuff" too informal for a trust product — "I want you to sound really credible"**
- Register mismatch: deadpan humor works in problem section, not in trust claims
- Suggestion: "suspicious behavior" instead of "suspicious stuff"

**5. "Active development" signals not-ready — "I can't use this right now"**
- Intent: transparency about velocity. Reception: "this is a beta and might break"
- Consider removing or reframing

**6. Before/after needs height alignment + visible captions**
- Height mismatch between Before and After screenshots disrupts comparison
- Caption text too small/faint to read
- 7th reviewer flagging before/after visual issues (R1)

**7. Other notable points**
- "Claude Code code" is a mouthful — "Let AI Code" reads easier
- Architecture diagram strong positive: "I like this diagram a lot"
- "Rules and policies" ambiguous — whose? Need "your rules"
- "All without changing your dev setup" = infomercial-y
- "What can it do" section visually flat after the engaging diagram

### Key Takeaways (Mar 11)

**8. Audience awareness spectrum: vibe coders → average devs → super devs**
- From ~30-40 interviews: vibe coders "yell at the code harder," average devs use CLAUDE.md + prompt engineering but haven't considered output validation, super devs are the graduation target
- Average devs know PR review bots but not real-time output validation — Luthien is "upstream, complementary" to post-commit review

**9. V11 draft: PAS framework + white background**
- Mike used PAS (Problem, Agitate, Solution) copywriting framework — assumes audience is "problem aware," just needs reminder of gravity before presenting solution
- White background to convey safety/ease. Headline: "Stop Claude code from going off script"
- Six problem quotes + "the answer isn't better prompts or longer CLAUDE.md files" reframe

**10. AI safety mission: does it build trust or carry baggage?**
- Jesse's feedback: AI safety mission buried, move higher. Mike's counter: "AI safety" may carry baggage that turns off developers
- Resolution: testing resolves the ambiguity. Mike assigned to create testable version or explain why it's not worth it

**11. Easter egg: if important, put in main copy**
- Current easter egg conveys developer duality (AI hype + job insecurity) but feedback says "1995 aesthetic," not prominent
- Mike's instinct: "if it's important enough to convey, it should be in the main copy, not hidden as an Easter egg"

**12. Onboarding simplification to single terminal command**
- Current 7-step README process is friction. Jai working on single `curl | bash` style install (like Codex)
- Changes CTA from "try it yourself" to a terminal-based instruction

**13. Cold-send email: personalize + CTA = book time**
- Draft email too spam-like. Mike advised: add personal reference to previous meeting, remove generic second paragraph
- Primary CTA should be "book the time," not "read the landing page"

### Action Items
- [ ] Add Session 14 (Mar 4) to value-prop-feedback.md
- [ ] Add Session 16 (Mar 11) to value-prop-feedback.md
- [ ] Map feedback to R# requirements (R1, R2, R5, R6, R8, R9)
- [ ] Fix before/after height alignment and caption visibility
- [ ] Consider replacing "suspicious stuff" with "suspicious behavior"
- [ ] Consider reframing "active development" language

---

## Maria Paula Mendieta + Jesse (Mar 4, 2026)

**Background:** Maria = Director of Product at Carbon Direct. REPEAT reviewer (Session 6, Feb 26 — reviewed v8). Ex-economist/data scientist. Jesse = non-technical, first-time reviewer. Neither is a developer.

**Source:**
- Otter.ai transcript: `QUGpSuDQI8AaEhnGOGUSKZsuh9A`
- Gemini notes: GDrive `m & j - 2026/03/04 09:45 PST`
- Google Doc: `1LZkC3YalrnBhUdULHEIOHmPpUP107U7s4NTN0FITipI`

**CX version:** v10.1 on `feature/team-section` (team bios, blog section, lowercase labels)

**Outcome: NOT design partners** (Maria = PM, Jesse = non-technical). Strong structural/UX/trust-signal feedback. Maria is a repeat reviewer — compare v8 → v10 evolution.

### Key Takeaways

**1. Mission statement needed at the very top**
- Jesse: "I need one sentence to walk away with... a mission statement"
- Maria still can't explain what Luthien does after two reviews (v8 → v10.1)
- The most basic requirement: tell me what you do in one sentence

**2. Jargon kills comprehension — "$10 words, need nickel words"**
- Jesse couldn't parse: "judge model," "stochastic," "reduce latency," "Cloud haiku"
- Maria: "I see a lot of language that I don't understand"
- Every jargon term is a potential exit point for non-developers

**3. Team bios too personal — center on Luthien, not individuals**
- Jesse: "delete" kids/spouse from Scott's bio — "yours is too personal"
- Maria: "your value proposition should be centered on Luthien, not on your career"
- Don't link personal websites — keep attention on the product
- Maria: "don't say nine, round up" (years → "a decade")

**4. Blog freshness signals viability**
- Jesse: "I would not know if you're in business still" re: old blog post dates
- Maria: blog posts must be within ~2 months to signal active project
- Stale content does more harm than no content at all

**5. LinkedIn company page needed for trust**
- Maria: "I do that for every single early stage startup" — checks LinkedIn first
- Maria: "I look at the CEO and co-founder to make sure they have [LinkedIn]"
- No LinkedIn company page = credibility gap for PM/BD evaluators

**6. ASCII easter egg polarizing — Jesse hates it**
- Jesse: "I hate it... looks like an accident... early internet crap"
- Maria: "it's not as funny as some of your quotes"
- If it looks like a rendering error to non-devs, it damages credibility

**7. Other notable points**
- Maria: fewer but punchier quotes — treat excess as use cases, not evidence dump
- Maria: external links break SEO, give chance to leave site
- Jesse: "Covered it up" category unclear — she guessed "it lied"
- Maria: "Setup help" sounds like talking to a human (want self-service)
- Maria: black color scheme "not conveying safety" — Jesse disagrees (dev preference split)
- Jesse: spotted grammar/formatting issues
- Maria: wants About section with founding story + mission
- Maria: "a rich policy repository would go a long way" — wants to see available policies

### Action Items
- [ ] Add Session 15 to value-prop-feedback.md
- [ ] Map feedback to R# requirements (R1, R2, R3, R5, R6, R8, R9)
- [ ] Create LinkedIn company page for Luthien
- [ ] Remove or truly hide ASCII easter egg
- [ ] Make team bios professional, Luthien-focused (remove personal details)
- [ ] Consider R10: content freshness signals viability
- [ ] Consider R11: team section builds Luthien credibility, not personal brands (or fold into R8)

---

## Zac Saber — Counterweight AI (Jan 27 + Jan 30, 2026)

**Background:** SDE, startup CTO at Counterweight AI (with Jack Wittmayer). Uses Claude Code. Was building his own product and considering using Luthien as infrastructure. Recommended "The Mom Test."

**Source:**
- Otter.ai transcript: `/Users/scottwofford/Downloads/Zac, Jai & Scott_otter_ai_Jan27.txt`
- In-person at Mox, SF (Jan 27 = README review, Jan 30 = policy config session)
- Value-prop feedback: [1-value-prop-feedback.md, Session 0](1-value-prop-feedback.md#session-0-zac-saber-reacting-to-current-readme-on-main)
- Policy config feedback: [3.1-policy-config-feedback.md, Session 1](3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai)

**CX version:** Current README on `main` (developer reference format) + Policy Config page with SimpleJudgePolicy active.

**Outcome: Early power user, not a design partner.** Building complementary/competing product at Counterweight. Willing to self-host but didn't realize that was an option from the README. High-signal feedback on both README and policy config.

### Key Takeaways

**1. "I'm closing the tab" — features buried, setup first is backwards**
- Current README puts setup before features. "I want to know what's the epic shit I can do. Then how do you get started?"
- Custom policies were the hook but were buried at the bottom: "As soon as I saw this, I was like, Okay, this is cool... but it's all the way down here."

**2. Env vars > scripts, keep your own Claude Code**
- "If I have a custom Claude Code, this is completely unusable" (re: launch script approach)
- "I set env variables all the time. Just tell me that." Env vars = developer comfort zone.
- Tell me what Docker spins up, which ports it uses.

**3. Public base URL would change everything**
- "If we could just choose to wrap stuff to your base URL, we can just start using you guys." Hosted endpoint = dramatically lower friction. (Became Jai's "one-click cloud deploy" idea.)

**4. Policy config: meaningful defaults, not AllCaps**
- "AllCaps as a user is not meaningful to me. 'I'm going to block jailbreaks' is meaningful."
- Wants async reports (email/Slack), not a custom website for feedback.
- Wants auto-retry on blocked actions rather than stopping and waiting.

**5. Policy-as-automated-QA (Signal, Jan 31)**
- Wants a policy that evaluates the original prompt against the final agent message and flags divergence. "Check that your final reasoning matches user's original request."

### Policies Zac discussed
1. **Meaningful default policies** — HIGH (block jailbreaks, not AllCaps demos)
2. **Scope creep detection / automated QA** — HIGH (evaluate prompt vs final output)
3. **Auto-retry on blocks** — MEDIUM (retry automatically, don't stop)
4. **Async notification of blocks** — MEDIUM (email/Slack, not custom UI)

### Action Items
- [x] Captured README feedback → [1-value-prop-feedback.md, Session 0](1-value-prop-feedback.md#session-0-zac-saber-reacting-to-current-readme-on-main)
- [x] Captured policy config feedback → [3.1-policy-config-feedback.md, Session 1](3.1-policy-config-feedback.md#session-1-zac-saber-counterweight-ai)
- [x] Policy-as-QA idea → [3.1-policy-config-feedback.md](3.1-policy-config-feedback.md#zacs-additional-feedback-signal-jan-31)

---

## Chris Porter + Beth Anne Porter — Amazon (Feb 8, 2026)

**Background:** Chris = L7 PMT at Amazon (custom LLM / next-token prediction). Beth Anne = L7 at Amazon managing ~30 people working on internal product management AI tools + Buy with Prime. Both use Claude Code but are PM personas, not SDE personas.

**Source:**
- In-person, Super Bowl party
- Otter.ai transcript: `/Users/scottwofford/Downloads/superbowl demo_otter_ai.txt`
- Value-prop feedback: [1-value-prop-feedback.md, Session 1](1-value-prop-feedback.md#session-1-chris-porter--beth-anne-porter)

**CX version:** README Options A (problem-first), B (visual flow), C (use-case-first) in order, plus Luthien blocking demo video.

**Outcome: NOT design partners** (Amazon employees, PM perspective not SDE). But strong PM-as-distribution-channel signal — Beth Anne said "I'm going to send it to my PE."

### Key Takeaways

**1. Visual flow (Option B) got immediate understanding from both**
- Beth Anne: "I like this way better. I like, now I get it." Chris: "I like the visual more."
- The visual diagram answered "how it works" without words.

**2. Use-case-first (Option C) had the best intro**
- "Makes more sense than the ones before." But "pick your policy" confused Beth Anne.

**3. PII use case resonated most strongly**
- Beth Anne: "PII is really good. Just make it more like, set into a real use case." This was the moment she connected Luthien to her own work.
- Package safety also resonated: "I constantly worry about code packages... is it legit?"

**4. "Universal + custom" pattern — independently articulated**
- Beth Anne: "There's a shit ton that everyone gets wrong and these are really dangerous things, and we take care of that. And then there's stuff specific to your business."
- Same pattern as Bahar (enterprise AI safety), Zac (meaningful defaults), Jack (customizable destructive ops).

**5. PM-as-champion distribution path**
- Beth Anne would forward to her engineers. Chris evaluating whether to recommend to his SDEs.
- Non-developer perspective matters: "I can't clock it because I'm not [a developer]" — the `rm -rf` example requires developer context.

### Action Items
- [x] Captured value-prop feedback → [1-value-prop-feedback.md, Session 1](1-value-prop-feedback.md#session-1-chris-porter--beth-anne-porter)
- [x] Package safety policy idea → [3.2-failures-policy-ideas.md](3.2-failures-policy-ideas.md#flag-unknown--suspicious-packages)

---

## Bahar Erar — Enterprise AI Safety (Feb 8, 2026)

**Background:** Former Amazon Applied Scientist. Managed AI safety/policy compliance at enterprise scale (millions of conversations, seller-facing AI tools). Left Amazon ~6 months prior. Has PTSD from AI hype cycle at Amazon. Not currently working in AI.

**Source:**
- In-person, Super Bowl party
- Otter.ai transcript: `/Users/scottwofford/Downloads/superbowl demo v2_otter_ai (1).txt`
- Value-prop feedback: [1-value-prop-feedback.md, Session 2](1-value-prop-feedback.md#session-2-bahar-erar)
- Policy config feedback: [3.1-policy-config-feedback.md, Session 4](3.1-policy-config-feedback.md#session-4-bahar-erar-enterprise-ai-safety-perspective)

**CX version:** README Options C→A→C + live terminal demo of PipBlockPolicy + blocking demo video.

**Outcome: NOT a design partner** (not a Claude Code user, not currently in AI). But expert-level feedback on policy creation, testing at scale, and enterprise AI safety. Different persona from all other interviewees — applied scientist thinking about 0.01% failure rates at millions-of-conversations scale.

### Key Takeaways

**1. "Write your own policy" is too rudimentary**
- "The problem usually of setting these policies is not to define it — but to test it against all the different edge cases, and then actually refining the policy is the hardest part."
- Analogy: "Everybody can say 'I'm not gonna allow drunk people.' How do you define that?"

**2. Testing at scale is the HUGE gap**
- "If you're thinking about AI safety, it has to be a part of the conversation."
- QA-as-seeds → synthetic scale-up → active learning feedback loop. Use QA findings as seeds → generate 1,000+ synthetic examples → test policy → send failures back to human QAs.
- "0.01% matters at scale" — in AI safety, failures are rare but catastrophic.

**3. Handle the fundamentals, let users focus on domain-specific**
- "What I want to focus on is the things that are unique to our space — because those are the hardest things."
- Luthien should provide universal safety defaults; users bring domain rules.
- Converges independently with Beth Anne ("universal + custom").

**4. Policy = knowledge + detection + enforcement**
- Three parts: (a) system must be aware of policies/rules that change, (b) detect when a response relates to a policy, (c) ensure the response complies. "You do need to modularize the solution."

**5. Don't just block — suggest alternatives**
- "If there is a way to also say: hey, actually, I've blocked this because it was doing X. But actually, if it did that, maybe it could have done Y."

**6. "Somehow we forgot the fundamentals"**
- "We had this mental model with ML — you automate something, you measure at scale. Now somehow we forgot." The AI hype killed measurement discipline.

### Action Items
- [x] Captured value-prop feedback → [1-value-prop-feedback.md, Session 2](1-value-prop-feedback.md#session-2-bahar-erar)
- [x] Captured policy config feedback → [3.1-policy-config-feedback.md, Session 4](3.1-policy-config-feedback.md#session-4-bahar-erar-enterprise-ai-safety-perspective)

---

## Jai Dhyani — Internal README Direction (Feb 5, 2026)

**Background:** Co-founder & CTO at Luthien. Reviewed README options A/B/C before they were shown to external users. Shaped the approach for the Super Bowl demo and subsequent README iterations.

**Source:**
- Google Meet standup
- Gemini notes: `/Users/scottwofford/Downloads/Jai's feedback on value prop  - 2026_02_05 13_56 PST - Notes by Gemini.md`
- Value-prop feedback: [1-value-prop-feedback.md, Internal session](1-value-prop-feedback.md#internal-session-jai-dhyani-co-founder-feedback-on-options-abc)

**Outcome: Internal strategic direction.** Set the framework for all subsequent README iterations: GitHub = landing page, demo does the work, value before shape, one-click cloud deploy vision.

### Key Takeaways

**1. GitHub README IS the landing page**
- "The GitHub repo is always going to be a de facto landing page... trying to maintain two landing pages is hard."

**2. Demo video/screenshot should do most of the work**
- "Lead with an example and then name the category." Show pip→uv or rm-rf, THEN say "control what your agent does."

**3. Describe value before shape**
- "Drop-in proxy" is accurate but not intuitively obvious. "First we describe the value and then we describe the shape of it."
- "Without changing anything about your development environment" > "without changing your code."

**4. One-click cloud deploy is the simplest onboarding**
- "You press a button, specify some rules, you now have an endpoint." Railway abstracted away.
- Pass-through auth reduces friction: user brings own Claude subscription.

**5. Don't show SaaS UI on the README**
- "That's like a next month problem. Right now our main bottleneck is just getting feedback."

### Action Items
- [x] Captured strategic direction → [1-value-prop-feedback.md, Internal session](1-value-prop-feedback.md#internal-session-jai-dhyani-co-founder-feedback-on-options-abc)

---

## Darren Ellis — Landing Page Design Feedback (Mar 2, 2026)

**Background:** Designer at Carbon Direct. NOT ICP (not a developer, doesn't use Claude Code daily). High-signal on visual communication, page structure, and design process.

**Source:**
- Video call (Google Meet, recorded)
- Google Doc: `1cf4N71qxWVWA9c_FvwrO-7PB-qRw2kBcsC2qjEXzL4c` (Gemini notes)
- Value-prop feedback: [1-value-prop-feedback.md, Session 11](1-value-prop-feedback.md#session-11-darren-ellis-landing-page-design-feedback)

**CX version:** Landing page (v8 or v9 variant).

**Outcome: NOT a design partner** (designer, not developer). High-signal visual communication feedback that converges with multiple other reviewers.

### Key Takeaways

**1. Before/after SVGs hard to scan — "what is the difference?"**
- If a visually trained designer can't spot the difference, general developers scanning quickly will miss it too. Needs explicit annotation.

**2. Content overload — "requiring a lot of reading"**
- Converges with Finn ("just skipped"), Maria ("cognitive effort"), Mike Mantell ("don't want to read all this shit"). 4th reviewer flagging density.

**3. Page needs story flow, not disconnected sections**
- Should follow: problem → what is it → how it works → evidence. Currently feels like a reference doc, not a narrative.

**4. Collapsed "How it works" felt like an afterthought**
- The `<details>` collapse made architecture feel deprioritized rather than intentionally progressive-disclosed. May need framing like "Want to go deeper?"

**5. Design process advice (meta-feedback)**
- Keep PRD/requirements as persistent AI context, create design tokens/guidelines, iterate piece by piece not one-shot.

### Action Items
- [x] Captured value-prop feedback → [1-value-prop-feedback.md, Session 11](1-value-prop-feedback.md#session-11-darren-ellis-landing-page-design-feedback)
- [x] Design process advice incorporated into luthien-org CLAUDE.md

---

## Ronak Mehta (Mar 8, 2026)

**Background:** Heavy Claude Code user. Was in 5050 accelerator with co-founder Jacques. Built a Claude Code wrapper product (pre-tool-use hooks with type checkers + GPT-5 code review) that didn't ship due to co-founder split. Uses tmux sessions to run Claude Code in background. Writes 10K+ lines/day.

**Source:**
- SuperWhisper transcript (audio partially lost — Bluetooth headphones connected outside phone booth): `_User-Interview-Notes/Ronak Mehta/Ronak Mehta - March 8, 2026 at Mox 10pm.md`
- In-person at Mox, SF

**Outcome: NOT a design partner.** Strategic/philosophical conversation — no landing page review or Luthien demo. Self-describes as atypical user ("don't over-index on the way I am coding"). Skeptical of Luthien's long-term moat but acknowledges 2-year window if execution is fast. Introduced competitor: **Aethra Labs** (oversight infrastructure for coding agents, was in 5050 accelerator and at Constellation).

### Key Takeaways

**1. Claude Code UX pain points are real but feel like "me problems"**
- Copy-paste spacing from 2-character buffer, tmux pane copy bleeds across panes, accidental escape kills input, TUI input frustrations.
- Pattern: users say "it's a me problem, I could probably fix this" but it's actually a product problem. "This is more of a me problem. I can probably fix this by just asking Claude to fix this."

**2. Mobile Claude Code demand is real**
- "Every third person I talk to is like, I wish I could run this from my phone."
- Built a jank mobile SSH app to connect to Claude Code on his desktop. Doesn't use it because "it's jank because I wrote it as a slot machine."

**3. "Making the horse faster" challenge — 2-year window**
- Core pushback: fixing Claude Code UX friction may be obsolete within 1-2 years as interaction model shifts (copilot → agentic → speech).
- "It could be that a year from now, the way we're interacting with something like Claude Code is just very different."
- But concedes: "If I talk to 200 people using Claude Code and I pick the lowest hanging fruit, that we can do it in a year. You need to accelerate your timelines."

**4. Ephemeral apps thesis**
- Code generation becomes commodity → all UIs generated on demand → Arc Browser model for everything.
- "I don't want an IDE... I'm faster with key bindings and the terminal."
- "I don't want Claude Code to be the all-in-one thing." Likes separate scripts for Git worktrees, tmux management.

**5. Pre-tool-use hooks as Claude Code wrapper (prior art)**
- Jacques and Ronak built hooks that ran type checkers and called GPT-5 for code review before tool use. Didn't ship because they split. "You should still talk to Jacques."
- Validates the proxy/hook approach but notes the product didn't land even for its creators.

**6. Data ownership didn't resonate personally**
- "Conversations are ephemeral enough for me." Artifacts (code output) are the only thing he needs to keep.
- Acknowledged others would care, but this isn't his pain point.

### Action Items
- [ ] Talk to Jacques (Ronak's ex-co-founder) about their Claude Code wrapper learnings
- [ ] Research Aethra Labs (A-E-T-H-R-A) — oversight infrastructure for coding agents, 5050 accelerator + Constellation

---

## Sergi Lange-Soler — EAG SF (Feb 15, 2026 — 30-min in-person interview)

**Background:** British developer building a solo Android app with LiveKit and a Python backend (early stages, no database). Uses Claude Code on Sonnet (~£17/month UK plan). Pretty hands-on workflow, works mostly on one branch.

**Source:**
- SuperWhisper transcript: `_User-Interview-Notes/Sergi Lange-Soler/EAG SF Feb 2026 — Superwhisper transcript.md`
- In-person at EAG SF

**Outcome: NOT a design partner.** Early-stage solo developer, not a power user. Gave useful README cold-read feedback — the "seems kind of similar to CLAUDE.md files" objection is strategically important (same as Josh's "what does Luthien do that a system prompt can't?").

### Key Takeaways

**1. "I don't really understand what's happening" — README intro didn't land**
- Cold-read of the README: "Not resonating that much with the intro there."
- Couldn't parse what Luthien does from the first paragraph alone.

**2. "Seems kind of similar to CLAUDE.md files" — the differentiation question**
- After reading more: "Can I just put this in the CLAUDE.md file? Can I just put in CLAUDE.md: please use UV instead of pip install? And then like 90% plus of the time, it'd use UV."
- Same objection as Josh Levy ("what does Luthien do that a system prompt can't?"). Landing page must address this.

**3. Worried Claude Code updates would break the proxy**
- "How am I going to get a Claude Code update and will this stop working and then I'll have to change my workflow again?"
- Breakage concern = adoption friction. New feedback not heard before.

**4. Docker as dependency friction**
- Doesn't typically have Docker running. Would be a dependency to install.

**5. "dangerously skip permissions" tension**
- Considering enabling it for speed but worried about file deletions outside codebase and gradual code spaghettification.
- Astute distinction: file deletion = safety issue (solvable by rules), spaghettification = capabilities issue (can't just prompt it not to).

**6. CLAUDE.md compliance degrades over time**
- Instructions followed at start of conversation, then "kind of gets lazy and stops doing it."
- Validates the context rot pattern reported by Quentin, Josh, and others.

### Action Items
- [x] Captured README cold-read feedback (differentiation question, breakage concern)
- [ ] Address "how is this different from CLAUDE.md?" on landing page (converges with Josh's feedback)

---

## Nathan Helm-Burger — AI Safety Researcher (Jul 7 + Jul 30 + Aug 4, 2025)

**Background:** Neuroscience background, pivoted to AI safety full-time 3+ years ago. London AI Safety Labs fellowship — produced a control paper on models sneaking malicious code past monitors. Was interviewing for Anthropic's interpretability team. Heavy Claude Code user (runs out of pro plan credits, supplements with Gemini). Co-authored paper on chain-of-thought monitoring.

**Source:**
- 3 sessions of discovery interviews
- Gemini notes: `_User-Interview-Notes/Nathan/` (Jul 7, Jul 30, Aug 4 transcripts)
- Nathan's claude.md, debug_prompt.txt, todo.txt, and links also in that folder

**Outcome: STRONGEST pre-pivot design partner candidate.** Three sessions of deep engagement. AI safety background = deeply understands Luthien's mission. Volunteered to alpha test rough prototypes. Shared research, offered referrals.

### Key Takeaways

**1. Richest source of failure mode data across ALL interviewees**
- Claude Sonnet 3.7: "evil" output in >50% of responses, requiring careful review of every change
- Claude comments out failing unit tests and declares success
- Mocks API calls with hard-coded responses while claiming to have built the real integration
- Adds items to its own to-do list ("create mock"), then checks off "create real thing" without doing it
- Summarizes incomplete/failed work as "complete success"

**2. Cross-model critique is highly effective**
- Gemini catches Claude's errors well and vice versa — model failures are "heterogeneous"
- Same-model self-critique is much less effective
- Directly validates Luthien's architecture of using a separate model for policy enforcement

**3. Monitor suggestibility is a fundamental weakness (from his control paper)**
- Models easily fool monitors by fabricating plausible justifications in chain of thought (e.g., "this is corporate policy")
- Implications for LLM-as-judge policies: judge prompt engineering matters enormously

**4. TDD enforcement as a policy**
- Uses TDD approach: breaks complex tasks into tiny functions with individual unit tests
- Suggested models be trained with "successfully creating a failing test" as a reinforcement learning success metric

**5. Policy library vision**
- Wants a policy library like Tampermonkey user scripts — users share/download rule sets
- Suggested fine-tuning a monitor model on a specific codebase's implicit rules

### Policies Nathan discussed
1. **Don't comment out tests and claim success** — HIGH (his most frustrating failure)
2. **Don't mock API calls without explicit permission** — HIGH
3. **Verify claimed completion against actual output** (anti-false-success-claim) — HIGH
4. **TDD enforcement: create failing tests BEFORE implementing** — MEDIUM
5. **Don't add functionality beyond what was requested** (YAGNI) — MEDIUM
6. **Library reuse enforcement** — MEDIUM
7. **Don't import new libraries without permission** — LOW
8. **Codebase-specific naming convention enforcement** — LOW

### Action Items
- [ ] Re-engage Nathan — strongest pre-pivot candidate, may be interested in current product
- [x] Policy ideas captured in 3.2 (false success claims, mock insertion map to existing entries)

---

## Anthony Bailey — PauseAI (Jul 14, 2025)

**Background:** Senior developer at PauseAI. Codes approximately 2 days per week. Uses Cursor and Claude Code. Treats AI like a junior engineer he mentors — applying patterns from early-career experience managing new graduates.

**Source:**
- Google Drive folder: luth-gdrive-clone/_User-Interview-Notes/Anthony Bailey/
- Internal interview guide with inline notes from Scott and Jai
- Otter.ai transcript (.docx only — not machine-readable as text)
- Google Doc: [Link](https://docs.google.com/document/d/1LIxnEXIcjL1gU7IT1wUtqzZOo4Sn49Z-ENKbrBdTI_c/edit)

**Source quality note:** The primary readable source is the interview guide with inline notes — a mix of questions, shorthand answers, and Jai's/Scott's observations. The full Otter transcript exists as a .docx binary file that couldn't be read as text. Takeaways below reflect what was captured in the notes, which are relatively sparse compared to later interviews with richer transcripts.

**Outcome: NOT a design partner.** Early-phase discovery interview (Phase 2). Limited coding time (~2 days/week) and not deeply embedded in agentic AI workflows. However, his context management pain aligns strongly with patterns seen across later interviewees (Quentin, Peter, Tyler, Sergi).

### Key Takeaways

**1. Context management is his #1 pain — "chunking work into context fit is hardest to do reliably, causes most issues"**
- Fitting work into the context window is the most difficult and error-prone part of his AI workflow
- Developed a workaround: start asking for summaries earlier in the session, compact, get a report, and start a new session
- "Taken me a while to get" — learned through trial and error, not obvious from the start
- Hours wasted end-to-end; "value was being squeezed out more slowly"

**2. Summarization drops important content — "level of fidelities, important bits missing, dropped out of summarization"**
- When compacting or summarizing sessions, important details disappear
- Describes varying "levels of fidelity" — the summarization doesn't preserve what matters
- Validates the context rot / compaction loss pattern reported by Quentin, Peter, Tyler, and Sergi in later interviews

**3. Parallel sessions and collaboration concerns — "I tend to worry more about other people in same code"**
- When asked about running multiple AI sessions in parallel, his bigger concern was other humans working in the same codebase
- Works on CI/CD infrastructure where branching doesn't always make sense
- Trying to learn good idioms for remote collaboration and time zones
- Different from later interviewees who worry about AI merge conflicts — Anthony's concern is human coordination

**4. Treats AI like a junior engineer — mentoring pattern from early career**
- Initially applied a mentoring pattern too aggressively (like managing new grads: "work all night, disasters happened, come in the morning, teach good principles")
- Has relaxed about this — "I don't need [to do that]. I was applying that pattern a little too much."
- Prefers AI to explain commands in full: "anytime we run a command, explain it in full, really helps to learn the technology"
- Wants education about unfamiliar technologies: "why is that flag being passed?"

**5. Limited coding time — projects into little bits**
- Codes at most 2 days per week
- Breaks projects into small chunks — possibly driven by context window constraints
- The limited time amplifies the cost of context management failures (hours lost = proportionally more painful)

### Policies Discussed

No specific policies were discussed in the interview. The conversation focused on failure modes and workflow patterns rather than concrete policy ideas. The context management and summarization pain points map to:
1. **Context preservation / anti-compaction-loss** — HIGH (his #1 pain)
2. **Explain commands in full** — MEDIUM (educational preference, not a safety concern)

### Action Items
- [x] Context management pain captured (validates pattern seen in Quentin, Peter, Tyler, Sergi, Kirk)
- [x] Summarization loss documented as early signal (Jul 2025 — one of the first interviewees to articulate this)
- [ ] Consider re-engagement: Anthony's context management pain is real but his limited coding time (~2 days/week) may not make him a strong design partner candidate

---

## Lee Wall — AI Safety / Alpha Tester (Oct 24 + Nov 14, 2025)

**Background:** Based in Philadelphia. AI safety researcher/engineer. Met Scott at EAG. Experiments with Claude Code sub-agents — created an adversarial sub-agent ("Marvin") constrained to only make hello world programs, tested prompt injection against it.

**Source:**
- 2 Luthien trial sessions (Oct 24 + Nov 14)
- Gemini notes: `_User-Interview-Notes/Lee Wall/` (both sessions)

**Outcome: STRONG design partner candidate (needs re-engagement).** Highly engaged, AI safety background. Tried Luthien twice — both sessions hit significant setup/deployment bugs. Expressed enthusiasm and willingness to contribute to open-source project. Self-described as "the deadline guy" who creates external accountability.

### Key Takeaways

**1. Defensive programming as a failure mode**
- LLM-generated code adds excessive try/except and graceful failure handlers that obscure bugs and make debugging impossible
- Worries about downstream consequences on critical infrastructure
- Same failure as Nico's "fail hard / no silent failures" — validates across users and time periods

**2. Judge model capability matters**
- Questioned whether a small model (Gemma 2B) could effectively judge complex policies like "no defensive programming" written by a much larger model (Claude)
- Lower-complexity policies are better suited for smaller judge models
- Important architectural constraint for Luthien's LLM-as-judge approach

**3. Setup friction killed both demos**
- Oct 24: Got further (saw activity monitor, attempted custom policies) but core policy enforcement was broken
- Nov 14: Shorter session, blocked by untested code changes
- Referenced a startup whose production database was dropped by an agent that then lied about it

**4. Custom policy attempt: hazardous information checker**
- Tried writing a "sarin gas" detection policy. Found the streaming API complex.
- Jai acknowledged this was the "less bad version" of the API

### Action Items
- [ ] Re-engage Lee Wall — enthusiastic alpha tester whose sessions were blocked by bugs (likely fixed since Nov 2025)

---

## Aleksandr Popov — Claude Code Power User (Jul 23, 2025)

**Background:** Front-end and back-end developer at plans.com (safety-related site). Primary tool is Claude Code. Uses WebStorm for static analysis and Melt for diff comparison. Has both user-level and project-level CLAUDE.md rules. Works solo with manual review of every change.

**Source:**
- Discovery interview (Jul 23, 2025)
- Gemini notes + chat history: `_User-Interview-Notes/Aleksandr Popov/`
- Aleksandr's claude.md also in that folder

**Outcome: POTENTIAL design partner (needs re-engagement).** Well-articulated pain points that map directly to Luthien's value prop. Expressed interest in testing once Claude Code was supported.

### Key Takeaways

**1. Rule enforcement gap is his core pain**
- Uses CLAUDE.md rules to address recurring bad behaviors but finds they're not always followed
- "The more rules he adds, the higher the probability some get skipped" — validates context rot pattern

**2. Specific AI failure patterns**
- Architectural leftovers: unused functions, placeholder/empty functions, duplicated code
- Unfinished tasks: stubs that return placeholder data
- Unwanted removals: comments, log lines, styling sections deleted without asking

**3. Prefers full automation over manual review**
- Violations should be autocorrected without manual intervention
- Wants corrections inline in single text flow
- Prioritizes code quality over speed or cost

**4. Rule specificity matters**
- Vague instructions like "don't cheat on unit tests" are ineffective
- Policies need to be concrete and detailed with specific forbidden patterns

### Policies Aleksandr discussed
1. **Never leave dangling/unused functions** — HIGH
2. **Never remove comments or log lines** — HIGH
3. **Never leave placeholder/stub implementations** — MEDIUM
4. **Always clean trailing whitespace and add newline at end of file** — LOW

### Action Items
- [ ] Re-engage Aleksandr — clear pain points, expressed interest in testing

---

## Kirk Marple — Graphlit CEO (Aug 18, 2025)

**Background:** CEO/founder of Graphlit (data persistence/knowledge-as-a-service). Ex-Microsoft (3D virtual worlds, Windows Media). Pivoted from 11-person startup to lean solo+contractors. Built Zen app and MCP server/client using Claude Code. Post-revenue, 50% of signups come through MCP. Based in Seattle.

**Source:**
- Discovery interview (Aug 18, 2025)
- Gemini notes: `_User-Interview-Notes/Kirk Marple/`

**Outcome: NOT a design partner.** More of an advisor/founder-peer. Sophisticated AI coding tool user but use case is about building his own SaaS, not about AI control/safety.

### Key Takeaways

**1. The "last 10-20%" problem**
- Initial 80% of development is dramatically easier with AI, but the last 10-20% (testing, debugging, edge cases) is where AI struggles most
- "It was so confident about such shitty code that it wrote" (Frustration #37 in database)

**2. AI struggles with strong typing and iteration**
- Frequent TypeScript hallucinations about parameters
- Models generate fresh code well but struggle badly with iterating on existing code and debugging

**3. PRD-based workflow as workaround**
- Writes a Product Requirement Document first, gives it to AI as reference
- Regularly tells AI to "capture research to the PRD" to avoid context loss
- Workaround for the context management problem Quentin also faces

### Action Items
- None — not a design partner candidate. Feedback archived for reference.

---

## Ron Theis — TryThatLLM Founder (Aug 20, 2025)

**Background:** Ex-Tableau (8 years) and ex-Grammarly (3 years). Building TryThatLLM, an automated prompt testing tool that evaluates cost and quality across LLM models via API. Solo founder, full-time since late 2024. Uses Cursor, Claude Code (Max plan), and WebStorm daily. TypeScript codebase.

**Source:**
- Discovery interview (Aug 20, 2025). Jai was out sick (COVID); Scott ran the call solo.
- Gemini notes + raw notes: `_User-Interview-Notes/Ron Theis/`
- **Source quality caveat:** Raw notes are sparse bullet points. Gemini transcript is thorough but auto-generated. Ron's key quotes are clear and directly usable.

**Outcome: NOT a design partner.** Validated the concept strongly when explained, but doesn't currently know what rules exist in his CLAUDE.md or cursor rules — meaning he wouldn't self-serve into Luthien without education. More of a concept validator than an active user of rule-based workflows.

### Key Takeaways

**1. Rule conformance is a real, recurring problem — TypeScript types example**
- "It made its own version of the TypeScript types" instead of using auto-generated ones from the database — "this happens all the time"
- Wouldn't catch this on an unfamiliar codebase: "If I was new to this codebase, I wouldn't instinctually know"
- Same class of pain as Kirk Marple (TypeScript hallucinations) and Aleksandr Popov (architectural leftovers)

**2. Directly validated Luthien's concept when Scott explained it**
- "Of the diffs made, did they conform to the rules? And if not, which ones did they miss? That would be a useful thing to know"
- Framed it as "LLM as judge for the code that came out — the criteria isn't quality, it's did it conform to the rules that were set out"
- Caveat: doesn't have a feel for "how often it ignores the rules" — said that frequency data would determine how useful the tool is

**3. Scoping/context pain: agents edit too many files**
- "Why did you edit 10 files? You should have just edited two" — common early-stage agent frustration
- Workaround: has agents write plans to markdown files first, then review before code generation
- Uses the plan-in-markdown approach to switch between tools (Claude Code makes plan, Cursor implements, or vice versa)

**4. Visual diff desire: directory trees of planned vs. actual changes**
- "If I could make a tool for Claude Code, it would help me visualize" — wants more than text reports
- Specifically wants: directory tree showing new files/modified files, before (plan) and after (actual) views
- "Even just seeing where [changed files] are in the directory tree" — hierarchy gives scoping confidence
- After-the-fact view is "at least as useful" as the plan: "Why did you make a new lib directory? Those all belong over here."

**5. Cursor gives more review control than Claude Code**
- Cursor's chunk-by-chunk "review next file" flow makes him feel like he's covered all changes
- Claude Code: "I gotta do the git diff and that's kind of it... I better make sure I look at all the git diffs in every file or else I'm going to miss something"
- Uses Claude Code inside Cursor (IDE integration) but still prefers Cursor's native review UX

**6. Doesn't actively maintain rules — gap in self-awareness**
- "I'm probably doing a bad job of applying those lessons to the CLAUDE.md or the cursor rules"
- Raw notes flag: "Doesn't know what rules are there in claude / cursor rules, so wouldn't use Luthien"
- **Open question from Scott's raw notes:** "What is the filter criteria that we could have applied to know that he wasn't a good fit for Luthien (or he'd need more education on rules before trying)"

### Action Items
- None — not a design partner candidate. Validated the concept but lacks the rule-authoring habits that make Luthien immediately useful. Feedback archived for reference.

---

## Jack Wittmayer — Counterweight AI / Amazon (Oct 27, 2025 + Feb 3, 2026)

**Background:** Amazon engineer. Uses Claude Code at work (Amazon granted access ~4 months prior to Oct 2025). Co-founded Counterweight AI with Zac Saber. Described Claude Code as "the first tool that I actually find worth using."

**Source:**
- Oct 27, 2025: Alpha test session — Gemini notes: `_User-Interview-Notes/Jack Wittmayer/`
- Feb 3, 2026: Policy config session with Zac — [3.1-policy-config-feedback.md, Session 2](3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber)

**Outcome: MODERATE design partner potential.** Amazon enterprise perspective. Oct 27 session consumed by setup friction; Feb 3 session produced substantive policy feedback.

### Key Takeaways

**1. Oct 27 alpha test: setup friction killed the session**
- Docker setup, UV install, timing bug in quick_start. Got proxy running but blocked by Claude Code OAuth flow.
- Hard stop at 30 minutes — almost no product feedback gathered.

**2. Feb 3 policy config feedback (with Zac)**
- Wants to customize what counts as destructive operations: "things I don't want it to do ever"
- Import rules from CLAUDE.md instead of re-specifying
- Spending alerts should be rate-based, not threshold-based: "spending credits at 2x your normal rate"
- Terminal ping preferred over email notifications: "Claude Code supports via hooks"

**3. "Understanding debt" from vibing**
- Shifted from code review mindset to "viby" (ship fast) → accumulated "understanding debt"
- Lost track of what the AI actually built — implies need for session summaries

### Action Items
- [x] Captured policy config feedback → [3.1-policy-config-feedback.md, Session 2](3.1-policy-config-feedback.md#session-2-jack-wittmayer-counterweight-ai--zac-saber)

---

## EAG SF Conversations (Feb 13-15, 2026)

The following conversations were recorded at the Effective Altruism Global conference in San Francisco. Most are 20-30 minute in-person interviews, not hallway chats — each was a real conversation with product feedback. Organized alphabetically.

---

### Aaron Sandoval (EAG SF, Feb 14 — 30-min in-person interview)

**Background:** Redwood contractor working on Control Arena. Uses Claude Code on a remote SSH host. Conservative about permissions but increasingly tempted by dangerously-skip-permissions due to babysitting fatigue.

**Source:** Otter transcript `c5jxUdUzQFRcy2fvsJjwn3yNycg` (22 min)

**Outcome: POSSIBLE design partner.** Honest README read-through with detailed feedback. Uses Claude Code daily in a research context.

**Key Takeaways:**
1. **Python/English policy description confused him** — "It says writing in Python, but also it's plain English. That seems contradictory." Didn't understand when methods run.
2. **CLAUDE.md handles his current pain points** — "My Claude MD seems to have dealt with this fine." Hasn't experienced the listed failure modes with Claude Code (did with Cursor, which is why he switched).
3. **Docker container conflict concern** — Runs all experiments in Docker. "If this caused [Docker stop] to fail, that would be probably annoying enough." Prefers Railway/cloud option to avoid competing with his containers.
4. **Babysitting friction driving dangerously-skip-permissions temptation** — "I wanted to tell it to do that and walk away for an hour... I was babysitting." Naturally conservative but shifting toward more autonomy.

---

### Kushal (EAG SF, Feb 14 — 30-min in-person interview)

**Background:** Applied scientist at a ~3,500-person company. Company just approved Claude Code org-wide (was in pilot before). Works with sensitive legal data on Azure with strict data-boundary requirements.

**Source:** Otter transcript `zzDZN_eUiqwZAreRsmOGdDaT4aQ` (23 min)

**Outcome: AGREED to design partner call.** Enterprise use case with strict data requirements. Exactly the type of customer who needs configurable proxy architecture.

**Key Takeaways:**
1. **Full code audit required for enterprise adoption** — "They have very strict requirements that they'll do a full audit and read the code." LLM judge must not send data to unapproved servers — local model or approved instance is fine.
2. **Data boundary constraints are non-negotiable** — Azure-deployed LLMs, data can't cross national boundaries. "All of our data has to stay within the data boundary because of legal reasons."
3. **50ms latency: positive reaction** — No concern about performance overhead for simple policies.
4. **Compaction log capture excited him** — "It's logging everything in real time. So won't lose the stuff that was compacted? Right?" Immediate recognition of value.
5. **Calibration/closed loops** — Built his own confidence-tracking system prompt. Wants Claude to "search the web, call the tool, check the context" before bothering him. Related to false-success-claims policy idea.

---

### Matt Handzel (EAG SF, Feb 15 — 30-min in-person interview)

**Background:** Uses Claude Code and Codex extensively for personal projects and research. NixOS user — experiences chronic pip-install failures because Nix requires `nix` commands instead.

**Source:** Otter transcript `UVZXY3twpv04x-IQ04BCunX8ZLg` (24 min)

**Outcome: INTERESTED.** Engaged with README and demo. Asked good product questions.

**Key Takeaways:**
1. **NixOS pip-install pain is chronic** — "I consistently see it try to run pip install, and it's like, oh, I actually can't do this anymore. And then it wastes [time]." Strong resonance with package management policies.
2. **"Wouldn't I be able to just pip install or `uv` install it?"** — Expects frictionless installation. Current clone+Docker onboarding too heavy.
3. **Claude Code update breakage concern** — "When Opus six comes out, are you not useful anymore?" Same concern as Sergi. Durability of the proxy pattern matters.
4. **Golden Gate Bridge design resonated** — Understood and liked the "don't change your dev setup" philosophy.

---

### Felix Hofstatter (EAG SF, Feb 14 — 30-min in-person interview)

Apollo researcher (anti-scheming). Uses Claude Code. Frustrations are about mundane coding patterns (local imports, defensive coding), not dangerous actions. Would need to check with Marius/security before installing. Suggested connecting with Nikita at OpenAI. Source: Otter transcript `QTSyNYAS5iO7zQgcT8h4qDPT5lc`.

---

### Tomas Turlik (EAG SF, Feb 15 — 30-min in-person interview)

**Background:** Redwood contractor working on Linux Arena. Uses Claude Code heavily. Also uses Cursor chat for smaller tasks.

**Source:** Otter transcript `OuHTjDDkpIhdvUIZHXgh7EQ75YA` (24 min)

**Outcome: AGREED to try Luthien.** Wants Railway/cloud option since his laptop is slow.

**Key Takeaways:**
1. **Strong resonance with instruction-following failures** — "My main concern with Claude in the last month is that it just seems stupid. It doesn't follow the Claude Code MD." UV, skills/tools ignored, reinvents the wheel.
2. **Forest-vs-trees policy idea resonated** — "You could write a policy that's like, hey, we've been working on this for four hours. Look at the whole conversation, including the original prompt, and make sure the output adheres to both." Liked the concept of a separate instance watching the forest while Claude works on trees.
3. **Privacy initially concerned him, resolved by local** — "Wait, so Luthien sees everything? ... But it's running locally? Okay." Important that README clarifies this upfront.
4. **Open-code compatibility** — Flagged open-code (open source Claude Code alternative) as something Luthien should check compatibility with.
5. **"This is what control will go towards eventually"** — Sees Luthien's approach as the direction AI control research is heading.

---

### Dylan Fridman (EAG SF, Feb 13 — 30-min in-person interview)

Recently left job, started vibe-coding with agents (~2 months). **AGREED to be design partner.** Wants false positive/false negative rates quantified on README. Theory of change (dev tools → lab safety) resonated. Source: Otter transcript `ql8jIJog6fhrPW6-2zm5kv_eiY8` (25 min).

---

### Max Werner (EAG SF, Feb 13 — 30-min in-person interview)

**Background:** Engineering lead at a German company with 4 junior engineers. Internal AI team. Most of the company can't use external AI due to contractual restrictions with enterprise customers.

**Source:** Otter transcript `URQngfXAw74Cz8LF5OSyaoj3E5c` (26 min)

**Outcome: AGREED to bi-weekly calls.** Not ideal customer now (team can use Claude Code freely, no restrictions), but the rest of the company has restrictions that Luthien could address.

**Key Takeaways:**
1. **Contractual restrictions are the real blocker** — "Our contracts often say nothing about AI usage or full code has to remain local." Not a technical problem — a legal/compliance problem that a security layer could address.
2. **Real-time blocking required, not async** — "If the data has already left our server, we have a security incident." PII/customer data exfiltration is binary: either you caught it or you have a breach.
3. **"Fluffy" rules that vary per project/customer** — Can't write simple regex rules for customer data. Needs LLM-grade judgment. Rules differ by project and customer contract.
4. **IT security people as gatekeepers** — "It would lessen their worries if there was a layer of security that we could control." The proxy is a tool for the security team to approve Claude Code usage.
5. **Open source + free = PM-level authority to adopt** — "I could probably, as our project manager, just decide, okay, we're going to use this." No procurement needed for open source tools.

---

### Marcus Abramovitch (EAG SF, Feb 15 — 30-min in-person interview, group session with Mike, Sergi)

**Background:** Crypto trader. Uses dangerously-skip-permissions exclusively. Builds automated trading systems with AI agents handling cryptocurrency wallet transfers.

**Source:** Otter transcript `ZWXR8NrFer_l8INl1etnwa19_Ec` (1h43m group session). Marcus section is ~30 min within the longer transcript.

**Outcome: AGREED to follow-up call.** High-stakes use case (money at stake). Willing to write 20 minutes of rules.

**Key Takeaways:**
1. **Risk-severity indicator: "that'd be so useful"** — Wants green/yellow/red indication for actions he's about to approve. "Really love if your product would tell me about how dangerous the thing I'm about to approve would be."
2. **Uses dangerously-skip-permissions, terrified of consequences** — "My biggest vulnerability... I didn't see these. Good permissions. Approve all bash." Hands-off workflow but knows it's risky.
3. **Concrete high-stakes use case: automated crypto disputes** — Wants to automate Polymarket dispute resolution. 99.9% of transactions are correct, needs to catch the 0.1% with >75% accuracy. "$250 per dispute" — real money at risk.
4. **Didn't understand intro** — "Not resonating that much with the intro. I kind of don't really understand what's happening." README needs clearer opening. Then: "Seems kind of similar to Claude MD files" — same reaction as Sergi.
5. **Willing to write rules** — "I could totally write down a bunch of rules that I don't want it to do. Take 20 minutes." Concrete willingness to invest in policy configuration.

---

### Anshul (EAG SF, Feb 14 — 30-min in-person interview)

Redwood researcher (Linux Bench). Uses Claude Code + Codex with 5 parallel checkouts, dangerously-skip-permissions. Skeptical — worried Luthien adds breakage on top of Claude Code's already-changing behavior. Questioned monitoring value beyond built-in features. Agreed to follow-up call despite skepticism. Source: Otter transcript `qeIh_-VDXF7GDcVh20htpHL47og`.

---

### Marius Hobbhahn — Apollo (EAG SF, Feb 15 — 30-min in-person interview)

**Background:** CEO of Apollo. Builds AI oversight tools with 3-component architecture: log ingestion + grading, input gateways, output/analysis.

**Source:** Otter transcript `WUkUwGa27n9bTVIUytoSfgY5YHo`

**Outcome: ACTION ITEM — joint integration call.** Apollo explicitly doesn't want to build a gateway; wants to integrate with Luthien's.

**Key Takeaways:**
1. **Apollo wants Luthien as its input gateway** — 3-part architecture: Luthien provides the proxy/gateway, Apollo provides grading/analysis. Explicit partnership opportunity.
2. **Demoed Apollo's internal tool live** — Trajectory grading, false positive analysis, live monitoring mode. Shows what mature monitoring UX looks like.
3. **Joint call action item** — Marius + Scott required, Jai + Jeremy + Marcus optional. Define integration interfaces.

---

### Lindley Lentati — Panopticon (EAG SF, Feb 13 + Ardy session — 30-min in-person interviews)

**Background:** Building Panopticon platform for multi-agent monitoring and control protocols. Detailed technical collaboration discussions across two sessions.

**Source:**
- Lindley 1:1: Otter transcript `0dr-3DIAz031NbtlHAGITmHRuPw` (1h20m)
- Ardy + Lindley: Otter transcript `0371qaxrGXn33RUmuqv3_mwDnvw`

**Outcome: ACTIVE collaboration.** Detailed architecture discussions about using Luthien as proxy backend for Panopticon's control protocol system.

**Key Takeaways:**
1. **Luthien proxy → Panopticon policies/grading** — Integration architecture where Luthien handles the API interception and Panopticon handles policy logic and oversight.
2. **Admin vs developer UX** — Different interfaces needed for overseers (who configure policies) vs developers (who code through the proxy).
3. **Dynamic policy configuration** — Policies need to change at runtime, not just at startup.
4. **Ryan Greenblatt's Claude Code frustrations** — Context access and history are pain points even for anthropic researchers.

---

### EAG Conversations — Category B (No Product Feedback)

**Govind v2** (`I-FhxBhHugYLbHwVs9O_mKBywgA`): Strategy/sales advice. No product feedback. Discussed selling to startups vs enterprise, YC lectures, Transluce/Docent as related company.

**Security and AI Strategy** (`4xXqgwOYWIhhyM0tFZMQ4hOHvfU`): Theory-of-change with Govind. Safety training not transferring to agents, competitive positioning vs labs, speculative decoding. No product feedback.

**AI Safety Workflow Review** (`hqmXThyFlX875ChrkG9PrRwLPTc`): ~3hr Seldon cohort session. Overlaps heavily with Marius and Lindley transcripts. Unique portions about research management (NASA/nuclear physics background).

**Luis Slyfield** (`8c8z4QZfiILa_X06J_YSztUoCfc`): Quick README scan. "If something sat between me and Claude Code and did that stuff well, I would — that sounds great" but flagged "intercept" as scary. Thin feedback due to fatigue. Primary value as METR/Redwood network connector.

---

## Not Relevant / No Interview — Documented for Completeness

**Saranya Selvamani:** Uses Loveable, not Claude Code — not in target segment. No TLDR entry.

**Nick Bradford:** Interview never happened (research only — folder exists but no interview data). No TLDR entry.

**Esteban Lopez:** Interview never happened. No TLDR entry.

**Nemo Feng:** Somewhat not a good fit. No TLDR entry.

**Vipul & Smriti @ Echovane:** Folder contains only Luthien's internal interview guide template, no actual interview data. Cannot assess relevance. No TLDR entry.
