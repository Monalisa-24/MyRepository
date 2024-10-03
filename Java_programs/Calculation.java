/*1. Write a Java program to print the sum (addition), multiply, subtract, divide and remainder of two
numbers taken as command line argument.*/
public class Calculation {
    public static void main(String[] args) {
        int a, b, sum, multi, sub, div, rem;
        a = Integer.parseInt(args[0]);
        b = Integer.parseInt(args[1]);
        sum = a + b;
        multi = a * b;
        sub = a - b;
        div = a / b;
        rem = a % b;
        System.out.println("The sum of" + " " + a + " and " + b + " " + "is : " + sum);
        System.out.println("The multiplication of" + " " + a + " and " + b + " " + "is : " + multi);
        System.out.println("The subtraction of" + " " + a + " and " + b + " " + "is : " + sub);
        System.out.println("The division of" + " " + a + " and " + b + " " + "is : " + div);
        System.out.println("The remainder of" + " " + a + " and " + b + " " + "is :" + rem);
    }
}