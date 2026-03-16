package leetcode;

import java.util.*;

public class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        // create freq map
        // create an array where index of the array will equal the freq value index[5] for all count 5s
        // then iterate through the freq count map and put the values into the array (each element in the array will be a list of values [5,1,7] etc])
        // then loop reversed through the array (since largest at the end) and keep track of how many we read off for the result so it only goes up to k

        Map<Integer, Integer> freqMap = new HashMap<>();
        for(int num: nums){
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        //need all of teh indexes populated with empty arrays. 
        List<List<Integer>> freqList = new ArrayList<>();
        for(int i=0; i<=nums.length;i++){
            freqList.add(new ArrayList<>());
        }

        for(Map.Entry<Integer,Integer> entry : freqMap.entrySet()){
            int key = entry.getKey();
            int freq = entry.getValue();
            freqList.get(freq).add(key); // need to get teh current list and append a new key to it. 
        }
        
        int[] result = new int[k];
        int index =0;
        //finally reversed loop by k values
        for(int freq = freqList.size()-1; freq >= 0; freq--){
            List<Integer> bucket = freqList.get(freq);
            for(Integer itemInBucket: bucket){
                if (index == k) {
                    return result;
                }

                result[index] = itemInBucket;
                index++;
            }
        }
        return result;
    }
}
