package March182026S2;

import java.util.*;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

public class BoundedBlockingQueue {

    Queue<Integer> queue;
    Semaphore fullSlots;
    Semaphore emptySlots;
    ReentrantLock lock;

    BoundedBlockingQueue(int capacity){
        queue = new ArrayDeque<>();
        fullSlots = new Semaphore(0);
        emptySlots = new Semaphore(capacity);
    }

    void enqueue(int element)throws InterruptedException{
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

        lock.lock();
        int result;
        try{
            result= queue.poll();
        }finally{
            lock.unlock();
        }

        emptySlots.release();
        return result;
    }

    int size(){
        lock.lock();
        try{
            return queue.size();
        }finally{
            lock.unlock();
        }
    }
}
