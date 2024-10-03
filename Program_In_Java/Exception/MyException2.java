// using throw keywod

import java.util.Scanner;

class checkNegative {
    public static void check(int num) {
        if (num < 1) {
            throw new IllegalArgumentException(num + " is negative.");
        } else {
            System.out.println(num + " is positive.");
        }
    }
}

public class MyException2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check : ");
        int num = sc.nextInt();

        try {
            checkNegative.check(num);
        } catch (Exception e) {
            System.out.println("Execution : " + e);
        } finally {
            System.err.println("Execution stopped.");
        }

        sc.close();
    }
}
