package March182026S2;

import java.util.*;

public class ContainsDuplicate {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniqueVals = new HashSet<>();
        for(int num: nums){
            if(uniqueVals.contains(num)){
                return true;
            }
            uniqueVals.add(num);
        }
        return false;
    }
}
