/* 10. Write a Java program to print the given Triangle row values given character through command line.
Expected Output
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
*/
public class TriangleNum {
  public static void main(String[] args) {
    int i, j;
    int n = Integer.parseInt(args[0]);
    for (i = 1; i <= n; i++) {
      for (j = i; j <= n; j++) {
        System.out.print(" ");
      }
      for (j = 1; j <= i; j++) {
        System.out.print(j);
      }
      for (j = i - 1; j >= 1; j--) {
        System.out.print(j);
      }
      System.out.println();
    }
  }
}