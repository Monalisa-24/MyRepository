class RectArea {
    // calculate area of a rectangle using getdata
    int length, width;

    void getdata(int x, int y) {
        length = x;
        width = y;
    }

    int area() {
        int area = length * width;
        return (area);
    }
}

class getData_EX1 {
    public static void main(String[] args) {
        RectArea R1 = new RectArea();
        RectArea R2 = R1; // not using "RectArea R2 = new RectArea();"
                          // R1 & R2 points the same object, so we can write
                          // the previous line without creating object.

        /*
         * // not using getdata
         * R1.length = 20;
         * R1.width = 20;
         * int area1 = R1.length * R1.width;
         */

        R1.getdata(20, 20); // using getdata
        int area1 = R1.area();

        /*
         * // not using getdata
         * R2.length = 10;
         * R2.width = 10;
         * int area2 = R2.length * R2.width;
         */

        R2.getdata(10, 10); // using getdata
        int area2 = R2.area();

        System.out.println("The area1(R1) = " + area1);
        System.out.println("The area2(R2) = " + area2);
    }
}