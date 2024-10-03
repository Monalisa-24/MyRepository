// MONALISA SAHA. R.No- 15201220118

/* 4. Write a program to accept a string from the user and find out the following statistics.
. Count of uppercase character.
. Count of lowercase character.
. Count of digits.
. Count of spaces.
*/

import java.util.*;

class Count1 {
    public void counting() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string :- ");
        String s = sc.nextLine();
        sc.close();
        int len = s.length();
        char c;
        int i, uppercase = 0, lowercase = 0, digit = 0, space = 0, other = 0;
        for (i = 0; i < len; i++) {
            c = s.charAt(i);
            if (c >= 'A' && c <= 'Z')
                uppercase++;
            else if (c >= 'a' && c <= 'z')
                lowercase++;
            else if (c >= '0' && c <= '9')
                digit++;
            else {
                if (c == ' ')
                    space++;
                else {
                    other++;
                }
            }
        }
        System.out.println("\nUppercase number : " + uppercase);
        System.out.println("Lowercase number : " + lowercase);
        System.out.println("Digit number : " + digit);
        System.out.println("Space number : " + space);
        System.out.println("Other number : " + other);
    }
}

public class Count {
    public static void main(String[] args) {
        Count1 obj = new Count1();
        obj.counting();
    }
}