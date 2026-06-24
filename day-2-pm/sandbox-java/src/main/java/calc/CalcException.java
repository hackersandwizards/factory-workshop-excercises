package calc;

// Single throw type for parse/eval errors. The REPL is the one catch point.
public final class CalcException extends RuntimeException {
    public CalcException(String message) {
        super(message);
    }
}
