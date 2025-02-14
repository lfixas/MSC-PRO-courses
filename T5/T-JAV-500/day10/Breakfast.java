public class Breakfast<T extends Drink, U extends Bread> extends Menu<T, U> {
    public Breakfast(T drink, U meal) {
        super(drink, meal);
    }
}
