//.....................................................
// float/double
//.....................................................
/*import java.lang.Math;

class DifferenceOfSquaresCalculator {
    int input;

    double computeSquareOfSumTo(int input) {
        int i, sum = 0;
        for (i = 1; i <= input; i++) {
            sum += i;
        }
        double sq = Math.pow(sum, 2);
        return sq;
    }

    double computeSumOfSquaresTo(int input) {
        int i, sum = 0;
        for (i = 1; i <= input; i++) {
            double sq = Math.pow(i, 2);
            // System.out.println(sq);
            sum += sq;

        }
        return sum;
    }

    double computeDifferenceOfSquares(int input) {
        return this.computeSquareOfSumTo(input) - this.computeSumOfSquaresTo(input);
    }

    public static void main(String[] args) {
        DifferenceOfSquaresCalculator dsc = new DifferenceOfSquaresCalculator();
        System.out.println(dsc.computeSquareOfSumTo(10));
        System.out.println(dsc.computeSumOfSquaresTo(10));
        System.out.println(dsc.computeDifferenceOfSquares(10));
    }
}
*/

//........................................................................................................................................//
// integer
//.....................................................

class DifferenceOfSquaresCalculator {
    int input;

    int computeSquareOfSumTo(int input) {
        int i, sum = 0;
        for (i = 1; i <= input; i++) {
            sum += i;
        }
        int sq = sum * sum;
        return sq;
    }

    int computeSumOfSquaresTo(int input) {
        int i, sum = 0;
        for (i = 1; i <= input; i++) {
            int sq = i * i;
            sum += sq;

        }
        return sum;
    }

    int computeDifferenceOfSquares(int input) {
        return this.computeSquareOfSumTo(input) - this.computeSumOfSquaresTo(input);
    }

    public static void main(String[] args) {
        DifferenceOfSquaresCalculator dsc = new DifferenceOfSquaresCalculator();
        System.out.println("computeSquareOfSumTo : " + dsc.computeSquareOfSumTo(10));
        System.out.println("computeSumOfSquaresTo : " + dsc.computeSumOfSquaresTo(10));
        System.out.println("computeDifferenceOfSquares : " + dsc.computeDifferenceOfSquares(10));
    }
}
