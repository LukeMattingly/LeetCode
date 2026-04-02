package March272026S12;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class TinyInvertedIndexEvolved {
        Map<String, Set<Integer>> invertedIndex = new HashMap<>();
        Map<Integer, Document> metaDataStore = new HashMap<>();
        Map<Long, Set<Integer>> timeStampIndex = new TreeMap<>();

    record Document(int id, String category, long timestamp) {}

    public void addDocument(int docId, String content, String category, long timestamp) {        
        if(content == null || content.isEmpty()) return;

        metaDataStore.put(docId, new Document(docId, category, timestamp));

        timeStampIndex.computeIfAbsent(timestamp, k-> new HashSet<>()).add(docId);

        //split content into words
        String[] words = content.split("\\P{Alpha}+");
        for(String word: words){
            invertedIndex.computeIfAbsent(word.toLowerCase(), k-> new TreeSet<>()).add(docId);
        }
    }

    public List<Integer> search(String term, String category, long currentTimeMillis) {
        if(term == null || term.isEmpty()){
            return Collections.emptyList();
        }

        long tenMinutesAgo = currentTimeMillis - (10 * 60 * 1000);

        String normalized = term.toLowerCase();
        if(invertedIndex.containsKey(normalized)){
            Set<Integer> docIds = invertedIndex.get(normalized);

            List<Integer> results = new ArrayList<>();

            for(Integer docId: docIds){
                Document metadata = metaDataStore.get(docId);
                if(metadata !=null && metadata.category().equals(category) && metadata.timestamp() >= tenMinutesAgo){
                    results.add(docId);
                }
            }

            return results;

        }else{
            return Collections.emptyList();
        }
    }
}
