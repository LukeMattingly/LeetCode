package streams;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class SortStringAZ {
        List < String > colors = Arrays.asList("Red", "Green", "Blue", "Pink", "Brown");

        List<String> sortedColors = colors.stream().sorted().toList();

        List<String> reverseSorted = colors.stream().toList().reversed();

        List<String> reversed = colors.stream().sorted(Comparator.reverseOrder()).toList();
}
