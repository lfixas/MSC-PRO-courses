public abstract class Character implements Movable, Comparable<Character> {
    protected String name;
    protected final String RPGClass;
    protected int life;
    protected int agility;
    protected int strength;
    protected int wit;
    protected int capacity;

    public String getName() {
        return name;
    }

    public String getRPGClass() {
        return RPGClass;
    }

    public int getLife() {
        return life;
    }

    public int getAgility() {
        return agility;
    }

    public int getStrength() {
        return strength;
    }

    public int getWit() {
        return wit;
    }

    public int getCapacity() {
        return capacity;
    }

    public Character(String name, String RPGClass, int capacity) {
        this.name = name;
        this.RPGClass = RPGClass;
        this.life = 50;
        this.agility = 2;
        this.strength = 2;
        this.wit = 2;
        this.capacity = capacity;
    }

    public Character(String name, String RPGClass) {
        this.name = name;
        this.RPGClass = RPGClass;
        this.life = 50;
        this.agility = 2;
        this.strength = 2;
        this.wit = 2;
        this.capacity = 0;
    }

    public void attack(String weapon) {
        System.out.println(name + ": Rrrrrrrrr....");
    }

    public void moveRight() {
        System.out.println(name + ": moves right");
    }

    public void moveLeft() {
        System.out.println(name + ": moves left");
    }

    public void moveForward() {
        System.out.println(name + ": moves forward");
    }

    public void moveBack() {
        System.out.println(name + ": moves back");
    }

    public final void unsheathe() {
        System.out.println(name + ": unsheathes his weapon.");
    }

    @Override
    public int compareTo(Character compare) {
        if (this.getClass() == compare.getClass()) { // if characters are both of the same type, compare the capacities 
            return Integer.compare(this.capacity, compare.capacity);

        } else if (this instanceof Warrior && compare instanceof Mage) {
            if (this.capacity % compare.capacity == 0) {
                return 1;
            }
            return -1;

        } else if (this instanceof Mage && compare instanceof Warrior) {
            if (compare.capacity % this.capacity == 0) {
                return -1;
            }
            return 1;
        }
        
        return 0;
    }
}
