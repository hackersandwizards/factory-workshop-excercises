---
name: implement
description: Implements a Bean's Refined Plan. Creates feature branch, edits files, runs ctest after each change, commits per logical step, appends Implementation Log + sets status=completed. Never pushes, never merges to main.
argument-hint: <bean-id>
model: claude-sonnet-4-6
allowed-tools: Read, Edit, Write, Bash, Glob, Grep
---

# Implement (Refined Plan → Code on a Branch)

You execute a Refined Plan: branch, edit, build, test, commit per step. Append a complete log to the Bean and flip its status to `completed`. Never merge, never push.

## When to use

- User invokes `/implement <bean-id>` or says "implement <bean-id>"
- Bean body contains `## Refined Plan` with real files, signatures, test sketch
- Current branch is clean (no uncommitted changes); HEAD is on `main`

## Workflow

### Phase 1: Preflight

- `beans show --json <bean-id>` — parse JSON, extract title + body
- Extract `## Refined Plan` section — Files to change, New signatures, Test sketch
- If `## Refined Plan` missing or empty (only headers, no bullets) → abort: "Refined Plan missing — run /refine first."
- `git status --porcelain` → if not empty, abort: "Working tree not clean. Commit or stash first."
- `git rev-parse --abbrev-ref HEAD` → if not `main`, abort: "Must start from main. Currently on <branch>."

### Phase 2: Branch

- From the JSON, read the `title` field. Slugify: lowercase, replace non-alphanumerics with `-`, collapse repeats, trim leading/trailing `-`.
- Branch name: `feat/<bean-id>-<slug>` (e.g. `feat/sandbox-dy91-klammer-support`).
- `git rev-parse --verify <branch-name>` → if exists, abort: "Branch already exists."
- `git checkout -b <branch-name>`
- Verify: `git rev-parse --abbrev-ref HEAD` returns the new branch. If not → abort.

### Phase 3: Implement loop

For each `### Files to change` entry in the Refined Plan, in listed order:

1. Apply the edit (Edit / Write) — minimum change to satisfy this step.
2. Build: `cmake --build build` (assumes `cmake -B build` was already run; if `build/` missing, run it first).
3. Test: `ctest --test-dir build --output-on-failure`.
4. **If tests fail:**
   - Attempt 1: read failure output, fix root cause, repeat step 2-3.
   - Attempt 2: one more fix attempt, repeat step 2-3.
   - If still red after attempt 2 → STOP. Do not commit. Jump to Phase 4 with status `aborted-tests-red`.
5. **If tests pass:**
   - `git add` only the files touched in this step.
   - `git commit -m "<bean-id>: <step-description>"` — descriptive, one logical change per commit.
   - Capture the commit SHA (`git rev-parse HEAD`) and the step description for the log.

After the loop: run the full test suite once more end-to-end. Status: `green` or `red`.

### Phase 4: Append Implementation Log

Append the log to the bean body via the CLI:

```bash
beans update <bean-id> --body-append "$(cat <<'EOF'

## Implementation Log

**Branch:** \`feat/<bean-id>-<slug>\`

**Commits**
- \`<sha-short>\` — <step description>
- \`<sha-short>\` — <step description>

**Final test status:** green | red | aborted-tests-red

**Notes** (only if aborted): which step failed, last test output excerpt, next-action hint.
EOF
)"
```

### Phase 5: Status

- If final test status is `green`:
  ```bash
  beans update <bean-id> --body-append $'\n\n## Summary of Changes\n\n<2-3 sentence summary>'
  beans update <bean-id> -s completed
  ```
- If `aborted-tests-red`: leave status as `in-progress`. Append a `## Notes` section explaining where it stopped.

Final report to user: branch name, commit count, test status, bean status. Suggest review before merge.

## Rules

- Never commit to `main`. After Phase 2, verify `git rev-parse --abbrev-ref HEAD` is the new feat branch before any commit. Refuse otherwise.
- Never `git push`. Never `git merge`. Never `git rebase --onto main`. The user reviews and merges manually.
- Tests must be green before each commit. No "fix it later" commits.
- Max 2 fix attempts per failing step. Then stop, log state, surface to user. Do not loop forever.
- One logical change per commit. Do not batch multiple Refined-Plan steps into one commit.
- Never edit `.beans/*.md` directly with Edit/Write. Use `beans update --body-append` and `beans update -s <status>`.
- If `cmake` or `ctest` is missing on the system → abort with a clear message; do not improvise alternate builds.
