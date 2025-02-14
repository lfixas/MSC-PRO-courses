public abstract class Unit implements Fighter {
    protected String name;
    protected int hp;
    protected int ap;
    protected Fighter enemy;

    protected Unit(String name, int hp, int ap) {
        this.name = name;
        this.hp = hp;
        this.ap = ap;
    }

    public String getName() {
        return name;
    }

    public int getHp() {
        return hp;
    }

    public int getAp() {
        return ap;
    }

    public void receiveDamage(int damage) {
        if (hp <= 0) {
            return;
        }

        hp -= damage;

        if (hp <= 0) {
            hp = 0;
        }
    }

    public boolean moveCloseTo(Fighter target) {
        if (this == target || enemy == target || hp <= 0) {
            return false;
        }

        System.out.println(name + " is moving closer to " + target.getName() + ".");
        enemy = target;
        return true;
    }

    public void recoverAP() {
        if (hp <= 0) {
            return;
        }

        ap += 7;
        if (ap > 50) {
            ap = 50;
        }
    }
}
