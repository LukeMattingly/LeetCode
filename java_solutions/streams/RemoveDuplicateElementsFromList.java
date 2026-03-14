package streams;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

//remove all duplicate elements from a list using streams.

public class RemoveDuplicateElementsFromList {
        List < Integer > nums = Arrays.asList(10, 23, 22, 23, 24, 24, 33, 15, 26, 15);

        List<Integer> distinctElements = nums.stream().distinct().toList(); //immuatable

        List<Integer> distinctInts = nums.stream().distinct().collect(Collectors.toList()); //mutatble
        
        Set<Integer> seen = new HashSet<>();
        List<Integer> distIntegers = nums.stream().filter(seen::add).collect(Collectors.toList());
}
