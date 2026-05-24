---
name: implement
description: Implement a bean — execute the Implementation Plan from the bean body. Usage /implement <bean-id>
---

Launch `@implement` for bean `$ARGUMENTS`.

Use the Agent tool:
- `subagent_type: implement`
- `description: "Implement bean $ARGUMENTS"`
- `prompt: "Implement bean $ARGUMENTS. Read .beans/$ARGUMENTS--*.md, find the ## Implementation Plan section, execute steps on a new branch with commits per step. Do not push, do not merge."`

After the agent returns:
- Show the branch name and commits
- Print the PR-ready summary
- Print "Run `git diff main...HEAD` to review or `gh pr create` to open a PR (manual step)."
