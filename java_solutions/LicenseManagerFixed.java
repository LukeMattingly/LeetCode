import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

/*
You have a limited pool of 3 physical licenses. You need to ensure that if a 4th thread asks for one,
 it waits until one is released, rather than just getting a null.
*/

public class LicenseManagerFixed {

    private final BlockingQueue<String> pool;

    public LicenseManagerFixed(int capacity){
        pool = new ArrayBlockingQueue<>(capacity);
        this.pool.add("l1");
        this.pool.add("l2");
        this.pool.add("l3");
    }

    public String acquire() throws InterruptedException{
        return pool.take();
    }

    public void release(String license) throws InterruptedException{
        pool.put(license);
    }

} 
