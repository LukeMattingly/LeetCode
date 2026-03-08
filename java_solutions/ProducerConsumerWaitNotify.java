import java.util.ArrayDeque;
import java.util.Queue;

public class ProducerConsumerWaitNotify<T> {
    
    //producer must wait if the buffer is full
    //consumer must wait if the buffer is empty
    Queue<T> buffer;
    private int capacity;
    public ProducerConsumerWaitNotify(int capacity){
        this.capacity = capacity;
        buffer = new ArrayDeque<>(capacity);
    }

    public synchronized void produce(T item)throws InterruptedException{
        if(buffer.size()==capacity){
            wait(); //buffer is full, producer must wait
        }
        buffer.offer(item);

        notifyAll(); // wake waiting consumers/producers
    }

    public synchronized T consume() throws InterruptedException{
        if(buffer.isEmpty()){
            wait(); // buffer is empty wait to consume
        }
        T item = buffer.poll();

        notifyAll(); // wake waiting producers and consumers
        return item;
    }
}
