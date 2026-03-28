package March262026S9;

import java.util.*;;

public class InsertInterval {
    //non overlapping
    //already sorted by start[i]
    //insert new interval (must still be sorted, but may need to merge. )
    //[1,2] and [2,3] ARE overlapping so if = overlap. 

    //situations
    //1. intervals ends before next interval starts, append before, and append the rest. 
    //2. currEnd is larger than next start, will need to merge.
    //3. last element? so it's newInterval start is after last interval end. 

    public int[][] insert(int[][] intervals, int[] newInterval) {
        
        int newStart = newInterval[0];
        int newEnd = newInterval[1];

        List<int[]> resultList = new ArrayList<>();

        for(int i =0; i< intervals.length; i++){
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];

            if(currentEnd < newStart){ //current end before new start, add current interval
                resultList.add(intervals[i]);
            }else if(currentStart > newEnd){ //prepend new, then postpend current + rest
                resultList.add(new int[]{newStart, newEnd});
                resultList.add(intervals[i]);
            }else{ //overlap conditions
                newStart = Math.min(newStart,currentStart);
                newEnd = Math.max(newEnd, currentEnd);
            }

            //need to determine if we should add the merged value or not. 
        }
        return resultList.toArray(new int[resultList.size()][]);
    }
}
