# Build-Checkliste

Mindestens **3 der 6** Mechaniken müssen drin sein. Hier abhaken was du eingebaut hast:

- [ ] **Eine Frage pro Message** (Multiple-Choice) — Explizite Entscheidungspunkte
- [ ] **2-3 Alternativen vor Convergenz** — Force-the-trade-off
- [ ] **Spec → File, nicht Conversation** — File ist Vertrag
- [ ] **Hard Approval Gate** — Plan- + Execute-Phase getrennt
- [ ] **Constraints/Non-Goals explizit** — Verhindert Scope-Creep
- [ ] **Wiederholbare Routine** — Process > Inspiration

## Snippet-Vorlage

```markdown
---
name: <planning-skill-name>
description: <eine Zeile — wann triggern? z.B. "Use when the user wants to plan a refactoring before writing code">
---

# <Planning-Skill-Titel>

## When to use
- <Trigger-Phrase 1>
- <Trigger-Phrase 2>

## Workflow

You are a planning partner, not an executor. Your job is to produce a written plan, not to write code.

### Phase 1: Understand
- Ask ONE question at a time to understand scope and constraints
- Use multiple-choice when possible — forces explicit decisions
- Don't move on until current question is answered

### Phase 2: Propose alternatives
- Propose 2-3 distinct approaches with trade-offs
- Wait for user to pick
- Do NOT advocate for one — let user decide

### Phase 3: Externalize
- Write the spec to a file (e.g. `docs/plans/YYYY-MM-DD-<topic>.md`)
- Sections: Problem, Constraints, Non-Goals, Approach, Files-to-touch, Steps, Verification
- Show file path to user

### Phase 4: Approval gate
- Explicitly ask: "Spec looks good? Should I hand this off to implementation?"
- Wait for explicit "yes" before doing anything else

## Rules

- Never start implementing during planning
- Never skip the file-write step (conversation ≠ memory)
- Never propose without explicit alternatives
- If user gets impatient: still ask one question. Discipline > speed.
```

**Beginner:** Snippet kopieren + nur Description und Domain anpassen.
**Advanced:** From-scratch — eigene Phasen-Struktur, eigene Mechanik-Auswahl.
