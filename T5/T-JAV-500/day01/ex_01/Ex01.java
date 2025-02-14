class Ex01 {
    public static void main(String[] args) {
        String str1 = args[0];
        String str2 = args[1];
        myConcat(str1, str2);

    }
    public static void myConcat(String str1, String str2) {
        System.out.println(str1 + " " + str2);
    }
}