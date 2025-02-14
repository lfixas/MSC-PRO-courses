import java.util.List;
import java.util.ArrayList;

public abstract class Sandwich implements Food {
    private float price;
    private int calories;
    protected boolean vegetarian;
    protected List<String> ingredients;

    public Sandwich(float price, int calories) {
        this.price = price;
        this.calories = calories;
        this.vegetarian = false;
        this.ingredients = new ArrayList<String>();
    }

    public float getPrice() {
        return price;
    }

    public int getCalories() {
        return calories;
    }

    public boolean isVegetarian() {
        return vegetarian;
    }

    public List<String> getIngredients() {
        return ingredients;
    }
}
