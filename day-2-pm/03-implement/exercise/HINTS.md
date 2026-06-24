# Implement Skill Build Checklist

You are building a new `implement` skill from scratch. **The first skill that writes** — on a branch, with a test gate, commits per step. Never push, never merge.

## Prerequisite — Beans CLI

`beans --version` must run. The bean from Exercise 02 should have a `## Refined Plan` in its body and status `in-progress`.

## Required — Core Mechanic

- [ ] **Frontmatter** — `name: implement`, `argument-hint: <bean-id>`, `model: claude-sonnet-4-6` (faster for code), `allowed-tools: Read, Edit, Write, Bash, Glob, Grep`
- [ ] **Phase 1 (Preflight)** — parse `beans show --json <bean-id>`, extract the `## Refined Plan`. Abort if empty. The working tree must be clean. HEAD must be `main`.
- [ ] **Phase 2 (Branch)** — build a slug from the bean's `title` field. Branch: `feat/<bean-id>-<slug>`. Abort if the branch exists. Verify via `git rev-parse --abbrev-ref HEAD`.
- [ ] **Phase 3 (Implement loop)** — per Refined-Plan step: Edit → `cmake --build build` → `ctest` → commit. Tests red? Max 2 fix attempts, then abort.
- [ ] **Phase 4 (Implementation Log)** — `beans update <bean-id> --body-append "..."` with the branch name, commit SHAs + descriptions, and the final test status.
- [ ] **Phase 5 (Status)** — if green: `beans update <bean-id> -s completed` + append `## Summary of Changes`. If red: status stays `in-progress`, append notes.

## Required — Discipline (hard rules)

- [ ] **Never commit to `main`** — before every commit, check `git rev-parse --abbrev-ref HEAD`
- [ ] **Never `git push`, `git merge`, `git rebase`**
- [ ] **Tests green before every commit** — no "fix it later" commits
- [ ] **Max 2 fix attempts per step** — then stop + log the state
- [ ] **One logical step per commit** — do not batch
- [ ] **Never edit `.beans/*.md` directly** — always via `beans update`

## Self-Check before the Solution Comparison

```bash
cd ../sandbox
cp -r ../03-implement/exercise/.claude .
# Build the skill, then the full v0:
/planner 
# produces bean implement-exercise-olqc
/refine implement-exercise-olqc
/implement implement-exercise-olqc
```

implement-exercise-olqc

- [ ] The branch `feat/implement-exercise-olqc` (or similar) exists
- [ ] `git log feat/implement-exercise-olqc-...` shows several commits, one per Refined-Plan step
- [ ] `ctest --test-dir build` green
- [ ] `beans show implement-exercise-olqc` shows status `completed`
- [ ] The skill refuses to commit to `main` (test: after Phase 2, deliberately `git checkout main` → the skill must abort)

## Expected Bugs (note them, don't fix during the build)

- Hallucinated files (the Refined Plan was too vague)
- Test loop / endless fix attempts
- Commit to `main` (the skill ignores the constraint)
- Subagent token bloat
- Direct edits to `.beans/*.md` instead of the CLI (the skill bypasses beans)

These bugs are the template for the Pitfalls slot 16:30–17:00.
