# Build-Checkliste

Pflicht-Subset: **4★ Mechaniken** aus `obra/superpowers/brainstorming`. Hier abhaken:

## Pflicht (★)

- [ ] **Explore project context** — Recon BEVOR erste Frage (Read README, top-level dirs, key files)
- [ ] **Eine Frage pro Message** — Multiple-Choice wo möglich, warten auf Antwort
- [ ] **2-3 Alternativen vor Convergenz** — explizite Trade-offs, NICHT advocaten
- [ ] **Self-Review (Guardrail)** — Check-Sektion vor Plan-Abschluss

## Optional (für Stretch)

- [ ] Spec → File (`.plans/<task>.md`) — File ist Vertrag
- [ ] Hard Approval Gate — explizit "yes" abwarten vor Hand-off
- [ ] Constraints/Non-Goals explizit
- [ ] Wiederholbare Routine — gleicher Process jedes Mal

## Output

Plan landet als **Markdown-File** in `.plans/<task>.md`. Bridge zu PM-Factory (Bean-Files).

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

**Beginner:** Snippet kopieren + Description und Domain anpassen.
**Advanced:** From-scratch — eigene Phasen-Struktur, eigene Mechanik-Auswahl. Trotzdem 4★ Subset drin.
