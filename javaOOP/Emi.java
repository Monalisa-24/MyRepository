package myPackage0;

import java.util.*;
import java.lang.Math;

public class Emi {
    // int m = 10;
    float p, r, t, emi;
    Scanner sc = new Scanner(System.in);

    public void getPrincipal() {
        System.out.println("\n");
        System.out.println("------------------------------------------------");
        System.out.print("Enter your amount : ");
        p = sc.nextInt();
    }

    public float getTime() {
        System.out.println("Time to be chosen : 3yr, 6yr, 9yr, 12yr");
        System.out.print("Enter the time : ");
        t = sc.nextInt();
        if (t == 3) {
            t = 3;
        } else if (t == 6) {
            t = 6;
        } else if (t == 9) {
            t = 9;
        } else if (t == 12) {
            t = 12;
        } else {
            System.out.println("please choose valid duration.\nWe have only 4 option : 3m, 6m, 9m, 12m");
            t = 0;
        }
        System.out.println("------------------------------------------------");
        return t;
    }

    public void getRate() {
        if (this.t == 3) {
            r = 2;
        } else if (this.t == 6) {
            r = 4;
        } else if (this.t == 9) {
            r = 7;
        } else if (this.t == 12) {
            r = 10;
        } else {
            System.out.println("please choose valid duration.\nWe have only 4 option : 3m, 6m, 9m, 12m");
            r = 0;
        }
        // System.out.print("Enter the rate : ");
        // r = sc.nextInt();
        // System.out.println("\n");
    }

    public void ShowInput() {
        System.out.println("principal amount = " + p + "/-");
        System.out.println("rate = " + r + "%");
        System.out.println("time = " + t + "years");
        System.out.println("------------------------------------------------");
    }

    public float emiCalculator() {
        r = r / (12 * 100); // one month interest
        System.out.println("So, the monthly interest : " + r + "%");
        t = t * 12; // one month period
        System.out.println("So,how many months ? : " + t + "months");
        emi = (p * r * (float) Math.pow(1 + r, t)) / (float) (Math.pow(1 + r, t) - 1);
        System.out.println("------------------------------------------------");
        return emi;
    }

    // public static void main(String[] args) {
    // Emi es = new Emi();
    // es.getPrincipal();
    // es.getRate();
    // es.getTime();
    // es.ShowInput();
    // System.out.println("EMI AMOUNT = " + es.emiCalculator());
    // System.out.println("\n");
    // }
}