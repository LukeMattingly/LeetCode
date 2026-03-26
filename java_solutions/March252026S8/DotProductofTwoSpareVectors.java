package March252026S8;

import java.util.*;

public class DotProductofTwoSpareVectors {
 
class SparseVector {
    public Map<Integer, Integer> nonZeroMap = new HashMap<>(128);
    //keys represent indicies of non-zero elements
    //values are the actual non-zero values at those indicies

    SparseVector(int[] nums) {
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != 0) {
                nonZeroMap.put(i, nums[i]); 
            }
        }
    }

    //checks to see which vector has fewer nonzero elements for optimization
    //iterates through smaller hashmap
    //for each element checks if the same index exists in the vector's hashmap
    // if both vectors have non zero values iat the same index, their product i added to teh result
    public int dotProduct(SparseVector vec) {
        Map<Integer, Integer> mapA = this.nonZeroMap;
        Map<Integer, Integer> mapB = vec.nonZeroMap;

        //swap references if other way around
        //temp swap so always loop through smaller
        if(mapB.size() < mapA.size()){
            Map<Integer, Integer> temp = mapA;
            mapA = mapB;
            mapB = temp;
        }

        int result = 0;
        //calculate dot production by iteration
        for(Map.Entry<Integer, Integer> entry: mapA.entrySet()){
            int index = entry.getKey();
            int value = entry.getValue();
            //mutliple values if they exist in both vectors
            //use getOrDefault to handlign missing indcidies (Treat as 0)
            result += value * mapB.getOrDefault(index, 0);
        }
        return result;
    }
     
    }
    
}
