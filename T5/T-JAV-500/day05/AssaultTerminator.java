public class AssaultTerminator extends SpaceMarine {

    public AssaultTerminator(String name) {
        super(name, 150, 30);
        equip(new PowerFist());
        System.out.println(name + " has teleported from space.");
    }

    public void receiveDamage(int damage) {
        int reducedDamage = damage - 3;
        if (reducedDamage < 1) {
            reducedDamage = 1;
        }
        super.receiveDamage(reducedDamage);
    }
}
