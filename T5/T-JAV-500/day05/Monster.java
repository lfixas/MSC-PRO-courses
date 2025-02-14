public abstract class Monster extends Unit {
    protected int damage;
    protected int apcost;

    public int getDamage() {
        return damage;
    }

    public int getApcost() {
        return apcost;
    }

    public Monster(String name, int hp, int ap) {
        super(name, hp, ap);
        damage = 0;
        apcost = 0;
    }

    public boolean equip(Weapon weapon) {
        if (hp <= 0) {
            return false;
        }
        System.out.println("Monsters are proud and fight with their own bodies.");
        return false;
    }

    public boolean attack(Fighter target) {
        if (hp <= 0) {
            return false;
        }
        
        if (!moveCloseTo(target)) {
            System.out.println(name + ": I'm too far away from " + target.getName());
            return false;
        }

        if (ap >= apcost) {
            System.out.println(name + " attacks " + target.getName());
            ap -= apcost;
            target.receiveDamage(damage);
            return true;
        } else {
            System.out.println(name + ": Not enough AP to attack.");
            return false;
        }
    }
}
