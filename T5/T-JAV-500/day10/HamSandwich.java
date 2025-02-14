import java.util.Arrays;

public class HamSandwich extends Sandwich {
    public HamSandwich() {
        super(4.00f, 230);
        vegetarian = false;
        ingredients = Arrays.asList("tomato", "salad", "cheese", "ham", "butter");
    }
}
