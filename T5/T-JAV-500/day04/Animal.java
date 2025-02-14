public class Animal {
    private static int numberOfAnimals = 0;
    private static int numberOfMammals = 0;
    private static int numberOfFish = 0;
    private static int numberOfBirds = 0;

    protected enum Type {
        MAMMAL,
        FISH,
        BIRD
    }

    private String name;
    private int legs;
    private Type type;

    protected Animal(String name, int legs, Type type) {
        this.name = name;
        this.legs = legs;
        this.type = type;
        numberOfAnimals++;
        updateTypeCount(type);
        System.out.println("My name is " + name + " and I am a " + getType() + "!");
    }

    public String getName() {
        return name;
    }

    public int getLegs() {
        return legs;
    }

    public String getType() {
        switch (type) {
            case MAMMAL:
                return "mammal";
            case FISH:
                return "fish";
            case BIRD:
                return "bird";
            default:
                return "unknown";
        }
    }

    public static int getNumberOfAnimals() {
        if (numberOfAnimals == 1) {
            System.out.println("There is currently " + numberOfAnimals + " animal in our world.");
        } else {
            System.out.println("There are currently " + numberOfAnimals + " animals in our world.");
        }
        return numberOfAnimals;
    }

    private void updateTypeCount(Type type) {
        switch (type) {
            case MAMMAL:
                numberOfMammals++;
                break;
            case FISH:
                numberOfFish++;
                break;
            case BIRD:
                numberOfBirds++;
                break;
            default:
                break;
        }
    }

    public static int getNumberOfMammals() {
        if (numberOfMammals == 1) {
            System.out.println("There is currently " + numberOfMammals + " mammal in our world.");
        } else {
            System.out.println("There are currently " + numberOfMammals + " mammals in our world.");
        }
        return numberOfMammals;
    }

    public static int getNumberOfFish() {
        if (numberOfFish == 1) {
            System.out.println("There is currently " + numberOfFish + " fish in our world.");
        } else {
            System.out.println("There are currently " + numberOfFish + " fish in our world.");
        }
        return numberOfFish;
    }

    public static int getNumberOfBirds() {
        if (numberOfBirds == 1) {
            System.out.println("There is currently " + numberOfBirds + " bird in our world.");
        } else {
            System.out.println("There are currently " + numberOfBirds + " birds in our world.");
        }
        return numberOfBirds;
    }
}