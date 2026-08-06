# Build checklist

No copy-paste starting point this time — `.claude/skills/` is empty. You
build the SKILL.md from scratch. Two sources come together here: the
Explore→Clarify→Propose→Self-Review mechanic from the planning skill, and
the ticket-creator rework points that turn the file drop `.plans/<task>.md`
into a real ticket.

## Mandatory — the 4★ mechanic (core of the planner)

- [ ] **Explore project context** — recon BEFORE the first question (read README, top-level dirs, relevant files)
- [ ] **One question per message** — multiple choice where possible, wait for the answer
- [ ] **2-3 alternatives before converging** — explicit trade-offs, do NOT rank them yourself
- [ ] **Self-review (guardrail)** — a check step before finalising, before the ticket is created

## Mandatory — ticket creator (instead of a file drop)

> **Backend:** the default is **Jira** (local Jira MCP), the fallback is the
> **`beans` CLI**. Everything below applies to both — only the creation step
> differs.

- [ ] **Frontmatter** — `argument-hint: [short feature description]` (optional, no `<ticket-id>` — that is created here). Adjust the description: "creates a new ticket (Jira via MCP, fallback beans CLI) with description + high-level plan + AC".
- [ ] **Capture** — take in the feature idea from the user, mirror it back in one sentence
- [ ] **STOP guard at the alternatives** — the skill presents 2-3 options and **waits for an explicit choice**. Even if "autonomous" / "no questions" was said earlier — choosing the approach is a mandatory gate, not a follow-up question in the ordinary sense.
- [ ] **Create the ticket — one write** with the complete body:
  - *Jira:* issue via the Jira MCP. Summary = title, Description = description + notes + `## High-Level Plan` (Approach, Steps, AC, Non-Goals), all in one go. Return the issue key to the user (`/refine <key>`, day 2)
  - *Beans:* `beans create "<title>" -t feature -d "<heredoc>"` with the same content. No `--body-append` flag — for very long bodies use `--body-file <path>` instead of `-d`. Parse the ID from stdout
  - No second write to add things afterwards — the body goes out in one go
- [ ] **Pin the schema** — Approach / Steps / Acceptance Criteria / Non-Goals
- [ ] **Heading contract** — the plan sits verbatim under the heading `## High-Level Plan`. `/refine` parses it by exact match — if the heading is missing, refine aborts. With Jira, check after the first ticket whether the description kept the heading verbatim.
- [ ] **Hard rule** — no file paths, no function signatures, no class names in the plan (acceptance criteria instead of implementation detail)

## Mandatory — trigger behaviour

- [ ] Set **`disable-model-invocation: true`** in the frontmatter — the planner starts a ticket side effect and a multi-step question-and-answer chain. Both should be triggered deliberately via `/planner ...`, not inferred by the model itself.
- [ ] Verified that a casual request ("could you quickly plan this?") does **not** trigger the skill on its own

## Mandatory — discipline

- [ ] Never write to the backend behind its tool's back — Jira only via the MCP, `.beans/*.md` only via the CLI
- [ ] Never edit source code — the planner is read-only on source
- [ ] Self-review stays in — it is the last guardrail before handover

## Self-check before looking at the solution

- [ ] `/planner <your feature>` → a new ticket is created (Jira issue or `beans list`)
- [ ] The description shows description + `## High-Level Plan` with Approach/Steps/AC/Non-Goals
- [ ] The plan contains **no** file paths, **no** function names, **no** line references
- [ ] The skill does NOT trigger on its own on a casual phrasing (see above)
- [ ] The skill refuses cleanly when its backend is missing (Jira MCP gone or `beans` CLI absent)

## Snippet template (if you want a starting point)

```markdown
---
name: planner
description: Creates a new ticket (Jira via MCP, fallback beans CLI) with description + high-level plan + AC. Only call explicitly via /planner.
disable-model-invocation: true
argument-hint: [short feature description]
---

# Planner

You are a planning partner, not an executor. The result is a ticket, not code.

## Workflow

### Phase 1: explore project context
- Read the README, top-level dirs, relevant core files
- Identify entry points, tests, conventions
- Report your findings back briefly BEFORE the first question

### Phase 2: clarify (one question per message)
- Exactly ONE question per message
- Multiple choice where possible
- Do not move on before the current question is answered

### Phase 3: propose alternatives
- 2-3 different approaches with honest trade-offs
- Wait for an explicit choice (STOP guard)
- Do not rank them yourself — the choice belongs to the user

### Phase 4: self-review (guardrail)
- Before handover: read your own proposal again
- Check: constraints respected? Trade-offs honest? Anything hand-waved?
- If there are gaps: back to phase 2

### Phase 5: create the ticket
- Backend: Jira via MCP. If the MCP is unreachable, fall back to
  `beans create "<title>" -t feature -d "<heredoc>"` and say so —
  never quietly plan into a file
- The body contains description + `## High-Level Plan` (Approach, Steps, AC, Non-Goals)
- No file paths, no function signatures, no class names
- Return the ID or issue key to the user, point them to `/refine <id>` (day 2)

## Rules

- Never implement during planning
- Never skip explore — blind plans are guesswork
- Never skip self-review — it is the last guardrail before handover
- Never skip the ticket creation step (conversation is not memory)
- Never propose without explicit alternatives
- If the user gets impatient: ask a question anyway. Discipline over speed.
- Only write to the backend through its own tool (Jira MCP or beans CLI), never around it
```

**Beginners:** take the snippet and adapt the domain/description.
**Advanced:** from scratch — your own phase structure, your own selection of
mechanics. The 4★ subset stays mandatory.

## Run

```bash
cd exercise
cp -r .claude <your-sandbox-folder>/            # + .beans.yml, if using the fallback
cd <your-sandbox-folder>
claude
> /planner <your feature>
```
