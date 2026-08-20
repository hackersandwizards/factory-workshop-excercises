# Day 2 · Exercise 04 — Review (Review-Rework-Converge Loop)

**Slot:** Block 4, pairing sessions · phase 4 of the Factory pipeline

> **New for Barista — no original template.** Unlike Planner/Refine/Implement,
> this skill does not exist anywhere yet: it is not in the original
> exercise repo, and there is no reference solution branch. You are
> building the actual mechanism the agenda calls the **Review-Rework-Converge
> Loop**, not copying/adapting an existing one. Treat `exercise/HINTS.md` as
> a starting checklist, not a spec — deviating from it in a way that still
> satisfies the goal below is fine.

## Goal

Green tests are not the same as "done". Build a `review` skill that checks
an implemented ticket against its **Acceptance Criteria** — not just
against whether the tests pass — and either sends it back to Refine
(rework) or marks it done (converge).

## Why this exists

Implement's test loop only proves the code does what *someone thought to
test*. It says nothing about whether the result actually satisfies what the
ticket asked for. The gap between "tests green" and "acceptance criteria
met" is exactly what Review closes.

## Prerequisites

- A ticket from `../03-implement` with status completed: `## Refined Plan`,
  `## Implementation Log` (branch, commits, test status), and the original
  `## High-Level Plan` (with its Acceptance Criteria) still in the ticket
  body/description
- The feature branch from Implement still exists locally, tests green

## Task

Detailed hints + build checklist: `exercise/HINTS.md`. Skeleton:
`exercise/.claude/skills/.gitkeep` — an empty starting point, the skill is
built from scratch.

1. Copy `exercise/.claude/` into the repo you're pairing on.
   `mkdir .claude/skills/review && touch .claude/skills/review/SKILL.md`.
2. Frontmatter: `name: review`, `argument-hint: <ticket-id>`,
   `allowed-tools: Read, Grep, Glob, Bash, Task` (+ Jira MCP tool if used).
   Read-only on source, same as Refine — a review that edits code while
   reviewing it is not a review.
3. Phase 1: read the ticket. Pull out **three** things: the Acceptance
   Criteria from `## High-Level Plan`, the `## Refined Plan`, and the
   `## Implementation Log`.
4. Phase 2: get the actual diff — `git diff main...feat/<ticket-id>-<slug>`
   (the branch name is in the Implementation Log).
5. Phase 3: dispatch **ONE** subagent (or do it inline if your pair prefers
   — decide and justify) that checks the diff against **each** Acceptance
   Criterion individually, not against the diff as a whole. For each AC:
   met / not met / can't tell, with a one-line reason pointing at the diff.
6. Phase 4 (Converge decision):
   - All AC met → mark the ticket `completed` (or leave it, if Implement
     already did), append a `## Review` section confirming pass.
   - Any AC not met → send it back: move status to `in-progress` (or
     whatever your board calls "needs another Refine pass"), append a
     `## Review` section listing exactly which AC failed and why. This is
     the "back to Refine" arrow from the agenda diagram — for the exercise,
     writing the failing ACs into the ticket in a form Refine could act on
     is enough; you do not have to actually re-run `/refine` in this slot.
7. Hard rule: the review verdict is never "tests are green, so ship it" —
   it must reference the Acceptance Criteria explicitly, one by one.

## Hard rule — rework cap, hook-enforced

Without a limit, a ticket can bounce between Refine and Implement forever
without ever converging — expensive, and worse, unnoticed. **Maximum two
rework cycles**, same number as Implement's "two fix attempts, then abort"
pattern — this is a running motif across the whole workshop (Implement's
fix loop, the Day 1 planner mini-eval), not a coincidence.

Consistent with Day 1's "a prompt instruction is a request, not a
constraint" lesson: this one cap is **hard-enforced via a hook**, not just
skill-level text. Every other hard rule in today's material (Implement's
"never push/merge") stays prompt-only for time reasons — this is the one
place we actually follow through on the harder path, because it's the
gate against the single most expensive failure mode (a silently looping,
never-converging ticket).

Mechanism:

1. Review maintains a local counter file per ticket:
   `.claude/state/rework-count/<ticket-id>.txt` (plain integer, default 0
   if missing).
2. Every time Review decides "not converged" and sends the ticket back, it
   increments this counter as part of its Phase 4 write.
3. A **PreToolUse hook** sits in front of the exact tool call that
   transitions the ticket status back to "needs another Refine pass" (a
   `beans update ... -s in-progress` Bash call for the beans backend, or
   your Jira MCP's transition tool — match whichever your pair actually
   uses). The hook reads the counter file for that ticket ID; if it's
   already at 2, it blocks (exit code 2) with a message explaining the cap
   was reached and that the skill should escalate to a human instead
   (status → e.g. `needs-human`, with a `## Review` note explaining why).
4. Because the hook blocks the specific write, Review's own logic never
   gets a chance to send the ticket back a third time — the cap holds even
   if the skill's own reasoning "forgets" to check it.

This is required, not optional — build the counter file and the hook as
part of this exercise, not just the AC-by-AC review logic above.

## Self-Check

- `/review <ticket-id>` produces a `## Review` section in the ticket
- The verdict lists each Acceptance Criterion individually with met/not-met
  and a reason tied to the diff — not one blanket sentence
- No source files were edited by the review skill itself
- Test: deliberately implement a ticket that passes its tests but misses
  one AC (your trainer will hand pairs a prepared example, or reuse the one
  from the Hook) — the skill must catch it and send it back, not wave it
  through because CI is green
- Test: with the rework counter file manually set to `2`, a 3rd send-back
  attempt is blocked by the hook and Review escalates to a human instead

## Solution

None exists yet — see the note at the top. If your pair finishes early,
compare notes with another pair instead of a reference branch; differences
in how the AC-check is worded are the interesting part.

## Learning Goals

- Tests and Acceptance Criteria check different things — green tests are a
  necessary, not sufficient, condition for "done"
- The Converge decision is a genuine branch point in the pipeline, not a
  formality: "back to Refine" has to be a real, taken path in your build,
  not just a comment
- A prompt instruction is a request, not a constraint — the rework cap is
  the one hard rule today that's actually hook-enforced instead of just
  written down, and it holds even if the skill's own reasoning forgets to
  check it
- Orchestration in miniature: this is the piece that turns a linear
  Planner→Refine→Implement chain into a loop
