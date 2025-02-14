public class Example {
    public static void main(String[] args) {
        Gecko gecko = new Gecko("George", 3);

        // Display initial energy level
        System.out.println("Initial energy: " + gecko.getEnergy());

        // Test eating Vegetable (should lose 10 energy)
        gecko.eat("Vegetable");
        System.out.println("Energy after eating Vegetable: " + gecko.getEnergy());

        // Test eating Meat (should gain 10 energy)
        gecko.eat("Meat");
        System.out.println("Energy after eating Meat: " + gecko.getEnergy());

        // Test eating something else (energy remains the same)
        gecko.eat("Pizza");
        System.out.println("Energy after eating Pizza: " + gecko.getEnergy());

        // Set energy to the minimum (0)
        gecko.setEnergy(0);
        System.out.println("Energy set to 0: " + gecko.getEnergy());

        // Set energy to the maximum (100)
        gecko.setEnergy(100);
        System.out.println("Energy set to 100: " + gecko.getEnergy());

        // Set energy to an out-of-range value (should be clamped)
        gecko.setEnergy(120);
        System.out.println("Energy set to 120 (clamped to 100): " + gecko.getEnergy());

        // Set energy to a negative value (should be clamped)
        gecko.setEnergy(-10);
        System.out.println("Energy set to -10 (clamped to 0): " + gecko.getEnergy());
    }
}
