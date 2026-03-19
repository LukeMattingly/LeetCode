package March182026S1;

import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        //Return the answer with the smaller index first.

        //Map key = target - currentNum, value= index of currentNum
        Map<Integer, Integer> numMap = new HashMap<>();

        for(int i=0; i<nums.length; i ++){
            if(numMap.containsKey(nums[i])){
                return new int[] {numMap.get(nums[i]), i};
            }
            //storing complement for easy contains key lookup
            numMap.put(target - nums[i], i);
        }
        return new int[]{};
    }
}
