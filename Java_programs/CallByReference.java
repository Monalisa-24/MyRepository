class MyClass {
    int x;
    int y;

    MyClass(int a, int b) {
        x = a;
        y = b;
    }

    void print() {
        System.out.println("Value of X is : " + x);
    }

    void change(MyClass ob) {
        x = 2 * ob.x;
        y = 2 * ob.y;
    }
}

class CallByReference {
    public static void main(String[] args) {
        MyClass obj = new MyClass(7, 9);
        obj.print();
        obj.change(obj);
        obj.print();
    }
}