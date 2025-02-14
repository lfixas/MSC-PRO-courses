import java.util.ArrayList;
import java.util.Arrays;

class Ex03 {
    public static void main(String[] args) {
        ArrayList<String> myArray = new ArrayList<>(Arrays.asList(args));
        printArray(myArray);
    }

    public static void printArray(ArrayList<String> myArray) {
        for (String arg : myArray) {
            System.out.println(arg);
        }
    }
}
