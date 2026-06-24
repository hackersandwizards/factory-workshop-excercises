"""Recursive-descent parser.

Tiny AST. Two node kinds, one shared dataclass. We use a flat ``Node`` with a
``kind`` discriminator — simple structs over deep OOP.

Grammar:
    expr   -> term   (('+' | '-') term)*
    term   -> factor (('*' | '/') factor)*
    factor -> NUMBER
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

from . import CalcError
from .lexer import Lexer, Token, TokenType, token_type_name


class NodeKind(Enum):
    Number = auto()
    BinaryOp = auto()


class BinOp(Enum):
    Add = auto()
    Sub = auto()
    Mul = auto()
    Div = auto()


@dataclass
class Node:
    kind: NodeKind

    # Number payload
    value: int = 0

    # BinaryOp payload
    op: BinOp = BinOp.Add
    left: Optional["Node"] = field(default=None)
    right: Optional["Node"] = field(default=None)


class _Parser:
    """Recursive-descent parser holding a peeked token."""

    def __init__(self, source: str) -> None:
        self._lexer = Lexer(source)
        self._current: Token = self._lexer.next()

    def _advance(self) -> None:
        self._current = self._lexer.next()

    def parse_expr(self) -> Node:
        left = self._parse_term()
        while self._current.type in (TokenType.PLUS, TokenType.MINUS):
            op = BinOp.Add if self._current.type == TokenType.PLUS else BinOp.Sub
            self._advance()
            right = self._parse_term()
            left = self._make_binary(op, left, right)
        return left

    def _parse_term(self) -> Node:
        left = self._parse_factor()
        while self._current.type in (TokenType.STAR, TokenType.SLASH):
            op = BinOp.Mul if self._current.type == TokenType.STAR else BinOp.Div
            self._advance()
            right = self._parse_factor()
            left = self._make_binary(op, left, right)
        return left

    def _parse_factor(self) -> Node:
        if self._current.type != TokenType.NUMBER:
            raise CalcError(
                f"expected NUMBER but got {token_type_name(self._current.type)} "
                f"at position {self._current.pos}"
            )
        node = Node(kind=NodeKind.Number, value=self._current.value)
        self._advance()
        return node

    def expect_end(self) -> None:
        if self._current.type != TokenType.END:
            raise CalcError(
                f"unexpected token {token_type_name(self._current.type)} "
                f"at position {self._current.pos} (expected end of input)"
            )

    @staticmethod
    def _make_binary(op: BinOp, left: Node, right: Node) -> Node:
        return Node(kind=NodeKind.BinaryOp, op=op, left=left, right=right)


def parse(source: str) -> Node:
    """Parse a full expression from ``source``.

    Raises ``CalcError`` on syntactic problems (unexpected tokens, trailing
    input, etc.).
    """
    parser = _Parser(source)
    root = parser.parse_expr()
    parser.expect_end()
    return root
