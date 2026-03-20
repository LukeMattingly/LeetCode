package March192026S3;

import java.util.*;

public class TopKFrequentElements {
    //priority queue for top k values
    //freq map
    public int[] topKFrequent(int[] nums, int k) {
            Map<Integer, Integer> freqMap = new HashMap<>();
            for(int num : nums){
                freqMap.put(num, freqMap.getOrDefault(num, 0)+1);
            }       
            
            // default to min heap, need a max heap k MOST freq values
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<>((a,b)-> freqMap.get(b) -freqMap.get(a));
            priorityQueue.addAll(freqMap.keySet());

            //initialize array to size k
            int[] result = new int[k];
            for(int i=0; i<k; i++){
                result[i] = priorityQueue.poll();
            }
            return result;

    }

}
