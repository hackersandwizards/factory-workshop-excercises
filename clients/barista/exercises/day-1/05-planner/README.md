# Day 1 · Exercise 04 — Planner Skill with ticket backend

**Slot:** Block 3, 11:00–12:00 · 60 minutes (hands-on)

## Goal

Build your own planner skill that, on `/planner`, **creates a ticket
directly** instead of planning into a `.md` file — the "What" of the
pipeline, without paths or signatures.

**Two backends, one contract.** The default is **Jira** (via the local Jira
MCP). The fallback is the **`beans` CLI**, in case MCP access is not in
place. The mechanics of the skill are identical either way — only the last
step (phase 5) differs. That is exactly the point: the planner does not know
its backend, it fulfils a contract.

## Origin

Combined from `day-2-am/01-planning-skill` (4★ subset: Explore / One
question per message / Alternatives / Self-Review) and
`day-2-pm/01-planner-rework` (ticket creator instead of a `.plans/` file) —
two separate exercises on different days in the original, here **in one
step**. Saves a rebuild step and gives you the real pipeline building block
straight away.

## Preparation

**Check your backend.** For the Jira route: the Jira MCP must be reachable
and have write permission on a project where you may create, edit and close
tickets. For the fallback: `brew install hmans/beans/beans`, check with
`beans --version`. Have both ready if you can — then an outage at runtime
costs no exercise time.

Copy `exercise/.claude` (and, for the fallback, `exercise/.beans.yml`) into
a directory of your choice — ideally a real, non-critical piece of your own
stack, not an empty test directory. Pick a planning domain up front, e.g.
`migration-planner`, `refactor-planner`, `feature-planner`.

## Hook (~10 min, led by the trainer)

Give Claude Code a large, multi-step task without any planner at all
("rebuild feature X completely"). Watch: it charges off, makes its own
assumptions, and probably changes the wrong files first. The loss of control
is experienced live, before anyone talks about planning.

## Mechanism — building it (~35 min)

1. Copy `exercise/.claude` + `exercise/.beans.yml` into your chosen
   directory.
2. Build `.claude/skills/planner/SKILL.md` from scratch (no copy-paste
   starting point — see `HINTS.md` for a checklist and a snippet template).
3. Mandatory subset (4★): explore context before asking the first question ·
   one question per message · 2–3 alternatives before converging, without
   favouring one yourself · self-review before finishing.
4. Ticket creation instead of a file plan — **one** write with the complete
   body:
   - *Jira (default):* create the issue via the Jira MCP. Summary = title,
     Description = description + `## High-Level Plan`. Return the issue key
     (e.g. `BAR-123`) for the handover to `/refine` (day 2).
   - *Beans (fallback):* `beans create "<title>" -t feature -d "<heredoc
     with description + ## High-Level Plan>"`. The `beans` CLI has **no**
     `--body-append` — for long bodies use `--body-file <path>` instead of
     `-d`. Parse the ID from stdout.
5. Heading contract: the plan sits verbatim under the heading
   `## High-Level Plan` — `/refine` on day 2 parses it by exact match; if
   the heading is missing, refine aborts. **Careful with Jira:** the
   description must not reformat the markdown heading away. After your first
   ticket, read back what was actually stored.
6. Hard rule: **no** file paths, **no** function signatures, **no** class
   names in the plan — acceptance criteria instead.
7. **New, deliberate design decision:** set `disable-model-invocation: true`
   in the frontmatter. Two reasons: it keeps the hook above clean (Claude
   cannot decide on its own to plan "just in case" and soften the loss of
   control in the hook), and creating a ticket is a side effect — exactly
   the case where explicit rather than automatic triggering is recommended.
   It also fits the human-in-the-loop tone of the workshop.
8. Test: `/planner <your own task>` → a new ticket exists, and its
   description contains `## High-Level Plan` with
   Approach/Steps/AC/Non-Goals. (Jira: open the issue in the project. Beans:
   `beans list`, `beans show <id>`.)

## Verify

- After the `/planner` run a new ticket exists (Jira issue or bean)
- The plan contains no file paths, no function names, no line references
- The skill asks one question at a time, not all of them at once
- The skill does **not** trigger by itself — only on an explicit `/planner`
  call (test: mention a complex task in passing without typing `/planner` —
  nothing should happen)
- The skill fails in a controlled way when its backend is missing (Jira MCP
  unreachable or `beans` CLI not installed) — it does not invent a ticket
  and does not quietly plan into a file

## Twist (~10 min)

The expectation would be: "a planning step makes the agent slower, because
it asks first instead of getting started." The resolution is the opposite —
the ticket as a contract makes the next pipeline steps (refine, implement)
cheaper and faster, because they do not have to explore again. The
investment does not pay off within the single task, but across the whole
pipeline.

## Closing (~5 min)

"Ironically, the agent that asks the most questions up front is the one that
annoys you least in the end."

## Stretch

- Add the remaining 4 mechanics (approval gate, explicit constraints /
  non-goals as their own section, repeatable routine)
- Define your own subagent type (`.claude/agents/<name>.md`) — but see below
  for why that is not (yet) the right step for the planner itself
- Evaluate the skill with `skill-creator`, see
  `exercise/evals/PLANNED-CASES.md`

## Why not a subagent (yet)

The obvious question: why does this stay a normal skill instead of
`context: fork`? The planner lives on the follow-up question — "one question
per message" needs access to the running conversation, which a forked
subagent does not have (it only receives the skill content as a prompt,
isolated, with no history). The right place for a fork is refine on day 2
(pure, self-contained reading work, no need for follow-up questions) — and
it is already planned for there. On top of that: Björn wants to see the
planner mechanism stable in its simpler, easier-to-debug form before the
architecture gets more complicated.

## Bridge to day 2

The ticket ID (Jira issue key or bean ID) is the handover to `/refine <id>`
— paths and signatures are added there, not here.

## Solution

The reference solution lives on branch
**`solution/barista-day-1-03-planner`** (branch name still carries the old
number 03 — the exercise was renumbered to 04 so the folders follow the block
order; deliberately not on
`client/barista`, so it does not end up in Claude's context) —
`solution/.claude/skills/planner/SKILL.md` with the full 4★ subset +
`disable-model-invocation: true`. The reference solution writes to
**beans** — if you built against Jira, compare phases 1–4 one to one and
phase 5 by analogy. Build it yourself first, then compare:

```bash
git checkout solution/barista-day-1-03-planner   # inspect solution/.claude/skills/planner/SKILL.md
git checkout client/barista                      # back to your own work
git show solution/barista-day-1-03-planner:clients/barista/exercises/day-1/03-planner/solution/.claude/skills/planner/SKILL.md
```
