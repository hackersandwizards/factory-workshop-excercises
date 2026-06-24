"""REPL entry point. Run with ``python3 -m calc``.

Catches ``CalcError`` (the single catch point), prints ``error: <msg>``, and
continues. ``exit``, ``quit``, or Ctrl-D (EOF) leave the loop.
"""

from __future__ import annotations

import sys

from . import CalcError
from .evaluator import evaluate
from .parser import parse


def main() -> int:
    print("calc REPL — type 'exit' or Ctrl-D to quit")
    while True:
        try:
            line = input("> ")
        except EOFError:
            print()
            break

        if line in ("exit", "quit"):
            break
        if line == "":
            continue

        try:
            ast = parse(line)
            print(evaluate(ast))
        except CalcError as ex:
            print(f"error: {ex}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
