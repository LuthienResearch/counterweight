# EAG SF Workflow

## Goal

**Goal 1a: Recruit Design Partners** — Find 5 developers willing to commit to biweekly calls despite bugs. These partners complete Goals 2 & 3 — they do the guided and external trials.

**Design partner criteria:**
- Uses AI coding agents daily
- Frustrated enough to tolerate early-stage software
- Willing to do biweekly 30-min calls for 3+ months

---

## BEFORE EAG (Mon-Thu)

- Swapcard search: filter attendees by relevance (daily Claude Code users, AI tooling, safety)
- Screener criteria (all three = pursue, derived from [bullseye customer worksheet](https://docs.google.com/spreadsheets/d/1SyN6dPfHXkuQQ0Xwm5hEE82vdmFtYcnLqp1KcJKIq3I/edit?gid=526823761#gid=526823761)):
  - (a) Uses AI coding agents daily
  - (b) Senior enough to install their own tools
  - (c) Has a detailed claude.md (or equivalent rules file)
- Yes/no decision per person
- Send meeting invites to yes's

## AT EAG (Fri-Sun)

**During conversation:**
- Capture in user interview meeting notes (Otter.ai transcript / Superwhisper)
- 60-sec voice memo immediately after with key takeaway

Then move on to next person. Don't process, don't synthesize, just capture.

**Each evening:**
1. Organize notes in Drive (move recordings + transcripts to meeting notes folder)
2. Prompt Claude Code to synthesize into themes
3. Update requirements (ui-fb-dev/2-versions-requirements/)
4. Update UI mocks if warranted (ui-fb-dev/3-ui-mocks/)
5. Repeat

**Threshold for UI update:** If 3+ people say the same thing, update before tomorrow.

## AFTER EAG (Mon+)

- Follow up with yes's
- Get them to try Luthien
- Capture feedback (ui-fb-dev/1-feedback-synthesis/)
- Loop continues: feedback -> requirements -> UI -> more feedback
