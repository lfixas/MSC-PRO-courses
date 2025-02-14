public class Gecko {
    private String name;

    public Gecko() {
        this.name = "Unknown";
        System.out.println("Hello!");
    }

    public Gecko(String name) {
        this.name = name;
        System.out.println("Hello " + this.name + "!");
    }

    public String getName() {
        return this.name;
    }
}
