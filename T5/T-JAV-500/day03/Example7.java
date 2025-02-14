import planet.*;

public class Example7 {
    public static void main (String[] args) {
        Astronaut mutta = new Astronaut("Mutta");
        Astronaut hibito = new Astronaut("Hibito");
        Astronaut serika = new Astronaut("Serika");

        chocolate.Mars snack = new chocolate.Mars();
        chocolate.Mars sandwich = new chocolate.Mars();

        planet.Mars rock = new planet.Mars("Viking 1");

        Team spaceBro = new Team("SpaceBrothers");

        spaceBro.add(mutta);
        spaceBro.add(hibito);
        spaceBro.add(serika);

        System.out.println(spaceBro.countMembers());

        planet.Mars titi = new planet.Mars("Hill");

        planet.moon.Phobos scrap = new planet.moon.Phobos(titi, "Antique IV");

        mutta.doActions(titi);


        spaceBro.showMembers();
        spaceBro.remove(hibito);
        System.out.println(spaceBro.countMembers());

        System.out.println("--------------");

        spaceBro.doActions();
        spaceBro.doActions(snack);
        spaceBro.doActions(sandwich);
        spaceBro.doActions(rock);
        spaceBro.doActions(scrap);

        mutta.doActions(scrap);
    }
}