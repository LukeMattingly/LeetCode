package March272026S10;

import java.util.*;

public class DesignHitCounter {
    Queue<Integer> queue;

    public DesignHitCounter() {
        queue = new ArrayDeque<>();
    }
    
    public void hit(int timestamp) {
        queue.add(timestamp);
    }
    
    public int getHits(int timestamp) {
        //need to poll off events older than 5 mins  //301
        while(!queue.isEmpty() && queue.peek() +300 <= timestamp){
            queue.remove();
        }

        return queue.size();
    }
}
