public class Example {
    public static void main(String[] args) {
        Gecko gecko = new Gecko("George", 3);

        // Display initial energy level
        System.out.println("Initial energy: " + gecko.getEnergy());

        // Test eating Vegetable (should lose 10 energy)
        gecko.eat("Vegetable");
        System.out.println("Energy after eating Vegetable: " + gecko.getEnergy());

        for (int i = 0; i < 10; i++) {
            // Test work (should lose 9 energy)
            gecko.work();
            System.out.println("Energy after work : " + gecko.getEnergy());
        }
    }
}
