package leetcode;

import java.util.Comparator;
import java.util.PriorityQueue;

public class KClosestPointsToOrigin {
    public int[][] kClosest(int[][] points, int k) {
        //priority queue (use comparator to sort by a[0])
        // int[] [dist, point1, point2]
        //loop through k times and poll off

        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparing(a -> a[0]));

        for(int i =0; i< points.length; i++){
            //(sqrt((x1 - x2)^2 + (y1 - y2)^2)).
            //x1 and y1 are 0s because we're at the origin
            //4-> sqrt(8)
            //0 -> 0 
            int distance = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            queue.offer(new int[]{distance, points[i][0], points[i][1]});
        }

        int[][] result = new int[k][2];
        for(int j =0; j<k;j++){
            int [] values = queue.poll();
            result[j][0] = values[1]; //1st point
            result[j][1] = values[2]; //2nd point
        }
        return result;

    }
}
