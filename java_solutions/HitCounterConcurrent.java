import java.util.*;
public class HitCounterConcurrent {
    int[] times;
    int [] counts;
    public HitCounterConcurrent() {
        times = new int[300];
        counts = new int[300];
    }
    
    public synchronized void hit(int timestamp) {
        int index = timestamp %300;
        if(times[index] !=timestamp){
            times[index] = timestamp;
            counts[index] =1;
        }else{
            counts[index]++;
        }
    }
    
    public synchronized int getHits(int timestamp) {
        int total = 0;
        for(int i =0; i<300; i++){
            if (timestamp - times[i] < 300){
                total += counts[i];
            }
        }
        return total;
    }
}
