import java.util.ArrayList;

public class Team {
    private String name;
    private ArrayList<Astronaut> members;

    public Team(String name) {
        this.name = name;
        this.members = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void add(Astronaut astronaut) {
        members.add(astronaut);
    }

    public void remove(Astronaut astronaut) {
        members.remove(astronaut);
    }

    public int countMembers() {
        return members.size();
    }

    public void showMembers() {
        if (!members.isEmpty()) {
            StringBuilder memberInfo = new StringBuilder();
            memberInfo.append(name).append(": ");
            for (Astronaut astronaut : members) {
                String status = astronaut.getDestination() != null ? "on mission" : "on standby";
                memberInfo.append(astronaut.getName()).append(" ").append(status).append(", ");
            }
            
            memberInfo.setLength(memberInfo.length() - 2);
            memberInfo.append(".");
            System.out.println(memberInfo.toString());
        }
    }

    public void doActions() {
        System.out.println(name + ": Nothing to do.");
    }

    // public void doActions(chocolate.Mars mars) {
    //     for (Astronaut astronaut : members) {
    //         astronaut.doActions(mars);
    //     }
    // }

    // public void doActions(planet.Mars mars) {
    //     for (Astronaut astronaut : members) {
    //         astronaut.doActions(mars);
    //     }
    // }

    public void doActions(chocolate.Mars mars) {
        for (Astronaut astronaut : members) {
            astronaut.shareSnacks();
            // System.out.println(astronaut.getSnacks());
        }
    }

    public void doActions(planet.Mars mars) {
        for (Astronaut astronaut : members) {
            astronaut.doActions(mars);
        }
    }

    public void doActions(planet.moon.Phobos phobos) {
        for (Astronaut astronaut : members) {
            astronaut.doActions(phobos);
        }
    }
}
