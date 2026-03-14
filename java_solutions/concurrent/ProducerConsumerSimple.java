package concurrent;
import java.util.ArrayDeque;
import java.util.*;

public class ProducerConsumerSimple<T> {

    Queue<T> buffer = new ArrayDeque<>();
    private int capacity;
    public ProducerConsumerSimple(int capacity){
        this.capacity = capacity;
    }

    public boolean produce(T item){
        if(buffer.size() == capacity){
            return false;
        }
        buffer.add(item);
        return true;
    }

    public T consume(){
        if(!buffer.isEmpty()){
            return buffer.poll();
        }
        else{
            return null;
        }
    }
    
}
