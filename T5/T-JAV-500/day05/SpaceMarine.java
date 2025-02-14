public abstract class SpaceMarine extends Unit {
    private Weapon weapon;

    public SpaceMarine(String name, int hp, int ap) {
        super(name, hp, ap);
        weapon = null;
    }
    
    public Weapon getWeapon() {
        return weapon;
    }

    public boolean equip(Weapon weapon) {
        if (this.weapon == null) {
            this.weapon = weapon;
            System.out.println(name + " has been equipped with a " + weapon.getName() + ".");
            return true;
        }
        return false;
    }

    public boolean attack(Fighter target) {
        if (weapon == null) {
            System.out.println(name + ": Hey, this is crazy. I'm not going to fight this empty-handed.");
            return false;
        }

        if (weapon.isMelee() && !moveCloseTo(target)) {
            System.out.println(name + ": I'm too far away from " + target.getName() + ".");
            return false;
        }

        if (ap < weapon.getApcost()) {
            return false;
        }

        System.out.println(name + " attacks " + target.getName() + " with a " + weapon.getName() + ".");
        ap -= weapon.getApcost();
        weapon.attack();
        target.receiveDamage(weapon.getDamage());
        return true;
    }

    public boolean moveCloseTo(Fighter target) {
        if (weapon != null && !weapon.isMelee()) {
            return false;
        }

        return super.moveCloseTo(target);
    }

    public void recoverAP() {
        ap += 9;
        if (ap > 50) {
            ap = 50;
        }
    }
}
