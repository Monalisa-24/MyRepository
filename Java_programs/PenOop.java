//class & objects

class Pen {
    String color;
    String type;

    public void write() {
        System.out.println("Write something :- ");
    }

    public void printcolor() {
        System.out.println(this.color);
        System.out.println(this.type);
    }
}

class Student {
    int age;
    String name;

    public void printinfo() {
        System.out.println(this.age);
        System.out.println(this.name);
    }
}

public class PenOop {
    public static void main(String[] args) {
        Pen pen1 = new Pen();
        pen1.color = "blue";
        pen1.type = "gel";

        Pen pen2 = new Pen();
        pen2.color = "orange";
        pen2.type = "fountain";

        pen1.write();
        pen1.printcolor();
        pen2.printcolor();

        Student std1 = new Student();
        std1.age = 10;
        std1.name = "Pratul";

        std1.printinfo();
    }

}