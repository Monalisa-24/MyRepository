/*4. Write a Java program to print the area and perimeter of a rectangle. Inputs taken from command line
argument. Test Data:
Width = 5.6 Height = 8.5
Expected Output
Area is 5.6 * 8.5 = 47.60
Perimeter is 2 * (5.6 + 8.5) = 28.20*/
public class Rectangle {
    public static void main(String[] args) {
        float width, height, area, peri;
        width = Float.parseFloat(args[0]);
        height = Float.parseFloat(args[1]);
        area = width * height;
        peri = 2 * (width + height);
        System.out.println("THE AREA = " + area);
        System.out.println("THE PERI = " + peri);
    }
}