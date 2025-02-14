package Factory;

public class NoSuchToyException extends Exception {

    private static final long serialVersionUID = 1L;

    public NoSuchToyException(String message) {
        super(message);
    }
}
