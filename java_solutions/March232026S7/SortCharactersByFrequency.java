package March232026S7;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class SortCharactersByFrequency {
        //sort by frequencie of most to least
    //1. create a hash map freq count of each string
    //2. could also add to a priority queue/max heap (min is default)
    //3. then read off all the values in order. 
    public String frequencySort(String s) {
        Map<Character, Integer> freqMap = new HashMap<>();
        
        char [] chars = s.toCharArray();
        for(char c : chars){
            freqMap.put(c, freqMap.getOrDefault(c, 0)+1);
        }
        
        //Need to reverse sort the pq because by default it's minheap?
        PriorityQueue<Character> pq = new PriorityQueue<>((a,b)-> Integer.compare(freqMap.get(b), freqMap.get(a)));
        pq.addAll(freqMap.keySet());

        //I needed to store the count of how many times it was there, so I can read off both. 
        StringBuilder result = new StringBuilder();
        while(!pq.isEmpty()){
            Character ch = pq.poll();
            int count = freqMap.get(ch);
            for(int i =0; i< count; i++){
                result.append(ch);   
            }
        }
        return result.toString();

    }
}
