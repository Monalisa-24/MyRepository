import java.util.*;

class Employee {
    private int eno;
    private String ename;
    private int salary;

    Employee(int eno, String ename, int salary) {
        this.eno = eno;
        this.ename = ename;
        this.salary = salary;
    }

    public int getEno() {
        return eno;
    }

    public String getEname() {
        return ename;
    }

    public int getSalary() {
        return salary;
    }

    public String toString() {
        return eno + " " + ename + " " + salary;
    }
}

class EmpSystemCrud {
    public static void main(String[] args) {
        List<Employee> c = new ArrayList<Employee>();
        Scanner scan = new Scanner(System.in);
        Scanner scan1 = new Scanner(System.in);
        int ch;

        while (true) {
            System.out.println("\n---------- MENU ----------");
            System.out.println("1. INSERT");
            System.out.println("2. DISPLAY");
            System.out.println("3. SEARCH");
            System.out.println("4. DELETE");
            System.out.println("5. UPDATE");
            System.out.println("6. EXIT");
            System.out.println("--------------------------");

            System.out.print("Enter your choice : ");
            ch = scan.nextInt();
            System.out.println("\n");
            switch (ch) {

                case 1:
                    System.out.print("Enter eno : ");
                    int eno = scan.nextInt();
                    System.out.print("Enter ename : ");
                    String ename = scan1.nextLine();
                    System.out.print("Enter salary : ");
                    int salary = scan.nextInt();

                    c.add(new Employee(eno, ename, salary));
                    break;

                case 2:
                    System.out.println("----------------------------");
                    Iterator<Employee> i = c.iterator();
                    while (i.hasNext()) {
                        Employee e = i.next();
                        System.out.println(e);
                    }
                    System.out.println("----------------------------");
                    break;

                case 3:
                    Boolean found = false;
                    System.out.print("Enter eno to search : ");
                    eno = scan.nextInt();
                    System.out.println("----------------------------");
                    i = c.iterator();
                    while (i.hasNext()) {
                        Employee e = i.next();
                        if (e.getEno() == eno) {
                            System.out.println(e);
                            found = true;
                        }
                    }
                    if (!found) {
                        System.out.println("Employee doesn't exist.");
                    }
                    System.out.println("----------------------------");
                    break;

                case 4:
                    found = false;
                    System.out.print("Enter eno to search : ");
                    eno = scan.nextInt();
                    System.out.println("----------------------------");
                    i = c.iterator();
                    while (i.hasNext()) {
                        Employee e = i.next();
                        if (e.getEno() == eno) {
                            i.remove();
                            found = true;
                        }
                    }
                    if (!found) {
                        System.out.println("Employee doesn't exist.");
                    } else {
                        System.out.println("\nRecord has been deleted successfully.\n");
                    }
                    System.out.println("----------------------------");
                    break;

                case 5:
                    found = false;
                    System.out.print("Enter eno to search : ");
                    eno = scan.nextInt();
                    System.out.println("----------------------------");
                    ListIterator<Employee> li = c.listIterator();
                    while (li.hasNext()) {
                        Employee e = li.next();
                        if (e.getEno() == eno) {
                            System.out.print("enter new name : ");
                            ename = scan1.nextLine();

                            System.out.print("enter new salary : ");
                            salary = scan.nextInt();

                            li.set(new Employee(eno, ename, salary));
                            found = true;
                        }
                    }
                    if (!found) {
                        System.out.println("Employee doesn't exist.");
                    } else {
                        System.out.println("\nRecord has been updated successfully.\n");
                    }
                    System.out.println("----------------------------");
                    break;

                case 6:
                    System.out.println("Disconnecting.......\n");
                    System.out.println("Disconnected. See you soon!");
                    System.exit(0);
                    break;

                default:
                    System.out.println("Invalid option...");
                    break;
            }
        }

    }
}
