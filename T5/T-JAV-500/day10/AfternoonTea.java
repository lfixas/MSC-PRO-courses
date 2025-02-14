public class AfternoonTea<T extends Drink, U extends Dessert> extends Menu<T, U> {
    public AfternoonTea(T drink, U meal) {
        super(drink, meal);
    }
}
