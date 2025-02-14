public class SuperMutant extends Monster {
    private static int id = 1;

    public SuperMutant() {
        super("SuperMutant #" + id, 170, 20);
        damage = 60;
        apcost = 20;
        id++;
        System.out.println(name + ": Roaarrr!");
    }

    public void recoverAP() {
        if (hp <= 0) {
            return;
        }
        
        super.recoverAP();
        hp += 10;
    }
}
