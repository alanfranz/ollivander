package eu.franzoni.examples.pythonvsjavaencoding;


import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.PrintStream;

public class CantEncode {
    public static void main(String[] args) throws Exception {
        // change default output stream
        OutputStream outputStream = new FileOutputStream("eu.franzoni.examples/src/eu/franzoni/examples/pythonvsjavaencoding/CantEncode.output");
        PrintStream printStream = new PrintStream(outputStream, true, "ASCII");
        System.setOut(printStream);

        String myString = "àèìòù";

        System.out.println(System.out.getClass());
        System.out.println(myString);
     }
}
