---
glob: "**/*.py"
---

# Modern Python Conventions

Enforce these when working with Python source.

## Types & Data

- Type hints on function signatures (`def f(x: int) -> str:`) and public attributes
- `@dataclass` for plain data carriers instead of hand-written `__init__`
- `enum.Enum` for closed sets of named constants

## Idioms

- f-strings for formatting — no `"a" + str(b)` concatenation or `%`/`.format()`
- Iterate directly (`for x in items:`) — no `for i in range(len(items)):`
- Comprehensions over manual `append` loops where they stay readable
- `is None` / `is not None` for None checks — never `== None`

## Pitfalls

- Never a mutable default argument (`def f(xs=[])`); use `None` + assign inside
- Catch specific exceptions — no bare `except:`; prefer `except SomeError:`
- Context managers (`with open(...) as f:`) for files and other resources

## Structure

- Guard scripts with `if __name__ == "__main__":`
- snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- Prefer pure functions and small modules over deep class hierarchies
