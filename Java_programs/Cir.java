public class Cir {
    double pi = 3.14;

    double area(double r) {
        double a;

        a = pi * r * r;
        System.out.println("the ans is" + a);
        return (0);
    }

    double peri(double r) {
        double p;
        p = 2 * pi * r;
        System.out.println("the ans is" + p);
        return (0);
    }

    public static void main(String args[]) {
        double a, b;
        Cir obj = new Cir();
        a = obj.area(7.5);
        b = obj.peri(7.5);

    }
}