import java.util.Scanner;

public class prog1 {
    int c;

    // public method void addition(int a, int b) { static method
    // public void addition(int a, int b) { // non-static method
    // Scanner sc = new Scanner(System.in);
    // int c = a + b;
    // System.out.println(c);
    // }
    prog1(int a, int b) {
        c = a + b;
        System.out.println("result = " + c);
    }

    public static void main(String[] args) {
        prog1 p1 = new prog1(6, 5);
        // p1.addition(6, 5); // non-static method
        // System.out.println(p1.c);
        // prog1.addition(6, 5); static method call
    }
}
