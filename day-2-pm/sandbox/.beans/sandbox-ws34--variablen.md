---
# sandbox-ws34
title: Variablen
status: todo
type: feature
created_at: 2026-05-26T10:15:59Z
updated_at: 2026-05-26T10:15:59Z
---

Calculator soll Variablen unterstützen. `let x = 5` setzt eine Variable. Nachfolgendes `x + 3` ergibt 8. Unbekannte Variable führt zu lesbarem Error. State überlebt die REPL-Session, aber nicht den Prozess (in-memory ok).

**Hinweise:**

- Lexer braucht `LET`, `IDENT`, `ASSIGN` (`=`).
- Parser braucht Statement-Ebene: entweder `assignment` oder `expression`.
- Evaluator braucht ein Environment (z. B. `std::unordered_map<std::string, int64_t>`).
- Identifier-Regeln: starten mit Buchstabe, dann Letter/Digit (keine Unicode-Sorgen).