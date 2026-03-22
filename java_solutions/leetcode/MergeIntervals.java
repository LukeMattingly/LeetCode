package leetcode;

import java.util.*;

public class MergeIntervals {
    
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0])); 


        List<int[]> resultList = new ArrayList<>();

        int prevStart = intervals[0][0];
        int prevEnd = intervals[0][1];
        for(int i=1; i< intervals.length; i++){

            //merge if prevEnd is larger or equal to current start
            if(prevEnd>= intervals[i][0]){
                prevStart = Math.min(prevStart, intervals[i][0]);
                prevEnd = Math.max(prevEnd, intervals[i][1]);
            }else{
                resultList.add(new int[]{prevStart, prevEnd});
                prevStart = intervals[i][0];
                prevEnd = intervals[i][1];
            }
            
        }

        resultList.add(new int[]{prevStart, prevEnd});

        return resultList.toArray(new int[resultList.size()][]);
    }
}
