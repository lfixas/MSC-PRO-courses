class Ex06 {
    public static void main(String[] args) {
        int nbr = Integer.parseInt(args[0]);
        sequence(nbr);
    }

    public static void sequence(int nbr) {
        String current = "1";
        System.out.println(current);
        for (int i = 0; i < nbr; i++) {
            current = generateNext(current);
            System.out.println(current);
        }
    }

    public static String generateNext(String current) {
        StringBuilder result = new StringBuilder();
        char currentChar = current.charAt(0);
        int count = 1;

        for (int i = 1; i < current.length(); i++) {
            if (current.charAt(i) == currentChar) {
                count++;
            } else {
                result.append(count);
                result.append(currentChar);
                currentChar = current.charAt(i);
                count = 1;
            }
        }

        result.append(count);
        result.append(currentChar);
        return result.toString();
    }
}
