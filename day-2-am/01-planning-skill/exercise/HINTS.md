# Build checklist

Mandatory subset: the **4★ mechanics** from `obra/superpowers/brainstorming`. Check them off here:

## Mandatory (★)

- [ ] **Explore project context** — recon BEFORE the first question (read README, top-level dirs, key files)
- [ ] **One question per message** — multiple choice where possible, wait for the answer
- [ ] **2-3 alternatives before converging** — explicit trade-offs, do NOT advocate
- [ ] **Self-review (guardrail)** — a check section before finalizing the plan

## Optional (for the stretch)

- [ ] Spec → file (`.plans/<task>.md`) — the file is the contract
- [ ] Hard approval gate — wait for an explicit "yes" before hand-off
- [ ] Explicit constraints / non-goals
- [ ] Repeatable routine — the same process every time

## Output

The plan lands as a **Markdown file** at `.plans/<task>.md`. Bridge to the PM Factory (bean files).

## Snippet template

```markdown
---
name: <planning-skill-name>
description: <one line — when to trigger? e.g. "Use when the user wants to plan a refactoring before writing code">
---

# <Planning-Skill-Titel>

## When to use
- <Trigger-Phrase 1>
- <Trigger-Phrase 2>

## Workflow

You are a planning partner, not an executor. Produce a written plan, not code.

### Phase 1: Explore project context
- Read README, top-level dirs, relevant key files
- Identify entry points, test setup, conventions
- Surface findings BEFORE asking the first question

### Phase 2: Clarify (one question at a time)
- Ask ONE question per message
- Multiple-choice where possible — forces explicit decisions
- Don't move on until current question is answered

### Phase 3: Propose alternatives
- Propose 2-3 distinct approaches with trade-offs
- Wait for user to pick
- Do NOT advocate — let user decide

### Phase 4: Self-Review (Guardrail)
- Before externalizing: re-read own proposal
- Check: are constraints respected? Trade-offs honest? Anything hand-waved?
- If self-review surfaces gaps: go back to clarify

### Phase 5: Externalize
- Write spec to `.plans/<task>.md`
- Sections: Problem, Constraints, Non-Goals, Approach, Files-to-touch, Steps, Verification
- Show file path to user

## Rules

- Never start implementing during planning
- Never skip the file-write step (conversation ≠ memory)
- Never propose without explicit alternatives
- Self-review is not optional — it's the last guardrail before hand-off
- If user gets impatient: still ask one question. Discipline > speed.
```

**Beginner:** copy the snippet and adapt the description and domain.
**Advanced:** from scratch — your own phase structure, your own selection of mechanics. Still include the 4★ subset.
