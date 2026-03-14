package concurrent;

import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class OrderServiceAllOf {
    ExecutorService executor = Executors.newFixedThreadPool(2);



    public String getFullOrderDetails(List<String> userIds) {

        
        // 1. Map each ID to a started CompletableFuture            
        List<CompletableFuture<String>> futures = userIds.stream().map(id -> CompletableFuture.supplyAsync(()-> fetchUser(id), executor)).collect(Collectors.toList());

        // 2. Create a "Master Future" that completes when ALL futures in the list finish
        CompletableFuture<Void> allDone = CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]));

        // 3. Wait for all to finish, then map the futures to their results
        return allDone.thenApply(v -> {
            return futures.stream()
                    .map(CompletableFuture::join) // join() won't block here because allOf is done
                    .collect(Collectors.joining(", "));
        }).join();
    
    }

    private String fetchUser(String id) {
            // Simulate network delay
            return "User_" + id;
        }
    }