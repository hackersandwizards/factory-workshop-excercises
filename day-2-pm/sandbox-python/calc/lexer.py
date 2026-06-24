"""Token stream for the calculator.

Stream-style lexer. Construct over a source string, then call ``next()`` to
advance through the token stream. Returns ``TokenType.END`` at end of input
(and keeps returning it on subsequent calls).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

from . import CalcError


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    END = auto()


@dataclass
class Token:
    type: TokenType = TokenType.END
    value: int = 0  # populated when type == NUMBER
    pos: int = 0  # 0-based offset in source, for error messages


# Punctuation characters mapped to their token types.
_SINGLE_CHAR_TOKENS = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "*": TokenType.STAR,
    "/": TokenType.SLASH,
}


class Lexer:
    def __init__(self, source: str) -> None:
        self._source = source
        self._pos = 0

    def _skip_whitespace(self) -> None:
        while self._pos < len(self._source) and self._source[self._pos].isspace():
            self._pos += 1

    def next(self) -> Token:
        self._skip_whitespace()

        if self._pos >= len(self._source):
            return Token(TokenType.END, 0, self._pos)

        start = self._pos
        c = self._source[self._pos]

        if c.isdigit():
            value = 0
            while self._pos < len(self._source) and self._source[self._pos].isdigit():
                value = value * 10 + (ord(self._source[self._pos]) - ord("0"))
                self._pos += 1
            return Token(TokenType.NUMBER, value, start)

        self._pos += 1
        token_type = _SINGLE_CHAR_TOKENS.get(c)
        if token_type is not None:
            return Token(token_type, 0, start)

        raise CalcError(f"unexpected character '{c}' at position {start}")


def token_type_name(token_type: TokenType) -> str:
    return token_type.name
