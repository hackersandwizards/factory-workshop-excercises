package calc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class LexerTest {

    @Test
    void SingleNumber() {
        Lexer lexer = new Lexer("42");
        Token tok = lexer.next();
        assertEquals(TokenType.NUMBER, tok.type);
        assertEquals(42, tok.value);
        assertEquals(TokenType.END, lexer.next().type);
    }

    @Test
    void AllOperators() {
        Lexer lexer = new Lexer("+-*/");
        assertEquals(TokenType.PLUS, lexer.next().type);
        assertEquals(TokenType.MINUS, lexer.next().type);
        assertEquals(TokenType.STAR, lexer.next().type);
        assertEquals(TokenType.SLASH, lexer.next().type);
        assertEquals(TokenType.END, lexer.next().type);
    }

    @Test
    void SkipsWhitespaceAndMixedExpr() {
        Lexer lexer = new Lexer("  12 + 30 ");
        Token a = lexer.next();
        assertEquals(TokenType.NUMBER, a.type);
        assertEquals(12, a.value);
        assertEquals(TokenType.PLUS, lexer.next().type);
        Token b = lexer.next();
        assertEquals(TokenType.NUMBER, b.type);
        assertEquals(30, b.value);
        assertEquals(TokenType.END, lexer.next().type);
    }

    @Test
    void EndIsIdempotent() {
        Lexer lexer = new Lexer("");
        assertEquals(TokenType.END, lexer.next().type);
        assertEquals(TokenType.END, lexer.next().type);
    }

    @Test
    void UnknownCharacterThrows() {
        Lexer lexer = new Lexer("1 ? 2");
        assertEquals(TokenType.NUMBER, lexer.next().type);
        assertThrows(CalcException.class, () -> lexer.next());
    }
}
