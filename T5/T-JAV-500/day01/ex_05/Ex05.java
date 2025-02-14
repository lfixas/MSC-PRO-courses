import java.util.ArrayList;

public class Ex05 {
    public static void main(String[] args) {
        ArrayList<String> result = myGetArgs(args);
        for (String arg : result) {
            System.out.println(arg);
        }
    }

    public static ArrayList<String> myGetArgs(String... var) {
        ArrayList<String> result = new ArrayList<>();
        for (String argument : var) {
            result.add(argument);
        }
        return result;
    }
}
