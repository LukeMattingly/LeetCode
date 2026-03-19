package March182026S1;

import java.util.concurrent.Semaphore;

public class PrintInOrder {
    
    private final Semaphore waitForFirst;
    private final Semaphore waitForSecond;
    public PrintInOrder() {
        waitForFirst = new Semaphore(0);
        waitForSecond = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        waitForFirst.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        waitForFirst.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        waitForSecond.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        waitForSecond.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
