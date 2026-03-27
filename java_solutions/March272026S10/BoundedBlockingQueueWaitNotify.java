package March272026S10;

import java.util.ArrayDeque;
import java.util.Queue;

public class BoundedBlockingQueueWaitNotify {
    private final Queue<Integer> queue;
    private int capacity;

    public BoundedBlockingQueueWaitNotify(int capacity){
        queue = new ArrayDeque<>(capacity);
        this.capacity = capacity;
    }


    synchronized void enqueue(int element)throws InterruptedException {
        if(queue.size() == capacity){
            wait();
        }
        queue.offer(element);
        notifyAll();
    }
    synchronized int dequeue()throws InterruptedException { 
        while(queue.isEmpty()){
            wait();
        }
        int result = queue.poll();
        notifyAll();
        return result;

    }

    synchronized int size(){
        return queue.size();
    }
}
