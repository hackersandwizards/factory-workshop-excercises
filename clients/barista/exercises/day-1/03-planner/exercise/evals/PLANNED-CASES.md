# Planned Eval Cases (Skizze, kein evals.json)

Diese Datei beschreibt in Prosa, was ein späterer `/skill-creator`-Eval-Lauf
für den Planner prüfen sollte. Es ist **bewusst kein** fertiges `evals.json`
— das JSON-Schema des skill-creator-Plugins ist an dieser Stelle nicht
verifiziert. Das echte `evals.json` sollte über den interaktiven
skill-creator-Flow generiert werden ("evaluate my planner skill with
skill-creator"), nicht von Hand nachgebaut.

## Szenario 1 — Hard Rule (computational check)

Prompt: `/planner Suche nach Duplikaten in der Kundenliste`.
Erwartung: der erzeugte Bean-Body enthält im `## High-Level Plan`-Abschnitt
keine Dateipfade, keine Funktionssignaturen, keine Klassennamen. Prüfbar
automatisiert per Pattern-Match (z. B. auf `.py`, `.ts`, `def `, `class `,
`/`-Pfadmuster) — ein Sensor, kein Modell-Urteil nötig.

## Szenario 2 — One question per message (inferential check)

Prompt mit mehreren offenen Punkten gleichzeitig (z. B. Zielgruppe,
Deadline, Blast-Radius unklar). Erwartung: der Skill stellt in jeder
Antwort genau eine Frage, nicht mehrere gebündelt. Das lässt sich nicht rein
strukturell prüfen (Zeilenzahl reicht nicht) — braucht ein Modell-Urteil,
ob inhaltlich wirklich nur eine Entscheidung pro Nachricht verlangt wird.

## Szenario 3 — Disable-Model-Invocation (non-trigger check)

Prompt, der thematisch nach Planung klingt, aber der Skill NICHT explizit
per `/planner` aufgerufen wird (z. B. "kannst du kurz skizzieren, wie wir
das angehen?"). Erwartung: der Skill triggert nicht von selbst — kein Bean
entsteht, keine Bean-CLI wird aufgerufen. Prüfbar computational (kein
`beans create`-Aufruf im Tool-Log dieser Session).

## Szenario 4 — Heading-Contract (computational check)

Nach `/planner ...` und abgeschlossenem Bean: `beans show <id>` enthält die
Überschrift `## High-Level Plan` exakt (kein Tippfehler, keine andere
Ebene wie `### High-Level Plan`). Das ist der Vertrag, auf den `/refine`
(Tag 2) sich verlässt — bricht dieser Vertrag, bricht Refine.

## Szenario 5 — Optional, vergleichend

Pipeline-Vergleich: Planner-Output → `/refine` → Implementierung, einmal
mit sorgfältigem Bean (alle Phasen durchlaufen) und einmal mit einem
Bean, der Phase 3 (Alternativen) übersprungen hat. Misst, ob die investierte
Planungszeit sich in weniger Rework in der Implementierungsphase
niederschlägt. Eher ein Demo-Baustein für Block 6 (Twist) als ein
klassischer Pass/Fail-Eval.
