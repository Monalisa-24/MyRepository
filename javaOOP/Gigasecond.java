import java.time.LocalDate;
import java.time.LocalDateTime;

public class Gigasecond {

    private LocalDateTime dateTime;

    public Gigasecond(LocalDate moment) {
        this.dateTime = moment.atTime(0, 0);
    }

    public Gigasecond(LocalDateTime moment) {
        this.dateTime = moment;
    }

    public LocalDateTime getDateTime() {
        return this.dateTime.plusSeconds(1000000000);
    }

    public static void main(String[] args) {
        Gigasecond gs = new Gigasecond(LocalDate.of(2001, 03, 24));
        System.out.println("DateTime : " + gs.getDateTime());
    }
}