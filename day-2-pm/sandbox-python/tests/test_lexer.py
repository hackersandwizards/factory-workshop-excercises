import unittest

from calc import CalcError
from calc.lexer import Lexer, TokenType


class LexerTest(unittest.TestCase):
    def test_single_number(self):
        lexer = Lexer("42")
        tok = lexer.next()
        self.assertEqual(tok.type, TokenType.NUMBER)
        self.assertEqual(tok.value, 42)
        self.assertEqual(lexer.next().type, TokenType.END)

    def test_all_operators(self):
        lexer = Lexer("+-*/")
        self.assertEqual(lexer.next().type, TokenType.PLUS)
        self.assertEqual(lexer.next().type, TokenType.MINUS)
        self.assertEqual(lexer.next().type, TokenType.STAR)
        self.assertEqual(lexer.next().type, TokenType.SLASH)
        self.assertEqual(lexer.next().type, TokenType.END)

    def test_skips_whitespace_and_mixed_expr(self):
        lexer = Lexer("  12 + 30 ")
        a = lexer.next()
        self.assertEqual(a.type, TokenType.NUMBER)
        self.assertEqual(a.value, 12)
        self.assertEqual(lexer.next().type, TokenType.PLUS)
        b = lexer.next()
        self.assertEqual(b.type, TokenType.NUMBER)
        self.assertEqual(b.value, 30)
        self.assertEqual(lexer.next().type, TokenType.END)

    def test_end_is_idempotent(self):
        lexer = Lexer("")
        self.assertEqual(lexer.next().type, TokenType.END)
        self.assertEqual(lexer.next().type, TokenType.END)

    def test_unknown_character_throws(self):
        lexer = Lexer("1 ? 2")
        self.assertEqual(lexer.next().type, TokenType.NUMBER)
        with self.assertRaises(CalcError):
            lexer.next()


if __name__ == "__main__":
    unittest.main()
