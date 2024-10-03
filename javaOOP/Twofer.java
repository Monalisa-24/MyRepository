/*public class Twofer {
    String name;

    public String twofer(String name) {
        return "One for " + name + ", one for me.\n";
    }

    public String twofer() {
        return "One for you, one for me.\n";
    }

    public static void main(String[] args) {
        Twofer tf = new Twofer();
        System.out.printf("with name : " + tf.twofer("Neha"));
        System.out.println("Without name : " + tf.twofer());
    }
}*/

public class Twofer {
    String twofer(String name) {
        if (name == null) {
            return "One for you, one for me.";
        } else {
            return "One for " + name + ", one for me.";
        }
    }

    // public String twofer() {}

    public static void main(String[] args) {
        Twofer tf = new Twofer();
        System.out.printf(tf.twofer("Nandini"));
        System.out.println(tf.twofer(null));
    }
}

/*
 * public class Twofer {
 * String name;
 * 
 * public String twofer(String name) {
 * if (name != null) {
 * return "One for " + name + ", one for me.\n";
 * } else {
 * return "One for you, one for me.\n";
 * }
 * 
 * }
 * class Twofer {
 * String twofer(String name) {
 * if (name == null) {
 * return "One for you, one for me.";
 * } else {
 * return "One for " + name + ", one for me.";
 * }
 * }
 * }
 * 
 * // public String twofer() {}
 * 
 * public static void main(String[] args) {
 * Twofer tf = new Twofer();
 * System.out.printf(tf.twofer("Nandini"));
 * System.out.println(tf.twofer(null));
 * }
 * }
 */
/*
 * public class Twofer {
 * public static void main(String[] args) {
 * //Twofer tf[] = new Twofer[];
 * 
 * String name;
 * String n[];
 * 
 * public String twofer(String name) {
 * if (name != null) {
 * n[3] = name;
 * return "One for " + n[3] + ", one for me.\n";
 * } else {
 * n[3] = "you";
 * return "One for " + n[3] + ", one for me.\n";
 * }
 * }
 * System.out.println(twofer("bob"));
 * System.out.println(twofer(null));
 * }
 * // public String twofer() {}
 * 
 * }
 */
/*
 * public class Twofer {
 * String name;
 * String n[];
 * 
 * public String twofer(String name) {
 * if (name != null) {
 * n[3] = name;
 * return "One for " + n[3] + ", one for me.\n";
 * } else {
 * n[3] = "you";
 * return "One for " + n[3] + ", one for me.\n";
 * }
 * 
 * }
 * 
 * // public String twofer() {}
 * 
 * public static void main(String[] args) {
 * Twofer tf[] = new Twofer();
 * System.out.printf(tf[3].twofer("Neha"));
 * System.out.println(tf[3].twofer(null));
 * }
 * }
 */

/*
 * public class Twofer {
 * String name;
 * 
 * public String twofer(String name) {
 * String nameToReturn = name == null ? "you" : name;
 * return "One for " + nameToReturn + ", one for me.";
 * }
 * 
 * // public String twofer() {}
 * 
 * public static void main(String[] args) {
 * Twofer tf = new Twofer();
 * System.out.printf(tf.twofer("Alice"));
 * System.out.println(tf.twofer(null));
 * }
 * }
 */