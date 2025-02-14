package planet;

public class Mars {
    private static int instanceId = 0;
    private int id;
    private String landingSite;

    public Mars(String landingSite) {
        this.id = instanceId;
        instanceId++;
        this.landingSite = landingSite;
    }

    public int getId() {
        return this.id;
    }

    public String getLandingSite() {
        return this.landingSite;
    }
}
