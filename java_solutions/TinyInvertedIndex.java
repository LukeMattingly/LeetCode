import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

public class TinyInvertedIndex {
    private final Map<String, Set<Integer>> index = new HashMap<>();

    AtomicInteger documentIdGenerate = new AtomicInteger();

    public void addDocument(String content){
        //validate input
        if(content == null || content.isEmpty()){
            return;
        }

        //string splti and toLowercase
        String [] words = content.toLowerCase().split("[^a-zA-Z]+");

        //loop through use computeIfAbsent and increment and Get
        for(String word: words){
            int docId = documentIdGenerate.incrementAndGet();
            index.computeIfAbsent(word, k -> new TreeSet<>()).add(docId);
        }

    }
}
