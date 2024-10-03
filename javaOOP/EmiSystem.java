package myPackage0;

public class EmiSystem {
    public static void main(String[] args) {
        Emi es = new Emi();
        es.getPrincipal();
        es.getTime();
        es.getRate();
        es.ShowInput();
        System.out.println("\tEMI AMOUNT = " + es.emiCalculator() + "/-");
        System.out.println("\n");
    }
}
