package March232026S7;

import java.util.*;

public class TaskScheduler {
    //create unique groupings, and then total number of unique groupings. -1 = spaces 
    //groupings + spaces = total. 
    //total number of groupings is based on the more frequent character, if AAA means have to have 3 groups. 
    //find most frequent char, and keep track of it, then do math. 
    
    public int leastInterval(char[] tasks, int n) {
         Map<Character, Integer> freqMap = new HashMap<>();
        
         for(char task: tasks){
            freqMap.put(task, freqMap.getOrDefault(task, 0)+1);
         }

        // 1. Get the max frequency
        int maxFreq = Collections.max(freqMap.values());

        // 2. Count how many tasks have that max frequency
        int maxCount = 0;
        for (int count : freqMap.values()) {
            if (count == maxFreq) {
                maxCount++;
            }
        }

        // 3. The Math
        // (maxFreq - 1) is the number of "gaps" between the most frequent tasks
        // (n + 1) is the size of each gap (the task itself + the cooling period)
        // maxCount is the number of tasks that will sit in the final row
        int result = (maxFreq - 1) * (n + 1) + maxCount;

        // 4. Return the larger of the calculated value or the actual task length
        // If we have so many tasks that no idle time is needed, tasks.length is the answer.
        return Math.max(tasks.length, result);
    }

}
