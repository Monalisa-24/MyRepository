public class LogLevels {

    public static String message(String logLine) {
        return logLine.split("]: ")[1].trim();
    }

    public static String logLevel(String logLine) {
        // System.out.println(message(logLine));
        logLine = logLine.toUpperCase();
        if (logLine.contains("INFO")) {
            return "info";
        } else if (logLine.contains("WARNING")) {
            return "warning";
        } else if (logLine.contains("ERROR")) {
            return "error";
        } else {
            return " ";
        }
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }

    public static void main(String[] args) {
        // LogLevels ll = new LogLevels();
        // System.out.println(message("Info"));
        // System.out.println(logLevel("Warning"));
        System.out.println(reformat("[info]: Operation completed"));
    }
}

// public class LogLevels {

// public static String message(String logLine) {
// return String.format("[" + logLine + "]") + ": Disk almost full\r\n";
// }

// public static String logLevel(String logLine) {
// return String.format("[" + logLine + "]") + ": Invalid operation";
// }

// public static String reformat(String logLine) {
// return String.format("[" + logLine + "]") + ": Operation completed";
// }

// public static void main(String[] args) {
// // LogLevels ll = new LogLevels();
// System.out.println(message("Info"));
// System.out.println(logLevel("Warning"));
// System.out.println(reformat("Error"));
// }
// }