class Box {
    int height;
    int width;

    Box() {
        height = 10;
        width = 20;
    }

    Box(int h, int w) {
        height = h;
        width = w;
    }

    Box(Box b) {
        height = b.height;
        width = b.width;
    }

    int area() {
        return height * width;
    }
}

class ConsturctorOverloading {
    public static void main(String[] args) {
        Box box1 = new Box();
        System.out.println("AREA : " + box1.area());
        Box box2 = new Box(78, 56);
        System.out.println("AREA : " + box2.area());
        Box box3 = new Box(box2);
        System.out.println("AREA : " + box3.area());
    }
}