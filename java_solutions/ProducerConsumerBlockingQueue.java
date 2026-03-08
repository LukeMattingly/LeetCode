import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ProducerConsumerBlockingQueue <T>{

    BlockingQueue<T> buffer;
    public ProducerConsumerBlockingQueue(int capacity){
        buffer= new ArrayBlockingQueue<>(capacity) {};
    }

    public void produce(T item) throws InterruptedException {
        // blocks if full
        buffer.put(item);
    }

    public T consume()throws InterruptedException {
        // blocks if empty
        return buffer.take();
    }
    
}
