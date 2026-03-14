package concurrent;
import java.util.*;

/*
You have a limited pool of 3 physical licenses. You need to ensure that if a 4th thread asks for one,
 it waits until one is released, rather than just getting a null.
*/

public class LicenseManagerOriginal {
    private final List<String> licenses = new ArrayList<>(List.of("L1", "L2", "L3"));

    public String acquire() {
        if (!licenses.isEmpty()) {
            return licenses.remove(0);
        }
        return null; 
    }

    public void release(String license) {
        licenses.add(license);
    }
}