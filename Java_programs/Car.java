/*parameterized constructor*/

//example 1
/*public class Car {
    String carColor;
    String carType;

    public Car(String Color, String Type) {
        carColor = Color;
        carType = Type;
    }

    public static void main(String[] args) {
        Car myCar = new Car("Black", "Audi");
        System.out.println("CAR COLOR IS : " + myCar.carColor + " AND " + "CAR TYPE IS : " + myCar.carType);
    }
}
*/

// example 2
public class Car {
    int x;

    public Car(int y) {
        x = y;
    }

    public static void main(String[] args) {
        Car myCar1 = new Car(5);
        System.out.println("x = " + myCar1.x);
    }
}