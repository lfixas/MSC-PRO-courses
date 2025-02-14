class Ex02 {
    public static void main(String[] args) {
        int nbr = Integer.parseInt(args[0]);
        getAngryDog(nbr);
    }
    public static String getAngryDog(int nbr) {
        for (int loop = 0; loop < nbr; loop++ ) {
            System.out.print("woof");
        }
        System.out.println("");
        return "";
    }
}