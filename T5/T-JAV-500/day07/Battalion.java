import java.util.ArrayList;
import java.util.List;

public class Battalion {
    private List<Character> characters;

    public Battalion() {
        this.characters = new ArrayList<>();
    }

    public void add(List<? extends Character> characterList) {
        characters.addAll(characterList);
    }

    public void display() {
        for (Character character : characters) {
            System.out.println(character.getName());
        }
    }

    public boolean fight() {
        if (characters.size() >= 2) {
            Character character1 = characters.get(0);
            Character character2 = characters.get(1);

            int result = character1.compareTo(character2);

            if (result > 0) {
                // System.out.println("He is not worthy enough to stay... if he's still alive!");
                characters.remove(character2);
            } else if (result < 0) {
                // System.out.println("He is not worthy enough to stay... if he's still alive!");
                characters.remove(character1);
            } else {
                // System.out.println("They're not worthy if they can't defeat their opponents.");
                characters.remove(character1);
                characters.remove(character2);
            }

            return true;
        } else {
            return false;
        }
    }
}
