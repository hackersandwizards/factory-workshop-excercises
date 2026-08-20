# Day 2 · Exercise 06 — Evals: table tests for skills, not just for the Planner

**Slot:** Block 6, ~15 min hands-on portion · trainer-led, group runs it
together against what the group itself built today.

## Why this exists

Day 1's Mini-Eval-Check ran a handful of prepared tasks against the Planner
once, by hand. This exercise makes that repeatable: a table of test cases
in JSON, run automatically, fresh session per case — so a skill change
next month can be checked against the exact same cases again, not just
"looks fine" from memory.

## Core idea

An eval is the skill's own **Self-Check** section (already in every
`README.md` in `02-refine`, `03-implement`, `04-review`), turned into
something you can re-run instead of eyeballing once. Nothing new to
invent — just automate what's already written down.

## Session structure — the part that makes results repeatable

**Each case runs in its own fresh Claude Code session** (`claude -p`, not
interactive). No case shares context with another. This is not a new rule
— it's the same harness decision already made for Implementer and Reviewer
in Block 3 (fresh context every invocation, so judgment doesn't lean on its
own prior history) — the eval runner just applies it consistently to
itself too. Skip this and case 2's result depends on what case 1 happened
to say, which defeats the point of a repeatable table test.

**Fixture reset before each case:**
- Refine/Review (read-only on source): a fresh throwaway ticket per case
  is enough, no repo reset needed.
- Implement (writes branches/commits): `git checkout main && git branch -D
  <leftover-branch>` before every run, or cases collide with each other's
  branches.

**Two layers of assertion:**
- **Structural** — mechanically checkable: does `## Review` exist, does
  the status field match, is there no source diff. A script checks these,
  no judgment needed.
- **Semantic** — needs judgment: is the *correct* AC flagged as unmet, not
  some other one. For today, a quick human read is enough; a real
  LLM-judge grader is a next-iteration item (see Block 7's "Nächste
  Schritte").

## Example: `cases/review.json`

Reuses the AC-miss example that's already been the Hook in Block 3 and
comes back here — same fixture, now formalized as a table-test case
instead of a one-off demo.

```json
[
  {
    "id": "review-catches-missed-ac",
    "skill": "review",
    "setup": {
      "ticket_template": "implementation-tests-green-one-ac-missed",
      "note": "Same prepared fixture as the Block 3 Hook: tests pass, one Acceptance Criterion from the High-Level Plan is not actually met."
    },
    "input": "/review <ticket-id>",
    "expected": {
      "structural": [
        "## Review section exists in the ticket",
        "status is NOT completed",
        "no source files changed by review itself"
      ],
      "semantic": "the specific unmet AC is the one actually flagged, not a different one; verdict is per-criterion, not one blanket sentence"
    }
  },
  {
    "id": "review-accepts-genuinely-complete",
    "skill": "review",
    "setup": {
      "ticket_template": "implementation-fully-meets-all-acs",
      "note": "False-positive check — equally important as the miss-catching case above. A reviewer that rejects everything isn't useful either."
    },
    "input": "/review <ticket-id>",
    "expected": {
      "structural": [
        "## Review section exists",
        "status is completed"
      ],
      "semantic": "verdict correctly credits each AC as met, not a lucky pass"
    }
  },
  {
    "id": "review-blocks-third-rework",
    "skill": "review",
    "setup": {
      "ticket_template": "implementation-tests-green-one-ac-missed",
      "note": "Rework-count file pre-set to 2 (see 04-review's rework-cap hook)"
    },
    "input": "/review <ticket-id>",
    "expected": {
      "structural": [
        "the hook blocks the send-back-to-Refine tool call (exit 2)",
        "status becomes needs-human, not a third in-progress"
      ],
      "semantic": "the escalation note explains why, referencing the cap"
    }
  }
]
```

## Running it live in Block 6

1. Point at whatever's been merged/assembled so far (marketplace-installed
   or locally copied Reviewer skill).
2. Run each case as its own `claude -p` call, fresh session, per the
   structure above.
3. Check structural assertions with a short script or by hand; read
   through the semantic ones as a group.
4. Then the factory-level version: run the same AC-miss ticket through the
   full orchestrator prompt from `05-orchestrator/` — does the review step
   catch it at the pipeline level, not just in isolation?

## Bridge

This is the mechanism behind Block 6's closing line: "green doesn't mean
done, green only means nobody's noticed yet it isn't done" — now there's an
actual repeatable check standing behind that sentence, not just an
observation from Tag 1.
