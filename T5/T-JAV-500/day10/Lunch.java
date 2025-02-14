public class Lunch<T extends Drink, U extends Sandwich> extends Menu<T, U> {
    public Lunch(T drink, U meal) {
        super(drink, meal);
    }
}
