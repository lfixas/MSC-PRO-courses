public class RadScorpion extends Monster {
    private static int id = 1;

    public RadScorpion() {
        super("RadScorpion #" + id, 80, 50);
        damage = 25;
        apcost = 8;
        id++;
        System.out.println(name + ": Crrr!");
    }

    public boolean attack(Fighter target) {
        if (hp <= 0) {
            return false;
        }

        if (target instanceof SpaceMarine && !(target instanceof AssaultTerminator)) {
            ap -= apcost;
            target.receiveDamage(damage * 2);
        } else {
            ap -= apcost;
            target.receiveDamage(damage);
        }

        return true;
    }
   
}
