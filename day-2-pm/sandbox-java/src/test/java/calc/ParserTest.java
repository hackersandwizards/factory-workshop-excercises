package calc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

class ParserTest {

    @Test
    void SingleNumber() {
        Node ast = Parser.parse("7");
        assertEquals(NodeKind.Number, ast.kind);
        assertEquals(7, ast.value);
    }

    @Test
    void FlatAdditionIsLeftAssociative() {
        // 1 + 2 + 3 -> ((1 + 2) + 3)
        Node ast = Parser.parse("1 + 2 + 3");
        assertEquals(NodeKind.BinaryOp, ast.kind);
        assertEquals(BinOp.Add, ast.op);
        assertEquals(NodeKind.BinaryOp, ast.left.kind);
        assertEquals(BinOp.Add, ast.left.op);
        assertEquals(1, ast.left.left.value);
        assertEquals(2, ast.left.right.value);
        assertEquals(NodeKind.Number, ast.right.kind);
        assertEquals(3, ast.right.value);
    }

    @Test
    void MulBindsTighterThanAdd() {
        // 1 + 2 * 3 -> (1 + (2 * 3))
        Node ast = Parser.parse("1 + 2 * 3");
        assertEquals(NodeKind.BinaryOp, ast.kind);
        assertEquals(BinOp.Add, ast.op);
        assertEquals(NodeKind.Number, ast.left.kind);
        assertEquals(1, ast.left.value);
        assertEquals(NodeKind.BinaryOp, ast.right.kind);
        assertEquals(BinOp.Mul, ast.right.op);
    }

    @Test
    void TrailingTokenThrows() {
        assertThrows(CalcException.class, () -> Parser.parse("1 2"));
    }

    @Test
    void MissingOperandThrows() {
        assertThrows(CalcException.class, () -> Parser.parse("1 +"));
    }
}
