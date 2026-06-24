package calc;

// Tiny AST. Two node kinds, one flat node type. We use a `kind` discriminator
// and plain fields — simple structs over deep OOP.
public final class Node {
    public NodeKind kind;

    // Number payload
    public long value = 0;

    // BinaryOp payload
    public BinOp op = BinOp.Add;
    public Node left;
    public Node right;
}
