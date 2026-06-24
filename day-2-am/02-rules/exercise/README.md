# Test repo for the pirate rule

This folder is your test playground for the Rules exercise.

## Test plan

1. Create `.claude/rules/pirate.md` (see ../README.md for details)
2. Open Claude Code in this folder
3. Ask Claude: "Add an 'About' section to this README" → expected: **pirate language**
4. Ask Claude: "Explain what main.cpp does" → expected: **normal language**

## Files in this folder

- `README.md` — this file (Markdown → glob matches → pirate)
- `main.cpp` — C++ sample (does not match the pirate glob → normal)

## Notes

The pirate rule only exists if YOU create it. Solution reference: `../solution/.claude/rules/pirate.md`.
