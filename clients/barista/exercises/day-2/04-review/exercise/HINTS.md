# Review Skill Build Checklist

You are building a new `review` skill from scratch — **no existing template
to lean on**. This is the Review-Rework-Converge Loop from the agenda,
turned into an actual skill. Output: a `## Review` section in the ticket,
plus a real status change reflecting the converge decision.

## Prerequisite — your ticket backend

Same dual backend as the earlier exercises: **Jira** (default, via MCP) or
**`beans`** (fallback). The ticket from `../03-implement` should be status
completed with `## Implementation Log` and the original `## High-Level
Plan` (Acceptance Criteria) still present.

## Required — Core Mechanic

- [ ] **Frontmatter** — `name: review`, `argument-hint: <ticket-id>`,
  `allowed-tools: Read, Grep, Glob, Bash, Task` (+ Jira MCP tool if used)
- [ ] **Phase 1 (Read ticket)** — extract Acceptance Criteria (from
  `## High-Level Plan`), `## Refined Plan`, and `## Implementation Log`.
  Abort if any is missing — you cannot review what was never planned or
  implemented.
- [ ] **Phase 2 (Get the diff)** — `git diff main...<branch>` using the
  branch name from the Implementation Log. Do not trust "tests were green"
  as a substitute for looking at the actual diff.
- [ ] **Phase 3 (AC-by-AC check)** — for each Acceptance Criterion: met /
  not met / can't tell, one-line reason referencing the diff. This is the
  part that must not collapse into one summary judgement — a checklist,
  not a paragraph.
- [ ] **Phase 4 (Converge)** — all met → mark completed, append
  `## Review` (pass). Any not met → move status back (in-progress / needs
  refine, whatever your board supports), append `## Review` listing the
  failing criteria with reasons, worded so a human or `/refine` could act
  on it directly.
- [ ] **Phase 5 (Write back)** — one write, same discipline as the other
  skills: never edit the ticket by hand, always through `beans update` or
  the Jira MCP.

## Required — Rework cap (hook-enforced, not just prompt text)

Max 2 rework cycles, then escalate to a human instead of a 3rd send-back.
This one is hard-enforced, unlike the other hard rules today — build both
halves:

- [ ] Counter file `.claude/state/rework-count/<ticket-id>.txt` — Review
  reads it (default 0), and on every "not converged → send back" decision,
  increments and rewrites it as part of Phase 4/5
- [ ] `.claude/hooks/rework-cap.sh` — a PreToolUse hook matching the exact
  tool call that sends the ticket back (Bash `beans update.*-s
  in-progress`, or your Jira MCP transition tool name — check what your
  pair's Refine/Review actually calls)
- [ ] The hook reads the counter file for the ticket ID in the tool call,
  and if it's already `>= 2`, **exits 2** with a stderr message telling
  Claude to escalate instead (status → `needs-human`, `## Review` note
  explaining the cap was hit) — remember: only `exit 2` blocks, `exit 1`
  just logs and lets the call through (same trap as `03-env-block-hook`)
- [ ] `.claude/settings.json` registers the hook for the matching tool
  pattern
- [ ] Test: manually set the counter file to `2`, run `/review` on a
  ticket that would normally fail AC and go back to Refine — verify the
  send-back is blocked and Review escalates instead

## Required — Discipline

- [ ] **Read-only on source** — reviewing is not editing
- [ ] **AC-by-AC, not blanket** — "looks fine" is not an acceptable verdict
- [ ] **Green tests are not a review** — the skill must not shortcut to
  "tests passed, therefore done"
- [ ] **The back-to-Refine path is real** — build and test the failing
  case, not just the happy path

## Design questions to settle with your pair before coding

These do not have one correct answer — decide, write down why, be ready to
explain it in Block 5 when pairs assemble their pieces into one Factory:

- Subagent fork for the AC-check, or inline in the main skill context? (Compare
  to why Refine forks and Planner doesn't.)
- What exactly triggers Review — is it `disable-model-invocation: true`
  like Planner, or does it fire automatically once Implement completes a
  ticket? Which is safer for a review step specifically?
- What does "needs another Refine pass" concretely look like in your ticket
  backend — a status, a label, a comment? Whatever you pick, `../02-refine`
  should be able to pick it up from there.

## Self-Check before Block 5

```bash
cd <your repo>
cp -r ../04-review/exercise/.claude .
> /review <ticket-id>
```

- [ ] `## Review` section exists in the ticket with one line per Acceptance
  Criterion
- [ ] A deliberately AC-missing implementation gets sent back, not marked
  done
- [ ] A genuinely complete implementation gets marked done
- [ ] No source files changed as a side effect of running `/review`
- [ ] With the counter file at `2`, a would-be-3rd send-back is blocked by
  the hook and Review escalates instead

## Bridge

This closes the loop: Planner → Refine → Implement → Review, and Review's
"send back" path re-enters at Refine. In Block 5, pairs bring their
Planner/Refine/Implement/Review pieces together into one shared Factory —
know which ticket field or status your Review skill relies on, since the
other pieces need to agree on it.
