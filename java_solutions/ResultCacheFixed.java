import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/*
HashMap is not thread-safe. If multiple threads call save() or fetch() simultaneously, 
the internal structure of the map can become corrupted, leading to infinite loops or
 ConcurrentModificationException. */

public class ResultCacheFixed {
    // ConcurrentHashMap handles internal locking/segmentation for thread safety
    private Map<String, Object> cache = new ConcurrentHashMap<>();

    public void save(String key, Object value) {
        if (key != null && value != null) 
            cache.put(key, value);
    }

    public Object fetch(String key) {
        return cache.get(key);
    }
}
