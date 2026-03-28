package March202026S5;

import java.util.*;
import java.util.stream.Collectors;

public class MergeIntervals {
    //Intervals are non-overlapping if they have no common point. For example, 
    // [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

    //Start by sorting the intervals so that they are ordered
    //then for each interval compare prevEnd to nextStart and if overlapping merge
    // keep updating the current interval, if you keep merging it. 
    // cases
    // end is smaller than start -> no merge, just add first one
    // end is larger than next start -> merge
    // 3rd case.think

    public int[][] merge(int[][] intervals) {
        List<List<Integer>> resultList = new ArrayList<>();


        //
        Arrays.sort(intervals, (a,b)-> Integer.compare(a[0], b[0]));


        int prevStart = intervals[0][0];
        int prevEnd = intervals[0][1];
        for(int i=1; i<intervals.length; i++){
            
            //prev end is larger than or equal to new start
            if(prevEnd >= intervals[i][0]){
                int [] mergedInterval = {
                    Math.min(prevStart, intervals[i][0]),
                    Math.max(prevEnd, intervals[i][1])
                };
                prevStart = mergedInterval[0];
                prevEnd = mergedInterval[1];
            }
            else{ //prev end is smaller than new start no merge conflict
                resultList.add(List.of(prevStart, prevEnd));
                prevStart = intervals[i][0];
                prevEnd = intervals[i][1];
            }

        }
        resultList.add(List.of(prevStart, prevEnd));

        //convert resultList to int [][]
        int[][] result = new int[resultList.size()][2];
        for(int j=0; j<resultList.size();j++){
            result[j][0] = resultList.get(j).get(0);
            result[j][1] = resultList.get(j).get(1);
        }

        return result;
        
    }
}
