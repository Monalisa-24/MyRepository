import java.util.Scanner;

class DynamicInput {
    private String emp_name;
    private int emp_phone;
    private String emp_email;
    private double emp_sal;

    void read() {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER EMPLOYEE NAME : ");
        emp_name = sc.nextLine();
        System.out.println("ENTER EMPLOYEE PHONE NUMBER : ");
        emp_phone = sc.nextInt();
        // sc.nextLine();
        System.out.println("ENTER EMPLOYEE EMAIL ID : ");
        emp_email = sc.nextLine();
        System.out.println("ENTER EMPLOYEE SALARY : ");
        emp_sal = sc.nextDouble();
    }

    void print() {
        System.out.println("ENTER EMPLOYEE NAME : " + emp_name);
        System.out.println("ENTER EMPLOYEE PHONE NUMBER : " + emp_phone);
        System.out.println("ENTER EMPLOYEE EMAIL ID : " + emp_email);
        System.out.println("ENTER EMPLOYEE SALARY : " + emp_sal);
    }

    public static void main(String[] args) {
        DynamicInput d1 = new DynamicInput();
        d1.read();
        d1.print();
    }
}