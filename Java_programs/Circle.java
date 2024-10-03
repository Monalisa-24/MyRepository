/*3. Write a Java program to print the area and perimeter of a circle. The radius of circle must be taken from
command line argument as input.
Test Data:
Radius = 7.5
Expected Output
Perimeter is = 47.12388980384689 Area
is = 176.71458676442586*/

public class Circle {
    public static void main(String[] args) {
        double radius, peri, area;
        radius = Double.parseDouble(args[0]);
        area = Math.PI * radius * radius;
        peri = 2 * Math.PI * radius;
        System.out.println("The AREA is = " + area);
        System.out.println("The PERIMETER is = " + peri);
    }
}