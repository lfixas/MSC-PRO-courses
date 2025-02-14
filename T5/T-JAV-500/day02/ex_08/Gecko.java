public class Gecko {
    private String name;
    private int age;
    private int energy;

    public Gecko() {
        this.name = "Unknown";
        this.energy = 100;
        System.out.println("Hello!");
    }

    public Gecko(String name) {
        this.name = name;
        this.age = 0;
        this.energy = 100;
        System.out.println("Hello " + this.name + "!");
    }

    public Gecko(String name, int age) {
        this.name = name;
        this.age = age;
        this.energy = 100;
        System.out.println("Hello " + this.name + "!");
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void status() {
        switch (this.age) {
            case 0:
                System.out.println("Unborn Gecko");
                break;
            case 1:
            case 2:
                System.out.println("Baby Gecko");
                break;
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
                System.out.println("Adult Gecko");
                break;
            case 11:
            case 12:
            case 13:
                System.out.println("Old Gecko");
                break;
            default:
                System.out.println("Impossible Gecko");
        }
    }

    public void hello(String message) {
        System.out.println("Hello " + message + ", I'm " + this.name + "!");
    }

    public void hello(int times) {
        for (int i = 0; i < times; i++) {
            System.out.println("Hello, I'm " + this.name + "!");
        }
    }

    public void eat(String food) {
        food = food.toLowerCase();
        switch (food) {
            case "meat":
                System.out.println("Yummy!");
                this.energy += 10;
                break;
            case "vegetable":
                System.out.println("Erk!");
                this.energy -= 10;
                break;
            default:
                System.out.println("I can't eat this!");
        }
        checkEnergy();
    }

    public int getEnergy() {
        return this.energy;
    }

    public void setEnergy(int energy) {
        this.energy = energy;
        checkEnergy();
    }

    public void checkEnergy() {
        if (this.energy < 0) {
            this.energy = 0;
        } else if (this.energy > 100) {
            this.energy = 100;
        }
    }

    public void work() {
        if (this.energy >= 25) {
            this.energy -= 9;
            System.out.println("I'm working T.T");
        } else {
            setEnergy(50);
            System.out.println("Heyyy I'm too sleepy, better take a nap!");
        }
    }

    public void fraternize(Object friend) {
        if (friend instanceof Gecko) {
            Gecko geckoFriend = (Gecko) friend;

            if (this.energy >= 30 && geckoFriend.energy >= 30) {
                this.energy -= 30;
                geckoFriend.energy -= 30;
                System.out.println("I'm going to drink with " + geckoFriend.name + "!");
                System.out.println("I'm going to drink with " + this.name + "!");
            } else if (this.energy < 30 && geckoFriend.energy >= 30) {
                System.out.println("Sorry " + geckoFriend.name + ", I'm too tired to go out tonight.");
                System.out.println("Oh! That's too bad, another time then!");
            } else if (this.energy >= 30 && geckoFriend.energy < 30) {
                System.out.println("Sorry " + this.name + ", I'm too tired to go out tonight.");
                System.out.println("Oh! That's too bad, another time then!");
            } else {
                System.out.println("Not today!");
                System.out.println("Not today!");
            }
        } else if (friend instanceof Snake) {
            if (this.energy >= 10) {
                this.energy = 0;
                System.out.println("LET'S RUN AWAY!!!");
            } else {
                System.out.println("...");
            }
        }
    }
}
