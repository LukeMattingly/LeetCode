import java.util.*;
import java.util.concurrent.Semaphore;

public class ProducerConsumerConcurrent<T> {

    Queue<T> buffer = new ArrayDeque<>();
    private Semaphore emptySlots;
    private Semaphore fullSlots;
    private Semaphore mutex;
    public ProducerConsumerConcurrent(int capacity, Semaphore emptySlots, Semaphore fullSlots){
        this.emptySlots = new Semaphore(capacity);
        this.fullSlots = new Semaphore(0);
        this.mutex = new Semaphore(1);
    }

    public void produce(T item) throws InterruptedException{
        // wait until there's at least one empty Slot
        emptySlots.acquire();

        // critical section
        mutex.acquire();
        try{
            buffer.add(item);
        }finally{
            mutex.release();
        }
        // one more slots has been filled
        fullSlots.release();
    }

    public T consume() throws InterruptedException{
        // wait until there's atleast one fullSlot avail
        fullSlots.acquire();

        mutex.acquire();
        T item;
        try{
            item = buffer.poll(); 
        }
        finally{
            mutex.release();
        }

        emptySlots.release();
        return item;
    }
    
}
