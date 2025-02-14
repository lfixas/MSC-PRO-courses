public class Cat extends Animal {
    private String color;

    public String getColor() {
        return color;
    }
    
    public Cat(String name, String color) {
        super(name, 4, Type.MAMMAL);
        this.color = color;
        System.out.println(name + ": MEEEOOWWWW");
    }

    public Cat(String name) {
        this(name, "grey");
    }

    public void meow() {
        System.out.println(getName() + " the " + getColor() + " kitty is meowing.");
    }
}
