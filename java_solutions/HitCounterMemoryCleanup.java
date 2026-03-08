import java.util.ArrayDeque;
import java.util.Deque;

public class HitCounterMemoryCleanup {
    Deque<Integer> hits;

    public HitCounterMemoryCleanup() {
        hits = new ArrayDeque<>();
    }
    
    public void hit(int timestamp) {
        evictOldest(timestamp);
        hits.add(timestamp);
    }
    
    public int getHits(int timestamp) {
        evictOldest(timestamp);
        return hits.size();
    }

    public void evictOldest(int timestamp){
        while(!hits.isEmpty() && hits.peek() <= timestamp -300){
            hits.poll();
        }
    }
}
