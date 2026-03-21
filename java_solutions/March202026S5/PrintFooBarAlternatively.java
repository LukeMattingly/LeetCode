package March202026S5;

import java.util.concurrent.Semaphore;

public class PrintFooBarAlternatively {
        private int n;

        // Need to make sure 'foo' happen before 'bar' each time. 
        // semaphore of size n, release a slot from foo, then bar can consume it
        Semaphore emptySlots;
        Semaphore fullSlots;
    public PrintFooBarAlternatively(int n) {
        emptySlots = new Semaphore(1);
        fullSlots = new Semaphore(0);
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            emptySlots.acquire();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            fullSlots.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            fullSlots.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            emptySlots.release();
        }
    }
}
