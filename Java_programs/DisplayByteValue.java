// WAJP thats stores bytes and disolay it in screen.

public class DisplayByteValue {
    int rollNo;

    public DisplayByteValue(int y) {
        rollNo = y;
    }

    public static void main(String[] args) {
        DisplayByteValue dbv = new DisplayByteValue(56);
        String name = "Rima";
        System.out.println(name);
        System.out.println("roll no :- " + dbv.rollNo);

    }
}
