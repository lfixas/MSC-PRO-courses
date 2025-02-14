import java.lang.reflect.Field;
import java.lang.reflect.Method;

import java.lang.reflect.InvocationTargetException;

public class Inspector<T> {
    private final Class<T> inspectedClass;

    public Inspector(Class<T> inspectedClass) {
        this.inspectedClass = inspectedClass;
    }

    public void displayInformations() {
        System.out.println("Information of the \"" + inspectedClass.getName() + "\" class:");

        // Superclass
        Class<?> superclass = inspectedClass.getSuperclass();
        System.out.println("Superclass: " + (superclass != null ? superclass.getName() : "None"));

        // Methods
        Method[] declaredMethods = inspectedClass.getDeclaredMethods();
        System.out.println(declaredMethods.length + " methods:");
        for (Method method : declaredMethods) {
            System.out.println("- " + method.getName());
        }

        // Fields
        Field[] declaredFields = inspectedClass.getDeclaredFields();
        System.out.println(declaredFields.length + " fields:");
        for (Field field : declaredFields) {
            System.out.println("- " + field.getName());
        }
    }

    public T createInstance() throws IllegalAccessException, InstantiationException, InvocationTargetException, NoSuchMethodException {
        try {
            // Get the default constructor of the inspected class
            java.lang.reflect.Constructor<T> constructor = inspectedClass.getDeclaredConstructor();
            
            // Create a new instance using the default constructor
            T instance = constructor.newInstance();

            return instance;
        } catch (IllegalAccessException | InstantiationException | InvocationTargetException | NoSuchMethodException e) {
            // Rethrow any exceptions that may occur
            throw e;
        }
    }
}
