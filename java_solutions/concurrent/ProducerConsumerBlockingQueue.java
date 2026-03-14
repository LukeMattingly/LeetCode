package concurrent;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ProducerConsumerBlockingQueue <T>{

    BlockingQueue<T> buffer;
    public ProducerConsumerBlockingQueue(int capacity){
        buffer= new ArrayBlockingQueue<>(capacity) {};
    }

    public void produce(T item) throws InterruptedException {
        // blocks if full
        buffer.put(item); // use put for a blocking queue ( inserts the specific element, waiting if needed for space to becoem available if the queue is full)
    }

    public T consume()throws InterruptedException {
        // blocks if empty
        return buffer.take(); // retrieves and removes teh head of the queue waiting if necessary until an element becomes available
    } 
    
}
