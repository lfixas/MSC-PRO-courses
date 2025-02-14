public abstract class Bread implements Food {
    private float price;
    private int calories;
    protected int bakingTime;

    public Bread(float price, int calories) {
        this.price = price;
        this.calories = calories;
        this.bakingTime = 0;
    }

    public float getPrice() {
        return price;
    }

    public int getCalories() {
        return calories;
    }

    public int getBakingTime() {
        return bakingTime;
    }
}
