package March202026S6;

import java.util.AbstractMap;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;
import java.util.PriorityQueue;

public class KClosestPointsToOrigin {

    //sort the points to start?
    //since i want closest to origin
    public int[][] kClosest(int[][] points, int k) {
        //(a,b)-> points.get[0] points.get[b]
        //Arrays.sort(points, (a,b) -> Integer.compare(a[0], b[0])); do we need to sort? need to go through all anyway. 

        PriorityQueue<Map.Entry<Double, int[]>> pq = new PriorityQueue<>();
        //only the first values are sorted. 
        for(int i =0; i< points.length; i++){
            double distance = Math.sqrt(Math.pow(points[i][0]- points[i][1], 2));
            Map.Entry<Double, int[]> entry = new AbstractMap.SimpleEntry<Double, int[]>(distance,new int[] {points[i][0], points[i][1]});
            pq.add(entry);
        }

        int[][] result = new int[k][2];
        for(int j =0; j<k; j++){
            Map.Entry<Double, int[]> entry = pq.poll();
            result[j] = entry.getValue();
        }
        return result;
    }
}
