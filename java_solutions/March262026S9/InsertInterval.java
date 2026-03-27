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

        int[][] result = new int[intervals.length][2];
        List<int[]> resultList = new ArrayList<>();

        for(int i =0; i< intervals.length; i++){
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];
            if(newEnd >= currentStart){ //[i][0] is start of 'current' MERGE
                newStart = Math.min(newStart,currentStart);
                newEnd = Math.max(newEnd, currentEnd);
            }else if( newEnd < currentEnd ){ // ends before the end
                resultList.add(new int[]{newStart, newEnd});
                resultList.add(intervals[i:-1])//all of the rest of the intervals
                break;
            }
            resultList.add(intervals[i]);
        }
        int[] res = resultList.stream().mapToInt(Integer::intValue).toArray();
        return new int[][]
    }
}
