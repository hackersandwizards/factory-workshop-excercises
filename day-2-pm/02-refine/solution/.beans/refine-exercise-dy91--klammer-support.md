---
title: Klammer-Support
status: todo
type: feature
created_at: 2026-05-26T10:15:46Z
updated_at: 2026-05-26T10:15:46Z
---

Du findest eine Calculator - Software im sandbox folder in day-2-pm.

Der Calculator soll Klammern unterstützen, um Auswertungs-Reihenfolge explizit steuern zu können. `(1+2)*3` muss 9 ergeben, `((1+2))` muss 3 ergeben (verschachtelt). Unbalancierte Eingaben wie `(1+2` führen zu einem lesbaren Parse-Error statt einem Crash.

**Hinweise:**

- Der Lexer braucht zwei neue Token-Typen für `(` und `)`.
- Der Parser braucht eine neue Production-Rule für `group`, die in `factor` eingebunden wird.
- Bestehende Tests müssen weiter grün bleiben — Regression-Schutz nicht vergessen.