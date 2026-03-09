import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;
import java.util.*;

public class ProducerConsumerTestHarness<T> {

    Queue<T> buffer = new ArrayDeque<>();
    Semaphore fullSlots; 
    Semaphore emptySlots;
    ReentrantLock lock;
    public ProducerConsumerTestHarness(int capacity){
        fullSlots = new Semaphore(0);
        emptySlots = new Semaphore(capacity);
        lock = new ReentrantLock();
    }

    public void produce(T item) throws InterruptedException{
        emptySlots.acquire();

        // critical section
        lock.lock();
        try{
            buffer.offer(item); //offer is anonblocking operation tries to insert immediately
        }finally{
            lock.unlock();
        }

        fullSlots.release();
    }

    public T consume() throws InterruptedException{
        fullSlots.acquire();

        
        lock.lock(); //accessing shared mutable state
        T item;
        try{
            item = buffer.poll();
        }finally{
            lock.unlock(); //must unlock incase .poll throws
        }

        emptySlots.release();
        return item;
    }
    
    public static void main(String[] args) {
    
        ProducerConsumerTestHarness<Integer> buffer = new ProducerConsumerTestHarness<>(10);

        Runnable producerTask = () -> {
            int value = 1;
            try{
                while(true){
                    buffer.produce(value++);
                }
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
        };

        Runnable consumerTask = () ->{
            try{
                while(true){
                    buffer.consume();
                }
            }catch(InterruptedException e){
                Thread.currentThread().interrupt();
            }
        };

        Thread p1 = new Thread(producerTask, "producer-1");
        Thread p2 = new Thread(producerTask, "producer-2");

        Thread c1 = new Thread(consumerTask, "consumer-1");
        Thread c2 = new Thread(consumerTask, "consumer-2");
        
        p1.start();
        p2.start();
        c1.start();
        c2.start();
    }


}
