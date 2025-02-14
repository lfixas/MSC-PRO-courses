import java.lang.reflect.Method;

public class TestRunner {
    public static void runTests(Class<?> testClass) {
        try {
            // Create an instance of the test class
            Object testObject = testClass.getDeclaredConstructor().newInstance();

            // Get all the methods declared in the test class
            Method[] methods = testClass.getDeclaredMethods();

            for (Method method : methods) {
                // Check if the method is annotated with @Test
                if (method.isAnnotationPresent(Test.class)) {
                    // Get the Test annotation for the method
                    Test testAnnotation = method.getAnnotation(Test.class);

                    // Check if the test is enabled (true)
                    if (testAnnotation.enabled()) {
                        // Print the name of the executed test
                        System.out.println(testAnnotation.name());

                        try {
                            // Invoke the test method on the test object
                            method.invoke(testObject);
                            // Print "Test executed" after a successful test execution
                            // System.out.println("Test executed");
                        } catch (Exception e) {
                            // Catch and print any exceptions that occur during test execution
                            e.printStackTrace();
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
