package calc;

// Walk the AST and return the integer result. Throws CalcException on
// division by zero. Pure integer arithmetic — no floats.
public final class Evaluator {

    private Evaluator() {
    }

    public static long evaluate(Node node) {
        switch (node.kind) {
            case Number:
                return node.value;

            case BinaryOp: {
                final long left = evaluate(node.left);
                final long right = evaluate(node.right);
                switch (node.op) {
                    case Add:
                        return left + right;
                    case Sub:
                        return left - right;
                    case Mul:
                        return left * right;
                    case Div:
                        if (right == 0) {
                            throw new CalcException("division by zero");
                        }
                        return left / right;
                }
            }
        }
        throw new CalcException("evaluator: unknown node kind");
    }
}
