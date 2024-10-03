public class cv_shortlisting {

    public cv_shortlisting(int a, String fn, String ln) {
        if (a < 20 || a > 30) {
            System.out.println("\nAGE MUST BE WITHIN 20 - 30");
        } else {
            System.out.println("\nWELCOME!");
        }
        System.out.println("\n\nYour age is " + a);
        System.out.println("Your first-name is " + fn);
        System.out.println("Your last-name is " + ln);
    }

    public void CVStyle(String type, int e) {
        System.out.println("your cv type is " + type);
        if (type == "professional" && e >= 3) {
            System.out.println("\nCONGRATULATIONS.\nYOU'RE HIRED.");
        } else {
            System.out.println("\nOoho ! Sorry !\nYOUR DETAILS CAN NOT FULFILL OUR REQUIREMENTS.");
        }
    }

    public int Experience(int e) {
        System.out.println("You have the experience of " + e + " yrs");
        return e;
    }

    public void ageCheck(int yourage) {
        if (yourage < 20) {
            System.out.println("You can't sit for campussing xm....age must be within 21 - 30 !");
        } else {
            System.out.println("Welcome ! You can fill up the form.");
        }
    }

    public int getAge(int a) {
        System.out.println("your age is " + a);
        return a;
    }

    public static void main(String[] args) {
        cv_shortlisting cv = new cv_shortlisting(38, "Monalisa", "Saha");
        cv.CVStyle("professional", cv.Experience(5));
       

    }}

    

    

    
