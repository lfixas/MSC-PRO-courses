// public class Duet<T extends Comparable<T>, U extends Comparable<U>> {
//     private T first;
//     private U second;

//     public Duet(T first, U second) {
//         this.first = first;
//         this.second = second;
//     }

//     public T getFirst() {
//         return first;
//     }

//     public U getSecond() {
//         return second;
//     }

//     public static <T extends Comparable<T>> T min(T first, T second) {
//         return first.compareTo(second) <= 0 ? first : second;
//     }

//     public static <T extends Comparable<T>> T max(T first, T second) {
//         return first.compareTo(second) >= 0 ? first : second;
//     }
// }

public class Duet {
    public static <T extends Comparable<T>> T min(T first, T second) {
        return first.compareTo(second) <= 0 ? first : second;
    }

    public static <T extends Comparable<T>> T max(T first, T second) {
        return first.compareTo(second) >= 0 ? first : second;
    }
}
