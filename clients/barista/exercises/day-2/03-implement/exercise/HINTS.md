# Implement Skill Build Checklist

You are building a new `implement` skill from scratch. **The first skill
that writes** — on a branch, with a test gate, commits per step. Never
push, never merge.

## Prerequisite — your ticket backend

Same dual backend as the earlier exercises: **Jira** (default, via MCP) or
**`beans`** (fallback). The ticket from `../02-refine` should have a
`## Refined Plan` and status in-progress.

## Required — Core Mechanic

- [ ] **Frontmatter** — `name: implement`, `argument-hint: <ticket-id>`,
  `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`
- [ ] **Phase 1 (Preflight)** — read the ticket, extract
  `## Refined Plan`. Abort if empty. The working tree must be clean. HEAD
  must be `main`.
- [ ] **Phase 2 (Branch)** — build a slug from the ticket's title. Branch:
  `feat/<ticket-id>-<slug>`. Abort if the branch exists. Verify via
  `git rev-parse --abbrev-ref HEAD`.
- [ ] **Phase 3 (Implement loop)** — per Refined-Plan step: Edit → build →
  test (your own repo's commands) → commit. Tests red? Max 2 fix attempts,
  then abort.
- [ ] **Phase 4 (Implementation Log)** — write back into the ticket: branch
  name, commit SHAs + descriptions, final test status.
- [ ] **Phase 5 (Status)** — if green: mark completed + append
  `## Summary of Changes`. If red: status stays in-progress, append notes.

## Required — Discipline (hard rules)

These are the ones flagged explicitly for the block — call them out to your
pair before you start, not as an afterthought:

- [ ] **Never commit to `main`** — before every commit, check
  `git rev-parse --abbrev-ref HEAD`
- [ ] **Never `git push`, `git merge`, `git rebase`**
- [ ] **Tests green before every commit** — no "fix it later" commits
- [ ] **Max 2 fix attempts per step** — then stop + log the state
- [ ] **One logical step per commit** — do not batch
- [ ] **Never edit the ticket by hand** — always via `beans update` or the
  Jira MCP

## Self-Check before comparing against the generic solution

```bash
cd <your repo>
cp -r ../03-implement/exercise/.claude .
> /implement <ticket-id>
```

- [ ] The branch `feat/<ticket-id>-...` exists
- [ ] `git log feat/<ticket-id>-...` shows several commits, one per
  Refined-Plan step
- [ ] Tests green
- [ ] The ticket shows status completed
- [ ] The skill refuses to commit to `main` (test: after Phase 2,
  deliberately `git checkout main` → the skill must abort)

## Expected Bugs (note them, don't fix during the build)

- Hallucinated files (the Refined Plan was too vague)
- Test loop / endless fix attempts
- Commit to `main` (the skill ignores the constraint)
- Subagent token bloat
- Direct edits to the ticket instead of the CLI/MCP (the skill bypasses the
  contract)

## Bridge

Output → input for `/review` in `../04-review`.
