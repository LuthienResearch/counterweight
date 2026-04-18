# v6 Post-Mortem: Why the Mockups Failed

**Date:** 2026-03-18
**Tested with:** Finn Metz (Seldon Labs), live trial
**Mockups tested:** v6 Option A (Toggles), Option B (Demo), Option C (Status Board)

---

## What happened

Finn was shown all three v6 options for ~60 seconds each during a live session.

- **Option A (Toggles):** "What changed? I don't care. I don't know what to do with that." Tried clicking "configure" - nothing happened. Didn't understand the blocked log.
- **Option B (Demo): Winner.** "That's better. I understand what DeSlop means. Pretty good. I like it." Understanding came from seeing it work, not reading a description.
- **Option C (Status):** "Nice KPIs" on the stats. "Recent activity doesn't help me at all."
- **Overall:** "I don't get either of them in almost none of the versions, but I get the DeSlop one."

## Root causes

### 1. Non-functional interactive elements destroyed trust

The "configure" button on Option A existed visually but did nothing when clicked. Toggles looked clickable but had no visible state change feedback. Finn tried to click "configure" and got nothing - this made the mockup feel broken, not aspirational.

**Lesson:** Every clickable element in a mockup must do something visible, even if it's just showing/hiding a panel with mock data. If a user tries to interact and nothing happens, they stop evaluating the concept and start evaluating the quality of the prototype.

### 2. Value was described, not demonstrated

Options A and C described what policies do (text labels, stats). Option B showed what a policy does (before/after comparison). Finn understood Option B immediately because seeing is believing. The others required reading and inferring.

**Lesson:** Show, don't tell. A before/after demo communicates faster than any description.

### 3. Simple find-and-replace is not enough for the target user

Finn's key insight: "The very simple exchange thing would probably not be useful in most cases. I would need to have another LLM to rephrase those things specifically." DeSlop (string replacement) is a good demo, but power users want LLM-based evaluation + auto-retry. M-dashes are the #1 AI tell, but the fix users want is more sophisticated than search-and-replace.

**Lesson:** Demo the simple case, but make it clear that more powerful policies exist. Don't let users think Luthien is only a text cleaner.

### 4. Multi-policy was invisible

Josh (Slack, Mar 12) asked "can't have multiple policies active at the same time?" The v6 mockups only showed one policy active, which implied single-policy was the limit.

**Lesson:** Default state should show multiple policies active. Don't make users guess about capabilities.

## What v7 changes

- All interactive elements have working JavaScript (toggles, configure expand/collapse, sample selectors)
- Three browser mockups: demo-first (B1), LLM judge blocking demo (B2), style guide custom policy (B3)
- Three terminal mockups: inline feedback (T1), blocked + retry (T2), session summary (T3)
- Multiple policies shown active by default in B1
- LLM judge + auto-retry shown in B2 and B3 to address "simple replacement is not enough"
