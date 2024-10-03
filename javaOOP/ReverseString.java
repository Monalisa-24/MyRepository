class ReverseString {

    String reverse(String inputString) {
        String reverseString = "";

        for (int i = 0; i < inputString.length(); i++) {
            reverseString = inputString.charAt(i) + reverseString;
            System.out.println(reverseString);
        }

        return reverseString;
    }

    public static void main(String[] args) {
        ReverseString rs = new ReverseString();
        System.out.println("Before reserve : cool");
        System.out.println("After reverse : " + rs.reverse("cool"));
    }
}