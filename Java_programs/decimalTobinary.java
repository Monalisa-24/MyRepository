/* 6. Write a Java program to convert a decimal number taken as input from command line to binary number.
Input Data:
Input a Decimal Number: 5
Expected Output
Binary number is: 101
*/

public class decimalTobinary {
    public static void main(String[] args) {
        int binary[] = new int[30];
        int dec = 0, i = 0, j = 0;
        dec = Integer.parseInt(args[0]);
        while (dec > 0) {
            binary[i++] = dec % 2;
            dec = dec / 2;
        }
        for (j = i - 1; j >= 0; j--) {
            System.out.print(binary[j]);
        }

    }
}
