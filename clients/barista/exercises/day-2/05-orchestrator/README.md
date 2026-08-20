# Day 2 · Exercise 05 — Orchestrator: one prompt, the whole pipeline

**Slot:** Block 5, ~10 min · **Trainer-led live demo, not a participant
exercise.** One person types one prompt into a single Claude Code session
and lets it drive Refiner → Implementer → Reviewer via the Task tool.

## Why this exists

By this point the group has a `Ready-for-Factory` ticket (Block 5, "Ticket
+ Planner") and working Refine/Implement/Review skills (built by pairs in
Block 4, merged in Block 5/7). This exercise is the moment those pieces
become one thing: no script, no code — a single natural-language
instruction that orchestrates the whole loop and ends at the **Light
Switch** (Block 3's Light-vs-Dark-Factory framing): the point where control
deliberately goes back to a human.

## Scope, deliberately cut down

An earlier draft of this prompt added per-checkpoint review cycles inside
Implement (Implement flags a checkpoint → Reviewer checks that slice →
back to Implement if it fails). Cut for the live demo — extra complexity
that isn't needed to make the point, and it would need its own rework-cap
hook (the one built in `04-review` only guards the ticket-level "back to
Refine" loop, not a per-checkpoint one). Worth mentioning verbally as "this
can go further" if it comes up, but not built or demoed today. The
orchestrator below uses **one loop only**: the ticket-level
Review-Rework-Converge loop from Block 3.

## Prerequisites

- A ticket in Jira (or beans) with status `Ready-for-Factory` and a
  `## High-Level Plan` with Acceptance Criteria (from Block 5's "Ticket +
  Planner" step)
- Refiner, Implementer, Reviewer skills available in the demo repo (either
  marketplace-installed from Block 5's merge attempt, or locally copied)
- Reviewer's rework-cap hook (`.claude/hooks/rework-cap.sh`, from
  `04-review`) in place — the orchestrator prompt below relies on it to
  actually stop after 2 rework cycles, it doesn't reimplement the count
  itself

## The prompt

Type this into a single Claude Code session — in **English**, not all
participants understand German — adjust the label/ticket-source wording if
the team's actual Jira setup differs:

> Find a ticket via the Jira MCP with the label `Ready-for-Factory`. Hand
> it to the Refiner so it produces a Refined Plan (files, signatures, test
> sketch). Once the Refiner is done, hand the ticket to the Implementer,
> who creates a branch, edits, builds, tests, and commits. Once the
> Implementer is done, hand the ticket to the Reviewer. The Reviewer
> checks the diff against each Acceptance Criterion individually. If all
> are met, the PR goes to a human. If not, send the ticket back to the
> Refiner. If at any point you can't find a matching ticket or a step
> fails, stop and report that explicitly instead of continuing silently.

Deliberately not restated in the prompt: the max-2-rework-cycles cap and
the escalation to `needs-human`. That's enforced by the hook inside
Reviewer's own skill, not something the orchestrator needs to know about —
if the third attempt happens, the hook blocks it and Reviewer's own logic
escalates. The orchestrator prompt only needs its own two failure
sentences (no ticket found / a step fails) because those aren't covered by
any hook.

## What to watch for live

- **The Light Switch line** ("the PR goes to a human") is the payoff —
  call it out explicitly when it happens, tie back to Block 3's
  Light-vs-Dark-Factory framing.
- **Mechanically**, this runs as one long-lived orchestrator session that
  calls Refiner/Implementer/Reviewer via the Task tool — the simplified
  precursor from Block 3, not the external `claude -p --resume`
  session-persistence architecture. Say so if asked; it's intentional, not
  a shortcut taken for lack of time.
- If Review sends the ticket back and the group watches a second pass
  happen: good, that's the loop working. If a third pass would be needed:
  the hook should block it — this is the moment the rework-cap actually
  earns its place in the demo, not just as a slide.

## Bridge

Output → the actual test run at the end of Block 5 ("Testlauf"). Same
ticket, same prompt, same session — this file exists so the prompt doesn't
have to be reconstructed from memory on the day.
