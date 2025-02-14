// Create an annotation called Test
import java.lang.annotation.*;

// It must be available at runtime ;
@Retention(RetentionPolicy.RUNTIME)
// Only be able to use it on methods
@Target(ElementType.METHOD)
public @interface Test {
    // a string containing the name of the test ;
    String name() default "";
    boolean enabled() default true;
}
