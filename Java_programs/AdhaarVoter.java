import java.util.Scanner;

public class AdhaarVoter {
    int a;
    String n;
    int adhaarNum;
    int voterNum;

    public void getData() {
        Scanner in = new Scanner(System.in);
        System.out.print("your age : ");
        a = in.nextInt();
        in.nextLine();
        System.out.print("your name : ");
        n = in.nextLine();
        System.out.print("your adhaar Id : ");
        adhaarNum = in.nextInt();
        System.out.print("your voter Id : ");
        voterNum = in.nextInt();
    }

    void display() {
        System.out.println("\n\nAge :" + a + "   " + "Name : " + n);
        System.out.println("\nA.No : " + adhaarNum + "    " + "V.No : " + voterNum);
    }

    int check() {
        if (a == 0) {
            return 0;
        } else if (n == "") {
            return 0;
        } else {
            return 1;

        }
    }

    public static void main(String[] args) {
        System.out.println("\n\n| For Adhaar - Voter Linkage |\n");
        AdhaarVoter av = new AdhaarVoter();
        av.getData();
        av.display();
        av.check();
        if (av.check() == 1) {
            System.out.println("\nLinkage done successfully .");
        } else {
            System.out.println("\nInsufficient details. Couldn't proceed .");
        }
    }

}
