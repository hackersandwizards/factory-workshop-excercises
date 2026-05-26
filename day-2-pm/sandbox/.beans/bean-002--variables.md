---
id: bean-002
title: Variablen
type: feature
status: open
---

## Description

Der Calculator soll Variablen unterstützen. `let x = 5` setzt eine Variable. Ein nachfolgendes `x + 3` ergibt dann `8`. Eine unbekannte Variable führt zu einem lesbaren Error. Der State überlebt die REPL-Session, aber nicht den Prozess (in-memory ist ok).

**Hinweise:**

- Der Lexer braucht neue Token-Typen für `LET`, `IDENT` und `ASSIGN` (`=`).
- Der Parser braucht eine Statement-Ebene: entweder `assignment` oder `expression`.
- Der Evaluator braucht ein Environment, z. B. `std::unordered_map<std::string, int64_t>`.
- Identifier-Regeln: starten mit Buchstabe, dann beliebig Letter/Digit (keine Unicode-Sorgen).

## High-Level Plan

(wird von Planner-Skill befüllt, Phase 1 — Plan-Bullets + erste Acceptance Criteria)

## Refined Plan

(wird von Refine-Skill befüllt, Phase 2 — Files/Signaturen/Test-Sketch)

## Implementation Log

(wird von Implement-Skill befüllt, Phase 3 — Branch + Commit-SHAs)
