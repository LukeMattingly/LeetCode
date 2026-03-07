import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicBoolean;

public class RateLimitLoggerConcurrent {
    Map<String, Integer> messages;
    public RateLimitLoggerConcurrent(){
        messages = new ConcurrentHashMap<>();
    }

    public boolean shouldPrintMessage(int timestamp, String message){

        AtomicBoolean allowedPrint = new AtomicBoolean(false);

        messages.compute(message, (k, nextAllowedTime)-> {
            if(nextAllowedTime == null || timestamp>= nextAllowedTime){
                allowedPrint.set(true);
                return timestamp+10;
            }
            return nextAllowedTime;
        });

        return allowedPrint.get();

    }
}
