public class Example {
    public static void main(String[] args) {
        Gecko gecko1 = new Gecko("George", 3);
        Gecko gecko2 = new Gecko("Grace", 4);
        Snake snake = new Snake();

        // Gecko and Gecko interaction
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko1.fraternize(gecko2); 
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko2.fraternize(gecko1); 
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko1.setEnergy(5);
        gecko2.setEnergy(5);
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko1.fraternize(gecko2); 
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko1.setEnergy(50);
        gecko1.fraternize(gecko2); 
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());

        System.out.println("-----");

        // Gecko and Snake interaction
        System.out.println("Energy of gecko n°1: " + gecko1.getEnergy());
        gecko1.fraternize(snake);
        System.out.println("Energy of gecko n°2: " + gecko2.getEnergy());
        gecko2.fraternize(snake);
    }
}
