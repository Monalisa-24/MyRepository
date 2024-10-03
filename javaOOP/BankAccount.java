import java.util.Scanner;

class AccountOpening {

    private String accno;
    private String name;
    private String acc_type;
    private long balance;
    public int depositAmount;
    public int withdrawalAmount;
    Scanner sc = new Scanner(System.in);

    public void OpenAccount() {
        System.out.print("\nEnter Account No: ");
        accno = sc.next();
        System.out.print("\nEnter Account type: ");
        acc_type = sc.next();
        System.out.print("\nEnter Name: ");
        name = sc.next();
        System.out.print("\nEnter Balance: ");
        balance = sc.nextLong();
    }

    public void showAccount() {
        System.out.println("\nName of account holder: " + name);
        System.out.println("Account no.: " + accno);
        System.out.println("Account type: " + acc_type);
        System.out.println("Balance: " + balance);
        System.out.print("\n");
    }

    public void deposit() {
        System.out.println("Deposit");
        depositAmount = sc.nextInt();
        // sc.close();
        System.out.println("you have deposited rs." + depositAmount);
        balance += depositAmount;
        System.out.println("your balance is rs. " + balance);
        // return balance;
    }

    public void withdrawal() {
        System.out.println("Withdrawal");
        // Scanner sc1 = new Scanner(System.in);
        withdrawalAmount = sc.nextInt();
        // sc.close();
        if (withdrawalAmount > balance) {
            System.out.println("sorry!");
            System.out.println("you have rs. " + balance + " in your account");
        } else {
            System.out.println("you have withdrawed rs." + withdrawalAmount);
            balance -= withdrawalAmount;
            System.out.println("your balance is rs. " + balance);
        }
        // return balance;
    }

    // public void balanceInfo1(int balance) {
    // System.out.println("your balance is : " + balance);
    // }

}

public class BankAccount extends AccountOpening {

    public static void main(String[] args) {
        int choice;
        while (true) {
            System.out.print("\n");
            System.out.println("1.openAccount ->");
            System.out.println("2.display account ->");
            System.out.println("3.deposit ->");
            System.out.println("4.withdrawal ->");
            System.out.println("5.quit ->");
            System.out.print("\n");
            Scanner sc = new Scanner(System.in);
            System.out.print("enter your choice = ");
            choice = sc.nextInt();
            BankAccount ba = new BankAccount();

            switch (choice) {
                case 1:
                    ba.OpenAccount();
                    break;

                case 2:
                    ba.showAccount();
                    break;

                case 3:
                    ba.deposit();
                    break;

                case 4:
                    ba.withdrawal();
                    break;
                case 5:
                    System.out.println("\nSee you soon...");
                    break;
                default:
                    System.out.println("please enter the valid option!");
                    break;
            }

        }
    }
}