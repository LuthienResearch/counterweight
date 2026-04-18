# Value Proposition / README — User Feedback Log

> Modeled after [3.1-policy-config-feedback.md](3.1-policy-config-feedback.md)

## Assets & Permalinks

### README versions evaluated
- [x] **Current README on `main`** — developer reference, "Luthien Control" heading. [Permalink](https://github.com/LuthienResearch/luthien-proxy/blob/af3e819/README.md). Shown to Zac (Jan 27).
- [x] **`docs/landing.html`** — dark-theme HTML landing page draft, "AI Safety for Production Agents". On `value-prop` branch.
- [x] Option A: Problem-first — [readme-option-a-problem-first.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-a-problem-first.md)
- [x] Option B: Visual flow — [readme-option-b-visual-flow.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-b-visual-flow.md)
- [x] Option C: Use-case-first — [readme-option-c-use-case-first.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-option-c-use-case-first.md)

### Zac session (Jan 27) recording
- [x] Otter.ai transcript: `/Users/scottwofford/Downloads/Zac, Jai & Scott_otter_ai_Jan27.txt`

### Session 1 (Super Bowl) recording
- [x] Otter.ai transcript: `/Users/scottwofford/Downloads/superbowl demo_otter_ai.txt`
- [ ] Google Drive notes folder: [link](https://drive.google.com/drive/folders/11AYSxrb_5mC2xUZYg8XojVeLVVPANTZv?usp=drive_link)

### Internal session (Jai, Feb 5) recording
- [x] Gemini notes: `/Users/scottwofford/Downloads/Jai's feedback on value prop  - 2026_02_05 13_56 PST - Notes by Gemini.md`

### Session 9 (Claude simulated review) source
- [x] Full report (local): [claude-qa-trial-report-2026-02-25.md](claude-qa-trial-report-2026-02-25.md)
- [x] Google Drive copy: [_User-Interview-Notes/claude/](https://drive.google.com/file/d/1H5ju6NgUSvEff4ElrA_1z2bjW0CJmcLC/view?usp=sharing)

### Session 13 (Paolo onboarding) source
- [x] Voice memo transcript (local): `~/Downloads/paolo-scott-march-3-transcript.md`
- [x] Gemini notes + raw materials: [Google Drive folder](https://drive.google.com/drive/folders/1MPmvqqIXWp3M03yUCCukEKpiNr4u8kNs)

### Session 14 (Mike Mantell) source
- [x] Otter.ai transcript: `Rxaj9ooSUMjjDZneNmn34QoXHEk`
- [x] Gemini notes: GDrive `Scott (Mike Mantell) - 2026/03/04 15:00 PST`

### Session 15 (Maria + Jesse) source
- [x] Otter.ai transcript: `QUGpSuDQI8AaEhnGOGUSKZsuh9A`
- [x] Gemini notes: GDrive `m & j - 2026/03/04 09:45 PST`
- [x] Google Doc: `1LZkC3YalrnBhUdULHEIOHmPpUP107U7s4NTN0FITipI`

### Landing page context doc
- [x] Compiled context (Feb 5): `/Users/scottwofford/Downloads/drive-download-20260209T062034Z-1-001/Copy of luthien-landing-page-context.md`

---

## Session 0: Zac Saber (reacting to current README on `main`)

- **Date:** Jan 27, 2026
- **Forum:** In-person at Mox, SF (same day as policy config Session 1)
- **Attendees:** Scott Wofford, Jai Dhyani, Zac Saber
- **CX version:** Current README.md on `main` — developer reference format. Headings: Quick Start → Use Claude Code → Log In to Admin UI → Monitor Activity → Select a Policy → Architecture → Admin API → Policy System → Troubleshooting.

### README / value prop feedback

1. **"I'm closing the tab."** On seeing the launch script approach: "If I open this GitHub, I'm like, Okay, I have to launch it with this. I'm closing the tab." Wanted to just set env vars, not run a special script.

2. **Features are buried.** "I want to know what's the epic shit I can do with your product. Then at the end, have a bit like, oh, how do you get started?" Current order is backwards — setup first, features last.

3. **"Creating my own policy" was the hook — but buried.** "I'm way more interested in creating my own policy. As soon as I saw this, I was like, Okay, this is cool. I would consider using this, but it's all the way down here. I had to be like, Oh, I don't care about any of this... Oh, okay, this is cool. That was like the progression of my interest."

4. **"You guys should play this up a lot more."** Re: custom policies. "Have some dramatic, like, picture or something." Jai agreed: "This document is just very much not written as a pitching document."

5. **Emphasize that you keep your own Claude Code.** "Probably emphasize that I can use my own Claude Code, because as soon as I see this [launch script], if I have a custom Claude Code, this is completely unusable." Most power users have custom setups.

6. **Env vars > scripts.** "I set env variables all the time. Just tell me that — that would be even better than having some script, because I would feel way more comfortable."

7. **Wants to know what Docker spins up.** "If you guys are pulling a Docker container, sometimes I like to launch this first and then come back later. Maybe just say 'this is gonna spin up a Docker container.'"

8. **Port conflicts matter.** "You should definitely tell me which port it's using... if I have stuff running already, I can change it."

9. **Public base URL would change everything.** "If we could just choose to wrap stuff to your base URL when we want to, we can just start using you guys." Hosted endpoint would dramatically lower friction. (This became Jai's "one-click cloud deploy" idea.)

10. **"If your user wants to try your product, the trying should be the easy bit."** Core philosophy: "If they get hung up on the trying bit, it sucks for everyone involved."

### Broader context from this session

- Zac and Jack were building their own product at Counterweight and considering using Luthien as infrastructure
- Zac's use case: route skill invocations to different models, deterministic evaluation, LLM judge
- Mom Test recommendation: "Have you guys read the Mom Test? Changed my life."
- Zac was willing to self-host but didn't realize that was an option from the README

---

## Session 1: Chris Porter + Beth Anne Porter

- **Date:** Feb 8, 2026 (Super Bowl Sunday)
- **Forum:** In-person, Super Bowl party
- **Attendees:** Scott Wofford, Chris Porter, Beth Anne Porter
- **Chris:** L7 PMT at Amazon — works on custom LLM / next-token prediction model for predicting next customer action
- **Beth Anne:** L7 at Amazon — manages ~30 people working on internal product management AI tools + Buy with Prime
- **Format:** Walked through Options A → B → C in order. Scott showed a demo video of Luthien blocking a dangerous command in Claude Code.

### Option A reactions (Problem-first)

1. **Bold tagline didn't land.** Chris: "I read it like two times, and I still didn't get it. I was like, Cool, drop in."

2. **"Could be even simpler."** Chris: "There's probably like some simpler way to say what it does." Noted he's coming at it as a PM whose SDEs might use this.

3. **Beth Anne got the problem.** After scrolling to the problem table: "Okay, I got the problem." The before/after table of "what you asked vs what the agent did" worked.

4. **But couldn't clock the danger.** Beth Anne: "I'm supposed to see what the agent did. There's something wrong there, but I can't clock it because I'm not [a developer]." The `rm -rf` example requires developer context.

5. **"How does it understand what's dangerous?"** Beth Anne's first question: "Is that like consistent across every user, or is it specific to my business?"

6. **Wants universal + customizable.** Beth Anne: "I would want someone to tell me, hey, there's a shit ton that everyone gets wrong and these are really dangerous things, and we take care of that. And then there's stuff that's specific to your business that you can tell us."

7. **Chris wants visual, not terminal text.** "I want it to be visual rather than pure text, terminal text."

8. **Chris wants to try it without downloading.** "I kind of want to play around with it, even maybe like without even me downloading."

### Option B reactions (Visual flow)

9. **Strong positive from both — immediate understanding.** Beth Anne: "I like this way better. I like, now I get it." Chris: "I like this." / "I like the visual more."

10. **Visual answered "how it works."** Beth Anne: "I was also wondering how it works before."

11. **But wants to see the actual UI.** Beth Anne: "I don't know what the UI looks like, and so I'm like trying to envision that."

12. **Unclear what happens next.** Beth Anne: "Violated. Do I have to take an action?"

13. **Examples are good, code is too technical.** Chris: "I like these examples. The examples themselves underneath it again, are just like too technical for me."

### Option C reactions (Use-case-first)

14. **Best intro of the three.** Scott: "This is like the best intro we've seen so far." Beth Anne: "Makes more sense than the ones before."

15. **"Pick your policy" confused Beth Anne.** "I don't quite understand what pick your policy means."

16. **PII use case resonated strongly.** Beth Anne: "PII is really good. So I would just put that as an example... just make it more like, set into, like, a real use case." This was the moment she connected Luthien to her own work.

17. **Package safety / dependency verification.** Beth Anne: "I constantly worry about... code packages... I have no idea if I like put this code package down... is it legit?" Suggested Luthien monitor top 500 packages and flag unknown ones.

18. **pip vs uv resonated.** Scott explained the pip→uv pain point. Beth Anne: "I have specific requirements on how and what to install on my machine. That should be a rule."

19. **"Who it's for" should be higher.** Beth Anne: "Maybe even put this a little higher up." Her reaction: "I'm going to stop reading, but I'm going to send it to my PE to see if this is something that could help with our PII data."

20. **"It's not tailored enough to my use case yet."** Beth Anne's summary: "I like this idea. It's just it's not tailored enough to my use case yet. And I think you should think about that, because you're going to have really technically advanced people who are not coders."

### Broader observations

- **Non-developer perspective matters.** Beth Anne is L7 managing 30 engineers and uses Claude Code herself. She represents a "technical PM" persona that's distinct from the "senior SDE" persona.
- **Forward behavior.** Beth Anne would forward to her engineers — "I'm going to send it to my PE." This is the PM-as-champion path.
- **Chris as PM buyer.** Chris is evaluating whether to recommend to his SDEs. Wants simpler language and interactive demos.

---

## Internal session: Jai Dhyani (co-founder feedback on Options A/B/C)

- **Date:** Feb 5, 2026
- **Forum:** Google Meet (Scott + Jai standup)
- **Context:** Jai reviewed the same three README options before they were shown to external users. This session shaped the approach for the Super Bowl demo.

### Strategic direction

1. **GitHub README IS the landing page.** Jai: "The GitHub repo is always going to be a de facto landing page... trying to maintain two landing pages is hard, as we've made that mistake." Don't build a separate website.

2. **Demo video/screenshot should do most of the work.** Jai: "I want the demo to do most of the work." Show Claude Code with Luthien injecting text: "The agent wanted to run X but because of your rules, we did Y instead."

3. **Lead with example, then name the category.** Jai pushed back on leading with a bulleted problem list: "Leading with an example and then naming the category often works better." Show pip→uv or rm-rf, THEN say "control what your agent does."

4. **Describe value before shape.** On "drop-in proxy for AI coding agents": "It's accurate but on first seeing that it's not immediately intuitively obvious to everyone what that means. First we describe the value and then we describe the shape of it."

5. **"Without changing anything about your development environment"** — Jai preferred this framing over "without changing your code." The value prop is: use your exact same setup.

### Tagline space

6. **Tagline candidates from Jai:**
   - "Make Claude Code actually listen to your rules"
   - "Make Claude Code follow your rules"
   - "Rules that Claude can't ignore"
   - "Keep Claude Code on track"

### Onboarding vision

7. **One-click cloud deploy is the simplest onboarding.** Jai: "You press a button, specify some rules, you now have an endpoint, you now have a command to launch Claude or Codex." Options: text box for rules, or drag CLAUDE.md file. Railway is abstracted away — users don't care about infra.

8. **Pass-through auth reduces friction.** Jai: "Supporting just a pass-through authentication makes sense. It's probably not that much work and makes onboarding much easier."

9. **"Try in browser" is too much work and may confuse.** Jai: "Getting the UX to be intuitive — people understanding what's happening and which part is our product — is a lot to communicate." But the instinct to make it easy to try is correct.

### What NOT to include on the landing page

10. **Don't show SaaS/management UI on the README.** Jai: "That's like a next month problem at the earliest... right now our main bottleneck is just getting feedback."

11. **Don't tie too much to terminal.** Jai: "We're probably past peak terminal usage in terms of how we interact with LLMs." UIs communicate information faster — "humans learn best with pictures."

### Alignment on communication pattern

12. **Problem category = "agents doing things you don't want."** Both agreed: the core category is "I specified a thing, the agent did the opposite." Two subcategories: (a) violated CLAUDE.md rules, (b) went beyond prompt scope.

13. **Keep it concise and visual.** Jai: "I want to think about things that can be communicated very quickly in an image or short video. [Other value props] require a lot of context."

---

## Session 2: Bahar Erar

- **Date:** Feb 8, 2026 (Super Bowl Sunday)
- **Forum:** In-person, Super Bowl party
- **Attendees:** Scott Wofford, Bahar Erar
- **Bahar:** Former Amazon Applied Scientist — worked on seller-facing AI tools (seller assistant). Managed AI safety/policy compliance at enterprise scale (millions of conversations). Left Amazon ~6 months prior. Has PTSD from AI hype cycle at Amazon. Not currently working in AI.
- **Format:** Started with Option C intro → then Option A problem section → back to Option C "Write your own" section → live demo of pip-block policy in terminal. Also watched the Luthien blocking demo video.
- **Recording:** Otter.ai transcript: `/Users/scottwofford/Downloads/superbowl demo v2_otter_ai (1).txt`

### Option C intro reactions

1. **Got the concept from the intro.** "It sits between my AI coding engine... it intercepts. So does that mean when it finds dangerous stuff or red flags, it flags things for me so I can review?"

2. **Liked that it auto-retries.** "It blocks it and maybe gets the agent to retry without it first, so maybe it doesn't even need my intervention. It just makes it safe in the backend." Then: "That's cool, because this stuff just has so many false positives."

3. **"How does it know the current task scope?"** First technical question — wants to understand the mechanism for scope detection.

### Option A problem section reactions

4. **Scope creep example resonated.** After Scott explained the "fix login bug → agent refactors unrelated files" example: "Which is absolutely possible with a normal human developer." She got it immediately.

5. **Don't just block — suggest alternatives.** "If there is a way to also say: hey, actually, I've blocked this because it was doing X. But actually, if it did that, maybe it could have done Y. But I just want to check with you... here are the ramifications." Balance enforcement with not losing the debugging/discovery value.

### Option C "Write your own" reactions

6. **"Too rudimentary."** "This is good, but honestly I think it is too rudimentary this way, because the problem usually of setting these policies is not to define it — but to test it against all the different edge cases, and then actually refining the policy is the hardest part."

7. **Analogy: "I'm not gonna allow drunk people."** "Everybody can say 'I'm not gonna allow drunk people.' How do you define that?" Writing the policy statement is easy; operationalizing it is the hard part.

### Enterprise AI safety perspective

8. **"LLM-as-judge is already common."** "A lot of enterprise scale applications are doing LLM as a judge themselves... your clients can just go and have the LLM as a judge built into their backend." Challenge to Luthien: how are you different from what teams already build internally?

9. **Domain-specific rules are the hard part.** "When I was working on my team, what I want to focus on is the things that are unique to our space — because those are the hardest things. Foundation models can solve the fundamental thing, but they're not going to focus on seller reputation." Luthien should handle the fundamentals so teams can focus on domain-specific rules.

10. **Seller review manipulation example.** Detailed use case: Amazon seller assistant can't advise on getting fake/paid reviews. "It's not like a format thing... it's not a very easy red flag to detect, especially if the language is vague." Claude would suggest steps to get paid reviews on the second ask. Even an intern could surface this, but preventing it at scale is hard.

11. **Policy = knowledge + detection + enforcement.** Three parts: (a) system must be aware of policies/rules that change, (b) detect when a response relates to a policy, (c) ensure the response refers to/complies with the policy. "You do need to modularize the solution a little bit."

### Testing at scale — Bahar's core insight

12. **"Testing is a HUGE problem."** "If you're thinking about AI safety, it has to be a part of the conversation."

13. **"If you guys can figure out testing and metrics at scale..."** "Allow people to do testing and get metrics at scale — with some perturbations so you can get variation. Basically do a little bit of a robustness [check]."

14. **QA-as-seeds → synthetic scale-up.** Use QA findings as seeds → generate 1,000 or 10,000 synthetic examples → test policy → find edge cases → send failures back to human QAs for the hard cases. "Active learning" feedback loop instead of hiring 100 more QAs.

15. **0.01% matters at scale.** "In AI safety, the stuff you care about is not going to be 20% of the time — it's going to be 0.5%. Detecting that 0.01% is very hard, especially if you're not in production. That's 1,000 people every day."

16. **"Somehow we forgot the fundamentals."** "We had this mental model with ML — you automate something, you measure at scale to understand what it can and cannot do, then you keep measuring and iterating. Now somehow we forgot." The AI hype killed measurement discipline.

17. **Amazon example of the breakdown.** "You told me I can launch with 20 examples. Now you're asking for training data. I don't have training data — you told me to outsource that." Conflicting mandates from leadership killed data-driven development.

### Demo reaction

18. **"By the way, I should have started with — this is awesome."** Positive reaction after seeing the live terminal demo of Luthien blocking a dangerous command.

### Broader observations

- **Different persona from all prior users.** Bahar is not a daily Claude Code user or SDE. She's an applied scientist thinking about enterprise AI safety at scale (millions of conversations, 0.01% failure rates). Her use case is not coding agents — it's any LLM system that needs policy compliance.
- **Her core gap = testing, not enforcement.** "Defining policies is easy. Testing them at scale is the real gap." This is a potential future product direction but beyond current scope.
- **"Handle the fundamentals so I can focus on my domain."** Luthien's value for enterprise = universal safety baseline ("you don't have to worry about the fundamentals") + infrastructure to build domain-specific rules on top.
- **Convergence with Beth Anne.** Both Beth Anne and Bahar independently described: "handle the universal stuff, let me customize for my business." Same insight from PM and scientist perspectives.

---

## Session 3: Quentin Feuillade-Montixi (WeaveMind / Seldon Labs)

- **Date:** Feb 10, 2026 (Monday)
- **Forum:** Google Meet
- **Attendees:** Scott Wofford, Quentin Feuillade-Montixi
- **Quentin:** Senior engineer, founder of WeaveMind.ai. Seldon batch 2 peer. Uses Windsurf + Claude. Building control infrastructure for general AI workflows.
- **Format:** Walked through [readme-v6.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v6.md) on `value-prop` branch, then live demo of Luthien gateway.
- **Notes:** [Scott's discovery call notes](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/Quentin%EF%BC%8FLuthien%20discovery%20call.md), [Gemini transcript](https://github.com/LuthienResearch/luthien-org/blob/main/_User-Interview-Notes/Quentin/)
- **Full policy feedback:** [3.1-policy-config-feedback.md, Session 5](3.1-policy-config-feedback.md#session-5-quentin-feuillade-montixi-weavemind--seldon-labs)

### README / value prop feedback

1. **AI slop irony — README has em dashes while promoting em dash removal.** "I see some em dash on the GitHub, be careful." Then later: "It's funny to see 'clean up writing ticks, remove em dash' and then you have em dash on your own." The README undermines credibility by exhibiting the exact problems it claims to solve.

2. **Didn't understand expandable code sections.** "Oh, I didn't see that. I could expand the thing." Quentin missed that code examples were in expandable/collapsible sections. UX issue — expandable sections should be more visually obvious or default open.

3. **"Does Windsurf support this?"** First technical question. "Most developers are using stuff like Windsurf, Cursor, and maybe some are using Claude Code." Turned out Windsurf doesn't support custom proxy servers — became a hard blocker for Quentin. README needs to clearly state which clients are supported.

4. **"Does this support streaming?"** "How do you handle streaming? Models are going to stream token by token. Are you going to evaluate token by token or at the end?" Important technical question from a senior engineer — the README should make clear that streaming is supported, since it's a non-obvious technical challenge.

5. **Liked the left/right layout.** "I like the left-right, the issue and the 'with Luthien instead.'" The before/after comparison format worked for him.

6. **Got the proxy concept quickly.** "Something running in the background." Understood it was intercepting and checking responses against instructions. Asked good follow-up: "Are you going to use an AI to check if the response is aligned with the instructions?"

### Security concerns (README-relevant)

7. **Data transmission and encryption matter.** Most worried about: data transmission security and encryption at rest. For a proxy that sees all code conversations, users need to trust the transport layer.

8. **Private code — "what you put around the code."** Not just the code itself but the context, prompts, and metadata around it. The system prompt and tool calls may reveal proprietary patterns.

9. **SOC 2 compliance would encourage adoption.** Asked about business plan and security certifications. SOC 2 would be a trust signal for companies routing code through a third-party proxy.

### Broader observations

- **Windsurf as adoption blocker.** Quentin speculated Windsurf intentionally blocks custom servers to protect their context-building IP ("they don't want people to retro-engineer their context building"). This means any Windsurf user is blocked from using Luthien.
- **Potential Windsurf advocacy.** Quentin sees custom server support as a feature Windsurf should add: "I think it would be a good thing to push to allow people to have custom [servers] because it's also a feature I would like to have."

---

## Session 4: Tyler Tracy (Redwood Research — live install)

- **Date:** Feb 10, 2026 (Monday)
- **Forum:** Google Meet (Redwood/Luthien Office Hours)
- **Attendees:** Scott Wofford, Jai Dhyani, Tyler Tracy
- **Tyler:** Senior engineer at Redwood Research. Team of ~10 engineers. Uses Cursor + Claude Code. Building AI safety research tooling (Linux Arena).
- **CX version:** [readme-v6.md](https://github.com/LuthienResearch/luthien-proxy/blob/value-prop/docs/readme-v6.md) -- had "Who it's for" section, colored side-by-side comparison cards (red/green, not SVG terminals), "Policies" section with built-in common failure modes + custom policies, "Claude Code (or Codex)" in intro. Tyler installed live on the call. Docker compose up, activity monitor, curl test.
- **Notes:** [Office Hours notes](https://docs.google.com/document/d/1Qo2D5zrtuHO2MF6wJX4v86sJPm-YAmCNwKWPJTcFJvM/edit?tab=t.0), [Gemini transcript](https://docs.google.com/document/d/1lRX5U7_2Ig1oOw775xm9uoGGK6yJx2gip8N2BlAA0JQ/edit?tab=t.fp5fl2phgglm)
- **Full policy feedback:** [3.1-policy-config-feedback.md, Session 7](3.1-policy-config-feedback.md#session-7-tyler-tracy-redwood-research)

### Install / onboarding feedback

1. **Installed live on first attempt.** "Smoothest user trial ever" (Jai). Docker compose up worked. Activity monitor showed requests. Curl test passed. This is the first external user to install Luthien live without issues.

2. **Docker images built locally -- slow.** First install required building all images from source. Tyler hit this directly. For team deployment (10 engineers), pre-built Docker Hub images would make `docker compose up` near-instant.

3. **`quick_start.sh` health check fails without Grafana.** Tyler hit a known bug where `quick_start.sh` can't detect the gateway when Grafana hasn't been launched yet. Jai: "I've been meaning to fix forever."

4. **Confusion: `quick_start.sh` vs `docker compose up`.** Unclear which to use for getting started. Resolved in README v7: `docker compose up -d` for users, `quick_start.sh` documented in `dev/README.md` for developers only.

### README / value prop signals

5. **"Maybe I should just tell them to use this."** Tyler's reaction after successful install -- offered to deploy Luthien to his 10-person team. This is the strongest adoption signal from any external user so far.

6. **Tested readme-v6 layout.** The left/right before-after layout and expandable code sections worked for him (consistent with Quentin's positive reaction to the same version).

### Workflow context (from [raw Office Hours notes](https://docs.google.com/document/d/1Qo2D5zrtuHO2MF6wJX4v86sJPm-YAmCNwKWPJTcFJvM/edit?tab=t.0#heading=h.m4y4a9b4pqyd))

7. **10-40% of time on tech things.** Large codebase, 10-person team, all remote. Uses Cursor or shell.

8. **Context-switching pain.** "Sucks transition between main workflow and web-based UIs." Claude code .com is "buggy overall" -- no worktrees. Reinforces terminal-first / CLI-first product direction for Luthien.

9. **Dual-audience documentation problem.** Uses `claude.md` / `agent.md` symlink for interoperability between Claude Code and Cursor. "Docs made for humans and AIs." But "docs aren't up to date" and it's "hard to write docs for humans and AIs." The CLI is documented, but AI prefers MCP server over Click Python CLI.

10. **Auto-apply mode is the root cause of FPR problems.** "MAIN REASON IT DOESN'T [work]: AUTO." Auto-apply/auto-accept mode bypasses the human checkpoint where Tyler would catch false positives. When he does get prompted, "10 times after 20 sessions, prompt me 2-3 times" -- tolerable FPR when human is in the loop, intolerable when automated.

11. **Tyler's ideas for PR proof of testing.** "Upload to website, link run on PR, after run, show field on data change. Make it much easier to see." Also: "Hack: sub-agent could work" -- a sub-agent that verifies the PR before submission.

12. **What he trusts vs doesn't.** "Pretty happy with cursor bug bot -- I trust there aren't bugs." But PR reviewers "don't have access to my [context]." "I want them to have research taste" -- the judgment/taste gap that AI control can't solve.

13. **Meeting notes aggregation interest.** "Other 60% if I had all these meeting notes, pull my..." -- sees value in aggregating context across sessions. (Partially trails off in notes.)

### Broader observations

- **First external user to complete a live install.** All prior sessions were README reviews or demos, not hands-on installs. Tyler proved the install flow works for a senior engineer.
- **Team deployment is the next milestone.** Tyler's team of 10 could become the first real deployment, but it requires frictionless onboarding (pre-built Docker images, clear docs) before his team can self-serve.
- **5/5 across all design partner criteria.** Already does weekly calls. No Windsurf blocker. Installed live. Not just a design partner -- potential first real deployment.
- **Auto-apply is the policy adoption blocker.** Tyler's 60% FPR is tolerable with human-in-loop but intolerable with auto-apply. Any policy enforcement system needs to account for auto-apply mode as the deployment context where FPR matters most.

---

## Internal session: Jai Dhyani — PR #179 README Review (Feb 12, 2026)

- **Date:** Feb 12, 2026
- **Forum:** Google Meet (Scott + Jai weekly debrief / Seldon standup)
- **Attendees:** Scott Wofford, Jai Dhyani
- **Context:** Reviewing PR #179 (value-prop README rewrite). Scott preparing for EASF weekend meetings the next day — needed an approved, improved README to show potential users. Also discussed deployment strategy (one-click deploy, OAuth pass-through).
- **Recording:** Gemini transcript: `scott_jai debrief seldon wkly - 2026_02_12 17_28 PST - Notes by Gemini.md`

### README structure feedback

1. **"It's a few sentences and maybe one or two pictures."** Jai's view of what the value-prop addition to the README should be. Not a full rewrite — just add a compelling intro on top of the existing "boring nerdy stuff."

2. **Before/after comparison validated.** "Yes, that's great." — confirmed this format works. But: "We haven't actually implemented it yet" — don't show pip→uv replacement if it's not reliably working. "Until we've actually done that reliably, we don't put it in."

3. **Cut "Who it's for" section entirely.** "This is implicit in everything else. We don't need to make it more explicit." / "That filter holds is how we're funneling people towards this point. Once you're at this point, there's no reason to communicate that further."

4. **Add "across your org" to intro sentence.** The value prop is organizational, not individual — one sentence change captures this. "Luthien is an API AI proxy server that lets you implement security and monitoring policies for your entire org with no friction."

5. **Rename "What policies can do" → "Example use cases."** "Instead of trying to describe the principle of how it works, just showing examples of people getting utility out of it." Purpose = demonstrate utility, not explain mechanics. Each example should ideally link to how to activate that policy.

6. **Visual diagram is the right way to show architecture.** You → Luthien → Anthropic. "Luthien enforces your policies on everything that goes into or comes out of the backend. It can replace file edits that violate your rules with tool calls that follow your rules, and generate an easy-to-read log of everything your agent does."

7. **Correct section order: value prop → examples → visual diagram → setup details.** "The flow is: here's the value proposition, here's specific examples, here's how it's actually implemented so you can have a mental model, and then the nerd stuff." The "nerd stuff" = setup variables, Docker, env vars.

8. **Replace "How it works" with minimal quick start.** Instead of describing how env vars work, show the 3 commands: clone, docker, run Claude Code. "Show the commands." Detailed setup lives further down.

### Reliability bar for README claims

9. **Don't show features that aren't reliably dog-fooded.** "The ones that meet reliability don't meet utility. We need one that meets both." Jai's bar: he's daily-running with a rule that works. Until then, don't put it on the README.

10. **Block pip as the simplest real demo.** "Let's just have it block pip. That's a thing that exists right now. It's not good, but..." Pragmatic choice — show something real, even if janky, over something polished that doesn't exist.

11. **Logging URL as the default demo policy.** "The trivial helpful thing I can think of is just inserting a URL that takes you to a page doing a full log of everything that happened in the conversation. Inserting it at the beginning of the conversation, and you click it and then it updates live." Two policies to implement: English language rules + online full log.

### Deployment strategy

12. **One-click deploy is the ultimate goal.** "You press a button, specify some rules, you now have an endpoint, you now have a command to launch Claude or Codex." Not yet built, but the north star for onboarding.

13. **OAuth pass-through simplifies setup dramatically.** User brings their own Claude subscription. "Setup becomes much easier — you only have to set one env var which is the backend URL." No need for users to paste API keys. Price: Luthien pays for server, user pays for their own Anthropic usage.

14. **Punt auth entirely for now.** "Don't worry about auth — just do straight pass-through and flag auth as a thing to figure out later." If too many people use the free service, "that would be a really good problem to have."

### Current README assessment

15. **"The current readme is s\*\*\*."** Jai's self-assessment. But it's accurate (except missing Docker prerequisite). The proposed changes are a "vast improvement over the mess that I have there right now."

16. **Limit supported clients to Claude Code for now.** "Right now we should probably limit it to just Claude Code because that's what's thoroughly tested." Drop Windsurf mention, keep scope narrow.

### Broader observations

- **Time pressure shaped decisions.** Scott had EASF meetings starting the next morning. Both agreed: ship something better than what's on main, even if imperfect.
- **Pattern: Jai prefers showing what exists over promising what's coming.** Consistent with his Feb 5 feedback ("I want the demo to do most of the work") — always ground claims in working software.
- **Scott's frustration with the gap between user feedback and implementation.** Multiple validated patterns from user research (before/after, custom policies, PII use cases) that can't be shown because they're not reliably implemented yet. This tension drives the README scope discussion.
- **Convergence with all prior sessions:** Demo-first (Theme A), plain English (Theme B), example use cases over mechanics, visual diagram — all consistent with what worked in Sessions 0-3.

---

## Macro themes (consolidated from 18 cross-cutting observations)

Applying [Musk's 5-Step Design Process](https://modelthinkers.com/mental-model/musks-5-step-design-process): question every theme, merge duplicates, delete what doesn't hold up across users.

### Theme A: Demo-first (5/5 external users + Jai)

The README should open with a visual demo showing Luthien in action — not setup instructions, not abstract descriptions, not a bulleted problem list. **Before/after SVGs need explicit annotation** — all 6 reviewers (Tyler Mar 3, Darren Mar 2, Jai Feb 26, Josh Feb 25, Finn Feb 25, Maria Feb 26) flagged this as unclear without annotation.

| Who | Quote |
|-----|-------|
| Zac | "I want to know what's the epic shit I can do. Then how do you get started?" / "Have some dramatic picture or something" |
| Jai | "Demo should do most of the work" / "Lead with an example, then name the category" / "Value before shape" |
| Chris | "I want it to be visual" / "I like these examples" |
| Beth Anne | "I like this way better" (Option B visual) / "I don't know what the UI looks like" |
| Bahar | "By the way, I should have started with — this is awesome" (re: live demo) |
| Jai (Feb 26) | "Reshape as stories — a narrative of natural use case — it becomes more compelling." / Fabricated Luthien shield overlay "not okay" |
| Tyler (Mar 3) | "Literally just cat the CLAUDE.md in the thing." / "What the hell are the policies?" |
| Darren (Mar 2) | Before/after hard to scan — "what is the difference?" / Content overload — "requiring a lot of reading" |

**Absorbed themes:** Features first setup last, Visual > text, Show me the UI, Lead with example not category, Annotate the before/after diff

### Theme B: Plain English for both audiences (3 users)

PMs are a distribution channel ("I'll send it to my PE"). The README must be readable by non-SDEs who forward to engineers.

| Who | Quote |
|-----|-------|
| Chris | "Could be even simpler" / "Too technical for me" |
| Beth Anne | "I can't clock it because I'm not [a developer]" / "I don't understand what pick your policy means" / "Put [who it's for] a little higher up" |
| Jai | "Drop-in proxy" not obvious — "describe value before shape" |

**Absorbed themes:** Simplify language, Code examples too technical, "Who it's for" placement, PM-as-champion path, Tagline direction

### Theme C: Universal protection + your custom rules (4 independent users)

The value prop is two layers: (1) dangerous stuff everyone gets wrong — Luthien handles that, (2) rules specific to your business — you customize those.

| Who | Quote |
|-----|-------|
| Beth Anne | "There's a shit ton that everyone gets wrong... we take care of that. And then stuff specific to your business." |
| Bahar | "Handle the fundamentals so I can focus on domain-specific rules" |
| Zac | "I'm way more interested in creating my own policy... play this up a lot more" |
| Jack | "Customizable destructive ops list" (from policy config session) |

**Sub-theme: Complete the block story.** The demo shows a block — but then what? Two users independently flagged this gap:
- Beth Anne: "Violated. Do I have to take an action?"
- Bahar: "If it did that, maybe it could have done Y. Here are the ramifications."

**Absorbed themes:** Universal + custom, Custom policies = the hook, Don't just block — suggest alternatives

### Theme D: Zero-friction setup (2 users, 7+ quotes)

Setup should be: set 2 env vars, run docker compose. Don't make me change my client. Tell me what's running. Default policy should be active without configuration. Remove mentions of features that don't exist yet (e.g., "cloud account").

| Who | Quote |
|-----|-------|
| Zac | "I set env variables all the time" / "If I see I have to launch it with this, I'm closing the tab" / "Emphasize I can use my own Claude Code" / "Tell me what Docker spins up" / "Which port it's using" |
| Jai | "Without changing anything about your development environment" / "GitHub repo is always the de facto landing page" |
| Jai (Feb 26) | One-line install + CLI north star: "Luthien proxy, Add Rule, never use PIP always use UV" |
| Tyler (Mar 3) | "Cloud account" confusion / "Do I have to configure?" — default policy must be clear / Fictional class names undermine trust |

**Absorbed themes:** Env vars not scripts, Keep your own client, GitHub = landing page, Try before install, Default policy active out of the box, Don't mention unbuilt features

### Theme E: Policy creation is real work (1 user — expert signal)

Don't make custom policies look trivially easy. The "Write your own" section showing a 5-line Python class is misleading — the real work is testing edge cases and refining.

| Who | Quote |
|-----|-------|
| Bahar | "Too rudimentary... the problem is not to define it — but to test it against all the different edge cases" / "Everybody can say 'I'm not gonna allow drunk people.' How do you define that?" |

**Note:** Single source, but Bahar managed AI safety at enterprise scale. This is a guardrail on Theme C — prevents overselling.

**Absorbed themes:** Testing at scale, Policy = more than definition

---

## Comparison with all sessions

| | Zac (Jan 27, README) | Jai (Feb 5, internal) | Zac (Jan 30, policy UI) | Jack + Zac (Feb 3) | Finn (Feb 6) | Chris + Beth Anne (Feb 8) | Bahar (Feb 8) | Quentin (Feb 10) | Tyler (Feb 10, live install) | Jai (Feb 12, PR #179) | Peter (Feb 25, QA trial) | Josh (Feb 25) | Finn (Feb 25, landing page) | Maria (Feb 26) | Jai (Feb 26, Seldon) | Darren (Mar 2) | Tyler (Mar 3) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Persona** | SDE, startup CTO | Co-founder, SDE | SDE, startup CTO | SDE, daily Claude Code | SDE, daily Claude Code | L7 PMTs at Amazon | Applied Scientist, enterprise AI safety | Senior SDE, startup founder, Windsurf user | Senior SDE, AI safety research, Cursor + Claude Code | Co-founder, CTO | CTO, ex-Google, 14 Claude Code instances daily | AI safety researcher (NOT ICP) | Accelerator co-founder, daily Claude Code | Dir. of Product, ex-economist (NOT ICP) | Co-founder, CTO | Designer at Carbon Direct (NOT ICP) | Senior SDE, AI safety, Redwood Research |
| **What they evaluated** | Current README on `main` | README options A/B/C | Policy config UI | UI mockups (A/B/C retry) | Live Luthien + policies | README options A/B/C | README options C->A->C + live demo | readme-v6.md + live demo | readme-v6 + live install (first external install) | PR #179 value-prop README | Landing page + live install attempt | Landing page prototypes (Round 4b) + README quick start | Landing page prototypes (Round 4b) + quick start attempt | landing_v8 prototypes + README | v9 landing page variants + README SVGs | Landing page (v8/v9) | README on `feature/no-silent-failures-policy` + trial doc |
| **Core direction** | Features first, setup last. Custom policies = the hook. Env vars, not scripts. | Demo video + one-click deploy. GitHub = landing page. Value before shape. | Meaningful defaults, async reports | Terminal feedback, toggles | AI slop removal, LLM judge | Simpler language, real use cases, visual | Testing at scale is the real gap. Handle fundamentals, let users focus on domain-specific. Don't oversimplify policy creation. | Avoid AI slop irony. Clarify supported clients. Address security (encryption, private code). | Install works. Pre-built Docker images needed for team. Backward compat 60% FPR. AI ignores team utilities. PRs lack proof of testing. | Value prop -> examples -> visual diagram -> setup. Cut "Who it's for." Only show what's reliably implemented. OAuth pass-through. | "This is something that should exist." Guardrails for agents with API access. Latency is primary concern. Universal + custom policy layers. | Differentiate from system prompt baseline. Need metrics. "Book a call" = anti-pattern. Architecture too detailed. Context rot = sweet spot. | Cards spin too fast. Demo too dense. Architecture should be bigger. "Who are you guys?" Just ask Claude to do the quickstart. LLM judge is cool. | Value prop first, quotes at bottom. Punchier storytelling. "Claude Code" not "agent." Show actual policy rules. De-emphasize install. Visual identity needed. | Fabricated UI overlay not okay. Stories > feature lists. Frame as features not architecture. One-line install + CLI as north star. Dashboard link at session start. | Before/after hard to scan. Content overload. "How it works" felt like afterthought. Page needs story flow. Quotes compete for attention. Design process advice. | Benchmark data is #1 trust-builder. "What are the policies?" — confused after scrolling. Video > text for trust. Fictional class names undermine credibility. "Cloud account" confusion. Forward-to-team readability. |
| **"I'd pay for..."** | "I want to use you guys" -- wants to use Luthien as infra for Counterweight | N/A (co-founder) | Automated QA at proxy layer | Enforcing CLAUDE.md rules | Em-dash removal ($20/mo) | PII protection (would forward to team) | Testing + metrics at scale with synthetic perturbations. QA-as-seeds -> active learning loop. | Context management ($1hr/day saved). SOC 2 would encourage adoption. | Team-wide enforcement. "Maybe I should just tell them to use this." | N/A (co-founder) | Guardrails for agents with production API access. "I would love to try it." | N/A (researcher, potential hire) | LLM-as-judge policy. Em-dash removal (repeat from Feb 6). | N/A (not ICP) | N/A (co-founder) | N/A (not ICP) | Team-wide enforcement for contractors. Benchmark data would seal the deal. |
| **Primary feedback surface** | README / GitHub repo | N/A | Email/Slack | Claude Code terminal | UI (but nicer) | README / landing page | README / landing page (but thinking beyond coding agents) | README + live gateway demo | Live install + terminal | PR #179 review | Landing page + live install | Landing page + README quick start | Landing page + quick start attempt | Landing page prototypes | Landing page variants + README SVGs | Landing page | README + trial doc |

---

## External developer quotes: Agent overconfidence and lack of tool use

- **Date collected:** Feb 24, 2026
- **Context:** Quotes from published developer blog posts describing AI agent overconfidence — the failure mode where agents fabricate plausible-sounding answers instead of using available tools to verify. Collected during a Claude.ai session where Claude exhibited this exact behavior: gave wrong Substack UI navigation instructions 3x despite having screenshots and browser tools available. Never searched docs until forced.
- **Luthien relevance:** A control policy could intercept responses and verify whether the agent actually called a verification tool before giving factual instructions. No tool call before the instruction → flag/block/resample. Maps directly to Jai's [21 Points](https://luthienresearch.org/updates/21-points-on-ai-control/) argument that classification is easier than generation.

### Quotes

1. **Identical confidence whether certain or guessing.** "Claude says 'the function returns X' with identical confidence whether it's certain or guessing. Users can't tell what to verify."
   — Medium/@elliotJL, ["Claude Keeps Making the Same Mistakes"](https://medium.com/@elliotJL/your-ai-has-infinite-knowledge-and-zero-habits-heres-the-fix-e279215d478d) (Jan 2026)

2. **Bullshitting with confidence.** "Claude will absolutely try to bullshit its way through situations where it doesn't know the answer but won't admit it. So now I have to verify everything before letting it touch any code. It's like having a really enthusiastic junior developer who's confident about everything but actually knows nothing."
   — Scott Spence, ["Working with Claude Code! The Honest Version"](https://scottspence.com/posts/working-with-claude-code-the-honest-version) (Nov 2025)

3. **Retries same failed approach, never escalates.** "Claude fails at something, retries the exact same approach five times, burns 30 minutes. Never tries a different strategy. Never escalates. Just keeps going with the confidence of someone absolutely certain the wall will move this time."
   — Medium/@elliotJL (Jan 2026)

4. **"I'm a product manager for a stochastic parrot."**
   — Scott Spence (Nov 2025)

### First-party example (dogfooding, this session)

5. **Wrong instructions 3x with tools available.** In a Claude.ai session (Feb 24, 2026), Claude gave wrong Substack UI navigation instructions three times despite having screenshots AND browser tools available. Never searched docs until forced. Did an Amazon-style COE to create a verifiable mechanism. This is the exact failure mode Luthien's control policies address — confident fabrication when verification tools were available but unused.

### Broader observations

- **Pattern: "confident fabrication when tools were available."** All four external quotes and the first-party example describe the same failure mode from different angles: the agent produces plausible output without checking whether it's correct, and the user has no signal to distinguish confident-and-right from confident-and-wrong.
- **Convergence with existing frustrations.** Maps to Kirk Marple's #37 ("it was so confident about such shitty code that it wrote") and Nathan's #19 (mock API calls while claiming real integration). The overconfidence pattern is well-established; these quotes add the "no tool use" dimension.
- **Landing page opportunity.** Quote #4 ("I'm a product manager for a stochastic parrot") has viral-friendly energy. The deadpan tone matches Jai's register for the landing page (see [R9 in requirements](../2-versions-requirements/1-value-prop-requirements-live.md)).

---

## Session 5: Peter Teodosiu (QADNA — QA trial)

- **Date:** Feb 25, 2026
- **Forum:** Video call (QA trial)
- **Attendees:** Scott Wofford, Peter Teodosiu
- **Peter:** CTO of QADNA (Bucharest). Ex-Google. Runs 14 Claude Code instances daily building AI-driven QA SaaS platform. Plans to give agents internal API access to their platform.
- **CX version:** Current landing page + live Luthien install attempt
- **Notes:** [QA Trial Report](https://docs.google.com/document/d/1xugPuJjtfxXw3ale54rdhqAlsH5wcvo31RtPVPJLgz4/edit)

### Value prop feedback

#### Peter (QADNA, 2026-02-25)

> "This looks like something really cool and I would love to try it."

> "I haven't seen something like this before... this is something that should exist."

> "I don't find this confusing at all. It's very well simplified."

> On the architecture diagram: "Pretty much you have a bit of middleware in it that you're logging every request and response, arbitrary rules and policies to calls and responses."

**Context:** Peter is planning to give agents internal API access to QADNA's platform. His primary motivation for Luthien is guardrails against destructive actions that can't be fully prevented by application-level confirmation dialogs.

### Landing page / README specific

1. **"Very clear" and "love how it looks."** Dark mode appreciated. Landing page communicates the concept well for technical users.

2. **Reads as a dev tool — fine for ICP.** Peter noted non-technical users wouldn't understand it. But for our target persona (senior engineers using AI 40+ hrs/week), this is appropriate.

3. **Latency was his first technical concern.** "I'm very curious about how fast would this be... it's not gonna be perfectly seamless, but it's gonna be a bit slower than how you would usually do your work with Claude Code." Especially concerned about policies that call another LLM for subjective checks.

### Broader observations

- **Strongest "I want this" signal since Tyler.** Tyler said "maybe I should just tell them to use this." Peter said "this is something that should exist." Both are senior engineers with real agent deployments.
- **Different use case from other users.** Peter's primary concern is agents with API access to production systems (not just coding agents editing files). This broadens Luthien's applicable use case beyond Claude Code.
- **Convergence with Beth Anne + Bahar on "universal + custom."** Peter wants Luthien to handle the dangerous-action baseline so he can focus on domain-specific QA logic.

---

## Session 6: Maria Paula Mendieta (landing page feedback)

- **Date:** Feb 26, 2026
- **Forum:** In-person (late night, Maria was tired — noted "this is not my prime time")
- **Attendees:** Scott Wofford, Maria Paula Mendieta
- **Maria:** Director of Product at Carbon Direct. Ex-economist/data scientist. Strong product/UX instincts. NOT our ICP (not a developer, doesn't use Claude Code).
- **CX version:** landing_v8 prototypes + README
- **Transcript:** Otter.ai: `/Users/scottwofford/Downloads/Maria's feedback on Luthien landing_readme v8_otter_ai.txt` · Otter ID: `P0Lkx1rvdiMYjwTEH0fkP4Lmrro`
- **Additional assets:** [Sticky notes sketch](maria-sticky-notes-feb26.jpeg) (thought-bubble overlay concept for before/after SVGs, Feb 26)

### Value prop feedback

#### Maria (Carbon Direct, 2026-02-26)

**1. Reorder: quotes belong at the bottom, value prop at the top**

> "I don't think I get enough of a sense of what it does. Okay? It's cognitive effort for I would put the quotes at the bottom, not at the top, because it's almost like testimonial type so you have you want the what it does at the top, so that the quotes makes sense."

**Analysis:** Maria reads the developer frustration quotes as testimonials, not evidence of pain. She's right that the value prop should come first — but the quotes serve a different function than testimonials. They're proof that the problem is real. Reorder is valid; just maintain the framing distinction.

**2. Lead with user action, not architecture**

> "enforce rules and block dangerous operations, but with Luthien coma as a proxy that sits between or something along those lines, yeah, so that they enforce rules and block dangerous operations is like at the very beginning"

> "I would add a punchier version of this at the top"

**Analysis:** Start with what the user DOES (enforce rules, block dangerous operations), not what Luthien IS (a proxy that sits between). Action-first framing.

**3. "AI coding agent" is confusing and redundant with LLM**

> "I don't interpret this as a coding agent like the I don't know the language, but to me, this is an interface."

> "no, because it sounds redundant with... LLM" (about "AI coding agent" in the diagram)

**Analysis:** To a non-developer, "AI coding agent" and "LLM" sound like the same thing. Even for developers, "Claude Code" is more specific and recognizable than "AI coding agent." Decision: drop "agent" terminology from landing page copy.

**4. Visual identity — Luthien needs its own avatar**

> "if you had your own, like Avatar, it would be more visible. What is, what is Claude, and what is you?"

> "It doesn't matter, because it's like a like... it's an avatar. It's like this physical thing that simulates like animal that it's inserting itself there. If you add up something like that for here, I think it could make it very visible."

**Analysis:** Claude has visual identity (the Claude icon). Luthien's interventions blend into the terminal text. An icon/avatar (parrot, magnifying glass, spy) would make Luthien visually distinct in demos and screenshots.

**5. Post-it sketch: emotional overlays on the demo**

Maria sketched on paper during the session ([photo](maria-sticky-notes-feb26.jpeg)). **Top note:** recommended page structure — Value Prop → Demo → Quotes. **Bottom note:** a realistic terminal view with thought bubble overlays showing the user's emotional experience escalating:

> "this is your realistic view, which has a bunch of prompts and a bunch of Luthien stuff, and it looks realistic... And then you have, like, and it's clearly like, your overlay of this, and another one that it's like, sure things went down, no, and the user looks like, oh this... Or maybe like a thought bubble, yeah, exactly, exactly like a thought bubble or something that it's, it's clearly not part of the UI, but you're clearly [drawing] the eyes and, like, look at what's happening, and it's getting worse and worse and worse."

**Analysis:** The thought bubble / emotional overlay concept bridges the gap between "what the code shows" and "how the developer feels." It's a visual storytelling device — the terminal is factual, the overlay is emotional. Could be powerful for the before/after comparison.

**6. Policy examples are too vague — show actual rule text**

> "I think your example. Too vague, like popular MD policy, but what did the policy say? Which policy"

**Analysis:** When showing a block in the demo, include the actual policy rule that triggered it. "Blocked" is not enough — the user needs to see "blocked per policy: never use pip" to understand what Luthien is actually enforcing.

**7. Before/after should be vertically aligned**

> "I would level the both clubs at this starting point, at the same location, and have the same command at the same location. So, because it's so it's easier to compare exactly, because right now I'm like, Wait, I see one green thing here, but I can't see"

**Analysis:** The before/after comparison is currently side-by-side but not aligned at the same starting point. Vertical alignment (same command at the same Y position) makes the diff easier to spot.

**8. De-emphasize install in the demo section**

> "my first instinct is just, you don't need to tell them how to install it. If they're excited about this, you can have a value prop that it's easy to install"

**Analysis:** The install steps in the demo section distract from the demo. Install ≠ demo. The demo should show what Luthien does, not how to set it up. Installation can be a separate section or a "it's easy to install" value prop bullet.

**9. Use cases need storytelling, not technical detail**

> "you don't need this part of the use case. You need the storytelling of the use case, like block, dangerous operations like, enforce packages standards, like blocking people themselves"

**Analysis:** Use cases should read as stories ("block dangerous operations", "enforce package standards") not as technical specifications. The landing page use case section should be headlines + one-liners, not expandable code blocks.

**10. Marketing structure feedback**

> "What is it structure? What's the value prop? Preview of the tool? Like a GIF?"

> "what you're missing here is a puncher storytelling of like, why should you use me?"

> "you may be averse to the word marketing side, but it's what converts and that's exactly what you want there."

**Analysis:** Maria's structural recommendation: value prop → preview/GIF → use cases (as storytelling) → quotes/social proof → how to get started. This aligns with standard developer tool marketing (GitHub's own landing page follows this structure). The README-as-landing-page is still a conversion tool — just one that respects developer aesthetics.

### Broader observations

- **Strong structural feedback despite not being ICP.** Maria's product background surfaces issues our developer interviewees don't articulate — they feel the friction but describe it differently.
- **6th independent user on reorder.** Maria independently arrives at the same conclusion as Zac, Jai, Chris, Beth Anne, and Bahar: value prop and demo first, setup/details later. This is the most validated requirement (R1).
- **"Agent" terminology confirmed as confusing.** First explicit feedback that "AI coding agent" is redundant with "LLM" and confusing to read. Supports switching to "Claude Code" as the specific, recognizable term.
- **Important framing note on quotes.** Maria reads the developer frustration quotes as testimonials. They're actually evidence of pain — proof that the problem Luthien solves is real and widespread. The distinction matters: testimonials say "this product is great," evidence of pain says "this problem is real." Both belong on the page, but in different positions and with different framing.

---

## Session 7: Josh Levy (landing page + README feedback)

- **Date:** Feb 25, 2026
- **Forum:** Video call (Google Meet)
- **Attendees:** Scott Wofford, Josh Levy
- **Josh:** AI safety researcher. Previously worked on debate and control research related to persuasion (FAR grant). Based in Seattle. Deep understanding of AI control, evaluations, and the AI safety landscape. Potential Luthien hire.
- **CX version:** Landing page prototypes (Round 4b) + README quick start (PR on `value-prop` branch)
- **Notes:** [Gemini notes](https://docs.google.com/document/d/1g0WW86LfGgLObrWBl4JphRO34irgmdjn8B9smFBpWfw/edit) · [Recording](https://drive.google.com/file/d/15uU7Kc-XvXLajt2GeYsEbsN4WqU1r1TO/view)

### Value prop feedback

#### Josh (AI safety researcher, 2026-02-25)

**1. Remove "Meanwhile" — too corny**

> "Meanwhile, I would get rid of that meanwhile thing... seems corny. Like too corny."

**Analysis:** The "Meanwhile" transition between sections strikes the wrong tone for our ICP. Engineers read "corny" as "not serious." Aligns with R9 direction (cynical-engineer voice, not SaaS marketing).

**2. Scrolling > clicking for incident examples**

> "How about instead of maybe just have multiple of these scrolling through so it's easier to... latch on to one"

> "the nice thing about the scrolling is you have the best of both worlds. Like cuz you have multiple and so that way people can just like see which one."

**Analysis:** Current click-to-advance behavior for incident cards has a UX bug and forces sequential reading. Scrolling lets users scan multiple examples quickly and latch onto the one that resonates. Lower friction = more engagement.

**3. Block phrasing: remove colon, use active verb + policy name**

> "blocked pip install. Um, like the phrasing is a little weird... it could be like blocking pip install per [policy]. Like I don't think you need the colon... the colon's weird."

**Analysis:** "Blocked: pip install" reads as a log entry, not a human sentence. "Blocking pip install per [policy name]" is clearer and shows which policy triggered it. Converges with Maria's feedback on showing the actual policy rule.

**4. Emojis in terminal screenshots are confusing**

> "it's a little confusing because um like the LLMs use a lot of emojis"

> "I get rid of the nice. I'd get rid of... do I need all caps — just make it as tight and succinct as possible."

**Analysis:** Emojis in the terminal demo are ambiguous — could be LLM output, user input, or Luthien annotations. Both Josh and Maria flagged this independently. Josh's solution: strip them out entirely and tighten the UX section.

**5. Architecture section too detailed for landing page**

> "all of the above stuff is super clear and I think very good. It's just this cloud thing here."

> "I don't know what the cloud is either."

> "it's a lot of words for something that I think is ancillary relative to like the main stuff"

> "I think up to here is really good. I would keep it. And then I think you could have another tab below which is like 'how it works' if you want to include that."

**Analysis:** The LLM-as-judge detail in the architecture section confuses rather than clarifies. Josh's interpretation: "it calls another LLM to check your policies as written" — which isn't quite right. The architecture detail should move to a "How it works" drill-down, not the landing page. Aligns with R1 (demo-first, not mechanics-first).

**6. CTA: "book a call" is anti-pattern for engineers**

> "if I ever see as an engineer like book a call, I'm just like next like this is marketing BS."

> "make it clear on the landing page like try it yourself and then just link over to GitHub"

> "just include a warning... only highly motivated people are going to be here and looking at that."

**Analysis:** Engineers who want to try the product should be able to go straight to GitHub. A bug warning is fine — motivated users will report bugs, which is valuable feedback. "Book a call" should be secondary, not the primary CTA.

**7. VALUE PROP GAP: What does Luthien do that a system prompt can't?**

> "what Luthian is doing special here that can't just be like literally you have a set of instructions that are just getting passed to the prompt"

> "if I took these rules and literally just passed them as a prompt, they'd probably get followed most of the time. Maybe not all the time."

> "you need to be comparing the effectiveness of Lucian relative to that baseline of literally just putting into a prompt"

**Analysis:** This is the most strategically important feedback point. Josh is asking the differentiation question: if I can put rules in CLAUDE.md or a system prompt, why do I need a proxy? The answer is context rot (rules get forgotten over long sessions), enforcement (the proxy can actually block, not just suggest), and observability (you can see what happened). The landing page must address this head-on.

**8. Luthien's sweet spot: context rot and large codebases**

> "Lucian will be maybe most effective like in a context rot scenario or where there's like a huge amount of files"

**Analysis:** Context rot = instructions in CLAUDE.md get forgotten as the conversation grows. This is exactly where a proxy adds value over a system prompt. Josh immediately identified the differentiation angle — positions Luthien as insurance against the failure mode that system prompts can't prevent.

**9. Landing page needs metrics (bar chart comparing approaches)**

> "what's kind of missing here is like some metrics"

> "a little bar chart with like nothing, just prompting, and then Luthien and you're improving like probably 15% or whatever it is relative to just basic prompting"

> "you might even create one where you do have an adversarial agent in some way"

**Analysis:** No user has asked for quantitative data on the landing page before. Josh's research background makes him think in terms of baselines and measurements. This may not be a landing page requirement yet (we don't have the data), but it's a strong product direction signal: Luthien needs benchmarks to prove differentiation.

**10. Overall positive — loves the Claude Code use case**

> "this is great progress. Like I think it looks really good."

> "I love the use case of cloud code. So, good job like figuring that out."

### Broader observations

- **Most strategic feedback yet on value prop differentiation.** Josh is the first person to explicitly ask "what does this do that a system prompt can't?" — the baseline comparison question. Other users felt the value but didn't articulate this gap. The landing page must answer it.
- **Convergence with Maria on emojis and block phrasing.** Two independent sessions (Feb 25 and Feb 26) both flagged emojis as confusing and wanted more specific policy text in block messages. Pattern is confirmed.
- **Context rot as positioning angle.** Josh immediately identified context rot as Luthien's sweet spot — where system prompts fail and a proxy adds real value. This should inform how we frame the value prop.
- **Metrics request is new but premature.** No other user has asked for quantitative benchmarks on the landing page. This is a research-informed perspective — important for product direction, but we don't have the data yet. Flag for future sprint.
- **CTA anti-pattern confirmed.** "Book a call" as primary CTA will bounce technical users. "Try it yourself" + GitHub link is the right primary CTA, with "book a call" as secondary for those who want help.

---

## Session 8: Finn Metz (landing page + quick start feedback)

- **Date:** Feb 25, 2026
- **Forum:** Video call (Google Meet), recorded
- **Attendees:** Scott Wofford, Finn Metz (Jai invited but did not attend)
- **Finn:** Co-founder of Seldon Labs (AI safety accelerator). Runs accelerator batches in SF/Berkeley. Daily Claude Code user. Hates AI slop (em dashes especially). Previously reviewed Luthien policies (Feb 6, policy config Session).
- **CX version:** Landing page prototypes (Round 4b) + README quick start on GitHub
- **Notes:** [Gemini notes](https://docs.google.com/document/d/1Foi5Qjcyyn0vxCOXgqooV2EXdE5b3806kYXguS9xz1w/edit) · [Recording](https://drive.google.com/file/d/1fnGINriZOC6IRj25GaJFmuRxdDQSFw6N/view)

### Value prop feedback

#### Finn (Seldon Labs, 2026-02-25)

**1. Cards spin too fast — can't read them**

> "Why does it go so fast? I'm a product manager for a stoastic parrot. I can't read this."

> "Claude would absolutely try to b****** its way through situations where it doesn't know — why does it spin so fast?"

**Analysis:** Same feedback as Josh (Session 7) — cards auto-advance before you can read them. Confirms the carousel → multi-card grid change in v9. The quote card content resonates (Finn engaged with individual cards) but the delivery mechanism frustrates.

**2. Tweet cards should be clickable/linked**

> "Is this a real tweet? It's cool. Like the the things are cool that I can do this. If I could click on it and like the tweet was linked, that would be even cooler."

**Analysis:** Cards feel more credible when you can verify the source. This aligns with the design rule from Round 4b: platform-authentic cards where the entire card is clickable and opens the source.

**3. Before/after demo section is too dense and confusing**

> "I get very confused by this. Like, it's just too much. I think what you want to say is like this, like UV pip, please."

> "Hard for me to tell what is before and what is after. Uh probably would have... different headings would probably make it clear."

> "I would have probably just skipped this entire section and like not looked at it."

**Analysis:** The demo section tries to show the full Claude Code terminal experience, but the information density makes the before/after distinction unclear. Finn would skip it entirely. Convergence with Maria (Session 6) on simplifying the demo — strip to the core message, use clearer headings ("Without Luthien" / "With Luthien").

**4. Emotional arc of Claude frustration resonates**

> "I do definitely get the emotional arc. So, I've been here where like I've gotten frustrated at Claude. Like I that I like 100% agree with of like I've been plenty of times told Claude to do a thing or whatever and it still did it in different ways."

**Analysis:** The story works — developers recognize the frustration of Claude ignoring repeated instructions. But the current page doesn't communicate this story clearly enough (see #3). The emotional hook is validated; the presentation needs work.

**5. Architecture diagram is great — should be bigger**

> "Architecture Uclad. Uh, this is great. I think this should be bigger."

> "Yeah, that would be sick if it was like really big and then like have the whole architecture."

> "This is like easy to overlook."

**Analysis:** Interesting contrast with Josh (Session 7) who said the architecture section is too detailed and should move to a separate tab. Finn wants it MORE prominent. The difference may be audience: Josh is a researcher thinking about landing page conversion; Finn is an engineer/operator who wants to understand how it works. Solution: keep it on the page but collapsed by default (v9 approach).

**6. "Who are you guys?" — needs an about section**

> "The main thing I'm wondering is like, who are you guys?"

**Analysis:** Finn wants to know the team behind Luthien. Open source project credibility depends on knowing the people. This is the first explicit request for an "about" section on the landing page. Scott acknowledged it's on the backlog (faces, GitHub links, location).

**7. Incident cards are cool as proof, but purpose was unclear**

> "I think it's cool... having this as like proof of like how you know messed up things are."

> "Is this supposed to be like an incident database? Like, is this supposed to be like a somewhat structured record of like all these incidences that were reported?"

> "In those cases I would love to see like how Lucian then fixed it or something."

**Analysis:** The incident cards succeed as entertainment and proof of pain, but Finn expected them to be a structured database with incident-to-fix mapping. This suggests an opportunity: pair each incident category with "how Luthien handles this" — a natural bridge from problem to solution.

**8. "Book a call" — would use it, but notes misuse risk**

> "If I was really looking for this, I would probably book a call."

> "If I was trying to waste people's time trying to sell you things, I would also use this."

> "I use this a lot for competitors. So when I build stuff, I use it for competitors and then try to get out of them what they're doing."

**Analysis:** Finn provides a nuanced CTA perspective. Unlike Josh ("book a call = next"), Finn would actually book it — but flags that competitors and service sellers also use booking links for intel gathering. Not a reason to remove it, but a risk to be aware of.

**9. LLM-as-judge policy is "really cool"**

> "This is would be really cool if this worked properly... I haven't seen this before being like implemented in an easy and like whatever manner."

> "Where does the haiku come from? Is it the same instance? Is it a different instance?"

**Analysis:** Strong interest in the LLM-as-judge concept. Finn immediately asks the right technical question (separate instance?). This validates R3 — the "your custom rules" layer, especially when backed by an LLM judge, is a differentiator.

**10. Quick start: "Just ask Claude to do it"**

Finn's approach to the README quick start was to copy the entire README and paste it into Claude Code:

> "What I do with quick start guides, right? So like I go to my Claude and be like, 'Yo, do this. Let me know what you need.'"

Scott: "I don't know why I didn't think of simplifying this to just ask Claude to do it. That's brilliant."

**Analysis:** Finn demonstrates the modern developer's approach to setup: delegate to the AI. Instead of reading instructions, tell Claude Code to follow them. This suggests the quick start should include a one-liner: "Paste this into Claude Code: 'Set up Luthien proxy using these instructions.'" Radical simplification of R5.

**11. DeSlop policy attempt failed**

Finn tried to implement the em-dash removal policy ("D-slop policy") via Claude Code during the session. The attempt didn't immediately work — likely the same DeSlop activation bug Peter hit (Session 5).

> "I want the policy, but don't want to use a s***** interface. I want to just tell you to fix."

**Analysis:** Validates the "tell Claude to configure it" pattern from #10. Users don't want to learn a policy configuration UI — they want to describe what they want in natural language and have it work.

### Broader observations

- **9th user on cards-too-fast.** Finn + Josh (independently, same day) both said the carousel auto-advances too quickly. This is now the most-reproduced UX bug.
- **Convergence with Maria on demo clarity.** Both Finn and Maria found the before/after demo section confusing and too dense. Two independent sessions confirming the same issue = confirmed pattern.
- **Architecture: expand vs. collapse split.** Finn wants the architecture diagram bigger; Josh wants it hidden behind a tab. The v9 `<details>` collapse approach threads the needle — visible for those who want it, out of the way for those who don't.
- **"Just ask Claude to do it" is the onboarding breakthrough.** Finn's natural behavior (copy README → paste into Claude Code) is the simplest possible onboarding flow. This should become the primary quick start path.
- **About section is a gap.** First explicit request for team identity on the landing page. Open source credibility requires knowing who's behind it.
- **Incident → fix mapping.** Finn's instinct to see "how Luthien fixed it" for each incident is a natural next step for the incident cards. Could be a powerful conversion element: problem (quote) → solution (how Luthien handles it).

---

## Session 9: Claude (simulated new user review)

- **Date:** Feb 25, 2026
- **Forum:** Claude-generated walkthrough (simulating a senior dev who uses Claude Code daily)
- **Attendees:** N/A — AI-simulated review
- **CX version:** Landing page v8 (`scottwofford.com/luthien/landing_v8/`) + GitHub README on `feedback/tyler-feb-10` branch
- **Full report:** [claude-qa-trial-report-2026-02-25.md](claude-qa-trial-report-2026-02-25.md) · [Google Drive copy](https://drive.google.com/file/d/1H5ju6NgUSvEff4ElrA_1z2bjW0CJmcLC/view?usp=sharing)
- **Scores:** Landing page 7/10, README 8/10

### Landing page feedback

1. **Move BEFORE/AFTER up — it's the best asset, buried below the fold.** "This is the single most compelling element on the entire page. It should move UP — ideally right below the headline or immediately after the quote carousel." Convergence with Maria (Session 6) and Finn (Session 8) on demo section issues.

2. **Hero subhead is architecturally accurate but wrong for a first sentence.** "A new user doesn't care about 'proxy' or 'client/backend' — they care about their pain." Suggested rewrite: "Your AI coding agent ignores instructions, deletes tests, and lies about it. Luthien catches that — automatically, without changing your dev setup." Same critique as every session since Session 1.

3. **Missing: what happens when Luthien catches something?** "The BEFORE/AFTER shows blocking + auto-correction, but the page doesn't explain the range of actions (block, retry, notify, log). A 3-item 'Detect → Act → Notify' flow would clarify this."

4. **"see more →" link destination is unclear.** "I don't know where this goes or what I'd find. Either label it clearly ('see 9 more developer quotes') or remove it."

5. **No mention of what it costs.** "A dev will wonder: 'Is this free? Do I need to pay for the monitoring LLM?' One sentence addressing this would reduce friction."

6. **Quote carousel heading undersells the problem.** "Claude Code does weird and suspicious stuff sometimes..." is weak — consider "Sound familiar?" or "You're not the only one."

7. **Architecture "can call another LLM" needs context.** "A new dev might wonder: 'Wait, so it's running TWO LLMs?' — add one line about cost/latency."

### Landing page: what's working

- Dark theme feels developer-native, not "marketing site pretending to be technical"
- Quote carousel creates emotional buy-in before showing the solution
- BEFORE/AFTER screenshots worth 1,000 words of copy
- "Open source. Early stage." is perfect trust-building CTA
- ~50ms badge proactively handles latency objection
- Clean nav with anchor scrolling works smoothly

### README feedback

8. **Step 2 will lose people.** "'Add your Anthropic API key' assumes they have one. Many devs trying this for the first time may not. Add a one-liner: 'Don't have one? Get a free key at console.anthropic.com (takes 2 min).'"

9. **"What is it?" paragraph has the same problem.** "Leading with 'proxy that sits between...' is burying the lede. Start with the problem."

10. **Steps 5-7 feel optional but aren't clearly separated.** "Steps 1-4 get you running. Steps 5-7 show features. Consider a visual break: '✅ You're running! Now explore:' before steps 5-7."

11. **"DeSlop" is inside-baseball.** "A new user doesn't know what 'slop' means in this context. Consider: 'Clean up AI writing quirks (string replacement)' or at minimum explain 'DeSlop' in parentheses."

12. **LLM-as-judge expandable sections are collapsed.** "The three questions are the most compelling part. Consider showing one expanded by default so the user gets a taste without clicking."

### README: what's working

- SVG architecture diagram renders well on GitHub, easy to understand
- "Every policy action is logged. Measure what got blocked, track false positives, monitor latency overhead." — communicates maturity
- Expandable code examples keep README scannable while rewarding curiosity
- Quick Start is genuinely quick — 4 commands is competitive
- "Luthien runs on your machine or your cloud account" — addresses data privacy in 10 words

### Cross-cutting issues

- **Port SVG diagram to landing page** — the README's SVG version with colored boxes and icons is strictly better than the landing page's text-based monospace version
- **Missing from both: 30-second demo video** — static screenshots are good; motion is better
- **Missing from both: "Who's using this?"** — even "2 design partners, 50 GitHub stars" would add credibility
- **Missing from both: comparison to alternatives** — "How is this different from CodeRabbit / Greptile / just writing better prompts?"

### Broader observations

- **The #1 thing that would improve conversion:** BEFORE/AFTER above the fold + "4 commands to try it yourself" directly below = 9/10
- **The #1 concern:** "Is this going to break my workflow?" The ~50ms badge helps, but one sentence about graceful degradation (What if the proxy goes down? Can I bypass it?) would remove this concern.
- **Consistency is strong** — headline, tagline, screenshots, and brand voice match across landing page and README
- **This is the first AI-simulated review** — useful for testing completeness and perspective, but should be weighted differently than real user feedback since Claude can't experience actual friction (impatience, confusion, distraction) the way a human does

---

## Session 10: Jai Dhyani — Seldon meeting (SVGs + README direction)

- **Date:** Feb 26, 2026
- **Forum:** Seldon Labs internal meeting (Google Meet, recorded)
- **Attendees:** Jai Dhyani, Scott Wofford, Esben Kran, Finn Metz
- **Jai:** Co-founder and CTO of Luthien. Reviewed v9 landing page variants (a-current-order, b-demo-first, c-sandwich, d-interleaved) and current README SVGs on `feature/no-silent-failures-policy` branch.
- **CX version:** Landing page v9 variants + README SVGs on feature branch
- **Source:** Otter transcript ID `bL1wnC35Hji_6HWkfPPUABHFY3k` · Local file: `/Users/scottwofford/Downloads/Seldon Mtg Feb 26_otter_ai (1).txt`

### Value prop feedback

#### Jai (Luthien co-founder, 2026-02-26)

**1. Fabricated "Luthien shield" in the After SVG is not okay**

> "The major one is that this screenshot is actually not a thing that we can — having this Luthien shield thing in the corner, that's not a thing."

> "If we're presenting this as a README that looks like an actual use, and it's not, that's not okay."

**Analysis:** The green "Luthien shield" overlay in the After SVG shows product UI that doesn't exist. It was intended as an editorial annotation ("this is where Luthien acts") but reads as actual product functionality. This is worse than AI slop (R6) — it's fabricated product claims. Must be removed and replaced with clearly editorial annotations (arrows, thought bubbles, labels that are obviously not part of the terminal).

**2. "What can I do" bullet list is too abstract — reshape as stories**

> "I think the main problem with the 'What can I do' bullet list is that it's abstract and not evocative. I think that if we take the same space and reshape it as stories — a narrative of natural use case — it becomes more compelling."

**Analysis:** The current "What can it do?" section lists capabilities (block operations, enforce standards, clean up writing). Jai wants these converted to narratives: "I used Luthien and here's what happened." Stories > features lists.

**3. Frame README sections as features, not "how it works" architecture**

> "I think it's important that we frame these as features and not as 'this is the way that it works.'"

> "I would lead with it being extremely customizable, and then show two or three extremely different things you can do with it."

**Analysis:** The three question categories ("Did it do what I asked?", "Did it follow CLAUDE.md?", "Did it do something suspicious?") should feel like features you can activate, not internal architecture categories.

**4. North star: one-line install + CLI commands**

> "We show you the terminal. We show the one-line install, and then we show like: Luthien proxy, Add Rule, never use PIP always use UV. Luthien proxy, Add Rule, replace all em dashes with dashes."

> "I think I can get to a one-line installer that includes a prompt to say what policy do you want to implement in plain language."

**Analysis:** Jai's long-term vision: `luthien install` → `luthien add-rule "never use pip"` → `luthien start claude`. Entire setup in one screenshot. Not yet built, but the README should work toward this simplicity.

**5. Dashboard link at conversation start**

> "Inserting a link to a dashboard tracking the session and everything at the start of the conversation is potentially impactful. You start Claude, you have a message saying you can track what Luthien is doing here, and all actions Luthien takes can be seen."

**Analysis:** A persistent dashboard URL in the terminal immediately conveys the scope of what Luthien can do — logging, policy actions, conversation history — all visible from one link.

**6. Before/after updates the skeptical prior**

> "The prior that we're updating with this before/after is: it looks exactly like Claude Code. I don't have to change jack shit. And that message is simple enough that I think we can land it."

**Analysis:** The before/after's primary job isn't to show policy logic — it's to show that the developer experience is unchanged. The skeptic's fear is "another tool I have to learn." The before/after says "it's the same terminal, but now your rules get enforced."

### Broader observations

- **Jai is NOT opposed to the SVGs themselves** — only the fabricated formatting overlay. The before/after comparison format works; the execution just needs to show real terminal output with external annotations.
- **Convergence with Maria (Session 6) on annotations.** Maria sketched thought-bubble overlays for the before/after. Jai wants the same thing: realistic terminal view + clearly editorial annotations outside the terminal.
- **One-line install as north star.** Jai's `luthien add-rule` CLI vision is the ultimate simplification of R5 (zero-friction setup). Current quick_start.sh is the stepping stone.
- **Stories > features is a consistent Jai theme.** From Feb 5 ("demo does the work") through this session — always prefers showing over telling, narrative over lists.

---

## Session 11: Darren Ellis (landing page design feedback)

- **Date:** Mar 2, 2026
- **Forum:** 1-on-1 video call (Google Meet, recorded)
- **Attendees:** Scott Wofford, Darren Ellis
- **Darren:** Designer at Carbon Direct. NOT ICP (not a developer, doesn't use Claude Code daily), but high-signal on visual communication and design process.
- **CX version:** Landing page (likely v8 or v9 variant)
- **Source:** Google Doc `1cf4N71qxWVWA9c_FvwrO-7PB-qRw2kBcsC2qjEXzL4c` (Gemini notes in `_User-Interview-Notes/`)

### Value prop feedback

#### Darren (Carbon Direct designer, 2026-03-02)

**1. Before/after SVGs hard to scan — "what is the difference?"**

Darren couldn't identify what was different between the Before and After without already being a daily Claude Code user. The visual distinction wasn't clear enough for someone scanning the page.

**Analysis:** If a visually trained designer can't spot the difference, general developers scanning quickly will miss it too. The before/after needs explicit annotation pointing out what changed (not just relying on the reader to find the diff themselves).

**2. Content overload — "requiring a lot of reading"**

> "Head's like kind of like okay, what's going on."

The page requires too much reading to understand the value. Information density is too high across sections.

**Analysis:** Converges with Finn (Session 8: "I would have probably just skipped this entire section") and Maria (Session 6: "cognitive effort"). Three independent reviewers flagging density = confirmed pattern.

**3. "How it works" collapsed section "felt like an afterthought"**

> "Felt like an afterthought."

The collapsed `<details>` section made the architecture explanation feel deprioritized rather than intentionally progressive-disclosed.

**Analysis:** Interesting tension: collapsing was the v9 compromise between Josh ("hide it") and Finn ("make it bigger"). Darren's read: collapsed ≠ optional, it reads as "we couldn't fit this." May need better framing — e.g., "Want to go deeper?" header.

**4. Story should flow down the page**

Page should follow: problem → what is it → how it works → evidence. Currently sections feel disconnected rather than telling a progressive story.

**Analysis:** This is the same structural feedback Maria gave (Session 6: value prop → demo → quotes) but articulated as a story flow principle. The page should read as a narrative, not a reference doc with sections.

**5. Quote cards compete for attention — lead with concise problem statement**

Lead with a concise problem statement, then use quotes as backup evidence rather than leading with them. Quotes compete with each other when presented as the primary content.

**Analysis:** Converges with Maria (Session 6: "put quotes at the bottom"). Two non-ICP reviewers with design/product backgrounds independently say: concise statement first, quotes as supporting evidence.

**6. "Suspicious" carries a lot of weight**

Darren questioned the word choice of "suspicious" — it carries strong connotations and may be doing more work than intended.

**Analysis:** Worth noting but not necessarily actionable for the README. "Suspicious stuff" is Jai's framing and resonates with the ICP. May need softer language on the landing page vs. README.

**7. Design workflow advice (process, not content)**

- **PRD/requirements as persistent AI context:** Keep requirements doc loaded when generating designs
- **Design tokens/guidelines:** Create a design system doc so AI-generated output is consistent, not generic/templated
- **Piece by piece, not one-shot:** Tackle individual sections rather than regenerating the whole page
- **Schema usage guidelines:** Rules like "don't put 3 primary CTAs together" to prevent common mistakes

**Analysis:** Meta-feedback on our design process, not the design itself. Captured in luthien-org CLAUDE.md as "Design Iteration Workflow" section.

### Broader observations

- **Visual communication feedback converges with Finn (Session 8) on demo section density.** Both non-ICP reviewers struggle with the before/after — validates that it needs annotation even for the target audience.
- **"Afterthought" read of collapsed sections is a new signal.** Previous feedback (Josh, Finn) debated whether to show or hide the architecture. Darren's framing — that hiding reads as "we couldn't fit this" — suggests the `<details>` approach needs better framing.
- **Design process advice is directly actionable.** Darren's process suggestions (persistent context, piece-by-piece, design tokens) immediately improve how we iterate on UI mocks. Already incorporated into luthien-org workflow.
- **Story flow principle validates Maria's structural feedback.** Two product/design professionals independently recommend the same page structure: narrative flow, not reference sections.

---

## Session 12: Tyler Tracy — Redwood/Luthien Sync (README + trial doc feedback)

- **Date:** Mar 3, 2026
- **Forum:** Scheduled Redwood/Luthien sync meeting (Google Meet)
- **Attendees:** Tyler Tracy, Scott Wofford (Jai joined late)
- **Tyler:** Senior SDE at Redwood Research (AI safety). Uses Cursor + Claude Code. Previously installed Luthien live on call (Feb 10, Session — see v6/v7 version table). Key distribution channel: wants to forward Luthien to his team and contractors.
- **CX version:** README on `feature/no-silent-failures-policy` branch + trial document
- **Source:** Google Doc `1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI` (Gemini notes in `_User-Interview-Notes/`) · Redwood/Luthien Sync - 2026/03/03

### Value prop feedback

#### Tyler (Redwood Research, 2026-03-03)

**1. Trial doc unclear for cold sends**

> "Not necessarily clear what this is" for people Tyler shares it with (contractors, team).

Tyler wants to distribute Luthien to his team, but the current trial doc assumes context that cold readers don't have. Needs a generic version for forwarding.

**Analysis:** Tyler represents the "forward to my team" distribution pattern (like Beth Anne forwarding to her PE). The trial doc and README must work for cold sends — no assumed context about what Luthien is or why it exists.

**2. "Cat the CLAUDE.md" — annotation needed**

> "Literally just cat the CLAUDE.md in the thing beforehand so it's more apparent."

Tyler didn't initially see the CLAUDE.md rule in the SVG. The connection between the CLAUDE.md instruction ("Use uv, not pip") and Claude's violation of it wasn't obvious from the before/after visual alone.

**Analysis:** Converges with Darren (Session 11: "what is the difference?"), Josh (Session 7: "highlight the diff"), and Finn (Session 8: "hard to tell before vs after"). ALL 6 reviewers of the SVGs flagged this same issue — the before/after doesn't self-explain. Explicit annotation is needed.

**3. "What the hell are the policies?" — still confused after scrolling**

After scrolling through the README, Tyler was still confused about what policies look like and whether configuration is needed post-install. The anchor link to the policies section was broken.

**Analysis:** Two issues: (a) anchor link bug (technical fix), (b) policies aren't concrete enough. Tyler found the YAML config clear after reading — but had to scroll to find it. At least one policy example should be visible without clicking into a `<details>` section.

**4. "Cloud account" confusion**

> "I haven't heard mentions of this cloud account. I don't know what that is."

The line "Luthien runs on your machine or your cloud account" introduces a concept (cloud deployment) that isn't explained anywhere else. Creates confusion rather than clarity.

**Analysis:** Simple fix: remove "or your cloud account." Luthien currently runs locally. Cloud deployment is future work — mentioning it without context creates questions instead of answering them.

**5. Probability threshold direction unclear**

> "It's unclear which way the probability goes here. If it's a confidence... 95% of the time or 5% of the time."

The `probability_threshold: 0.6` in the YAML config doesn't explain whether higher means more permissive or more restrictive.

**Analysis:** Add inline comment: `# block if judge confidence >= 60% (higher = more permissive)`.

**6. SimpleJudgePolicy examples reference nonexistent classes**

Tyler found the YAML config clear, but the Python examples use fictional class names (`PromptCompliance`, `RuleEnforcement`, `SafetyGuard` extending `SimpleJudgePolicy`) that don't exist in the codebase. If a developer tries to use them, they'll fail.

**Analysis:** This undermines trust. Per Scott: "honest over and above anything else." Replace with real examples: the DeSlop `SimplePolicy` example (real, working code) and `ToolCallJudgePolicy` YAML config (real, configurable).

**7. Skepticism without evidence — "I don't have any data"**

> "There are a lot of things that are trying to do this... I don't have any data to know that yours is better or like actually works."

Tyler rates his excitement low without benchmark data. Many tools claim to solve similar problems — Luthien needs evidence of efficacy.

**Analysis:** The trust gap for the "random developer" persona. Tyler's team is already sold on the idea conceptually — the blocker is proof that it works, not explanation of what it does.

**8. Benchmark is the trust-builder — Bash Arena specifically**

> "Before Luthien the database is deleted 10% of the time, after Luthien 0% of the time."

Tyler wants a 2D frontier graph: safety metric vs utility metric. Recommends **Bash Arena (Control Arena)** specifically — show safety goes up while utility doesn't drop significantly.

**Analysis:** Converges with Josh (Session 7: "bar chart: nothing → prompting → Luthien") but Tyler is much more specific: name the benchmark, name the metrics. This is a major trust-building investment, not a README copy change. Requires Jai's involvement and significant engineering work.

**9. Video > text for trust**

> "GitHub repos that have a video at the beginning... would make me trust it a bit more."

Tyler references Fire Ship, coding YouTubers as discovery channels. A demo video at the top of the README would build trust faster than text.

**Analysis:** New trust signal not in existing macro themes: social proof via video/influencer content. Different from quotes (which Tyler discounts — see #10). Deferred as a separate content creation task.

**10. Quotes: credibility hierarchy matters**

> "Guy from Amazon, I wouldn't care as much. Someone from OpenAI, maybe a bit more."

Random developer quotes on GitHub don't drive Tyler. Institutional affiliation matters. A Fabian (Redwood) quote might work given Tyler's context.

**Analysis:** The quote carousel that resonates with some users (Finn, Maria) has limited impact on Tyler's persona — a senior engineer at a top AI safety lab who has high credibility standards. Benchmark data outweighs quotes for this persona.

**11. Redwood contractors already sold on the idea**

> "The core idea is inherently interesting to them."

The blocker for Tyler's distribution isn't the concept or the README copy — it's evidence that Luthien actually works (benchmarks) and a README that doesn't require Luthien context to understand (cold-send readability).

### Broader observations

- **Tyler's #1 ask is benchmark data, not README copy improvements.** This is the trust gap for "random developer" personas at top labs. They understand the problem — they want proof of the solution.
- **Convergence with Josh (Session 7) on needing quantitative evidence.** Tyler is more specific: Bash Arena, safety metric, utility metric, 2D frontier graph.
- **Tyler represents the "forward to my team" distribution pattern.** Like Beth Anne forwarding to her PE (Session 1). README must work for cold sends — people who haven't talked to Scott.
- **New theme: social proof via video/influencer** (Fire Ship, coding YouTubers). Different trust signal from quotes. Not captured in existing macro themes.
- **Credibility hierarchy for quotes.** Tyler explicitly discounts "random developer" quotes but would value quotes from OpenAI, Anthropic, or Redwood-adjacent researchers. Important for quote selection.
- **ALL 6 reviewers flagged the SVGs.** Tyler (#2), Darren (#1), Jai (#1), Josh (Session 7), Finn (Session 8), Maria (Session 6). The before/after needs annotation — this is the most-validated design issue.

---

## Session 13: Paolo Calvi (onboarding / early adopter)

- **Date:** Mar 3, 2026
- **Forum:** Google Meet (1:16 call)
- **Attendees:** Scott Wofford, Paolo Calvi
- **Paolo:** Airbus engineer (Germany), ~25 hours/week freelance capacity. Active Agent Zero contributor (bug fixes, guard plugin development). Pythonist. Two kids (ages 8 and 2.5). Paying personally.
- **CX version:** Not shown landing page or README — call focused on Paolo's background, use cases, and engagement model.
- **Source:** Voice memo transcript: `~/Downloads/paolo-scott-march-3-transcript.md` · Gemini notes: Google Drive folder `1MPmvqqIXWp3M03yUCCukEKpiNr4u8kNs`

### Value prop feedback

#### Paolo (Airbus / Agent Zero, 2026-03-03)

**1. "Proxy" naming undersells the product — suggest "guard proxy"**

> "A proxy, somebody will imagine something that just passes through blindly things."

> "You should basically call it a guard proxy... highlighting that it's not just [a proxy], because a proxy, you think about caching, you think about squid, and you're not really thinking about filtering."

**Analysis:** Paolo independently suggests "guard proxy" — a label that communicates the control/filtering function, not just the network topology. Converges with R1 messaging requirement: the current name doesn't communicate what Luthien actually does. This is the 7th independent signal that "proxy" alone isn't landing (previous: Zac, Chris, Beth Anne, Maria, Josh, Peter).

**2. Open source agent ecosystems as distribution channel**

> "The best way to go ahead, and even to popularize the proxy, is to say to people using Agent Zero — here you go. You have a really ready to go solution."

> "Open Code, and Agent Zero. These are two main projects that I follow intensively."

**Analysis:** Paolo sees Agent Zero's plugin system and OpenCode as natural distribution channels. Luthien can be a "provider" in Agent Zero's guard plugin architecture — users discover Luthien through their existing agent framework, not through a GitHub search. This is a novel distribution insight not raised by previous interviewees.

**3. Cisco AI Defense is complementary, not a competitor**

> "They offer this free AI firewall... it checks for prompt injection."

> "You're doing what I'm trying to do and actually doing it."

**Analysis:** Paolo built a Cisco AI Defense plugin for Agent Zero (prompt injection firewall), then found Luthien doing the broader proxy/control work. Sees them as layered: Cisco for prompt injection scanning, Luthien for full policy enforcement. This positions Luthien as the control plane that can integrate with specialized security tools rather than replacing them.

**4. Power user persona — will debug and contribute**

> "He needs it so f***ing much... he will say, I have the tools to do quick debugging. I'm gonna use Open Code to debug and to create PRs."

**Analysis:** Paolo is the first interviewee who is actively excited about contributing PRs, not just using the product. His engagement model — daily-drive it, fix bugs while using it, submit PRs — validates the "power user → contributor" pipeline that open source projects need. Contrast with Tyler (would deploy to team but not personally contribute PRs) or Peter (wants to use it, not build it).

**5. PR volume management — PR-Agent recommendation**

> "What you will need to do, at a certain point, more than somebody actually screening the PRs."

> "Whenever there is a new PR or change in the PR, this agent is going to be reviewing what are the changes, and give immediate feedback."

**Analysis:** Paolo recommends PR-Agent (Qodo) for AI-assisted PR review. Framed as red-blue strategy: "two different models one against each other." Practical advice for managing open source contribution volume — relevant as Luthien grows.

**6. "Tweakable and adaptable" is imperative**

> "It's absolutely imperative to be tweakable and adaptable."

**Analysis:** Converges with Quentin (customizable policy parameters), Beth Anne ("specific requirements"), and Tyler (cursor rules for backward compat). Yet another signal that toggle-based policy config isn't enough — users need to customize the rules themselves.

### Broader observations

- **Novel distribution insight.** Paolo is the first to explicitly propose open source agent ecosystems (Agent Zero, OpenCode) as Luthien distribution channels. Previous sessions focused on GitHub README or word-of-mouth. The plugin model — Luthien as a guard provider that agent frameworks list as an option — is a fundamentally different go-to-market.
- **"Guard proxy" naming converges with existing messaging gap.** 7th independent signal that "proxy" doesn't communicate value. "Guard proxy" specifically highlights the filtering/control function.
- **Power user → contributor pipeline validated.** Paolo is the first user who wants to contribute, not just consume. His engagement model (daily-drive + submit PRs) is the open source flywheel.
- **Cisco as complementary layer is new positioning context.** No previous interviewee mentioned Cisco AI Defense. Paolo's experience integrating it with Agent Zero suggests Luthien can position as an orchestration layer that works alongside specialized security tools.
- **Cultural alignment signal.** Co-defined Trust, Speak Up, Respect, Zen of Python as project values during the call. Strongest cultural resonance of any interviewee.

---

## Session 14: Mike Mantell (UX design contractor)

- **Date:** Mar 4, 2026
- **Forum:** Video call (recorded)
- **Attendees:** Scott Wofford, Mike Mantell
- **Mike:** UX design contractor. Professional design/copy perspective. NOT ICP (not a developer, not a daily Claude Code user).
- **CX version:** v10 on `main` — no team section, no blog, ALL CAPS section labels ("WITHOUT LUTHIEN" / "WITH LUTHIEN"), nav: `ui | problem | architecture | [GitHub] | Setup help`.
- **Transcript:** Otter.ai `Rxaj9ooSUMjjDZneNmn34QoXHEk`
- **Gemini notes:** GDrive `Scott (Mike Mantell) - 2026/03/04 15:00 PST`
- **Outcome:** NOT a design partner (UX contractor, not daily Claude Code user). High-signal UX/copy feedback from a professional design perspective.

### Value prop feedback

#### Mike (UX design contractor, 2026-03-04)

**1. "Claude Code code" is a mouthful — "Let AI Code" variant reads easier**

> "Claude Code code" — three similar words in a row is awkward to say and read.

Mike flagged the phrase "Claude Code code" as a mouthful. The "Let AI Code" variant reads much easier.

**Analysis:** Copy friction. When the product name appears in sentences about code, the repetition creates a stumbling block. "Let AI Code" or restructuring to avoid "Claude Code code" would flow better.

**2. "Enforces your rules" is the standout hook — "that's active"**

> "Enforces your rules" — that's active.

Mike singled out "enforces your rules" as the strongest hook on the page. The active verb ("enforces") communicates agency — Luthien does something, rather than passively describing what it is.

**Analysis:** 14th user confirming lead-with-value (R2). "Enforces" is an active verb that conveys the core value prop in two words. This is the phrase to build the tagline around.

**3. CTA too early / no transition to action — gym trainer analogy**

Mike used a gym trainer analogy: the page jumps straight to "sign up" without building enough of a bridge. You need "one more step" between showing the value and asking for action — a transition that makes the CTA feel earned, not premature.

**Analysis:** The CTA appears before the reader has enough context to act. The page needs a bridging section that moves from "here's what Luthien does" to "here's how to try it" — not just a button. Reinforces R5 (zero-friction) but from a different angle: it's not that setup is hard, it's that the reader isn't ready yet.

**4. Before/after: height misalignment, caption text invisible**

Mike noted the Before and After screenshots are different heights, which makes visual comparison harder. Additionally, the caption text below the screenshots is too small/faint to read.

**Analysis:** 7th reviewer flagging before/after visual issues (R1). The height mismatch disrupts the natural left-right comparison that the before/after format is designed to create. Caption text needs to be visible to explain what the reader is looking at.

**5. Problem section overwhelms (70, 15, 19, 20) — "I don't want to read all this shit"**

> "I don't want to read all this shit."

The problem section with its multiple numbered categories (70 incidents, 15 quotes, 19 categories, 20 sources) creates information overload. Mike's reaction was visceral — too much to parse.

**Analysis:** Converges with Maria (Session 6: "cognitive effort"), Finn (Session 8: "would have just skipped"), Darren (Session 11: "requiring a lot of reading"). 4th independent reviewer flagging problem section density. The numbers that are meant to convey scale instead convey "this is going to take a while."

**6. Didn't realize quotes were clickable links — "not inclined to click"**

> "Not inclined to click."

Mike didn't realize the quote cards were clickable links to their sources. Even after being told, he said he wouldn't click them.

**Analysis:** The platform-authentic card design (established in Round 4b) makes cards look self-contained rather than interactive. If users don't discover the links, the cards are functioning as standalone proof-of-pain rather than verified citations. This may be fine — the cards work without clicking.

**7. Architecture diagram strong positive — "I like this diagram a lot"**

> "I like this diagram a lot."

Mike reacted positively to the architecture diagram. It was clear and easy to understand from a non-developer perspective.

**Analysis:** Converges with Finn (Session 8: "this is great, should be bigger") and Peter (Session 5: "Pretty much you have middleware"). The diagram is one of the strongest elements on the page across all reviewer types (developers and non-developers alike).

**8. "Rules and policies" — whose? Luthien's or mine?**

Mike was confused by the phrase "rules and policies" — it's ambiguous whether these are Luthien's built-in rules or the user's custom rules.

**Analysis:** Ambiguity in a trust claim. "Rules and policies" could mean either "the rules Luthien comes with" or "your rules that Luthien enforces." This is the R3 (two layers) distinction — the copy needs to make clear that Luthien enforces YOUR rules. "Your rules and policies" or "the rules you define" would clarify.

**9. "Active development" = step back — "I can't use this right now"**

> "Active development" — "I can't use this right now."

The phrase "active development" made Mike think the product isn't ready to use. It signals incompleteness rather than momentum.

**Analysis:** Intent vs. reception gap. "Active development" is meant to convey transparency and velocity (we're building fast). But it reads as "this is a beta and might break." Consider "Open source. Growing fast." or simply removing the disclaimer — the GitHub activity speaks for itself.

**10. "Suspicious stuff" too informal — "I want you to sound really credible"**

> "Suspicious stuff" — "I want you to sound really credible."

Mike flagged "suspicious stuff" as too informal for a product making security/trust claims. The register doesn't match the seriousness of what Luthien does.

**Analysis:** Tone mismatch for a trust product. "Suspicious stuff" has the deadpan energy of R9, but when you're selling safety infrastructure, informality can undermine credibility. "Suspicious behavior" maintains the meaning while sounding professional. Compare: Darren (Session 11) also flagged "suspicious" as carrying a lot of weight.

**11. "All without changing your dev setup" = infomercial-y**

Mike flagged "all without changing your dev setup" as sounding like a late-night TV pitch — "But wait, there's more!"

**Analysis:** The phrase is factually accurate and addresses a real objection (R5: zero-friction setup), but the phrasing pattern ("all without...") triggers marketing BS detectors. Restructure: state the fact without the infomercial frame. "Works with your existing Claude Code setup" or "No changes to your dev environment" — same info, different register.

**12. "What can it do" section visually flat after the diagrams**

After the architecture diagram (which Mike liked), the "What can it do" section loses visual energy. The contrast between the engaging diagram and the text-heavy capabilities section creates a dropoff.

**Analysis:** Visual hierarchy issue. The page builds momentum through the demo and architecture sections, then loses it. Jai (Session 10) also flagged this: "reshape [capabilities] as stories." The section needs either visual treatment (icons, cards) or narrative structure (user stories) to maintain engagement.

### Broader observations

- **Professional UX/copy perspective fills a gap.** Mike is the first professional designer to review the page (Darren is a designer but reviewed the landing page, not the README). His feedback is about craft — height alignment, caption legibility, copy register — not about whether the value prop works.
- **"Enforces your rules" is the tagline anchor.** Mike's response ("that's active") confirms this is the strongest single phrase on the page. 14th user validating lead-with-value.
- **Tone calibration for trust products.** Mike's "credible" feedback (points 10, 11) creates a tension with R9 (funny/relatable copy). The resolution: humor works in the problem section (developer quotes), but the solution/CTA sections need professional register. Two tones, one page.
- **CTA timing is a new insight.** Previous feedback focused on CTA content (Josh: "not book a call") and CTA friction (R5). Mike's gym trainer analogy adds a new dimension: CTA placement. Even a good CTA fails if it appears before the reader is ready.
- **Before/after issues persist.** 7th reviewer flagging visual problems. Height alignment and caption visibility are concrete, fixable issues that would improve the section immediately.

---

## Session 15: Maria Paula Mendieta + Jesse (landing page + README feedback)

- **Date:** Mar 4, 2026
- **Forum:** Video call (recorded)
- **Attendees:** Scott Wofford, Maria Paula Mendieta, Jesse
- **Maria:** Director of Product at Carbon Direct. Ex-economist/data scientist. REPEAT reviewer — previously gave feedback on v8 landing page (Session 6, Feb 26). Strong product/UX instincts. Not a developer.
- **Jesse:** Non-technical. First-time reviewer. Fresh eyes on messaging clarity.
- **CX version:** v10.1 on `feature/team-section` — team bios, blog section, lowercase labels ("without luthien" / "with luthien"), expanded footer. Nav: `ui | problem | architecture | team | blog | [GitHub] | Setup help`.
- **Transcript:** Otter.ai `QUGpSuDQI8AaEhnGOGUSKZsuh9A`
- **Gemini notes:** GDrive `m & j - 2026/03/04 09:45 PST`
- **Google Doc:** `1LZkC3YalrnBhUdULHEIOHmPpUP107U7s4NTN0FITipI`
- **Note:** Maria (Session 6, Feb 26) is a repeat reviewer — compare her v8 → v10 feedback evolution. Jesse is new.
- **Outcome:** NOT design partners (Maria = PM, Jesse = non-technical). Strong structural/UX/trust-signal feedback.

### Value prop feedback

#### Maria + Jesse (Carbon Direct PM + non-technical reviewer, 2026-03-04)

**1. Maria: "I don't understand what proxy is" / "I don't understand the problem"**

> Maria: "I don't understand what proxy is."

> Maria: "I don't understand the problem. Why I would need it."

Despite being a repeat reviewer (Session 6), Maria still couldn't articulate what Luthien does after reading the page. The word "proxy" is meaningless to non-technical audiences, and the problem statement doesn't land without developer context.

**Analysis:** Maria saw v8 in Session 6 and now v10.1 — and still can't explain the product. This isn't a first-impression problem; it's a persistent messaging gap. The page assumes developer context that even technically-adjacent PMs don't have. Reinforces R2 (plain English) and converges with Paolo's "proxy undersells" feedback (Session 13).

**2. Jesse: needs mission statement — "one sentence to walk away with"**

> Jesse: "When I go on to any company website, I need one sentence to, like, walk away with, like, what does this do for me? ...a mission statement, essentially... and it's the first time I'm seeing it."

Jesse expected a clear mission statement at the top of the page — a single sentence explaining what Luthien does and why it matters. The current hero copy doesn't provide this.

**Analysis:** The most basic requirement for any product page: tell me what you do in one sentence. Jesse's "first time I'm seeing it" means the mission appears too late (if at all). The hero should answer "what is this?" before anything else.

**3. Both: jargon overload — "judge model," "stochastic," "reduce latency" — "$10 words, need nickel words"**

> Jesse: "Judge model — don't know what that is."

> Jesse: "Cloud haiku makes me think of a poem."

> Jesse: "Reduce latency — literally don't know what that means."

> Jesse: "That's a $10 word. You need nickel words."

> Maria: "I don't know what the word stochastic means."

> Maria: "I see a lot of language that I don't understand."

Multiple instances of jargon that are natural for developers but opaque to anyone outside the field. "Judge model," "stochastic," "reduce latency," "Cloud haiku" — each one creates a speed bump for non-technical readers.

**Analysis:** The page is written for developers but R2 requires it to be legible to PMs who forward it. Every jargon term is a potential exit point. "Nickel words" is a perfect framing — use the simplest possible language. Where technical terms are necessary, define them inline.

**4. Jesse: quotes require too much thinking — "I have to think really hard to understand what happened"**

> Jesse: "I have to, like, think really hard to understand what happened. Like, really, really hard."

The developer frustration quotes (the core of the problem section) require context that non-technical readers don't have. The quotes are evidence of pain, but the pain isn't self-explanatory.

**Analysis:** Tension between the ICP (developers who immediately get these quotes) and the distribution channel (PMs who forward the page). The quotes that work best are self-explanatory — "Claude destroyed my entire project" lands universally. Quotes requiring developer context ("it used pip instead of uv") need either explanation or should be lower on the page.

**5. Maria: fewer but punchier quotes — separate 10-15 as use cases**

> Maria: "You could be going for quantity instead of quality. 70 is a lot... I would have less but more relatable and concrete."

> Maria: "Put very punchy ones here, and then treat another 10 or 15 as actual use cases... 'If you're running into this problem'... that would also help the user know that they could use your tool to solve a problem."

Maria wants to split the quote collection: a few punchy, self-explanatory quotes at the top, with the rest reframed as use cases ("If you're running into this problem, Luthien can help").

**Analysis:** This is the same structural feedback from Session 6 but more specific. Maria's reframe — quotes as use cases — is a compelling pattern. Instead of "look at all these problems," it becomes "do you have this problem? Here's how Luthien fixes it." Bridges from problem to solution. Converges with R3 (two layers) and R4 (complete the block story).

**6. Maria: external links break SEO, give chance to leave site**

> Maria: "You're breaking SEO rules... you're giving a chance for them to get distracted and not come back to your site."

> Maria: "You're sending people away from your call to action."

External links in quote cards send users to Twitter/X, GitHub issues, and blog posts — away from the Luthien page. Each link is an exit opportunity.

**Analysis:** The platform-authentic card design (Round 4b) was built around "the card IS the citation" — entire card clickable. Maria's point: citations that take you off-site compete with the CTA. Options: `target="_blank"` + `rel="noopener"` (already done), or remove the links entirely and just show the quotes as standalone proof.

**7. Jesse: "Covered it up" category unclear**

> Jesse: "What does it mean?" [about "covered it up" category]

> Jesse guessed: "It lied."

The incident category label "Covered it up" wasn't clear to Jesse. She had to guess at the meaning.

**Analysis:** Category labels need to be immediately obvious. "Covered it up" is the deadpan R9 register — funny to developers who know the pattern (AI hiding errors), confusing to everyone else. Consider: "Hid the problem" or "Concealed errors" — clearer while maintaining the tone.

**8. Jesse: ASCII art easter egg — "I hate it... looks like an accident"**

> Jesse: "I hate it... it reminds me of, like, early internet crap. You're getting too creative with the HTML."

> Jesse: "It looks like an accident."

> Maria: "It's not as funny as some of your quotes."

The ASCII art easter egg (hidden meme) was strongly negative for Jesse. Rather than feeling like a clever developer insider joke, it looked like a rendering error or broken formatting.

**Analysis:** Polarizing element. The ASCII art is intended as an easter egg for developers who appreciate terminal culture. But if non-developers encounter it (and they will), it damages credibility. Consider: keep it truly hidden (only visible in page source), or remove it. Maria's note that "it's not as funny as some of your quotes" suggests the real quotes do the humor work better.

**9. Jesse: Scott's bio too personal — "delete" the kids/spouse part. Maria: "don't say nine, round up"**

> Jesse: "Yours is too personal... Everything with 'two young kids and a nervous spouse' — delete it."

> Maria: "Don't say nine. Round up." [re: rounding "nine years" to "a decade"]

Jesse reacted strongly to the personal details in Scott's bio (kids, spouse) — the team section should be about professional credibility, not personal life. Maria flagged a smaller point: "nine years of experience" should round up to "a decade" for punchier copy.

**Analysis:** Team bios exist to build Luthien's credibility, not to humanize founders. Jesse's "delete" is blunt but correct for this context: a developer tools product page should show relevant expertise, not family details. Converges with the broader theme from both reviewers — center on Luthien, not on the individuals.

**10. Maria: need "About" section with founding story + mission**

> Maria: "Have an about section. Talk about your founding story, your mission, and then the expertise that each of you bring to the table."

> Maria: "Add blog posts about why you started [Luthien]."

Maria wants a narrative About section that tells the Luthien founding story — why it exists, what problem the founders saw, and what expertise they bring. The current team section has bios but no story.

**Analysis:** Finn (Session 8) was the first to ask "who are you guys?" Maria goes further: it's not just faces and titles, it's the founding narrative. Why did two people start an AI safety nonprofit? The story IS the trust signal. This is different from the team bios — it's about organizational credibility.

**11. Maria: "Setup help" sounds like talking to a human**

> Maria: "It makes it sound like I have to talk to a human, which I don't want to do."

The "Setup help" CTA button label implies human interaction (a support call), which creates friction for users who want self-service.

**Analysis:** CTA label precision. "Setup help" could mean documentation, a walkthrough, or a call. Engineers prefer self-service (R5). Consider: "Setup guide," "Get started," or "Quick start" — labels that imply documentation, not conversation. Converges with Josh (Session 7: "book a call = next").

**12. Jesse: blog posts too old — "I would not know if you're in business still"**

> Jesse: "It's too old. I would not know if you're in business still."

> Jesse: "I don't like the blog is on the same page."

The blog section shows posts with dates that are too far in the past. For Jesse, stale content signals an abandoned project — "are these people still working on this?"

**Analysis:** Content freshness as a trust signal. This is distinct from R6 (avoid AI slop) — it's about signaling that the project is alive and actively maintained. A blog section with old posts does more harm than no blog section at all. Either keep posts within ~2 months or remove the section.

**13. Maria: black color scheme doesn't convey safety/trust. Jesse disagrees (dev preference)**

> Maria: "When you're trying to build trust, black is a color that does the opposite... it's not conveying safety."

> Jesse: "I love black websites. It relaxes me."

Maria sees the dark color scheme as working against Luthien's trust/safety message. Jesse (a non-developer who nonetheless prefers dark themes) disagrees.

**Analysis:** Split signal. The dark theme was chosen to feel "developer-native" (Claude Session 9: "not marketing site pretending to be technical"). Maria is applying consumer product design principles where lighter colors = trust/safety. For developer tools, dark themes ARE the trust signal — they say "this is built for terminal users." Flagged but likely no action needed: the ICP expects dark mode.

**14. Maria: need LinkedIn company page. Don't link personal websites — "your value proposition should be centered on Luthien"**

> Maria: "I think you should have a Luthien LinkedIn page... I do that for every single early stage startup."

> Maria: "I look at the CEO and co-founder to make sure they have [LinkedIn]. The way I get to the person is by looking at the company first."

> Maria: "Your value proposition should be centered on Luthien, not on your career."

> Jesse: "Do you want the attention to go to Luthien, or do you want the attention to go to you?"

Maria checks LinkedIn for every early-stage startup she evaluates. No LinkedIn company page = credibility gap. Both Maria and Jesse converge on the same principle: the page should build Luthien's brand, not the founders' personal brands. Linking personal websites diverts attention.

**Analysis:** LinkedIn company page is a concrete, low-effort trust signal. Maria's evaluation pattern (company LinkedIn → founder LinkedIn → product) is probably common among PMs and BD people who evaluate tools. The "centered on Luthien" principle applies to bios, links, and overall page framing. Converges with Jesse's bio feedback (#9) — the team section should serve Luthien, not individual careers.

### Broader observations

- **Maria is a repeat reviewer (v8 → v10.1) and STILL can't explain the product.** This is the most important signal from this session. Despite structural improvements between versions, the core messaging gap persists for non-developer audiences. The page needs a one-sentence mission statement that works without developer context.
- **Jesse provides the "fresh eyes" non-technical perspective.** Her feedback is consistently about clarity and simplicity — mission statement, nickel words, self-explanatory quotes. She represents the person a PM forwards the link to who has zero AI development context.
- **"Center on Luthien, not on you" is the unified theme.** Both reviewers independently converge: team bios should be professional, not personal; links should keep users on-site; the value proposition is about the product. Personal details dilute the product message.
- **Content freshness = viability signal (new theme).** Jesse's "would not know if you're in business still" is a trust signal not captured in existing requirements. Stale blog posts, old dates, and infrequent updates signal abandonment. This applies to blog, team section, and GitHub activity. Potential new requirement R10.
- **Jargon kills comprehension for the distribution channel.** Jesse's "$10 words, need nickel words" is the clearest articulation of the R2 tension: the page is written for developers but distributed by PMs. Every jargon term is a potential "I don't understand, I'm not forwarding this" moment.
- **Quote selection matters more than quantity.** Maria's "fewer but punchier" + Jesse's "I have to think really hard" converge: self-explanatory quotes (like "Claude destroyed my entire project") work universally, while context-dependent quotes only work for the ICP. Lead with universal ones.
- **ASCII easter egg: remove or truly hide.** Both reviewers had negative reactions. The developer audience might appreciate it, but if it "looks like an accident" to non-developers, it damages credibility more than it builds culture.

---

## EAG session: Sergi Lange-Soler (README cold-read feedback)

- **Date:** Feb 15, 2026
- **Forum:** In-person at EAG SF
- **Attendees:** Scott Wofford, Sergi Lange-Soler
- **Sergi:** British developer building a solo Android app with LiveKit + Python backend. Uses Claude Code on Sonnet (~£17/month UK plan). Pretty hands-on workflow. Has heard of Redwood's AI control agenda.
- **CX version:** README on GitHub (likely same version as Tyler's Feb 10 session or close to it)
- **Source:** SuperWhisper transcript: `_User-Interview-Notes/Sergi Lange-Soler/EAG SF Feb 2026 — Superwhisper transcript.md`

### Value prop feedback

#### Sergi (solo developer, EAG SF, 2026-02-15)

**1. "I don't really understand what's happening" — README intro didn't resonate**

> "To be honest, right now, not resonating that much with the intro there."

> "I kind of don't really understand what's happening. I don't understand what it's about."

**Analysis:** Cold-read failure. Sergi landed on the README and couldn't parse the value prop from the first paragraph. Consistent with Maria (Session 15: "I don't understand what proxy is") and Jesse ("I need one sentence to walk away with"). The intro fails for both non-developers AND early-stage developers.

**2. "Seems kind of similar to CLAUDE.md files" — the baseline differentiation question**

> "Can I just put this in the CLAUDE.md file? Can I just put in CLAUDE.md: please use UV instead of pip install? And then like 90% plus of the time, it'd use UV."

> "It seems kind of similar to CLAUDE.md files. That's my reaction."

**Analysis:** The most strategically important feedback from this session. Same question as Josh Levy (Session 7: "what does Luthien do that a system prompt can't?") but from a different persona — Josh asked it as a researcher thinking about baselines, Sergi asks it as a pragmatic user wondering why he should bother. The landing page MUST answer this question prominently. The answer: context rot (CLAUDE.md instructions get forgotten over long sessions), enforcement (proxy can actually block, not just suggest), and observability (you can see what happened).

**3. Claude Code update breakage concern**

> "The way this connects with Claude Code, how am I going to get a Claude Code update and will this stop working and then I'll have to change my workflow again?"

**Analysis:** New friction signal not raised by any other interviewee. Sergi is worried about dependency on a fast-moving upstream product. If Claude Code ships a breaking change, does Luthien break? This is a legitimate concern for a tool that sits between the client and backend. Scott: "Thank you for saying that. I hadn't heard that feedback before."

**4. Docker dependency is friction for solo developers**

> "Not really to be honest." (re: "Do you typically have Docker running?")

**Analysis:** Sergi doesn't use Docker regularly. For solo developers without a Docker-heavy workflow, the Docker dependency is an extra install step. Converges with Finn (Session 3/8: setup took ~10 minutes) and Peter (Session 5: Python version mismatch).

**5. CLAUDE.md compliance degrades over conversation length**

> "I think it usually does at the start of the context of the note, the start of the conversation, and then it kind of gets lazy and stops doing it."

**Analysis:** Independent confirmation of context rot from a solo developer with a simple setup. Third user (after Quentin and Josh) to explicitly describe the "high compliance early, low compliance later" pattern. This is the exact scenario where a proxy adds value over CLAUDE.md alone.

**6. "dangerously skip permissions" tension — safety vs speed**

Sergi is considering enabling "dangerously skip permissions" for speed but worried about: (a) file deletions outside his codebase, and (b) gradual code spaghettification. Astute distinction: file deletion is a safety issue (addressable by rules), spaghettification is a capabilities issue ("I can't just prompt it to be more capable").

**Analysis:** Luthien could address the safety half of this tension — let users run with skip permissions while the proxy catches destructive actions. The capabilities half (spaghettification) maps to code quality policies (YAGNI, DRY, backward compat cleanup).

### Broader observations

- **Sergi + Josh = the two strongest "why not CLAUDE.md?" voices.** Both asked the same question from different perspectives (researcher vs. practitioner). The answer must be prominent, specific, and backed by the context rot evidence.
- **Breakage concern is new and legitimate.** No other user raised this. Worth addressing on the README: "Luthien uses the standard Anthropic API format — Claude Code updates don't break the proxy."
- **Solo developers are a different persona from team leads.** Sergi doesn't need team-wide enforcement or multi-user context sharing. His value proposition is narrower: safety guardrails for "dangerously skip permissions" usage. This maps to the destructive action guardrails policy idea.

---

## Session 16: Mike Mantell — V11 Draft Review & Positioning Workshop (Mar 11, 2026)

- **Date:** Mar 11, 2026
- **Forum:** Google Meet
- **Attendees:** Scott Wofford, Mike Mantell
- **Mike:** UX design contractor. Professional copy/marketing perspective, not a developer. Not a Claude Code user.
- **CX version:** v10.6/v10.7 landing page + Mike's V11 draft (PAS framework)
- **Source:** Gemini notes: `Scott (Mike Mantell) - 2026/03/11 15:29 PDT`, debrief doc: `_Seldon_labs/Mike Mantell/2026-03-11_mike-debrief-proposed-cards.md`
- **TLDR:** [0-tldr-user-interview-takeaways.md](0-tldr-user-interview-takeaways.md#mike-mantell-mar-4--mar-11-2026)

### Value prop / positioning feedback

#### Mike Mantell (UX contractor, Mar 11, 2026)

**1. Audience awareness spectrum: vibe coders → average devs → super devs**

Based on Scott's ~30-40 user interviews, Mike helped frame the audience: "vibe coders" who just yell at the code harder, "average devs" who use CLAUDE.md + prompt engineering but haven't considered output validation, and "super devs" — the graduation target. Average devs know PR review bots but not real-time output validation.

**Analysis:** This framework clarifies Luthien's positioning: it's an "upstream, complementary" solution to post-commit PR review bots. The average dev → super dev graduation is the product's value narrative. The README should frame Luthien as the next step for developers who already use CLAUDE.md files.

**2. V11 draft: PAS (Problem, Agitate, Solution) framework**

Mike built a V11 draft using the PAS copywriting framework. Assumes the audience is "problem aware" — they know Claude misbehaves but haven't found a solution. The structure: (1) remind them of the problem's gravity, (2) agitate by showing it won't get better on its own ("the answer isn't better prompts or longer CLAUDE.md files"), (3) present Luthien as the infrastructure-level solution.

Also experimented with a white background to convey safety and ease, departing from the dark developer aesthetic.

**Analysis:** PAS is a proven framework for problem-aware audiences. The "not better prompts or longer CLAUDE.md files" reframe directly addresses the Sergi/Josh baseline question. White background is a departure from developer conventions — should be A/B tested (Maria Session 15 also flagged dark = "not trustworthy" but ICP expects dark mode).

**3. AI safety mission: does "AI safety" build trust or carry baggage?**

Jesse's feedback suggested moving the AI safety mission statement higher on the page to build trust. Mike raised a counter-concern: does explicitly mentioning "AI safety" actually build trust with developers, or does it carry baggage (academic, preachy, anti-progress)?

Resolution: testing resolves the ambiguity. Mike assigned to create a testable version or explain why it's not worth the effort.

**Analysis:** This is a genuine tension. The AI safety mission is authentic and differentiating (vs. competitors who are pure dev tools), but the label may alienate developer audiences. The answer likely depends on the sub-audience: Redwood/EA-adjacent devs will see it as a trust signal; mainstream devs may see it as a red flag. Worth A/B testing.

**4. Easter egg: if important, put in main copy**

Current easter egg conveys developer duality (AI hype + job insecurity) but feedback says "1995 aesthetic," not prominent enough. Mike's instinct: "If it's important enough to convey, it should be in the main copy, not hidden as an Easter egg."

**Analysis:** Converges with Maria/Jesse (Session 15: "looks like an accident") but adds a constructive reframe: the empathy message is worth conveying, just not as an easter egg. Either elevate it to a visible section ("Has this ever happened to you?") or drop it.

**5. Cold-send email: personalize + CTA = book time, not read page**

Scott drafted a design partner outreach email. Mike's feedback: too spam-like. Should add personal reference to previous meeting, remove generic second paragraph. Primary CTA should be "book the time," not "read the landing page."

**Analysis:** Distribution feedback, not product feedback. But relevant because the email IS part of the value prop funnel. If the email doesn't convert, the README never gets read. Personal touch + direct CTA is standard outbound best practice.

**6. Onboarding: single terminal command**

Current 7-step README is friction. Jai working on single `curl | bash` style install (like Codex competitor). This changes the CTA from "try it yourself" (which requires reading instructions) to a terminal-based instruction.

**Analysis:** Strongest actionable feedback from this session. Single-command onboarding removes the biggest friction signal from Finn (Session 3), Peter (Session 5), and every EAG conversation. When this ships, the README CTA changes fundamentally.

---

## EAG SF Sessions: Value Prop Reactions (Feb 13-15, 2026)

Multiple EAG conversations included README read-throughs or product reactions. Key value-prop signals extracted here; full session details in [0-tldr-user-interview-takeaways.md](0-tldr-user-interview-takeaways.md#eag-sf-conversations-feb-13-15-2026).

### Cross-cutting EAG value prop themes

**1. "Seems similar to CLAUDE.md" is the #1 objection**

Four EAG conversations independently surfaced this: Sergi ("seems kind of similar"), Marcus ("couldn't I just put this in Claude MD?"), Aaron ("my Claude MD seems to have dealt with this fine"). This is now the single most common initial reaction (also from Josh, Tyler). The README MUST address this head-on, ideally above the fold.

**2. Claude Code update breakage is a real fear**

Three EAG users (Sergi, Matt Handzel, Anshul) independently worried about proxy compatibility with Claude Code updates. Anshul was the most direct: "another source of confusion/breakage on top of Claude Code's already-changing behavior." The README should include a compatibility commitment.

**3. Docker friction blocks non-Docker users**

Sergi, Aaron, and multiple EAG users don't run Docker regularly. Single terminal command (Mike Mantell Session 16 feedback) addresses this directly. Until then, Railway/cloud option reduces friction for users who don't want Docker competing with their dev environment.

**4. Quantify catch rates (Dylan's feedback)**

Dylan suggested putting false positive/false negative rates "right in your face" on the README. This converges with Tyler's benchmark data request and the Anthropic internal monitor data (50% recall at 0.1% FPR on Sonnet). Quantified performance claims build credibility.

**5. Risk-severity indicator (Marcus's idea)**

Marcus wants green/yellow/red indication for actions: "that'd be so useful." This is a UX feature that directly addresses the dangerously-skip-permissions tension — let users run fast while getting severity-graded warnings on dangerous actions.

*Last updated: 2026-03-12 (added Mike Mantell Mar 11 session, EAG SF cross-cutting themes)*
