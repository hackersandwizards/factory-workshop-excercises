package calc;

// Simple data holder. `value` is populated when type == NUMBER.
// `pos` is the 0-based offset in source, used for error messages.
public final class Token {
    public final TokenType type;
    public final long value;
    public final int pos;

    public Token(TokenType type, long value, int pos) {
        this.type = type;
        this.value = value;
        this.pos = pos;
    }
}
