# Fabien Rogers / Luthien — April 1, 2026

## Agenda

### 1. Recap of Nov 19 call
- Your role: alignment science team, offline monitoring on internal traffic, building blocking classifiers
- Monitors: prompted black-box models (slightly weaker than monitored model); considering switch to trained models
- Three contribution paths you identified for Luthien: **(a)** training data for monitors, **(b)** evals for prosaic misalignment, **(c)** UX for classifier integration
- Key insight: smooth transition expected from prosaic → scheming ("same type signatures, small data change")
- We discussed Claude Code hooks (launched that day) + server-side tool call approval

### 2. Luthien updates since then
- 254 PRs, 4 contributors. Highlights:
- **Policy composition system**: serial/parallel chains with LLM judges, 5 consolidation strategies, 7 preset demos
- **Prosaic failure catalog from real users**: test-cheating (comments out failing tests), plan abandonment, self-destruction (agent killed its own proxy), silent failures
- **Full conversation logging** with policy intervention labels — raw material for training data, export pipeline not yet built
- **Onboarding**: `pip install luthien-cli && luthien onboard` — no Docker needed
- **User trials**: Tyler/Redwood (strongest design partner), Kushal/Relativity (3,500 engineers), hackathon (Jai spoke/judged)

### 3. Fabien updates since then
- a. Did you switch from prompted → trained monitors?
- b. New risk reports or model cards?
- c. SHADE-Arena — how does this relate to your monitoring work?
- d. Any new UX patterns for classifier integration in Claude Code?

### 4. Open questions Fabien might have takes on
- What format would make our logged sessions most useful as training data for your monitors?
- Do our prosaic failure types (test-cheating, plan abandonment) map to threat models you're building classifiers for?
- Is server-side tool call approval still an interesting integration pattern, or has the landscape shifted?

### 5. Next steps
- a. Define a training data export format — pilot with one session type
- b. Pick 1-2 prosaic failure types and build targeted evals
- c. Regular cadence? (You offered monthly last time)
