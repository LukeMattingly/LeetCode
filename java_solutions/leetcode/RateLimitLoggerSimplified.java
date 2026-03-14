package leetcode;
import java.util.HashMap;
import java.util.Map;


public class RateLimitLoggerSimplified {
    Map<String, Integer> messages;
    public RateLimitLoggerSimplified(){
        messages = new HashMap<>();
    }

    public boolean shouldPrintMessage(int timestamp, String message){
        int nextAllowedTime  = messages.getOrDefault(message, 0);

        if( timestamp<nextAllowedTime ){
            return false;
        }
        messages.put(message, timestamp +10);

        return true;

    }
}
