public class Example {
    public static void main(String[] args) {
        Gecko arthur = new Gecko("Arthur", 1);
        Gecko benjy = new Gecko();
        
        System.out.println(arthur.getName());
        System.out.println(benjy.getName());

        System.out.println("-----");

        arthur.status();
        System.out.println(arthur.getAge());

        benjy.status();
        System.out.println(benjy.getAge());

        System.out.println("-----");

        arthur.setAge(8);
        arthur.status();
        System.out.println(arthur.getAge());
    }
}
