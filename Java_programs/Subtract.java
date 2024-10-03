import java.util.Scanner;

class Subtract {
    public static void main(String[] args) {
        int a, b, c;
        System.out.println("Enter any two numbers for subtraction :- ");
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();

        c = a - b;
        System.out.println("The result is = " + c);
        sc.close();
    }

}