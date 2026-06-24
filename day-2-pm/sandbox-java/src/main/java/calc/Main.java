package calc;

import java.util.Scanner;

public final class Main {

    private Main() {
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("calc REPL — type 'exit' or Ctrl-D to quit");
        while (true) {
            System.out.print("> ");
            System.out.flush();
            if (!scanner.hasNextLine()) {
                System.out.println();
                break;
            }
            String line = scanner.nextLine();
            if (line.equals("exit") || line.equals("quit")) {
                break;
            }
            if (line.isEmpty()) {
                continue;
            }
            try {
                Node ast = Parser.parse(line);
                System.out.println(Evaluator.evaluate(ast));
            } catch (CalcException ex) {
                System.out.println("error: " + ex.getMessage());
            }
        }
    }
}
