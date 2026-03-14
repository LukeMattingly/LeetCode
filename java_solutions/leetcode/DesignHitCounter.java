package leetcode;
import java.util.*;
public class DesignHitCounter {
    Deque<Integer> queue;
    public DesignHitCounter() {
        queue = new ArrayDeque<>();
    }
    
    public void hit(int timestamp) {
        queue.add(timestamp);
    }
    
    public int getHits(int timestamp) {
        while(!queue.isEmpty() && queue.peek()<= timestamp-300){
            queue.poll();
        }
        return queue.size();
    }
}
