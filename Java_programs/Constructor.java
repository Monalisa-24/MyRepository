class Student1 {
    String name;
    int age;

    public void student_info() {
        System.out.println("\nStudent information :- ");
        System.out.println(this.name);
        System.out.println(this.age);
    }

    Student1() {
        System.out.println("Constructor called."); // Non-parameterized constructor.
    }

    Student1(String name, int age) {
        this.name = name; // parameterized constructor.
        this.age = age;
    }

    Student1(Student1 s3) {
        this.name = s3.name; // copy constructor.
        this.age = s3.age;
    }

}

public class Constructor {
    public static void main(String[] args) {

        Student1 s1 = new Student1();
        s1.name = "Amal";
        s1.age = 7;

        Student1 s2 = new Student1("Kamal", 5);
        Student1 s3 = new Student1(s1);

        s1.student_info();
        s2.student_info();
        s3.student_info();
    }
}