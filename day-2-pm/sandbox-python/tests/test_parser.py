import unittest

from calc import CalcError
from calc.parser import BinOp, NodeKind, parse


class ParserTest(unittest.TestCase):
    def test_single_number(self):
        ast = parse("7")
        self.assertEqual(ast.kind, NodeKind.Number)
        self.assertEqual(ast.value, 7)

    def test_flat_addition_is_left_associative(self):
        # 1 + 2 + 3 -> ((1 + 2) + 3)
        ast = parse("1 + 2 + 3")
        self.assertEqual(ast.kind, NodeKind.BinaryOp)
        self.assertEqual(ast.op, BinOp.Add)
        self.assertEqual(ast.left.kind, NodeKind.BinaryOp)
        self.assertEqual(ast.left.op, BinOp.Add)
        self.assertEqual(ast.left.left.value, 1)
        self.assertEqual(ast.left.right.value, 2)
        self.assertEqual(ast.right.kind, NodeKind.Number)
        self.assertEqual(ast.right.value, 3)

    def test_mul_binds_tighter_than_add(self):
        # 1 + 2 * 3 -> (1 + (2 * 3))
        ast = parse("1 + 2 * 3")
        self.assertEqual(ast.kind, NodeKind.BinaryOp)
        self.assertEqual(ast.op, BinOp.Add)
        self.assertEqual(ast.left.kind, NodeKind.Number)
        self.assertEqual(ast.left.value, 1)
        self.assertEqual(ast.right.kind, NodeKind.BinaryOp)
        self.assertEqual(ast.right.op, BinOp.Mul)

    def test_trailing_token_throws(self):
        with self.assertRaises(CalcError):
            parse("1 2")

    def test_missing_operand_throws(self):
        with self.assertRaises(CalcError):
            parse("1 +")


if __name__ == "__main__":
    unittest.main()
