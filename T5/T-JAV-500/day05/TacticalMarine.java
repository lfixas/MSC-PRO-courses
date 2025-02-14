public class TacticalMarine extends SpaceMarine {

    public TacticalMarine(String name) {
        super(name, 100, 20);
        equip(new PlasmaRifle());
        System.out.println(name + " on duty.");
    }

    public void recoverAP() {
        ap += 12;
        if (ap > 50) {
            ap = 50;
        }
    }
}
