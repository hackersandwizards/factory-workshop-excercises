import java.util.ArrayList;
import java.util.List;

// Simple sample file — used to test that the pirate rule does NOT activate
// when working on .java files (glob: "**/*.md" only).
//
// Bonus: if you build the Java stretch rule, this file has a few intentional
// anti-patterns to flag (raw types, == on strings, C-style index loop,
// mutable public field, missing final).
public class main {

    static class Greeter {
        public String name;   // public mutable field instead of private + accessor

        Greeter(String name) {
            this.name = name;
        }

        void greet() {
            System.out.println("Hello, " + name + "!");
        }
    }

    public static void main(String[] args) {
        Greeter g = new Greeter("world");
        g.greet();

        String mode = new String("loud");          // redundant new String(...)
        if (mode == "loud") {                       // reference compare instead of .equals
            System.out.println("mode is loud");
        }

        List nums = new ArrayList();                // raw type, no generics
        nums.add(1);
        nums.add(2);
        nums.add(3);
        for (int i = 0; i < nums.size(); i++) {     // C-style index loop
            System.out.print(nums.get(i) + " ");
        }
        System.out.println();
    }
}
