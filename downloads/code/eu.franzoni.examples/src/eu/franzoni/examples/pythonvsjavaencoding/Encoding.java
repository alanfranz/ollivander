package eu.franzoni.examples.pythonvsjavaencoding;

import java.nio.charset.Charset;

public class Encoding {
    public static void main(String[] args) throws Exception {
        String myString = "àèìòù";
        System.out.println(System.out.getClass());
        System.out.println(Charset.defaultCharset());
        System.out.println(myString);
        System.out.write(myString.getBytes(Charset.defaultCharset()));
        System.out.println("");
    }
}
