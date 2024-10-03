/*5. Write a Java program to print an equilateral triangle using the character ‘*’.
Input Data:
Input the number of rows: 6
Expected Output
*
* *
* * *
* * * *
* * * * *
* * * * * *     */
public class Triangle {
    public static void main(String[] args) {
        int n, i, j;
        n = Integer.parseInt(args[0]);
        for (i = 0; i < n; i++) {
            for (j = 0; j <= i; j++) {
                System.out.print(" * ");
            }
            System.out.println();
        }
    }
}
