// Create an annotation called AfterClass
import java.lang.annotation.*;

// It must be available at runtime ;
@Retention(RetentionPolicy.RUNTIME)
// Only be able to use it on methods
@Target(ElementType.METHOD)
public @interface AfterClass {
    
}
