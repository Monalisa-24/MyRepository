class Practice {
    void today_class() {
        int i;
        for (i = 1; i <= 10; i++) {
            if (i == 5)
                break;
            // continue;
            System.out.println(i + " ");

        }
        System.out.println("now i = " + i);
    }

    public static void main(String[] args) {
        Practice P = new Practice();
        P.today_class();
    }
}