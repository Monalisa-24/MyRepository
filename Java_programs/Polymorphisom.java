class Student2 {
    String name;
    int age;

    public void printinfo(String name) {
        System.out.println(name);
    }

    public void printinfo(int age) {
        System.out.println(age);
    }

    public void printinfo(String name, int age) {
        System.out.println(name + ' ' + age);
    }
}

public class Polymorphisom {
    public static void main(String[] args) {
        Student2 std1 = new Student2();
        std1.name = "Nandini";
        std1.age = 20;

        std1.printinfo(std1.name);
        std1.printinfo(std1.age);
        std1.printinfo(std1.name, std1.age);
    }

}

/*
 * polymorphisom is of 2 types - (1) compile-time polymorphisom (2) run-time
 * polymorphisom.
 * run-time polymorphisom could be hardar to us than the other type.
 */