---
id: bean-001
title: Klammer-Support
type: feature
status: open
---

## Description

Der Calculator soll Klammern unterstützen, um Auswertungs-Reihenfolge explizit steuern zu können. `(1+2)*3` muss `9` ergeben, `((1+2))` muss `3` ergeben (verschachtelt). Unbalancierte Eingaben wie `(1+2` führen zu einem lesbaren Parse-Error statt einem Crash.

**Hinweise:**

- Der Lexer braucht zwei neue Token-Typen für `(` und `)`.
- Der Parser braucht eine neue Production-Rule für `group`, die in `factor` eingebunden wird.
- Bestehende Tests müssen weiter grün bleiben — Regression-Schutz nicht vergessen.

## High-Level Plan

(wird von Planner-Skill befüllt, Phase 1 — Plan-Bullets + erste Acceptance Criteria)

## Refined Plan

(wird von Refine-Skill befüllt, Phase 2 — Files/Signaturen/Test-Sketch)

## Implementation Log

(wird von Implement-Skill befüllt, Phase 3 — Branch + Commit-SHAs)
