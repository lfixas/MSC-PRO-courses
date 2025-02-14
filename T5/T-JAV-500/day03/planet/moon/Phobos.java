package planet.moon;

import planet.Mars;

public class Phobos {
    private Mars mars;
    private String landingSite;

    public Mars getMars() {
        return this.mars;
    }

    public String getLandingSite() {
        return this.landingSite;
    }

    public Phobos(Mars mars, String landingSite) {
        this.mars = mars;
        this.landingSite = landingSite;
        System.out.println("Phobos placed in orbit.");
    }
    
}
