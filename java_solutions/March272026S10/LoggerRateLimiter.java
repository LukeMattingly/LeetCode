package March272026S10;

import java.util.*;

public class LoggerRateLimiter {

    Map<String, Integer> rateLimiter;
    public LoggerRateLimiter() {
        rateLimiter = new HashMap<>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(rateLimiter.containsKey(message)){
            int oldTimeStamp = rateLimiter.get(message);
            if(oldTimeStamp + 10 > timestamp){
                return false;
            }
            rateLimiter.put(message, timestamp);
            return true;
        }
        rateLimiter.put(message, timestamp);
        return true;
    }
}
