class Box {
    private int h;
    private int l;
    private int b;
    private int area;
    private int volumn;

    void show_area() {
        System.out.println("Area : " + area);
    }

    void show_volumn() {
        System.out.println("Volumn: " + volumn);
    }

    void Area(int height, int length) {
        h = height;
        l = length;
        area = h * l;
    }

    void Area(int a) {
        h = a;
        area = h * h;
    }

    void Area(int height, int length, int breadth) {
        h = height;
        l = length;
        b = breadth;
        area = 2 * (l * b) + 2 * (b * h) + 2 * (h * l);
    }

    void Volumn(int height, int length, int breadth) {
        h = height;
        l = length;
        b = breadth;
        volumn = h * l * b;
    }

    void Volumn(int length) {
        h = l = b = length;
        volumn = h * l * b;
    }
}

class MethodOverload {
    public static void main(String[] args) {
        Box obj1 = new Box();
        // Box ref;
        obj1.Area(7, 8);
        obj1.show_area();
        obj1.Area(8);
        obj1.show_area();
        obj1.Volumn(8, 5, 9);
        obj1.show_volumn();
        obj1.Volumn(6);
        obj1.show_volumn();

    }
}
