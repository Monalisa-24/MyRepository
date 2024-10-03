// using throws keyword

import java.util.Scanner;

class Division {
    public static void divide(int dividant, int divisor) throws ArithmeticException {
        int result = dividant / divisor;
        System.out.println("Result is : " + result);
    }
}

public class MyException1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the dividant : ");
        int dividant = sc.nextInt();
        System.out.print("Enter the divisor : ");
        int divisor = sc.nextInt();

        try {
            Division.divide(dividant, divisor);
        } catch (ArithmeticException e) {
            System.out.println("Exception occured : " + e);
        } finally {
            System.out.println("Program execution got finished.");
        }
        sc.close();
    }
}