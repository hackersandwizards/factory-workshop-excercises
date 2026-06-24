"""calc — a tiny teaching calculator (lexer + parser + evaluator + REPL)."""


class CalcError(Exception):
    """Raised on lexing, parsing, or evaluation errors.

    The REPL is the single catch point: it prints ``error: <msg>`` and
    keeps running.
    """
