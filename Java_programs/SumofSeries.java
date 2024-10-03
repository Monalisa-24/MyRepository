class Series {
    private int n;
    private double sum;

    void setValue(int num) {
        n = num;
    }
    // Series(int num) {
    // n = num;
    // }

    private int factorial(int range) {
        int fact = 1;
        for (int i = 1; i <= range; i++)
            fact = fact * i;
        return fact;
    }

    void result() {
        for (int i = 1; i <= n; i++) {
            sum = sum + (double) i / (double) factorial(i);
        }
    }
}

class SumofSeries {
    public static void main(String[] args) {

        Series obj = new Series();
        obj.setValue(Integer.parseInt(args[0]));

        // Series obj = new Series(Integer.parseInt(args[0]));
        obj.result();
    }
}