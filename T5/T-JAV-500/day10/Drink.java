public abstract class Drink implements Food {
    private float price;
    private int calories;
    protected boolean aCan;

    public Drink(float price, int calories) {
        this.price = price;
        this.calories = calories;
        this.aCan = false;
    }

    public float getPrice() {
        return price;
    }

    public int getCalories() {
        return calories;
    }

    public boolean isACan() {
        return aCan;
    }
}
