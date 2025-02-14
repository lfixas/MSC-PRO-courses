public class Mars {
    private static int InstanceId = 0;
    private int id;

    public Mars() {
        this.id = InstanceId;
        InstanceId ++;

    }

    public int getId() {
        return this.id;
    }
}