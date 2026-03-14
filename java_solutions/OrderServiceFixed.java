/*
both calls run at the same time, no logner sequential

CompletableFuture: Represents a future result of an asynchronous computation.

thenCombine: Used when you have two independent futures and you want to do something with both of their results once they are both complete. This reduces the total latency to the time of the slowest call, rather than the sum of all calls.
*/

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class OrderServiceFixed {
    ExecutorService executor = Executors.newFixedThreadPool(2);



    public String getFullOrderDetails() {

        //Start both tasks asynchornously
        CompletableFuture<String> userFuture = CompletableFuture.supplyAsync(this::fetchUser, executor);
        CompletableFuture<String> orderFuture = CompletableFuture.supplyAsync(this::fetchOrder, executor);

        return userFuture.thenCombine(orderFuture, (user, order)->{ return user + " details for " + order; } ).join(); //.join waits for the final combined result
    
    }

    private String fetchUser() { return "User_123"; }
    private String fetchOrder() { return "Order_999"; }
}