# Outreach Page - Live Requirements

**Owner:** Scott
**Last updated:** 2026-03-18
**Feedback sources:**
- [Finn Metz live trial (Mar 18)](https://docs.google.com/document/d/1o9duAvfLb_YMfeZsjJHdzVgLSrXIGzKoq3LMdAxP92c) - hackathon page feedback, installation walkthrough
- [Tyler Tracy (Feb 10)](https://docs.google.com/document/d/1lRX5U7_2Ig1oOw775xm9uoGGK6yJx2gip8N2BlAA0JQ) - live install, README review
- [Tyler Tracy (Mar 3)](https://docs.google.com/document/d/1v4c7d-8loBxjTvb6xOyig-6rwI2kW6ZV4l125VAJ_dI) - trial doc feedback, benchmark discussion
- Jai Dhyani (Mar 18) - hackathon page direction

---

## Document objective

Articulate requirements for pages that invite potential users to engage with Luthien: try it, build on it, or give us structured feedback (screen recordings, bug reports, usage impressions).

### Related documents (out of scope here)

- [1-value-prop-requirements-live.md](1-value-prop-requirements-live.md) - what Luthien is, how to explain it, README/landing page copy
- [5-policy-config-requirements-live.md](5-policy-config-requirements-live.md) - policy configuration UI
- [Apart hackathon page](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22) - AI control explainer, 3 tracks with example ideas, prizes, format, who should participate

---

## Personas

### The Redwood engineer

Based on Tyler Tracy (Senior SDE, Redwood Research) and the people he'd forward Luthien to.

Tyler leads a 10-person engineering team at Redwood, all remote. He uses Cursor and Claude Code daily, spends 10-40% of his time on technical work, and hates context-switching to web UIs ("sucks transition between main workflow and web-based UIs"). He's building Linux Arena, a control evaluation framework. He installed Luthien live on a call (Feb 10) and it was the smoothest external trial ever. His reaction: "Maybe I should just tell them to use this" -- meaning deploy to his whole team.

But Tyler is cautious about forwarding tools to his team. He used to be more of an early adopter, but now he's skeptical: "There are a lot of things that are trying to do this... I don't have any data to know that yours is better or like actually works." He needs benchmark evidence, not pitch copy. When asked what would make him trust a tool, he said: video demos (references Fire Ship, coding YouTubers), benchmark results ("before Luthien the database is deleted 10% of the time, after Luthien 0%"), and institutional credibility ("guy from Amazon, I wouldn't care as much. Someone from OpenAI, maybe a bit more"). Random developer quotes don't move him.

The person Tyler would forward Luthien to is a contractor or team member who already understands AI control conceptually ("the core idea is inherently interesting to them") but needs zero friction to try it. Tyler explicitly flagged that the trial doc was "not necessarily clear what this is" for cold sends. This persona doesn't need convincing about the concept -- they need proof that it works and a fast path to running it.

**What motivates this persona:** Evidence of efficacy (benchmarks, not claims). Fast setup. Trust signals from credible sources. They don't want to do us a favor -- they want a tool that actually helps.

**Sources:** [TLDR](../1-feedback-synthesis/0-tldr-user-interview-takeaways.md#tyler-tracy--redwood-research-feb-10--mar-3-2026), [Session 4](../1-feedback-synthesis/1-value-prop-feedback.md#session-4-tyler-tracy-redwood-research--live-install), [Session 12](../1-feedback-synthesis/1-value-prop-feedback.md#session-12-tyler-tracy--redwoodluthien-sync-readme--trial-doc-feedback)

### The hacker

Based on Finn Metz (Seldon Labs advisor, hackathon co-organizer) and his description of a typical Apart hackathon participant.

This person signed up for the Apart Research AI Control Hackathon (529 signups, Mar 20-22). They've heard about AI control, maybe attended an Apart hackathon before. They're remote, browsing Discord on Friday morning while half-listening to a talk. They don't have a project idea yet. They're looking for both an idea and a team. Most participants "are kind of there because they like the thing and they kind of heard about this and like, hey, this sounds fun."

They landed on a Luthien link because Kamil (Apart organizer) posted it in the Discord announcements, or because Tyler mentioned it, or because Jai plugged it in his noon talk. The convincing happened before they got here. Finn: "The convincing happens because Kamil or Tyler or you guys tell me that this is cool... the site should probably link to that or reiterate the TLDR." They have 3 other tabs open and are willing to poke around and explore, but they have 3 days to build something cool, so they need inspiration fast.

What they care about: "If you could give me like three or four rough ideas that immediately spark a match in my brain of like 'oh this is so cool I could build on top of this,' that would be great." The current landing page "doesn't immediately give me a thing that I could build." They want project ideas, not a platform pitch.

They also care about the people behind it. Finn: "I want to know you guys. I want to like you guys. If I don't know or like you guys, I don't want to do this." But they don't want to do "work" to engage. The feedback page with its screen recordings and email reports felt like a job, not a hackathon experience. Jai: "The leading call to action should be pitching it as a tool and/or a thing to build on... People at hackathon are by definition already time constrained."

The Apart hackathon page already explains the tracks, prizes ($2K total + $1K LinuxArena from Equistamp), and format (3 days, research report submission, self-organized teams). Our page should not repeat this.

**What motivates this persona:** Cool project ideas they can start building immediately. Knowing real people are behind the tool and available on Discord. They're giving us their weekend -- the page needs to spark ideas fast.

**Sources:** [Finn transcript](https://docs.google.com/document/d/1o9duAvfLb_YMfeZsjJHdzVgLSrXIGzKoq3LMdAxP92c), [hackathon-context.md](../0-outreach4feedback/hackathon-march-2026/hackathon-context.md), [Apart hackathon page](https://apartresearch.com/sprints/ai-control-hackathon-2026-03-20-to-2026-03-22)

---

## Feedback/trial page versions

For design partners, QA testers, and anyone we're asking for structured feedback. Target: the Redwood engineer.

| Version | Date | What it was | Permalink | Feedback |
|---------|------|-------------|-----------|----------|
| **v1: QA trial page** | Feb 26, 2026 | Original version for Upwork QA testers. 5-part structure: screen recording, dev workflow, landing page evaluation, README quickstart, email report. Titled "QA Trial." | [@ 4c0de49](https://github.com/LuthienResearch/luthien-pbc-site/blob/4c0de49/site/qa-trial/index.html) | Peter (Feb 25): used for first QA trial. Tyler (Mar 3): "not necessarily clear what this is" for cold sends. |
| **v2: Feedback page** | Mar 6, 2026 | Renamed to "Request for Feedback." Updated for generic audience. Same 5-part structure. | [@ 4444b97](https://github.com/LuthienResearch/luthien-pbc-site/blob/4444b97/site/feedback/index.html) | Finn (Mar 18): "too much work" for hackathon context. Works for scheduled research sessions, wrong for time-constrained visitors. |

## Hackathon page versions

For Apart hackathon participants. Target: the hacker.

| Version | Date | What it was | Permalink | Feedback |
|---------|------|-------------|-----------|----------|
| **v1: Hackathon page** | Mar 18, 2026 | Hero + 8 project idea cards + quickstart link + Discord. Forked feedback page CSS. | [@ 3ab030a](https://github.com/LuthienResearch/luthien-pbc-site/blob/3ab030a/site/hackathon/index.html) | Not yet shown to users. Too long (8 cards is a wall). Re-pitches Luthien in callout. No photos/bios. No connection to Apart page's track ideas. |

---

## Current Requirements

### Feedback/trial page requirements

| # | Requirement | Current state (v2) | Key evidence |
|---|-------------|---------------------|--------------|
| R1 | The visitor must feel a personal connection to the people behind Luthien -- enough that they'd be willing to spend extra time giving us feedback, not just using the tool. People help people they know and like, not faceless projects. Photos, bios, and self-deprecating honesty build this connection faster than feature lists. The Redwood engineer cares about institutional credibility (Jai's background, Redwood connection). The hacker cares about personal warmth (are these people real, will they be on Discord when I'm stuck at 2am). | v2 has no photos, no bios, no personality. Just "Request for Feedback" and an email address at the bottom. It's a form, not a human asking for help. | Finn: "I want to know you guys. I want to like you guys. If I don't know or like you guys, I don't want to do this." Tyler: institutional affiliation matters ("guy from Amazon, I wouldn't care. Someone from OpenAI, maybe a bit more"). Tyler: video > text for trust. |
| R2 | Additional information must be easily accessible without cluttering the page. Want to know what Luthien is? Link to the landing page. Want to get started? Link to the GitHub README. The page should be focused (R1 + the ask) with everything else one click away. | v2 duplicates context about Luthien in a callout instead of linking. README link buried below 5 parts of structured feedback protocol. | Apart page explains AI control and tracks. Landing page explains Luthien. README has setup instructions and communicates setup ease. Don't duplicate -- link. |
| R3 | The visitor must know how to get help when stuck. Channel must match context: call link for design partners, email for async. | v2 says "email Scott." No call booking link. | Finn: clunky setup even with live facilitation. Tyler's contractors would need support but wouldn't email a stranger. |

### Hackathon-specific requirements

These layer on top of R1-R3 for the hacker persona.

| # | Requirement | Current state (hackathon v1) | Key evidence |
|---|-------------|------------------------------|--------------|
| R4 | The page must show how Luthien specifically enables the hackathon's track ideas. The Apart page already lists "giving the trusted model access to a firewall" (Track 2), "environments with security vulnerabilities" (Track 1), and "dataset of sneaky transcripts" (Track 3). Our page connects those to Luthien: we ARE the firewall, we DO the interception, we LOG the transcripts. Ideas should map to tracks so participants can self-sort and find teammates. | v1 has 8 standalone idea cards with no connection to the Apart page's track descriptions. Ideas read like our own pitch rather than "here's how Luthien fits what you're already looking for." | Finn: "three or four rough ideas that immediately spark a match in my brain." The match should connect to ideas they've already seen on the hackathon page. LinuxArena has a separate $1K Equistamp prize worth calling out. |
| R5 | The page must tell the visitor exactly how to reach us AND give them confidence we'll actually be there throughout the hackathon when they get stuck. Not just "Discord" but specifics: Jai is a speaker and judge (talk Friday noon), Scott is on Discord all weekend, DM us or tag @luthien, or book a 15-min call. The visitor should feel like they have a direct line to real humans who will be responsive in real time, not a support email that might reply Monday. | v1 has Discord + call link but no detail about who will be where when. Needs specifics about availability. | Kamil coordinates announcements via Discord. Tyler ("Tylord") already active there answering questions. Finn: "I want to know you guys." Discord is where hackathon people live. The confidence that help is available matters as much as the channel itself. |

---

## Open questions

Ideas to explore, not requirements yet:

- **Site nav integration:** Should the hackathon page be a section of the luthien-pbc-site? Users could navigate between the landing page and the hackathon page. Options: (a) add `/hackathon` to the nav bar, (b) make it a section on the landing page, (c) keep it standalone. The landing page currently has no nav -- adding one changes the feel.
- **YouTube video intro:** Tyler said "GitHub repos that have a video at the beginning... would make me trust it a bit more." Scott's pitch: "We're working backwards from a demo presentation on April 16. We're rapidly iterating and collecting user feedback, so we'd really appreciate any and all feedback you have on what we've built so far. We'd love to hear what you'd like us to build next. And if you're so inclined, help us build it." Could be one generic video that covers both personas, or two (one hackathon-specific, one for Redwood). Generic is faster to ship and probably sufficient -- the personal connection (R1) matters more than targeting.
- **Embed video on the page vs link to YouTube:** Embedded feels more immediate (visitor doesn't leave). YouTube link gets views/SEO. Could do both -- embed with a "watch on YouTube" link.

---

## Appendix A: Out of scope

These are covered by other documents or are constraints, not requirements.

**Be factual: describe what exists today.** Luthien can: proxy, log, run policies (regex, DLP, LLM-as-judge), block responses. Cannot: auto-retry/resample, one-liner CLI install, multi-agent coordination. Pitching unshipped features wastes their time and destroys trust. (Tyler: fictional class names in YAML "undermine trust." Finn asked about auto-retry -- Jai confirmed it's not shipped.) This is table stakes honesty, not a design requirement.

**Lead with utility, not "help us."** Already captured in [1-value-prop-requirements-live.md](1-value-prop-requirements-live.md) R1: "Lead with features/value, not setup." Jai (Mar 18): "Pitch it as a tool, not as us asking for help." Finn: "The convincing happens not on this page."

## Appendix B: Design principles for outreach/CTA pages

Principles drawn from [dev tool landing page research (Evil Martians, 100 pages studied)](https://evilmartians.com/chronicles/we-studied-100-devtool-landing-pages-here-is-what-actually-works-in-2025) and [landing page best practices (Zoho, 2026)](https://www.zoho.com/landingpage/landing-page-design-principles.html):

- **One page, one purpose, one CTA.** Strip away everything that doesn't serve the primary action. For the feedback page: "try Luthien and record what happens." For the hackathon page: "pick a project idea and start building."
- **Visual hierarchy: headline and CTA first.** In one glance, people should know what you're offering and where to click. Most important elements above the fold.
- **No salesy BS.** Dev tool pages that work: "clever and simple wins." Avoid corporate language. Two humans building a thing beats a marketing team.
- **Two CTAs in the hero.** Primary action (e.g. "Get started") + secondary (e.g. "View GitHub" or "Watch demo"). Secondary is visually distinct -- outlined or lighter.
- **Social proof via people, not logos.** Curated testimonials or bios with photos. For early-stage: the founders' faces and credentials ARE the social proof.
- **Scannable content.** Headers, bullet points, white space. Nobody reads paragraphs on a landing page.
- **Mobile-first.** Sticky CTA button, large tap targets. Hackathon participants are on laptops but also phones.

## Appendix C: What was deleted from the feedback page for hackathon

| Feedback page element | Why deleted | Requirement |
|----------------------|------------|-------------|
| Screen recording requirement | Solves our research need, not theirs | R1 |
| Dev workflow walkthrough (15 min) | Irrelevant -- they have a hackathon task | R2 |
| Landing page evaluation section | We're not testing messaging right now | Out of scope: don't re-pitch |
| "Email results to Scott" | Output is their hackathon project, not a report to us | R1 |
| Part numbering / time badges | Implies a long structured process | R2 |

---

## Changelog

- **2026-03-18**: Created. Two personas (Redwood engineer, hacker) with detailed evidence. Deduplicated against value-prop requirements.
- **2026-03-18**: Rewritten with excruciating persona detail from Tyler Tracy sessions (Feb 10, Mar 3) and Finn Metz transcript (Mar 18).
- **2026-03-18**: Merged R1+R2 into R1 (personal connection is the reason to engage). Renamed personas. Moved design principles to appendix.
- **2026-03-18**: Split into two requirement tables (feedback/trial + hackathon). Renumbered versions (feedback: v1 QA trial, v2 feedback; hackathon: v1). Permalinks pinned to git commits. R2 reframed as "setup is easy, communicate that." R3 reframed as "link, don't duplicate." Added open questions (video, site nav). Replaced design principles with researched CTA/landing page principles. Appendix A renamed to "Out of scope." Sources linked to Gemini notes.
