package March272026S10;

import java.util.*;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

public class BoundedBlockingQueue {
    private final Queue<Integer> queue;
    private final Semaphore fullSlots;
    private final Semaphore emptySlots;
    private final ReentrantLock lock;
    public BoundedBlockingQueue(int capacity){
        queue = new ArrayDeque<>(capacity);
        fullSlots = new Semaphore(0);
        emptySlots = new Semaphore(capacity);
        lock = new ReentrantLock();
    }


    void enqueue(int element) throws InterruptedException{
        emptySlots.acquire();
        lock.lock();
        try{
            queue.offer(element);
        }finally{
            lock.unlock();
        }

        fullSlots.release();

    }
    int dequeue() throws InterruptedException{ 
        fullSlots.acquire();

        int result;
        lock.lock();
        try{
            result = queue.poll();
        }finally{
            lock.unlock();
        }

        emptySlots.release();
        return result;
    }
    // Returns the number of elements currently in the queue.
    int size(){
        lock.lock();
        int size; 
        try{
            size = queue.size();
        }finally{
            lock.unlock();
        }
        return size;
    }
}
