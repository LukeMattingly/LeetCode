import java.util.HashMap;
import java.util.Map;

class RateLimitLogger {
    Map<String, Integer> messages;

    public RateLimitLogger() {
        messages = new HashMap<>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(messages.containsKey(message)){
            Integer storedTimestamp = messages.get(message);
            if(timestamp < storedTimestamp +10){
                return false;
            }
            messages.put(message, timestamp);
            return true;
        }
        messages.put(message, timestamp);
        return true;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */
