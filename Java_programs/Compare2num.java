/* 7. Write a Java program to compare two numbers taken as input from command line. Input Data:
Input first integer: 25
Input second integer: 39

Expected Output : 
25! = 39
25 < 39
25 <= 39
*/

public class Compare2num {
    public static void main(String[] args) {
        // int x, y;
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);
        if (x != y)
            System.out.println(x + " != " + y);
        if (x < y)
            System.out.println(x + " < " + y);
        if (x <= y)
            System.out.println(x + " <= " + y);
        if (x > y)
            System.out.println(x + " > " + y);
        if (x >= y)
            System.out.println(x + " >= " + y);
        if (x == y)
            System.out.println(x + " == " + y);

        System.out.println("COMPARISON IS COMPLETED SUCCESSFULLY...");

    }
}