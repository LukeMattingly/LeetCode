package streams;

import java.util.Arrays;
import java.util.List;

//o calculate the average of a list of integers using streams.

public class CalculateAverageOfInts {
        List<Integer> nums = Arrays.asList(1, 3, 6, 8, 10, 18, 36);
        double avg = nums.stream().mapToDouble(Integer::doubleValue).average().orElse(0);

}
