package myPackage1;

import java.util.*;

public class Emp {
    String name, address, ID, ph_no, jobrole, salary;
    Scanner scan = new Scanner(System.in);

    public void newEntry() {
        System.out.print("Enter the name of the employee : ");
        name = scan.next();
        scan.nextLine();
        System.out.print("Enter the address of the employee : ");
        address = scan.next();
        System.out.print("Enter the Govt. ID of the employee : ");
        ID = scan.next();
        System.out.print("Enter the phone no of the employee : ");
        ph_no = scan.next();
        System.out.print("Enter the jobrole of the employee : ");
        jobrole = scan.next();
        System.out.print("Enter the salary no of the employee : ");
        salary = scan.next();
    }

    public boolean searchingEntryByID(String search) {
        // System.out.println("Hi!");
        if (ID.equals(search)) {
            showAllEntries();
            return (true);
        }
        return (false);
    }

    public boolean searchingEntryByName(String search) {
        // System.out.println("Hi!");
        if (name.equals(search)) {
            showAllEntries();
            return (true);
        }
        return (false);
    }

    public boolean searchingEntryBySalary(String search) {
        // System.out.println("Hi!");
        if (salary.equals(search)) {
            showAllEntries();
            return (true);
        }
        return (false);
    }

    public boolean searchingEntryByPhNo(String search) {
        // System.out.println("Hi!");
        if (ph_no.equals(search)) {
            showAllEntries();
            return (true);
        }
        return (false);
    }

    public boolean searchingEntryByJobRole(String search) {
        // System.out.println("Hi!");
        if (jobrole.equals(search)) {
            showAllEntries();
            return (true);
        }
        return (false);
    }

    public void showAllEntries() {
        System.out.println("name of the employee : " + name);
        System.out.println("address of the employee : " + address);
        System.out.println("Govt. ID of the employee : " + ID);
        System.out.println("Phone no of the employee : " + ph_no);
        System.out.println("Jobrole of the employee : " + jobrole);
        System.out.println("Salary of the employee : " + salary);
    }

    public void showParticularEntry() {
        System.out.println("name of the employee : " + name);
        System.out.println("address of the employee : " + address);
        System.out.println("Govt. ID of the employee : " + ID);
        System.out.println("Phone no of the employee : " + ph_no);
        System.out.println("Jobrole of the employee : " + jobrole);
        System.out.println("Salary of the employee : " + salary);
    }

    public void updateEntry() {
        System.out.println("you");
    }

    public void deleteEntry() {
        System.out.println("bro?");
    }
}
