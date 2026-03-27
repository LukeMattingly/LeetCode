import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

public class SimpleSearchIndex{
    // store docId -> document
    private final Map<Integer, String> documents = new ConcurrentHashMap<>();

    // token -> [doc1, doc2] set of docIds
    private final Map<String, Set<Integer>> invertedIndex = new ConcurrentHashMap<>();

    //Id generator thread safe
    private final AtomicInteger docIdGenerator = new AtomicInteger();


    // add new docId and document to documents map, and update the inverted index
    public int addDocument(String text){
        if(text == null || text.trim().isEmpty()) return -1;

        int docId = docIdGenerator.incrementAndGet();

        documents.put(docId, text);

        //generate tokens
        Set<String> tokens = tokenize(text);

        for(String token: tokens){
            //computeIfAbsent with a thread-safe Set
            invertedIndex.computeIfAbsent(token, k-> ConcurrentHashMap.newKeySet()).add(docId);
        }
        return docId;
    }

    public Set<String> tokenize(String text){
        Set<String> tokens = new HashSet<>();

        String[] words = text.toLowerCase().replaceAll("[^a-zA-Z\\d\\s:]","" ).split("\\s+");

        for(String word: words){
            if(!word.isEmpty())
                tokens.add(word);
        }
        return tokens;
    }

    public List<String> search(String query){
        if(query == null|| query.trim().isEmpty()) return Collections.emptyList();

        List<String> results;

        return results;
    }
}
