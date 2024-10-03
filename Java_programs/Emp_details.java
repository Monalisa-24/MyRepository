import java.util.*;

class Employee {
    private int id;
    private String name;
    private String department;
    private String designation;
    private float salary;

    void get_data() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter employee id = ");
        id = sc.nextInt();
        sc.nextLine();
        System.out.println("Enter employee name = ");
        name = sc.nextLine();
        System.out.println("Enter employee department = ");
        department = sc.nextLine();
        System.out.println("Enter employee designation = ");
        designation = sc.nextLine();
        System.out.println("Enter employee salary = ");
        salary = sc.nextFloat();

        sc.close();
    }

    void get_print() {
        System.out.println("Employee id : " + id);
        System.out.println("Employee name : " + name);
        System.out.println("Employee department : " + department);
        System.out.println("Employee designation : " + designation);
        System.out.println("Employee salary : " + salary);
    }

    void match(String name) {
        String temp = name;
        if (this.name.equals(temp))
            get_print();
    }

}

public class Emp_details {
    public static void main(String[] args) {
        Employee e1 = new Employee();
        Employee e2 = new Employee();
        Employee e3 = new Employee();
        Employee e4 = new Employee();
        Employee e5 = new Employee();
        Employee e6 = new Employee();
        Employee e7 = new Employee();
        Employee e8 = new Employee();
        Employee e9 = new Employee();
        Employee e10 = new Employee();
        System.out.println(" for 1st employee : ");
        e1.get_data();
        // e1.get_print();
        System.out.println(" for 2nd employee : ");
        e2.get_data();
        // e2.get_print();
        System.out.println(" for 3rd employee : ");
        e3.get_data();
        // e3.get_print();
        System.out.println(" for 4th employee : ");
        e4.get_data();
        // e4.get_print();
        System.out.println(" for 5th employee : ");
        e5.get_data();
        // e5.get_print();
        System.out.println(" for 6th employee : ");
        e6.get_data();
        // e6.get_print();
        System.out.println(" for 7th employee : ");
        e7.get_data();
        // e7.get_print();
        System.out.println(" for 8th employee : ");
        e8.get_data();
        // e8.get_print();
        System.out.println(" for 9th employee : ");
        e9.get_data();
        // e9.get_print();
        System.out.println(" for 10th employee : ");
        e10.get_data();
        // e10.get_print();

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter employee name to be searched : ");
        String emp = sc.nextLine();

        e1.match(emp);
        e2.match(emp);
        e3.match(emp);
        e4.match(emp);
        e5.match(emp);
        e6.match(emp);
        e7.match(emp);
        e8.match(emp);
        e9.match(emp);
        e10.match(emp);

        sc.close();
    }
}