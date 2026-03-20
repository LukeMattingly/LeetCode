package March192026S4;

import java.util.*;;

public class LoggerRateLimiter {
    //hashmap 
    //only ever need 1 key of 'foo' or 'bar' with associated value of 1 or 2
    Map<String, Integer> timestampMap;
    public LoggerRateLimiter() {
        timestampMap = new HashMap<>();
    }
    //foo 1
    //timestamp 10
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(timestampMap.containsKey(message)){
            if(timestampMap.get(message) + 10 <= timestamp){
                timestampMap.put(message, timestamp);
                return true;
            }else{
                return false;
            }
        }
        timestampMap.put(message, timestamp);
        return true;
    }
}
