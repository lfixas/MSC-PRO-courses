package Decorator;

public class StuffDecorator extends Warrior {
    protected Warrior holder;

    public StuffDecorator(Warrior holder) {
        super(holder.getHp(), holder.getDmg());
        this.holder = holder;
    }

    @Override
    public int getHp() {
        return holder.getHp();
    }

    @Override
    public int getDmg() {
        return holder.getDmg();
    }
}
