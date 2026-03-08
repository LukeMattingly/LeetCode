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
            // When a read calls wait();
            //1. it releases the monitor lock (of synchronized?)
            //2. it goes to sleep on that object
            //3. it stays blocked until another thread calls notify or notify all
            //4. before continuing, it must re-acquire the same monitor lock
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
