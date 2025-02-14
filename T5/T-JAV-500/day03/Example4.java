import chocolate.*;
import planet.*;

public class Example4 {
    public static void main(String[] args) {
        Astronaut mutta = new Astronaut("Mutta");

        chocolate.Mars snack = new chocolate.Mars();
        chocolate.Mars sandwich = new chocolate.Mars();

        planet.Mars rock = new planet.Mars("Viking 1");

        mutta.doActions();
        mutta.doActions(snack);
        mutta.doActions(sandwich);
        System.out.println("Destination : " + mutta.getDestination());
        mutta.doActions();
        mutta.doActions(rock);
        System.out.println("Destination : " + mutta.getDestination());
        mutta.doActions();
    }
}
