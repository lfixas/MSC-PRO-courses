import java.util.Map;
import java.util.HashMap;

public class Stock {
    private Map<Class<? extends Food>, Integer> stock;

    public Stock() {
        stock = new HashMap<>();

        stock.put(FrenchBaguette.class, 100);
        stock.put(SoftBread.class, 100);
        stock.put(AppleSmoothie.class, 100);
        stock.put(Coke.class, 100);
        stock.put(HamSandwich.class, 100);
        stock.put(Panini.class, 100);
        stock.put(Cookie.class, 100);
        stock.put(CheeseCake.class, 100);
    }

    public int getNumberOf(Class<? extends Food> foodType) throws NoSuchFoodException {
        if (stock.containsKey(foodType)) {
            return stock.get(foodType);
        } else {
            throw new NoSuchFoodException("No such food type: " + foodType.getSimpleName() + ".");
        }
    }

    public boolean add(Class<? extends Food> foodType) throws NoSuchFoodException {
        if (stock.containsKey(foodType)) {
            stock.put(foodType, stock.get(foodType) + 1);
            return true;
        } else {
            throw new NoSuchFoodException("No such food type: " + foodType.getSimpleName() + ".");
        }
    }

    public boolean remove(Class<? extends Food> foodType) throws NoSuchFoodException {
        if (stock.containsKey(foodType)) {
            int currentCount = stock.get(foodType);
            if (currentCount > 0) {
                stock.put(foodType, currentCount - 1);
                return true;
            }
        } else {
            throw new NoSuchFoodException("No such food type: " + foodType.getSimpleName() + ".");
        } 
        return false;
    } 
}
