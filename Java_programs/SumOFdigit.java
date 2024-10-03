/* 8. Write a Java program and compute the sum of the digits of an integer number taken as input from
command line.
Input Data:
Input an integer: 25
Expected Output
The sum of the digits is: 7
*/

public class SumOFdigit {
    public static void main(String[] args) {
        int n, dig, sum = 0;
        n = Integer.parseInt(args[0]);
        while (n > 0) {
            dig = n % 10;
            sum = sum + dig;
            n = n / 10;
        }
        System.out.println("THE SUM OF DIGIT IS : " + sum);
    }
}

/* .........with program input......... */

// import java.util.Scanner;

// public class SumOFdigit {
// public static void main(String args[]) {
// int number, digit, sum = 0;
// Scanner sc = new Scanner(System.in);
// System.out.print("Enter the number: ");
// number = sc.nextInt();
// while (number > 0) {
// // finds the last digit of the given number
// digit = number % 10;
// // adds last digit to the variable sum
// sum = sum + digit;
// // removes the last digit from the number
// number = number / 10;
// }
// // prints the result
// System.out.println("Sum of Digits: " + sum);
// }
// }