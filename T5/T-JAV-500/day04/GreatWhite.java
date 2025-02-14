public class GreatWhite extends Shark {

    public GreatWhite(String name) {
        super(name);
    }

    public boolean canEat(Animal animal) {
        return super.canEat(animal) && !(animal instanceof Canary);
    }

    @Override
    public void eat(Animal animal) {
        if (animal instanceof Canary) {
            System.out.println(getName() + ": Next time you try to give me that to eat, I'll eat you instead.");
        } else if (animal.getClass() == Shark.class) {
            super.eat(animal);
            System.out.println(getName() + ": The best meal one could wish for.");
        } else {
            super.eat(animal);
        }
    }
}
