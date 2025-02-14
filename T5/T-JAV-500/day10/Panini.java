import java.util.Arrays;

public class Panini extends Sandwich {
    public Panini() {
        super(3.50f, 120);
        vegetarian = true;
        ingredients = Arrays.asList("tomato", "salad", "cucumber", "avocado", "cheese");
    }
}
