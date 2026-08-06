# Planned eval cases (sketch, not an evals.json)

This file describes in prose what a later `/skill-creator` eval run should
check for the planner. It is **deliberately not** a finished `evals.json` —
the JSON schema of the skill-creator plugin is not verified at this point.
The real `evals.json` should be generated through the interactive
skill-creator flow ("evaluate my planner skill with skill-creator"), not
rebuilt by hand.

## Scenario 1 — hard rule (computational check)

Prompt: `/planner Find duplicates in the customer list`.
Expectation: the generated ticket body contains no file paths, no function
signatures and no class names in the `## High-Level Plan` section. Checkable
automatically by pattern match (e.g. for `.py`, `.ts`, `def `, `class `,
`/` path patterns) — a sensor, no model judgement needed.

## Scenario 2 — one question per message (inferential check)

A prompt with several open points at once (e.g. audience, deadline, blast
radius all unclear). Expectation: the skill asks exactly one question per
reply, not several bundled together. This cannot be checked purely
structurally (counting lines is not enough) — it needs a model judgement on
whether only one decision per message is really being asked for.

## Scenario 3 — disable-model-invocation (non-trigger check)

A prompt that sounds like planning thematically, but where the skill is NOT
called explicitly via `/planner` (e.g. "could you sketch out how we'd
approach this?"). Expectation: the skill does not trigger on its own — no
ticket is created, no backend call is made. Checkable computationally (no
ticket-creating call in the tool log for that session).

## Scenario 4 — heading contract (computational check)

After `/planner ...` and a completed ticket: the stored description contains
the heading `## High-Level Plan` exactly (no typo, no different level such
as `### High-Level Plan`). This is the contract `/refine` (day 2) relies on
— if the contract breaks, refine breaks.

## Scenario 5 — optional, comparative

Pipeline comparison: planner output → `/refine` → implementation, once with
a careful ticket (all phases completed) and once with a ticket that skipped
phase 3 (alternatives). Measures whether the planning time invested shows up
as less rework in the implementation phase. More of a demo building block
for block 6 (twist) than a classic pass/fail eval.
