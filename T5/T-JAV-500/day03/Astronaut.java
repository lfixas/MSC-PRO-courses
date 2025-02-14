import chocolate.*;
import planet.*;

public class Astronaut {
    private static int astronautCount = 0;

    private String name;
    private int snacks;
    private String destination;
    private int id;

    public Astronaut(String name) {
        this.name = name;
        this.snacks = 0;
        this.destination = null;
        this.id = astronautCount;
        astronautCount++;
        System.out.println(this.name + " ready for launch!");
    }

    public String getName() {
        return this.name;
    }

    public int getSnacks() {
        return this.snacks;
    }

    public String getDestination() {
        return this.destination;
    }
    
    public int getId() {
        return this.id;
    }

    public void doActions() {
        System.out.println(this.name + ": Nothing to do.");
        if (this.destination == null) {
            System.out.println(this.name + ": I may have done nothing, but I have " + this.snacks + " Mars to eat at least!");
        }
    }

    public void doActions(chocolate.Mars mars) {
        this.snacks++;
        System.out.println(this.name + ": Thanks for this mars number " + mars.getId());
        if (this.destination == null) {
            System.out.println(this.name + ": I may have done nothing, but I have " + this.snacks + " Mars to eat at least!");
        }
    }

    public void doActions(planet.Mars mars) {
        this.destination = mars.getLandingSite();
        System.out.println(this.name + ": Started a mission!");
        if (this.destination == null) {
            System.out.println(this.name + ": I may have done nothing, but I have " + this.snacks + " Mars to eat at least!");
        }
    }

    public void doActions(planet.moon.Phobos phobos) {
        this.destination = phobos.getLandingSite();
        System.out.println(this.name + ": Started a mission!");
        if (this.destination == null) {
            System.out.println(this.name + ": I may have done nothing, but I have " + this.snacks + " Mars to eat at least!");
        }
    }

    public void shareSnacks() {
        this.snacks++;
    }
}