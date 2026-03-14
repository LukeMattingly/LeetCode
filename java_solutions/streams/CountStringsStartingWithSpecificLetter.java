package streams;

import java.util.Arrays;
import java.util.List;

public class CountStringsStartingWithSpecificLetter {
        List < String > colors = Arrays.asList("Red", "Green", "Blue", "Pink", "Brown");

        char startingLetter = 'B';
        //starts with and count
        long count = colors.stream().filter(k->k.startsWith(String.valueOf(startingLetter))).count();

        char startingLetter1 = 'Y';

        long countY = colors.stream().filter(y->y.startsWith(String.valueOf(startingLetter1))).count();
}
