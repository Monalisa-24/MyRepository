/*2. Write a Java program that takes a number as input from command line and prints its multiplication table
up to 10.*/
public class Multiplication {
    public static void main(String[] args) {
        int n, i, mul;
        n = Integer.parseInt(args[0]);
        System.out.println("The result = ");
        for (i = 1; i <= 10; i++) {
            mul = n * i;
            System.out.println(mul);
        }
        System.out.println("COMPLETE :-)");
    }
}