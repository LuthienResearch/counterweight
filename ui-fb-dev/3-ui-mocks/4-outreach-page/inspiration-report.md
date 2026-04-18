# Outreach Page Inspiration Report

**Date:** 2026-03-18
**Purpose:** Competitive analysis of how early-stage open source projects, dev tools, and AI safety research tools convert curious visitors into engaged testers, contributors, or hackathon builders. Intended to inform Luthien's outreach/landing page design.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Category 1: AI Safety Research Tools ("Try It & Tell Us What You Think")](#category-1-ai-safety-research-tools)
3. [Category 2: Hackathon Sponsor Pages ("Build On Us")](#category-2-hackathon-sponsor-pages)
4. [Category 3: Developer Tool Landing Pages (Early-Stage Conversion)](#category-3-developer-tool-landing-pages)
5. [Category 4: Apart Research Hackathon Sprint Pages](#category-4-apart-research-hackathon-sprint-pages)
6. [Category 5: AI Safety "Build On Us" Infrastructure Pages](#category-5-ai-safety-build-on-us-infrastructure)
7. [Cross-Cutting Patterns & Recommendations for Luthien](#cross-cutting-patterns)
8. [Sources](#sources)

---

## Executive Summary

After analyzing 20+ pages across AI safety tools, developer platforms, hackathon sponsors, and open source projects, several clear patterns emerge for converting visitors into engaged users:

**What works:**
- Zero-friction entry (no signup to try, `pip install` or `npx` one-liners)
- Problem-first framing ("As AI becomes more capable..." not "Our tool does X")
- Institutional trust signals upfront (logos, paper citations, user counts)
- Dual CTAs: "Start building" (action) + "Read docs" (learn more)
- Code snippets in the hero section showing 3-5 line getting started
- Clear "what you'll build" framing for hackathons

**What doesn't work:**
- Lead capture gates before showing value (email-first, demo-booking-first)
- Abstract descriptions without concrete examples
- Pages that are all styling/brand and no substance (several Framer-built sites)
- Jargon-heavy introductions that assume domain knowledge
- Burying the "try it" flow below the fold

**Most relevant to Luthien's situation:**
Luthien sits at the intersection of categories 1 and 5 -- an AI safety tool that wants developers to try it and give feedback, potentially as hackathon infrastructure. The best models are **Petri** (Anthropic), **ControlArena** (UK AISI + Redwood), and **Inspect AI** (UK AISI) for the "research tool seeking contributors" angle, and the **DeveloperWeek sponsor challenge format** for the "build on us at a hackathon" angle.

---

## Category 1: AI Safety Research Tools

### Petri (Anthropic)
- **URL:** https://www.anthropic.com/research/petri-open-source-auditing
- **GitHub:** https://github.com/safety-research/petri

**What they're asking visitors to do:** Try an open-source tool for automated AI safety auditing. Run multi-turn conversations with AI systems, score behavior across safety dimensions.

**How they introduce themselves:** Problem-first framing: "As AI becomes more capable and is deployed across more domains and with wide-ranging affordances, we need to evaluate a broader range of behaviors." They position Petri as solving a scaling problem that manual auditing can't handle.

**Trust signals:**
- Used in Claude 4 and Claude Sonnet 4.5 system cards
- Adopted by UK AI Security Institute pre-release
- Early adopters include MATS scholars and Anthropic Fellows
- Tested across 14 frontier models using 111 seed instructions
- Anthropic brand itself

**CTAs:**
- "Read the technical report" (learn more)
- "GitHub page" (try it)

**What works well:**
- Crystal-clear value prop: "Researchers provide seed instructions in natural language describing what they want to investigate, and Petri handles the rest in parallel"
- Named early adopters provide social proof
- Specific capability list (deception, sycophancy, power-seeking, etc.) makes it concrete
- Open-source approach invites community contribution

**What doesn't work:**
- No inline code snippet or quick-start on the page itself -- you have to click through to GitHub
- Research paper framing may deter practitioners who just want to try it
- No feedback mechanism mentioned (how do they want users to report findings?)

**Relevance to Luthien:** HIGH. Petri is an AI safety tool asking researchers to try it. Their problem-first framing and named early adopter approach is directly applicable.

---

### METR / Vivaria
- **URL:** https://metr.org/ and https://vivaria.metr.org/

**What they're asking visitors to do:** Use Vivaria to run AI evaluations, or use their newer recommended tool Inspect AI.

**How they introduce themselves:** "A research nonprofit that scientifically measures whether and when AI systems might threaten catastrophic harm to society."

**Trust signals:**
- Partnership logos: OpenAI, Anthropic, Amazon, AISI
- "METR does not accept compensation for this work" (independence signal)
- Press coverage: Nature, Financial Times, MIT Technology Review
- Published evaluation reports dating to 2023

**CTAs:**
- "Read paper" and "View repo" for research
- Newsletter subscription via Substack
- Docker Compose tutorial for Vivaria

**What works well:**
- Partnership logos immediately establish credibility
- Independence claim ("does not accept compensation") builds trust
- Vivaria docs are straightforward and technical

**What doesn't work:**
- Vivaria is being deprecated ("Transitioning to Inspect"), which creates confusion
- No inline quick-start -- directs to Docker Compose tutorial
- Homepage is research-focused, not tool-adoption-focused
- No clear "here's what you can build with this" framing

**Relevance to Luthien:** MEDIUM. The trust signal approach (logos, independence) is useful. The deprecation confusion is a cautionary tale about signaling tool maturity.

---

### Redwood Research
- **URL:** https://www.redwoodresearch.org/

**What they're asking visitors to do:** Explore their research, read publications, consider careers.

**How they introduce themselves:** "A nonprofit AI safety and security research organization" focused on risks from AI systems that "purposefully act against the interests of their developers."

**Headline:** "Pioneering threat assessment and mitigation for AI systems"

**Trust signals:**
- Named partnerships: Anthropic, Google DeepMind
- UK AISI collaboration
- ICML oral presentations
- 501(c)(3) nonprofit status

**CTAs:** "Our Research" (primary), "View All Research", "Read the full case study", career links.

**What works well:**
- Clean, authoritative presentation
- Specific named collaborations build credibility
- Clear research area descriptions (AI Control, Strategic Deception, Applied Consulting)

**What doesn't work:**
- No tool adoption CTA at all -- purely a research showcase
- No "try our tools" or "build with our infrastructure" framing
- Feels like an academic department page, not a developer platform

**Relevance to Luthien:** LOW for direct page structure, but their framing of AI Control as a research area is useful context.

---

## Category 2: Hackathon Sponsor Pages

### DeveloperWeek 2026 Hackathon Sponsor Challenges
- **URL:** https://developerweek-2026-hackathon.devpost.com/

This is the gold standard for "build on us" framing at hackathons. Each sponsor follows a consistent pattern.

**Common sponsor challenge structure:**
1. Challenge title with prize amount
2. One-line pitch positioning tool as infrastructure
3. What to build (specific enough to guide, open enough to inspire)
4. Requirements (meaningful API integration required)
5. Resources (free accounts, starter templates, docs links)
6. Judging criteria
7. Submission format (repo + demo video + brief explanation)

**Best examples from DeveloperWeek 2026:**

**Kilo ($4,000):** "Build an open source developer tool -- or create something that improves Kilo itself." Positions their tool as both infrastructure AND an invitation to contribute to the tool itself. This is closest to what Luthien might want.

**Deepgram ($2,000):** Two separate challenges -- one for analysis ("Smart Listener") and one for building ("Voice Operator"). This dual-track approach lets participants choose their comfort level.

**Sanity + AI ($1,000):** "Build a feature only structured content makes possible." This is clever framing -- it forces participants to think about what the tool uniquely enables rather than generic integration.

**Foxit ($1,000):** "Build anything you want -- as long as you use both Foxit Document Generation and Foxit PDF Services APIs." Maximum creative freedom with minimum integration requirements.

**What works well across all sponsor challenges:**
- Specific prize amounts create urgency
- Free API credits/accounts remove friction
- Starter repos and docs links are always provided
- Submission format is standardized (repo + video + writeup)
- Judging criteria are transparent

**What doesn't work:**
- Some challenges are too vague ("build something innovative")
- Some require too many specific APIs, which constrains creativity
- Contact info is sometimes just an email, no Discord/Slack community

**Relevance to Luthien:** VERY HIGH. If Luthien sponsors a hackathon (e.g., Apart Research's AI Control Hackathon), this is exactly the format to follow. The Kilo and Sanity examples are closest to Luthien's situation.

---

### Anthropic London Hackathon
- **URL:** https://anthropiclondon.devpost.com/

**What they asked:** "Build a Claude 2-enabled app that is relevant to Anthropic's mission, useful for startups and businesses, and good for the world."

**Trust signals:**
- $30,500 in prizes
- 145 participants
- Judges from Anthropic, Sequoia, Balderton, MongoDB, Brave, Weaviate

**What works well:**
- Clear mission alignment requirement ("relevant to Anthropic's mission")
- Named judges from prestigious organizations
- Three example project categories (government transparency, business assistance, misinformation detection) give direction without constraining

**Relevance to Luthien:** MEDIUM. The mission-alignment framing is useful -- Luthien could require projects to be "relevant to AI control/safety."

---

### WeaveHacks (Weights & Biases)

**What they do:** W&B hosts themed hackathons at their SF office (e.g., "Self-Improving Agents," "Agent Protocols") with Google Cloud as co-sponsor.

**Prizes:** Grand Prize $4,000 + robot dogs (~$8,500 value), category prizes with Claude Max subscriptions.

**What works well:**
- Themed hackathons create focus
- Physical location (SF office) builds community
- Fun/memorable prizes (robot dogs) generate buzz

**Relevance to Luthien:** MEDIUM. The themed approach could work for Luthien ("AI Control Hackathon" with Luthien as infrastructure).

---

## Category 3: Developer Tool Landing Pages

### CodeRabbit
- **URL:** https://www.coderabbit.ai/

**Headline:** "Cut code review time & bugs in half Instantly."
**Subheadline:** "Reviews for AI-powered teams who move fast (but don't break things)"

**Trust signals:**
- "2M repositories" and "75M defects found"
- "Most installed AI App" on GitHub
- Jensen Huang quote: "We're using CodeRabbit all over NVIDIA"
- SOC 2 Type II, zero data retention, end-to-end encryption

**CTAs:** "Try it for free" (primary), "See a sample review" (secondary)

**Getting started flow:**
1. Free trial, no credit card
2. "2-click install" on GitHub/GitLab
3. Available in Git, IDE (VS Code), and CLI

**What works well:**
- Outcome-focused headline (cut time & bugs in half)
- "2-click install" removes perceived friction
- Jensen Huang testimonial is a conversation-stopper
- "See a sample review" lets visitors evaluate before committing
- Free forever for open source

**What doesn't work:**
- Enterprise-focused messaging may not resonate with individual developers
- Dense page with many sections -- could overwhelm

**Relevance to Luthien:** MEDIUM. The "See a sample review" concept maps to "See a sample policy in action" for Luthien. The free-for-open-source model is worth considering.

---

### Qodo (formerly Codium)
- **URL:** https://www.qodo.ai/get-started/

**Headline:** "Smarter reviews. Better code."

**Trust signals:**
- Logos: Intel, Walmart, Intuit, Box
- "2M+ installations" and "4M+ PRs reviewed every year"
- Gartner report download
- AI model partnerships: Anthropic, OpenAI, Google

**Three entry points:**
1. Git Integration (most popular) -- "AI-powered PR reviews with built-in workflow automation"
2. IDE Plugin -- "Catch issues before commit"
3. CLI Tool & MCP/API -- "Custom agent creation"

**What works well:**
- Multiple entry points let developers choose their workflow
- "Most popular" badge guides uncertain visitors
- Installation metrics (841K VS Code, 610K JetBrains) provide social proof per platform

**What doesn't work:**
- "Book a Demo" as a co-primary CTA adds friction
- Competitive benchmark claim ("Qodo Outperforms Claude Code") may feel aggressive

**Relevance to Luthien:** LOW-MEDIUM. The multiple entry points concept is interesting but Luthien is too early for this.

---

### OpenCode
- **URL:** https://opencode.ai/

**Headline:** "The open source AI coding agent"
**Subheadline:** "Free models included or connect any model from any provider"

**Trust signals:**
- "120K GitHub Stars, 800 Contributors, 5M Monthly Devs"
- "10,000+ commits"
- Privacy: "does not store any of your code or context data"

**Getting started:** Download via curl or desktop app. Browse docs. Connect any LLM provider or use free models.

**What works well:**
- Massive open-source community numbers are compelling
- Privacy commitment addresses key developer concern
- Multiple interfaces (terminal, desktop, IDE) meet developers where they are

**Relevance to Luthien:** LOW. Different product category, but the privacy commitment framing is useful.

---

### Portkey AI Gateway
- **URL:** https://github.com/Portkey-AI/gateway

**Headline:** "Route to 250+ LLMs with 1 fast & friendly API"

**Trust signals:**
- 11K GitHub stars, 943 forks
- "Battle tested, with over 10B tokens processed everyday"
- MIT license
- AWS EC2 one-click deploy button

**Getting started (3 steps):**
1. `npx @portkey-ai/gateway` (single command)
2. Python code example (OpenAI-compatible)
3. Config example for routing & guardrails

**What works well:**
- Single-command install is the gold standard
- OpenAI-compatible API reduces learning curve
- "Battle tested" language with specific numbers (10B tokens/day)
- Multiple deployment options (Cloud, Docker, Node, Cloudflare, Replit)

**What doesn't work:**
- GitHub README format is developer-friendly but not a marketing page
- No problem framing -- goes straight to features

**Relevance to Luthien:** HIGH. Portkey is a direct competitor/adjacent tool (LLM gateway with guardrails). Their README structure and single-command install pattern is directly applicable. Luthien already has `luthien onboard` which is similar.

---

## Category 4: Apart Research Hackathon Sprint Pages

### Apart Research Sprints Overview
- **URL:** https://apartresearch.com/sprints

**Format:** Monthly hackathons (called "sprints") where participants collaborate on AI safety research worldwide. 55+ sprints with 6,000+ participants across 200+ global locations.

**What they provide:**
- Keynote talks and technical workshops
- Code starters, ideas, and inspiration
- Mentors via Discord (office hours + drop-in help)
- Expert researchers available throughout
- Resources tab with curated reading list organized by track

**Prizes:** Vary by hackathon ($2,000 to $10,000 in cash). Top projects featured on Apart website. Outstanding work may be invited for further development, publication, or presentation.

**Post-hackathon support:** Apart Lab Fellowship provides mentorship, publication help, and funding.

### AI Control Hackathon 2026
- **URL:** https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22

**Dates:** March 20-22, 2026
**Co-organizer:** Redwood Research (founded the field of AI control)
**Sponsor:** Equistamp

**What participants will do:** "Develop novel control protocols, build evaluation tools, and stress-test existing safety measures using infrastructure like ControlArena and SHADE-Arena."

**What works well:**
- Co-organized with the group that founded the field (massive credibility)
- Named infrastructure tools (ControlArena, SHADE-Arena) give concrete starting points
- Multiple global locations lower barriers
- Teams form at event start (solo participants welcome)
- Can join mid-sprint

**What doesn't work:**
- Framer-built pages don't render well for web scrapers (content is JS-loaded)
- No inline code example or quick-start
- Relies heavily on Discord for real-time support (ephemeral, not searchable)

**Relevance to Luthien:** VERY HIGH. This is exactly the kind of hackathon where Luthien could position itself as infrastructure. The March 20-22 dates are imminent. Key question: could Luthien be pitched as a tool participants use alongside ControlArena/SHADE-Arena?

---

## Category 5: AI Safety "Build On Us" Infrastructure

### ControlArena (UK AISI + Redwood Research)
- **URL:** https://control-arena.aisi.org.uk/
- **GitHub:** https://github.com/UKGovernmentBEIS/control-arena

**Headline:** "A library for running AI Control experiments"

**How they introduce themselves:** "The field of AI Control aims to design and evaluate control protocols. Control protocols are plans designed to prevent unsafe actions by AI systems, even if those AIs were misaligned."

**Getting started flow:**
1. `pip install control-arena`
2. Install Docker for sandboxing (optional)
3. Install VSCode extension (optional)
4. Run provided code example
5. View results via `inspect view`

**Trust signals:**
- UK AI Security Institute + Redwood Research
- Logos: Google DeepMind, Anthropic, MATS program
- Built on Inspect AI framework
- Academic paper citation (arXiv:2312.06942)

**CTAs:** Install via pip, explore tutorial, join Slack community (`control-arena-discussion`), review examples

**What works well:**
- `pip install` one-liner is frictionless
- Slack community provides ongoing engagement channel
- Tutorial + glossary supports newcomers
- Pre-built settings mean you can run something meaningful immediately
- Clear institutional backing without being bureaucratic

**What doesn't work:**
- "Introduction to control" page assumes you need background reading before trying
- No "here's what you can build" framing
- Documentation-heavy rather than outcome-oriented

**Relevance to Luthien:** VERY HIGH. ControlArena is the closest analogy to what Luthien does -- it's AI control infrastructure for researchers. Their approach (pip install, Slack community, tutorial) is directly applicable. Key difference: Luthien targets working developers, not just researchers.

---

### Inspect AI (UK AISI)
- **URL:** https://inspect.aisi.org.uk/
- **GitHub:** https://github.com/UKGovernmentBEIS/inspect_ai

**Headline:** "An open-source framework for large language model evaluations"

**Getting started flow:**
1. `pip install inspect-ai`
2. Install VS Code extension
3. Get model API credentials
4. Write or use pre-built evaluations
5. Run via CLI: `inspect eval [file] --model [provider]`
6. View results in browser-based log viewer

**Trust signals:**
- UK AI Security Institute
- 100+ external contributors
- 100+ pre-built evaluations
- BibTeX citation for academic credibility

**What works well:**
- "100+ pre-built evaluations ready to run" is a killer feature claim
- VS Code extension recommendation shows they care about developer experience
- Open contribution model ("If you put effort into a pull request, they will work with you to get it merged")
- Clean, documentation-site aesthetic (not a marketing page)

**What doesn't work:**
- Purely functional presentation -- no emotional or mission-driven hook
- No community engagement channel prominently featured
- No "here's a real-world problem this solves" framing

**Relevance to Luthien:** MEDIUM. The documentation-as-landing-page approach works for mature tools but may not be right for Luthien's current stage. The contribution invitation language is worth borrowing.

---

### Invariant Labs (now acquired by Snyk)
- **URL:** https://invariantlabs.ai/guardrails

**Headline:** "Invariant Guardrails" -- "a next-generation security platform for agentic AI and MCP systems"

**CTA:** "Sign up now for early access"

**What works well:**
- Snyk acquisition provides massive credibility signal
- Early access framing creates exclusivity

**What doesn't work:**
- Email gate before any product access
- Minimal page content -- no code examples, no demo, no documentation
- "Early access" without showing what you're getting access to

**Relevance to Luthien:** LOW. This is a cautionary example -- gating everything behind email capture before showing value is the opposite of what works for developer tools.

---

### SafeBench (Center for AI Safety + Schmidt Sciences)
- **URL:** https://www.mlsafety.org/safebench

**Headline:** "$250,000 in prizes for ML Safety benchmarks"

**What they asked:** Develop benchmarks assessing AI safety across Robustness, Monitoring, Alignment, or Safety Applications.

**Conversion flow:** Visitor -> email signup -> review ideas -> study guidelines -> submit benchmark -> judging -> winner announcement

**Trust signals:**
- $250,000 prize pool (Schmidt Sciences)
- Named judges from Carnegie Mellon, University of Chicago, Center for AI Safety
- ~100 submissions received

**What works well:**
- Prize money is the headline -- immediately grabs attention
- "View example ideas" CTA lowers the barrier to starting
- Clear judging criteria and timeline
- Requirement that code/datasets be public on GitHub ensures community benefit

**What doesn't work:**
- Competition format limits ongoing engagement (one-time event)
- Academic framing may deter practitioners

**Relevance to Luthien:** MEDIUM. The "example ideas" approach could work for Luthien -- showing specific policies or control scenarios visitors could build.

---

## Cross-Cutting Patterns

### What the Best Pages Have in Common

**1. Zero-to-running in under 60 seconds**
The most effective pages get visitors to a working state immediately:
- `pip install control-arena` (ControlArena)
- `npx @portkey-ai/gateway` (Portkey)
- "2-click install" (CodeRabbit)
- `curl` one-liner (OpenCode)

Luthien already has `luthien onboard` -- this should be prominently featured.

**2. Problem-first, not tool-first**
Best pages lead with the problem, not the product:
- "As AI becomes more capable..." (Petri)
- "Cut code review time & bugs in half" (CodeRabbit)
- "AI Control aims to prevent unsafe actions by AI systems" (ControlArena)

Luthien should lead with: "AI coding agents are writing your code unsupervised. What rules are they following?"

**3. Dual CTAs: Act Now + Learn More**
Every effective page offers two paths:
- "Start building" + "Read docs" (Anthropic)
- "Try it for free" + "See a sample review" (CodeRabbit)
- "Install" + "Tutorial" (ControlArena)

Luthien should have: "Try the proxy" + "See how it works"

**4. Named users / institutional logos**
Even early-stage tools name their early adopters:
- "MATS scholars, Anthropic Fellows, and UK AISI" (Petri)
- "OpenAI, Anthropic, Amazon, AISI" (METR)
- "Google DeepMind, Anthropic, MATS" (ControlArena)
- Jensen Huang quote (CodeRabbit)

Luthien should name any teams or individuals using the proxy, even if the list is short.

**5. Community channel prominently featured**
- Slack: ControlArena (`control-arena-discussion`)
- Discord: Apart Research hackathons
- GitHub Issues/Discussions: Most open source tools

Luthien should feature its community channel (Discord? Slack? GitHub Discussions?).

**6. Hackathon sponsor pages follow a template**
Every successful sponsor challenge includes:
1. Prize amount
2. One-line tool pitch
3. What to build
4. Integration requirements
5. Free resources/credits
6. Judging criteria
7. Submission format

If Luthien sponsors the Apart Research AI Control Hackathon (or similar), follow this template exactly.

### What Doesn't Work

**1. Email gates before showing value**
Invariant Labs requires signup before any product access. This kills developer trust. Always show value first.

**2. Abstract descriptions without examples**
"A next-generation security platform" tells you nothing. "Run this command and see your agent's behavior scored across 7 safety dimensions" tells you everything.

**3. Documentation-only pages for early-stage tools**
Inspect AI's pure-documentation approach works because they have 100+ evaluations and 100+ contributors. At Luthien's stage, an outcome-oriented page works better.

**4. Deprecation notices on landing pages**
Vivaria's "Transitioning to Inspect" notice undermines confidence. If you're evolving, frame it as growth, not abandonment.

### Recommendations for Luthien's Outreach Page

**Hero Section:**
- Problem statement: "AI coding agents write code unsupervised. What rules are they following?"
- One-line value prop: "Luthien is an open-source proxy that enforces policies on AI agent traffic"
- Dual CTA: "Try it now" (links to quick start) + "See it in action" (demo/video)
- Trust signals below: any logos, user counts, or named users

**Quick Start Section:**
- Show the `luthien onboard` one-liner
- 3-step getting started (install -> configure policy -> run)
- Link to example policies

**"What You Can Build" Section (for hackathon/builder audience):**
- 3-4 concrete project ideas with difficulty levels
- Example: "Build a policy that prevents your coding agent from modifying auth files"
- Example: "Create a monitor that alerts when an agent makes >50 file changes in one session"
- Link to policy architecture docs

**Social Proof Section:**
- Named early users/testers
- GitHub stars count
- "Built by" team credentials (Jai's AWS/Meta background, nonprofit mission)

**Feedback Section:**
- "We're building this for developers like you. Tell us what's missing."
- Link to structured feedback form or GitHub Discussions
- Specific questions: "What policies would you want?" "What's your biggest concern about AI agents?"

**For Hackathon Sponsor Page (if sponsoring Apart Research or similar):**
- Follow the DeveloperWeek template exactly
- Prize amount prominently displayed
- "Build a Luthien policy that [specific challenge]"
- Free proxy access + API credits
- Starter repo with example policies
- Submission: GitHub repo + 3-min demo video + policy description
- Judging: creativity, real-world applicability, technical execution

---

## Sources

### AI Safety Research Tools
- [Petri (Anthropic)](https://www.anthropic.com/research/petri-open-source-auditing)
- [METR](https://metr.org/)
- [Vivaria](https://vivaria.metr.org/)
- [Redwood Research](https://www.redwoodresearch.org/)
- [ControlArena](https://control-arena.aisi.org.uk/)
- [ControlArena GitHub](https://github.com/UKGovernmentBEIS/control-arena)
- [SHADE-Arena](https://control-arena.aisi.org.uk/settings/shade_arena.html)
- [Inspect AI](https://inspect.aisi.org.uk/)
- [Inspect AI GitHub](https://github.com/UKGovernmentBEIS/inspect_ai)
- [SafeBench](https://www.mlsafety.org/safebench)
- [Invariant Labs](https://invariantlabs.ai/guardrails)

### Hackathon Pages
- [DeveloperWeek 2026 Hackathon](https://developerweek-2026-hackathon.devpost.com/)
- [Anthropic London Hackathon](https://anthropiclondon.devpost.com/)
- [Apart Research Sprints](https://apartresearch.com/sprints)
- [AI Control Hackathon 2026](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22)
- [Apart Research Ultimate Guide to AI Safety Hackathons](https://apartresearch.com/news/the-ultimate-guide-to-ai-safety-research-hackathons)
- [WeaveHacks (W&B)](https://weavehacks-1.devpost.com/)
- [Anthropic Build with Claude](https://www.anthropic.com/learn/build-with-claude)

### Developer Tool Landing Pages
- [CodeRabbit](https://www.coderabbit.ai/)
- [Qodo Get Started](https://www.qodo.ai/get-started/)
- [OpenCode](https://opencode.ai/)
- [Portkey AI Gateway (GitHub)](https://github.com/Portkey-AI/gateway)

### Developer Landing Page Research
- [Evil Martians: We studied 100 dev tool landing pages](https://evilmartians.com/chronicles/we-studied-100-devtool-landing-pages-here-is-what-actually-works-in-2025)
- [Markepear: Dev tool landing page examples](https://www.markepear.dev/examples/landing-page)
