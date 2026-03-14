package leetcode;
import java.util.HashMap;
import java.util.Map;

public class RateLimitLoggerConcurrent {
    Map<String, Integer> messages;

    public RateLimitLoggerConcurrent(){
        messages = new HashMap<>();
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
