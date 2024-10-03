class Swap {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c;
        System.out.println("a = " + a + " " + "b=" + b);
        c = a;
        a = b;
        b = c;
        System.out.println("a = " + a + " " + "b=" + b);
    }
}