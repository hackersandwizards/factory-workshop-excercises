package calc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class EvaluatorTest {

    private static long evalStr(String src) {
        Node ast = Parser.parse(src);
        return Evaluator.evaluate(ast);
    }

    @Test
    void Addition() {
        assertEquals(3, evalStr("1+2"));
    }

    @Test
    void Multiplication() {
        assertEquals(12, evalStr("3*4"));
    }

    @Test
    void IntegerDivisionTruncates() {
        assertEquals(5, evalStr("10/2"));
        assertEquals(3, evalStr("7/2"));
    }

    @Test
    void Subtraction() {
        assertEquals(2, evalStr("5-3"));
    }

    @Test
    void MixedPrecedence() {
        assertEquals(7, evalStr("1+2*3"));
        assertEquals(10, evalStr("2*3+4"));
        assertEquals(17, evalStr("20-6/2"));
    }

    @Test
    void DivisionByZeroThrows() {
        assertThrows(CalcException.class, () -> evalStr("1/0"));
    }
}
