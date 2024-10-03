class Shape {
    double area(double r) {
        return (3.14 * r * r);
    }

    double area(double a) {
        return (a * a);
    }

    double area(int a, double b) {
        return (a * b);
    }

    double area(double a, int b) {
        return (a * b);
    }
}

class MethodOverloadShape {
    public static void main(String[] args) {
        Shape s = new Shape();
        System.out.println("AREA OF CIRCLE :  " + s.area(8.6));
        System.out.println("AREA OF RECTANGLE :  " + s.area(8.6, 5));
        System.out.println("AREA OF RECTANGLE :  " + s.area(8.6, 5));
    }
}