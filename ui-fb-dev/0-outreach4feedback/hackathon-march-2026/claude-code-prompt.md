# Claude Code Prompt: Hackathon Landing Page + Project Ideas

## Instructions

Read the attached context file `hackathon-context.md` first. It contains exhaustive research on the Apart Research AI Control Hackathon 2026 (March 20-22), Luthien's product, hackathon format, key infrastructure (ControlArena, SHADE-Arena, BashBench), and meeting notes from today's session with our Seldon advisor Finn Metz.

You have two tasks:

---

## Task 1: Brainstorm Hackathon Project Ideas

Generate 6-8 concrete project ideas that hackathon participants could build using Luthien Proxy as infrastructure. Each idea should:

1. **Map to a specific hackathon track** (Track 1: Control Setting Design, Track 2: Control Protocol Design, Track 3: Building Better Red Teams)
2. **Be achievable in a weekend** by a team of 2-4 people
3. **Use Luthien as a real component** (not just theoretical)
4. **Sound exciting to someone scanning a page in 10 seconds** -- short title + 2-sentence hook
5. **Connect to existing infrastructure** where possible (ControlArena, SHADE-Arena, BashBench, LinuxArena)

For each idea, provide:
- **Title** (catchy, specific)
- **Track** (1, 2, or 3)
- **One-liner** (what you'd build)
- **How Luthien fits** (1 sentence)
- **Bonus:** Which judge/speaker would find this most interesting and why

### Idea constraints
- At least 2 ideas should be achievable by someone with minimal AI safety background
- At least 2 ideas should be ambitious enough for experienced control researchers
- At least 1 idea should involve the LinuxArena track (Equistamp prizes)
- Avoid ideas that require Luthien features that don't exist yet (e.g., auto-retry loop is NOT yet implemented)

### What Luthien CAN do today
- Sit as proxy between any AI coding agent and model API
- Intercept and log all requests/responses
- Apply configurable policies: regex-based filters, dangerous command blocking, DLP, LLM-as-judge evaluation
- Block or flag responses that fail policy checks
- Full conversation history and audit trail
- Docker-based setup; works with Claude Code, Cursor, etc.

### What Luthien CANNOT do yet
- Auto-retry/resample loop (planned but not shipped)
- One-liner CLI install (coming soon)
- Polished policy configuration UI (being redesigned)
- Multi-agent coordination

---

## Task 2: Create Hackathon Landing Page

Create a single HTML file (hackathon.html) that serves as a bespoke landing page for hackathon participants. This will be deployed to `luthienresearch.github.io/luthien-pbc-site/hackathon/`.

### Design requirements

**Audience:** Hackathon participant who knows nothing about Luthien. Landed here from a Discord link. Probably has 3 other tabs open. Deciding in 30 seconds whether to use Luthien for their project.

**Tone:** Direct, slightly informal, not corporate. Two builders who care about AI safety, not a marketing team.

**Structure (in this order):**

1. **Hero** -- What Luthien is in one sentence. "Open-source proxy for AI control research" or similar. Include Jai's speaker/judge status as social proof.

2. **Why build on Luthien this weekend** -- 3-4 bullet points max. Why it's useful for THIS hackathon specifically. Connect to the hackathon tracks.

3. **Project ideas** -- The ideas from Task 1, presented as cards or a compact grid. Each card: title, track badge, 2-sentence description. This is the most important section per Finn's feedback: "give me 3-4 rough ideas that immediately spark a match in my brain."

4. **Quick start** -- Minimal: link to GitHub README, note that Docker is required, mention Jai's talk on Friday at noon for live demo/questions. NOT the full feedback flow (too much "work" per Finn).

5. **Get help** -- "Jai (speaker/judge) and Scott will be on the hackathon Discord all weekend. Tag @luthien or DM us." + link to book a call if they want setup help.

**What NOT to include:**
- The full feedback/screen-recording flow (save for post-hackathon)
- Long "about us" section
- Architecture diagrams
- Pricing or business model
- Anything that makes it feel like "work" to engage

**Technical requirements:**
- Single HTML file, no external dependencies beyond CDN fonts
- Mobile-responsive (hackathon participants on laptops but also phones)
- Dark mode compatible
- Clean, minimal CSS -- not over-designed
- No JavaScript required (static page)

**Reference the existing landing page style if possible:**
- Current prototypes are at https://luthienresearch.github.io/luthien-pbc-site/prototypes.html
- Keep consistent visual language where practical

---

## Context files to read

1. `hackathon-context.md` -- All research, hackathon details, meeting notes, infrastructure docs
2. The Luthien GitHub README at https://github.com/LuthienResearch/luthien-proxy#readme
3. The current feedback page at https://luthienresearch.github.io/luthien-pbc-site/feedback/

## Output

1. A markdown section with the 6-8 project ideas (formatted for easy copy-paste into the landing page)
2. The `hackathon.html` file ready to deploy

## Key quote to keep in mind

From Finn Metz (Seldon advisor, tested Luthien today):
> "If you could give me like three or four rough ideas that immediately spark a match in my brain of like 'oh this is so cool I could build on top of this', that would be great."

And from Jai Dhyani:
> "The leading call to action should be pitching it as a tool and/or a thing to build on as an open source project... People at hackathon are going to be by definition already time constrained."
