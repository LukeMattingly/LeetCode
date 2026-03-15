package streams;

import java.util.Arrays;
import java.util.List;

public class Find2ndSmallestLargest{
        List < Integer > nums = Arrays.asList(1, 17, 54, 14, 14, 33, 45, -11);

        
        Integer secondSmallest = nums.stream().distinct().sorted().skip(1).findFirst().orElse(null);

        //sort then find the 2nd from last?
        // do some compare of the two largest?

        //Integer secondSmallest = nums.stream().sorted().filter(k-> k.);

}