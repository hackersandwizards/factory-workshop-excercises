---
id: bean-003
title: Math-Funktionen
type: feature
status: open
---

## Description

Der Calculator soll mathematische Funktionen unterstützen: `sqrt(9)` ergibt `3`, `sin(0)` ergibt `0`, `cos(0)` ergibt `1`. Das erfordert Floating-Point — der Lexer muss `.` lesen können (`1.5`), und Mixed-Types wie `1 + 1.5 == 2.5` müssen sauber funktionieren.

**Hinweise:**

- Tiefere Änderung im Token-Typ-System: entweder `NUMBER` aufspalten in `INT` + `FLOAT` oder durchgehend auf `double` umstellen.
- Die Werte-Representation im Evaluator muss erweitert werden, z. B. `std::variant<int64_t, double>` oder konsequent `double`.
- Funktions-Aufruf-Syntax: der Parser braucht eine neue Rule `call → IDENT '(' expr ')'`.
- Erwartet: bestehende Tests müssen ggf. angepasst werden — die Trade-off-Entscheidung ist Teil der Übung.

## High-Level Plan

(wird von Planner-Skill befüllt, Phase 1 — Plan-Bullets + erste Acceptance Criteria)

## Refined Plan

(wird von Refine-Skill befüllt, Phase 2 — Files/Signaturen/Test-Sketch)

## Implementation Log

(wird von Implement-Skill befüllt, Phase 3 — Branch + Commit-SHAs)
