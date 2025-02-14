package Factory;

public abstract class Toy {
    protected String title;

    public String getTitle() {
        return this.title;
    }

    public Toy(String title) {
        this.title = title;
    }
}
