import chocolate.*;
import planet.*;

public class Example3 {
    public static void main(String[] args) {
        chocolate.Mars snack = new chocolate.Mars();
        planet.Mars rock = new planet.Mars("Viking 1");

        System.out.println(snack.getId());
        System.out.println(rock.getLandingSite());
    }
}
