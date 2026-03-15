package streams;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class FindMinMaxinList {
        List < Integer > nums = Arrays.asList(1, 17, 54, 14, 14, 33, 45, -11);
        Integer max = nums.stream().max(Comparator.comparingInt(Integer::intValue)).orElse(null);

        Integer max_val = nums.stream().max(Integer::compare).orElse(null);

        Integer maxVal = nums.stream().max(Comparator.naturalOrder()).orElse(null);
}
