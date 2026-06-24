package calc;

// Recursive-descent parser holding a peeked token. Grammar:
//   expr   -> term   (('+' | '-') term)*
//   term   -> factor (('*' | '/') factor)*
//   factor -> NUMBER
public final class Parser {
    private final Lexer lexer;
    private Token current;

    private Parser(String source) {
        this.lexer = new Lexer(source);
        this.current = lexer.next();
    }

    // Parse a full expression from `source`. Throws CalcException on
    // syntactic problems (unexpected tokens, trailing input, etc.).
    public static Node parse(String source) {
        Parser parser = new Parser(source);
        Node root = parser.parseExpr();
        parser.expectEnd();
        return root;
    }

    private void advance() {
        current = lexer.next();
    }

    private Node parseExpr() {
        Node left = parseTerm();
        while (current.type == TokenType.PLUS || current.type == TokenType.MINUS) {
            BinOp op = (current.type == TokenType.PLUS) ? BinOp.Add : BinOp.Sub;
            advance();
            Node right = parseTerm();
            left = makeBinary(op, left, right);
        }
        return left;
    }

    private Node parseTerm() {
        Node left = parseFactor();
        while (current.type == TokenType.STAR || current.type == TokenType.SLASH) {
            BinOp op = (current.type == TokenType.STAR) ? BinOp.Mul : BinOp.Div;
            advance();
            Node right = parseFactor();
            left = makeBinary(op, left, right);
        }
        return left;
    }

    private Node parseFactor() {
        if (current.type != TokenType.NUMBER) {
            throw new CalcException(
                    "expected NUMBER but got " + Lexer.tokenTypeName(current.type)
                            + " at position " + current.pos);
        }
        Node node = new Node();
        node.kind = NodeKind.Number;
        node.value = current.value;
        advance();
        return node;
    }

    private void expectEnd() {
        if (current.type != TokenType.END) {
            throw new CalcException(
                    "unexpected token " + Lexer.tokenTypeName(current.type)
                            + " at position " + current.pos + " (expected end of input)");
        }
    }

    private static Node makeBinary(BinOp op, Node left, Node right) {
        Node node = new Node();
        node.kind = NodeKind.BinaryOp;
        node.op = op;
        node.left = left;
        node.right = right;
        return node;
    }
}
