package leetcode;

import java.util.*;

public class ContainsDupliate {
    public boolean containsDuplicate(int[] nums) {
        
        // loop through nums check if item is in set, 
        //if it is then return true
        //if not then add it
        //if we make it to the end then return false
        Set<Integer> noDupes = new HashSet<>();
        for(int i =0; i< nums.length; i++){
            if(noDupes.contains(nums[i])){
                return true;
            }
            noDupes.add(nums[i]);
        }
        return false;
        
    }
}
