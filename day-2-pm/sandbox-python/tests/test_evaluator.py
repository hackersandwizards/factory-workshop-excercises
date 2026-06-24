import unittest

from calc import CalcError
from calc.evaluator import evaluate
from calc.parser import parse


def eval_str(src: str) -> int:
    ast = parse(src)
    return evaluate(ast)


class EvaluatorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(eval_str("1+2"), 3)

    def test_multiplication(self):
        self.assertEqual(eval_str("3*4"), 12)

    def test_integer_division_truncates(self):
        self.assertEqual(eval_str("10/2"), 5)
        self.assertEqual(eval_str("7/2"), 3)

    def test_subtraction(self):
        self.assertEqual(eval_str("5-3"), 2)

    def test_mixed_precedence(self):
        self.assertEqual(eval_str("1+2*3"), 7)
        self.assertEqual(eval_str("2*3+4"), 10)
        self.assertEqual(eval_str("20-6/2"), 17)

    def test_division_by_zero_throws(self):
        with self.assertRaises(CalcError):
            eval_str("1/0")


if __name__ == "__main__":
    unittest.main()
