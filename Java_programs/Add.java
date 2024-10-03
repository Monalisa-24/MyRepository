import java.util.Scanner;

class Add {

    public static void main(String[] args) {
        int a, b, c;
        System.out.println("Enter any two numbers to add :- ");
        Scanner sc = new Scanner(System.in);

        a = sc.nextInt();
        b = sc.nextInt();
        c = a + b;
        System.out.println("The result is = " + c);
        sc.close();
    }
}