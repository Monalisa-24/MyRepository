class Shape {
    String color;

    public void area() {
        System.out.println("Displays area.");
    }
}

class Triangle extends Shape { // single level inheritance
    public void area(int l, int h) {
        System.out.println((l * h) / 2);
        System.out.println(this.color);
    }
}

// class EquilateralTriangle extends Triangle { // multi level inheritance
// public void area(int l, int h) {
// System.out.println(1 / 2 * l * h);
// }
// }

class Circle extends Shape {
    public void area(int r) {
        System.out.println(3.14 * r * r);
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Triangle t1 = new Triangle();
        t1.color = "Green";
        t1.area(15, 13);

        Circle c1 = new Circle();
        c1.area(2);
    }

}

/*
 * inheritance is of 4 types ...(1) single level inheritance (2) multi level
 * inheritance
 * (3) hierarchical inheritance (4) hybrid inheritance
 * 
 * (5) multiple inheritance(rarely used in java, vast use in C++)
 */