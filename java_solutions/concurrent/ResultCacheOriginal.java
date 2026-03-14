package concurrent;
import java.util.*;

/*
A simple in-memory cache used by multiple background threads. 
It occasionally throws ConcurrentModificationException or returns stale data during high traffic.

Java */

public class ResultCacheOriginal {
    private Map<String, Object> cache = new HashMap<>();

    public void save(String key, Object value) {
        cache.put(key, value);
    }

    public Object fetch(String key) {
        return cache.get(key);
    }
}