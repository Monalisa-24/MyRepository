/* 9. Write a Java program to compute the area of a hexagon. The length of a side must be taken as an input
from keyboard.
Area of a hexagon = (6 * s^2)/(4*tan(π/6))
where s is the length of a side Input Data:
Input the length of a side of the hexagon: 6
Expected Output
The area of the hexagon is: 93.53074360871938
*/

public class Hexagon {
    public static void main(String[] args) {
        double area;
        double s = Double.parseDouble(args[0]);
        area = (6 * (s * s)) / (4 * Math.tan(Math.PI / 6));
        System.out.println("AREA OF HEXAGON = " + area);
    }
}