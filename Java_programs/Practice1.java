import java.util.Scanner;

class Practice1 {
    void swit() {
        int choice;
        int num1, num2, num3;

        while (true) {
            System.out.println("menu :-\n");
            System.out.println("1. add.\n");
            System.out.println("2. subtract.\n");
            System.out.println("3. Multiply.\n");
            System.out.println("4. Divide.\n");
            System.out.println("5. Remainder.\n");
            System.out.println("6. Quit.\n");
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter your choice = \n");
            choice = sc.nextInt();
            System.out.println("Enter 2 numbers =\n");
            num1 = sc.nextInt();
            num2 = sc.nextInt();
            switch (choice) {
                case 1:
                    num3 = num1 + num2;
                    System.out.println("Addition = " + num3);
                    break;
                case 2:
                    num3 = num1 - num2;
                    System.out.println("Subtraction = " + num3);
                    break;
                case 3:
                    num3 = num1 * num2;
                    System.out.println("Multiplication = " + num3);
                    break;
                case 4:
                    num3 = num1 / num2;
                    System.out.println("Division = " + num3);
                    break;
                case 5:
                    num3 = num1 % num2;
                    System.out.println("Remainder = " + num3);
                    // sc.close();
                    break;
                case 6:
                    System.exit(0);
                default:
                    System.out.println("Invalid choice !!!\n");
                    break;

            }
        }

    }

    public static void main(String[] args) {
        Practice1 prac = new Practice1();
        prac.swit();
    }
}