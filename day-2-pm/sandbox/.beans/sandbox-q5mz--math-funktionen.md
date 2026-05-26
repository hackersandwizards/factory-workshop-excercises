---
# sandbox-q5mz
title: Math-Funktionen
status: todo
type: feature
priority: low
created_at: 2026-05-26T10:15:59Z
updated_at: 2026-05-26T10:15:59Z
---

Calculator soll mathematische Funktionen unterstützen: `sqrt(9)` ergibt 3, `sin(0)` ergibt 0, `cos(0)` ergibt 1. Das erfordert Floating-Point — der Lexer muss `.` lesen (`1.5`) und Mixed-Types (`1 + 1.5 == 2.5`) müssen funktionieren.

**Hinweise:**

- Tiefere Änderung: Token-Typ-System (NUMBER → INT + FLOAT) oder einheitlich double.
- Evaluator-Werte-Representation muss erweitert werden (z. B. `std::variant<int64_t, double>` oder durchgehend `double`).
- Funktions-Aufruf-Syntax: Parser bekommt neue Rule `call → IDENT '(' expr ')'`.
- Erwartet bestehende Tests werden ggf. angepasst werden müssen — Trade-off-Decision Teil der Übung.