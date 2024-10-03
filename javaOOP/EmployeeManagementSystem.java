package myPackage1;

import java.util.*;

public class EmployeeManagementSystem {
    public static void main(String[] args) {
        Emp em = new Emp();
        Scanner scan = new Scanner(System.in);
        System.out.print("\nHow many number of employees do you want to input? ");
        int n = scan.nextInt();
        Emp EM[] = new Emp[n];
        for (int i = 0; i < EM.length; i++) {
            System.out.println("\n customer no : " + (i + 1));
            System.out.println("\n..........................\n");
            EM[i] = new Emp();
            EM[i].newEntry();
        }
        int choice;
        while (true) {
            System.out.println("\n-------------------- MENU --------------------");
            System.out.println("1.New Entry of an Employee -> ");
            System.out.println("2.Searching by a unique Id ->");
            System.out.println("3.Show all entries ->");
            System.out.println("4.show entry details by ID ->");
            System.out.println("5.show entry details by Name ->");
            System.out.println("6.show entry details by Salary ->");
            System.out.println("7.show entry details by Phone Number ->");
            System.out.println("8.show entry details by Job Role ->");
            System.out.println("9.Update entry ->");
            System.out.println("10.Delete entry ->");
            System.out.println("11.Quit ->");
            System.out.println("----------------------------------------------\n");

            System.out.print("Enter your choice : ");
            choice = scan.nextInt();
            System.out.println("\n");
            switch (choice) {
                case 1:
                    em.newEntry();
                    break;
                case 2:
                    System.out.print("enter the Govt. ID : ");
                    String id = scan.next();
                    System.out.println("\n");
                    Boolean found = false;
                    for (int i = 0; i < EM.length; i++) {
                        found = EM[i].searchingEntryByID(id);
                    }
                    if (found) {
                        break;
                    }
                    if (!found) {
                        System.out.println("Govt. Id you have entered doesn't match.");
                    }
                    break;
                case 3:
                    for (int i = 0; i < EM.length; i++) {
                        EM[i].showAllEntries();
                        System.out.println(".................................................");
                    }
                    break;
                case 4:
                    System.out.print("enter the Govt. ID : ");
                    String searchBYid = scan.next();
                    Boolean found1 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found1 = EM[i].searchingEntryByID(searchBYid);
                    }
                    if (found1) {
                        break;
                    }
                    if (!found1) {
                        System.out.println("Govt. Id you have entered doesn't match.");
                    }
                    break;
                case 5:
                    System.out.print("Enter the name of the employee : ");
                    String searchBYname = scan.next();
                    Boolean found2 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found2 = EM[i].searchingEntryByName(searchBYname);
                    }
                    if (found2) {
                        break;
                    }
                    if (!found2) {
                        System.out.println("Employee doesn't exist.");
                    }
                    break;
                case 6:
                    System.out.print("Enter the salary of the employee : ");
                    String searchBYsalary = scan.next();
                    Boolean found3 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found3 = EM[i].searchingEntryBySalary(searchBYsalary);
                    }
                    if (found3) {
                        break;
                    }
                    if (!found3) {
                        System.out.println("Employee doesn't exist.");
                    }
                    break;
                case 7:
                    System.out.print("Enter the salary of the employee : ");
                    String searchBYphno = scan.next();
                    Boolean found4 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found4 = EM[i].searchingEntryByPhNo(searchBYphno);
                    }
                    if (found4) {
                        break;
                    }
                    if (!found4) {
                        System.out.println("Employee doesn't exist.");
                    }
                    break;
                case 8:
                    System.out.print("Enter the salary of the employee : ");
                    String searchBYjobrole = scan.next();
                    Boolean found5 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found5 = EM[i].searchingEntryByJobRole(searchBYjobrole);
                    }
                    if (found5) {
                        break;
                    }
                    if (!found5) {
                        System.out.println("Employee doesn't exist.");
                    }
                    break;
                case 9:
                    System.out.print("enter the Govt. ID : ");
                    String updateByid = scan.next();
                    Boolean found6 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        found6 = EM[i].searchingEntryByID(updateByid);
                    }
                    if (found6) {
                        break;
                    }
                    if (!found6) {
                        System.out.println("Govt. Id you have entered doesn't match.");
                    }
                    break;
                    // em.updateEntry();
                    break;
                case 10:
                    System.out.print("enter the Govt. ID : ");
                    int index = 3;
                    // Boolean found7 = false;
                    System.out.println("\n");
                    for (int i = 0; i < EM.length; i++) {
                        if (index == EM[i]) {
                        }

                    }
                    // if (found7) {
                    // break;
                    // }
                    // if (!found7) {
                    // System.out.println("Govt. Id you have entered doesn't match.");
                    // }
                    break;
                    em.deleteEntry();
                    break;
                case 11:
                    System.out.println("Finished.");
                    System.exit(0);
                    // String opt;
                    // System.out.print("Are you sure to quit ? y/n : ");
                    // opt = scan.next();
                    // if (opt == "y") {
                    // System.exit(0);
                    // }
                default:
                    System.out.println("You entered invalid choice.Please check.");
                    break;

            }

        }
    }
}
