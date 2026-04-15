# asks/AGENTS.md

Each file in this directory is one self-contained scope of work. You should be able to execute an ask without reading any other ask file.

## Template

Every ask file follows this structure:

```markdown
# <Ask title>

## Summary
<1–3 sentences: what this ask is and why>

## Context pointers
- What to read first (file paths + PR numbers)
- Invariants to preserve

## Deliverables
- [ ] Concrete, verifiable item
- [ ] ...

## Non-goals
- Things to explicitly NOT do (prevents scope creep)

## Access needed
- GitHub permissions, Railway account, credentials

## Success criteria
- Observable state that means "done"

## Verification
- How Luthien and counterweight_ can confirm it's done

## Authority
- What decisions you can make unilaterally (default: all Railway implementation)
- What to surface to Scott (business strategy, customer-requirement changes)
```

## Conventions

- Naming: `<phase-or-scope>-<kebab>.md` (e.g. `phase-1-stabilize.md`, `day-1-dogfood.md`).
- **Self-contained.** Repeat context if you have to. No "see other ask first" chains.
- **Verifiable deliverables.** Every checkbox should be something Scott can observe without asking you.
- **Authority section is required.** Don't make the reader guess who decides.
- **Non-goals section is required.** Naming what's excluded is how we prevent drift.

## When to add a new ask file

- You've identified a scope that doesn't fit any existing ask
- The scope is bigger than a single issue and needs its own deliverables/non-goals framing
- Open a PR (or push directly — see repo-root AGENTS.md) with `docs: add <new-ask>.md`

If a scope fits inside an existing ask, just open a GitHub issue against this repo and link the ask file.
