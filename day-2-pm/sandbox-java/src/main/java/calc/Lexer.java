package calc;

// Stream-style lexer. Construct over a source string, then call next() to
// advance through the token stream. Returns TokenType.END at end of input
// (and keeps returning it on subsequent calls).
public final class Lexer {
    private final String source;
    private int pos = 0;

    public Lexer(String source) {
        this.source = source;
    }

    private void skipWhitespace() {
        while (pos < source.length() && Character.isWhitespace(source.charAt(pos))) {
            ++pos;
        }
    }

    public Token next() {
        skipWhitespace();

        if (pos >= source.length()) {
            return new Token(TokenType.END, 0, pos);
        }

        final int start = pos;
        final char c = source.charAt(pos);

        if (Character.isDigit(c)) {
            long value = 0;
            while (pos < source.length() && Character.isDigit(source.charAt(pos))) {
                value = value * 10 + (source.charAt(pos) - '0');
                ++pos;
            }
            return new Token(TokenType.NUMBER, value, start);
        }

        ++pos;
        switch (c) {
            case '+':
                return new Token(TokenType.PLUS, 0, start);
            case '-':
                return new Token(TokenType.MINUS, 0, start);
            case '*':
                return new Token(TokenType.STAR, 0, start);
            case '/':
                return new Token(TokenType.SLASH, 0, start);
            default:
                throw new CalcException(
                        "unexpected character '" + c + "' at position " + start);
        }
    }

    public static String tokenTypeName(TokenType type) {
        switch (type) {
            case NUMBER:
                return "NUMBER";
            case PLUS:
                return "PLUS";
            case MINUS:
                return "MINUS";
            case STAR:
                return "STAR";
            case SLASH:
                return "SLASH";
            case END:
                return "END";
        }
        return "?";
    }
}
