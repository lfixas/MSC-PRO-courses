package Decorator;

public abstract class Warrior {
    private int hp;
    private int dmg;

    public Warrior(int hp, int dmg) {
        this.hp = hp;
        this.dmg = dmg;
    }

    public int getHp() {
        return hp;
    }

    public int getDmg() {
        return dmg;
    }
}
