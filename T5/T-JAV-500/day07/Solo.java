public class Solo<T> {
    private T value;

    public Solo(T value) {
        this.value = value;
    }

	public T getValue() {
		return this.value;
	}

	public void setValue(T value) {
		this.value = value;
	}
}
