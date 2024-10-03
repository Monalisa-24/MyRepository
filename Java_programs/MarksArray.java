import java.util.*;

public class MarksArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the range of array index :- ");
        int n = sc.nextInt();
        int marks[] = new int[n];
        int i;
        // marks[0] = 85;
        // marks[1] = 87;
        // marks[2] = 88; // statically input.
        // marks[3] = 84;
        System.out.println("Exam was sout of ? :- ");
        int fullmarks = sc.nextInt();

        System.out.println("Inputting marks out of " + fullmarks + " :- ");
        for (i = 0; i < n; i++) {
            marks[i] = sc.nextInt(); // input taken from users.
        }

        System.out.println("Marks got :- ");
        for (i = 0; i < n; i++) {
            System.out.println(marks[i]);
        }

        System.out.println("Enter the marks to be searched = ");
        int x = sc.nextInt();
        for (i = 0; i < marks.length; i++) {
            if (marks[i] == x) { // element searching.
                System.out.println(x + " Marks found at index " + i + ".");
            }
            /*
             * else {
             * System.out.println("not found.");
             * } // here condition in else is doing some trouble.
             */

        }
    }
}