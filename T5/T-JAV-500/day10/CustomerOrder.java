import java.util.ArrayList;
import java.util.List;

public class CustomerOrder {
    private Stock stock;
    private List<Object> order;

    public CustomerOrder(Stock stock) {
        this.stock = stock;
        this.order = new ArrayList<>();
    }

    public boolean addItem(Food food) throws NoSuchFoodException {
        if (stock.remove(food.getClass())) {
            order.add(food);
            return true;
        }
        return false;
    }

    public boolean removeItem(Food food) throws NoSuchFoodException {
        if (order.contains(food)) {
            order.remove(food);
            stock.add(food.getClass());
            return true;
        }
        return false;
    }

    public float getPrice() throws NoSuchFoodException {
        float totalPrice = 0;
        for (Object item : order) {
            if (item instanceof Food) {
                Food food = (Food) item;
                totalPrice += food.getPrice();
            } else if (item instanceof Menu<?, ?>) {
                Menu<?, ?> menu = (Menu<?, ?>) item;
                totalPrice += menu.getPrice();
            }
        }
        return totalPrice;
    }

    public boolean addMenu(Menu<?, ?> menu) throws NoSuchFoodException {
        if (stock.getNumberOf(menu.getDrink().getClass()) > 0 && stock.getNumberOf(menu.getMeal().getClass()) > 0) {
            stock.remove(menu.getDrink().getClass());
            stock.remove(menu.getMeal().getClass());
            order.add(menu);
            return true;
        }
        return false;
    }

    public boolean removeMenu(Menu<?, ?> menu) throws NoSuchFoodException {
        if (order.contains(menu)) {
            order.remove(menu);
            stock.add(menu.getDrink().getClass());
            stock.add(menu.getMeal().getClass());
            return true;
        }
        return false;
    }

    public void printOrder() {
        try {
            System.out.println("Your order is composed of:");
            float total = 0;
            for (int i = order.size() -1; i >=0; i--) {
                Object item = order.get(i);
                if (item instanceof Food) {
                    Food food = (Food) item;
                    System.out.println("- " + food.getClass().getSimpleName() + " (" + food.getPrice() + " euros)");
                    total += food.getPrice();
                } else if (item instanceof Menu<?, ?>) {
                    Menu<?, ?> menu = (Menu<?, ?>) item;
                    System.out.println("- " + menu.getClass().getSimpleName() + " menu (" + menu.getPrice() + " euros)");
                    System.out.println("-> drink: " + menu.getDrink().getClass().getSimpleName());
                    System.out.println("-> meal: " + menu.getMeal().getClass().getSimpleName());
                    total += menu.getPrice();
                }
            }
            System.out.println("For a total of " + total + " euros.");
        } catch(Exception e) {
           System.out.println(e.getMessage());
        }
    }
}