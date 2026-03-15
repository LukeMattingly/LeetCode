package leetcode;
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        for(int i =0; i<nums.length; i++){
            if(numsMap.containsKey(nums[i])){
                int firstIndex = numsMap.get(nums[i]);
                return new int[]{firstIndex, i};
            }
            numsMap.put(target - nums[i], i);
        }
        return new int[]{};
    }
}