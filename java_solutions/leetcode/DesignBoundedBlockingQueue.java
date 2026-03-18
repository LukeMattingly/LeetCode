package leetcode;


import java.util.*;
/*
1. Queue //take and put
2. Use 2 semaphores based on capacity (openSlots and fullSlots)
3. Protect critical section of writing and reading from queue with Reentrant lock
*/
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

public class DesignBoundedBlockingQueue {

    private final Queue<Integer> queue;
    private final Semaphore fullSlots;
    private final Semaphore emptySlots;
    private final ReentrantLock lock;

    DesignBoundedBlockingQueue(int capacity){
        queue = new ArrayDeque<>();
        fullSlots = new Semaphore(0);
        emptySlots = new Semaphore(capacity);
        lock = new ReentrantLock();
    }

    public void enqueue(int element) throws InterruptedException{
            emptySlots.acquire();

            lock.lock();
            try{
                queue.offer(element);
            }finally{
                lock.unlock();
            }

            fullSlots.release();
        
    }

    public int dequeue()throws InterruptedException{
            int result;
            fullSlots.acquire();
            lock.lock();    
            try{
                result = queue.remove();
            }finally{
                lock.unlock();
            }
            emptySlots.release();
            return result;
    }

    public int size(){
        lock.lock();
        try{
            return queue.size();
        }
        finally
        {
            lock.unlock();
        }
    }
    
}
