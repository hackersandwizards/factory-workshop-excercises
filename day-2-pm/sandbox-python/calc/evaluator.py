"""Tree-walking evaluator.

Walk the AST and return the integer result. Raises ``CalcError`` on division
by zero. Pure integer arithmetic — no floats.
"""

from __future__ import annotations

from . import CalcError
from .parser import BinOp, Node, NodeKind


def _truncate_div(left: int, right: int) -> int:
    """Integer division that truncates toward zero (C++ semantics)."""
    quotient = abs(left) // abs(right)
    if (left < 0) != (right < 0):
        quotient = -quotient
    return quotient


def evaluate(node: Node) -> int:
    if node.kind == NodeKind.Number:
        return node.value

    if node.kind == NodeKind.BinaryOp:
        left = evaluate(node.left)
        right = evaluate(node.right)
        if node.op == BinOp.Add:
            return left + right
        if node.op == BinOp.Sub:
            return left - right
        if node.op == BinOp.Mul:
            return left * right
        if node.op == BinOp.Div:
            if right == 0:
                raise CalcError("division by zero")
            return _truncate_div(left, right)

    raise CalcError("evaluator: unknown node kind")
