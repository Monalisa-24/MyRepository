import java.io.DataInputStream;

public class cmdLineArg {
    public static void main(String[] args) {
        DataInputStream in = new DataInputStream(System.in);
        int a, b;
        a = Integer.parseInt(args[0]);
        b = Integer.parseInt(args[1]);
        System.out.println("the number : " + a + " " + b);
    }
}
