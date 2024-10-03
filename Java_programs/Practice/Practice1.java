
/*class Practice1 {
    public static void main(String[] args) {
        System.out.println("Hellow World!");
    }
}*/

class Practice1 {
    public String name = "Monalisa";

    public String getname() {
        System.out.println("Name is : " + name);
        return name;
    }

    public static void main(String[] args) {
        Practice1 rv = new Practice1();
        rv.getname();
    }
}
