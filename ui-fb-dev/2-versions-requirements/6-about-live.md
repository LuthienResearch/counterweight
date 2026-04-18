# About Page — Live Requirements

Owner: Scott  
Last updated: 2026-04-11  
Feedback source: Internal review + adjacent user feedback (value-prop sessions, hackathon page feedback) + **2026-04-09 Scott/Jai call on pitch & about page direction**

---

## What this doc is

The single source of truth for what we're building on the About page. Requirements come from user feedback and get questioned before entering the backlog.

Feedback lives elsewhere — this doc links to it but doesn't duplicate it:

- `../1-feedback-synthesis/1-value-prop-feedback.md` — raw quotes from sessions including Finn, Maria, Jesse, Tyler, Josh
- `1-value-prop-requirements-live.md` — landing page requirements (R8: security trust, R11: team section builds Luthien credibility)
- `2-feedback-hack-requirements-live.md` — outreach page requirements (R1: personal connection)

---

## Every version of this page

| Version | Date | What it was | Permalink | Who saw it | User Feedback |
|---|---|---|---|---|---|
| v0: No about page | Pre-Apr 2026 | No dedicated About page exists. Team bios appeared briefly on feature/team-section branch (v10.1) as a section of the landing page. | v10.1 @ feature/team-section | Maria + Jesse (Mar 4) | Jesse: "team bios too personal — center on Luthien not individuals." Maria: "I do check LinkedIn for every single early stage startup." |
| v1: Mike's MVP draft | 2026-04-04 → 2026-04-08 | Mike Mantell produced an HTML draft with a comic, diagram, "What We're Up To" section, "Our Approach" section, and mission copy. Went through several iterations (updated comic, beefed-up mission, credibility logos). | Slack attachments in `#better-luthien-ui` thread `1775297033.957859` | Scott, Mike iterating | Scott shared with Jai on 2026-04-06 for pre-ship review. |
| v2: Team-first minimal | 2026-04-08 → 2026-04-11 | Shipped with Lumen palette migration (PR #41). Stripped to page header + Team grid + footer. No Mission section, no comic, no diagram. Team bios intentionally Luthien-centered per R2. | `site/about.html` @ main prior to PR #XX | Public (luthien.cc/about.html) | Jai on 4/09 call: "I just want to drop this personally… more downside than upside" (re: the comic Mike produced). |
| v3: Inline quotes per founder | 2026-04-11 | Adds Jai's and Scott's first-person quotes inline under each team card (italic, no attribution box since each quote sits directly below its speaker's photo and name). "team" section label at left per the landing page pattern. No separate Mission section, no comic, no diagram. | `site/about.html` @ main after [PR #85](https://github.com/LuthienResearch/luthien-pbc-site/pull/85) | Public (luthien.cc/about.html) | Landed after several iterations (separate "Why" section → inline card with attribution → inline italic with no attribution). Jai's quote pulled verbatim from the 2026-04-09 call. Scott's quote provided 2026-04-11: "I left Amazon to work on this because powerful agents are about to be everywhere, and we need to make sure they follow the rules." |

---

## 5 Whys

**Surface problem:** Visitors don't know who is behind Luthien or whether the project is credible and active.

**Why?** The landing page leads with product and technical content. No page surfaces team identity, institutional affiliation, or project status in one place.

**Why does that matter?** For early-stage dev tools, trust in the people comes before trust in the product. Visitors evaluate whether to try something partly based on whether they believe the team can execute.

**Why can't they just look elsewhere?** There's no LinkedIn company page, no team section. Blog does serve as Freshness Signal. Visitors who care about these signals hit dead ends.

**Root problem:** A visitor who wants to know whether Luthien is worth their time — and whether the people behind it are credible — has no page to go to.

---

## Requirements

| # | Requirement (problem only) | Current state as of 2026-04-04 | Key evidence |
|---|---|---|---|
| R1 | <u>Credibility before product.</u> Visitors must be able to evaluate the team's credibility before deciding whether to try Luthien. Institutional affiliation, relevant background, and a human face matter more than a feature list at this stage. | No about page exists. Team bios appeared in previous versions, but felt tacked on the end. | Maria (S15): "I do check LinkedIn for every single early stage startup." Tyler (S7): "guy from Amazon, I wouldn't care as much. Someone from OpenAI, maybe a bit more." Finn (S3): "I want to know you guys. I want to like you guys. If I don't know or like you guys, I don't want to do this." |
| R2 | <u>Luthien-centered bios.</u> Team bios must frame each person's background in terms of what it means for Luthien, not for the individual. Visitors should leave understanding why this team is suited to build this product. | v10.1 team section was described as "too personal" — bios read as personal brand content rather than credibility signals for the product. | Jesse (S15): "value prop centered on Luthien." Maria (S15): "don't link personal websites." |
| R3 | <u>Proof the project is alive.</u> Visitors must be able to tell that Luthien is active and being maintained. A project that appears dormant will not be adopted. | Jesse (S15): "I would not know if you're in business still." R10 candidate from value-prop doc: "content freshness signals viability." |
| R4 | <u>One place for trust signals.</u> A visitor who wants to verify Luthien's legitimacy must be able to find all relevant trust signals (team, affiliation, mission, status) in one place without hunting across pages or external sites. | Trust signals are scattered or missing: no About page, no LinkedIn company page at time of writing, no single entry point for credibility evaluation. | Maria (S15): "I do check LinkedIn for every single early stage startup." Finn (S3): "I want to know you guys." Tyler (S7): institutional credibility matters before benchmark data. |

---

## Questioning the requirements

- **R1 — Is this real?** Yes. Three independent users across different sessions named team credibility as a factor in whether they'd try the tool. This is not internal assumption.
- **R2 — Is "Luthien-centered" too prescriptive?** It's a content constraint, not a design solution. The requirement is real: visitors should leave with more confidence in the product, not the person.
- **R3 — Does this belong on About or elsewhere?** Blog post dates, a changelog, or a "last updated" note on the landing page could also solve R3. About page is one location. The requirement is page-agnostic.
- **R4 — Is this a real requirement or just a summary of R1–R3?** R4 is distinct: it's about consolidation, not content. A visitor who has to cross-reference LinkedIn, GitHub, and the landing page to answer "are these real people?" has a navigation problem, not just a content problem. R4 is real.

---

## Decisions from 2026-04-09 Scott/Jai call

Pitch + Luthien <> Seldon weekly check-in, 2026-04-09 10:30 PDT. About-page discussion: transcript `01:17:23` → `01:25:50`.

- **Recording:** https://drive.google.com/file/d/1URJokQzAqXZYXvHytcpYRg7G_zo80y1S/view
- **Gemini notes:** https://docs.google.com/document/d/1MABg287ZT6Rl2OI2S6fIxSWrZsMR8ad5Bg4Skhlhf0c/edit
- **Slack thread:** `#better-luthien-ui` thread `1775297033.957859` (started by Mike Mantell, 2026-04-04)

### Jai, verbatim

On the comic draft Mike produced:
> "I just want to drop this personally. I I I don't think that this is a a good direction. I don't think that I think I think there's more downside than upside. Uh I think that the potential upsides are very limited. … like I'm I'm willing to keep an argument, but like my my gut and most my think thinking on this is is strongly against"

On "What We're Up To":
> "I'm I'm inclined to kill what we're up to. One, because it's kind of become fail quickly. … Like two two because like I I I don't know what it adds here like to like the the hook here."

On the Mission section:
> "I think uh like the idea of us being cloud code power users is is good. Um, I think like this this is this is a a a good place for us to do like a little first person uh commentary like uh this is where I I I don't I'd want to put uh we built this because this is me projecting my sentiment uh onto the or but I think this justified I was furious furious that that this didn't already exist and I wanted to change that. We we wanted to change that. Uh this just a thing that that should exist. Um, we we want AI to do the things that we want it to do and we want this to be consistent uh and and predictable and we want to be able to do whatever we want. We want we want to have uh full control over over identic that's not subject to cloud science to ignore cloudmd."

On tone and the "Our Approach" section:
> "I strike we don't want to slow down a progress. Uh one because I I would that's entirely entirely objective statement. … Uh and two because yeah I I think actually just like framing this as like aggressively subjective and being like we want this. This is what the thing that we want things to do. … Uh if you benefit that's cool. We want this."

On Teams placement:
> "I think I want teams to be the the top thing on this page. Uh, two reasons. One, I think that's that's the thing people are most looking for when they when they go when they go to about. Uh, and two, it has pictures. Uh, and look at pretty pictures got attention."

### Scott, verbatim (for context)

Opening the topic:
> "there is an open question about the about page. … basically I had Mike do the comic thing and the about page and he was like hesitant on it. Then I like got we got gave him feedback on the call like yeah just do it and then now it's in pause. I think what should happen is we should talk about it right now and then I'll take another stab. It's still not where I want it to be."

Scott confirming and summarizing:
> "so we're definitely killing the comment comment."
>
> "I want to kill the diagram."
>
> "We've already got that question is do we also kill what we're up to?"
>
> "I think we'll keep we'll we'll replace what's there with what you just said."
>
> "I think what you should do is also tell Claude to just implement what you just said and see what it comes back with. And um I can tweak the words tonight if needed."
>
> "we're we're going to update uh our current about based on the conversation … And it's just limited to the our mission section."

### Decisions (as stated on the call)

1. Kill the comic. *(Jai: "I just want to drop this personally.")*
2. Kill "What We're Up To". *(Jai: "I'm inclined to kill what we're up to.")*
3. Kill the diagram. *(Scott: "I want to kill the diagram." Jai: "Well, also good.")*
4. Strike "we don't want to slow down progress" from the "Our Approach" section. *(Jai.)*
5. Rewrite the Mission section using Jai's words quoted above — first-person, "cloud code power users," "furious that this didn't already exist," "full control," "not subject to Claude deciding to ignore CLAUDE.md."
6. Teams section at the top of the page. *(Jai.)*
7. Scope of this revision is the Mission section only. *(Scott.)*
