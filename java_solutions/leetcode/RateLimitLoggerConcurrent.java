package leetcode;
import java.util.concurrent.ConcurrentHashMap;

public class RateLimitLoggerConcurrent {
    ConcurrentHashMap<String, Integer> messages;

    public RateLimitLoggerConcurrent(){
        messages = new ConcurrentHashMap<>();
    }

    public synchronized boolean shouldPrintMessage(int timestamp, String message){
        //default to 0 if no value found as any timestamp will be larger
        int nextAllowedTime = messages.getOrDefault(message, 0);

        if(timestamp < nextAllowedTime){
            return false;
        }

        messages.put(message, timestamp +10);
        return true;
    }
}
