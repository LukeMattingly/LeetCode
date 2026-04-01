package leetcode_variations;

import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ValidateParenthesisParallel {
    
    private static class ChunkResult{
        final int netBalance;
        final int minPrefixBalance;

        ChunkResult(int netBalance, int minPrefixBalance){
            this.netBalance = netBalance;
            this.minPrefixBalance = minPrefixBalance;
        }
    }

    public boolean isBalanceParallel(String text, int numThreads){
        if(text == null || text.isEmpty()){
            return true;
        }

        int n = text.length();

        int chunkSize = Math.max(1, (n+numThreads -1)/ numThreads);

        ExecutorService executorService = Executors.newFixedThreadPool(numThreads);

        List<Future<ChunkResult>>futures = new ArrayList<>();

         try {
            for (int start = 0; start < n; start += chunkSize) {
                int chunkStart = start;
                int chunkEnd = Math.min(n, start + chunkSize);

                futures.add(executorService.submit(() -> processChunk(text, chunkStart, chunkEnd)));
            }

            int runningBalance = 0;

            for (Future<ChunkResult> future : futures) {
                ChunkResult result = future.get();

                if (runningBalance + result.minPrefixBalance < 0) {
                    return false;
                }

                runningBalance += result.netBalance;
            }

            return runningBalance == 0;
        } finally {
            executorService.shutdown();
        }
    }


    private ChunkResult processChunk(String text, int start, int end) {
        int balance = 0;
        int minPrefix = 0;

        for (int i = start; i < end; i++) {
            char c = text.charAt(i);

            if (c == '(') {
                balance++;
            } else if (c == ')') {
                balance--;
                minPrefix = Math.min(minPrefix, balance);
            }
        }

        return new ChunkResult(balance, minPrefix);
    }
}
