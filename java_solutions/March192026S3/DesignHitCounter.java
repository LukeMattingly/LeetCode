package March192026S3;

import java.util.ArrayDeque;
import java.util.Queue;

public class DesignHitCounter {
    //Need a queue 
    private final Queue<Integer> queue;
    public DesignHitCounter() {
        queue= new ArrayDeque<>();
    }
    
    public void hit(int timestamp) {
        queue.offer(timestamp);
    }
    
    public int getHits(int timestamp) {
        //need to remove any outdated items first
        // timestamp = 300 top is 1 
        // timestamp = 301 top is 1 then remove top
        while(!queue.isEmpty() &&  (timestamp - queue.peek()) >=300 ){
            queue.remove();
        }

        return queue.size();
    }
}
