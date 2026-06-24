# Test repo for the pirate rule

This folder is your test playground for the Rules exercise.

## Test plan

1. Create `.claude/rules/pirate.md` (see ../README.md for details)
2. Open Claude Code in this folder
3. Ask Claude: "Add an 'About' section to this README" → expected: **pirate language**
4. Ask Claude: "Explain what this file does" about the sample for your stack (`main.cpp` / `main.java` / `main.py`) → expected: **normal language**

## Files in this folder

- `README.md` — this file (Markdown → glob matches → pirate)
- `main.cpp` — C++ sample (does not match the pirate glob → normal)
- `main.java` — Java sample (does not match the pirate glob → normal)
- `main.py` — Python sample (does not match the pirate glob → normal)

Each `main.*` carries a few intentional anti-patterns for the language stretch rule.

## Notes

The pirate rule only exists if YOU create it. Solution reference: `../solution/.claude/rules/pirate.md`.
