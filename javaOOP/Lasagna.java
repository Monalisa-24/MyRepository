public class Lasagna {
    int actualMins, layers;

    public int expectedMinutesInOven() {
        return 40;
    }

    public int remainingMinutesInOven(int actualMins) {
        return this.expectedMinutesInOven() - actualMins;
    }

    public int preparationTimeInMinutes(int layers) {
        return 2 * layers;
    }

    public int totalTimeInMinutes(int layers, int actualMins) {
        return this.preparationTimeInMinutes(layers) + actualMins;
    }

    public static void main(String[] args) {
        Lasagna lasagna = new Lasagna();
        System.out.println("Expected Time to finish cooking : " + lasagna.expectedMinutesInOven());
        System.out.println("Remaining Time : " + lasagna.remainingMinutesInOven(30));
        System.out.println("Preparation Time : " + lasagna.preparationTimeInMinutes(2));
        System.out.println("Total Time to finish cooking : " + lasagna.totalTimeInMinutes(3, 20));
    }
}