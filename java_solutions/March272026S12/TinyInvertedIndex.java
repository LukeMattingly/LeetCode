package March272026S12;

import java.util.*;

//Map each word to set of doc ids
// hashmap "String" -> Set (so it's sorted) for docIds

public class TinyInvertedIndex {

    Map<String, Set<Integer>> invertedIndex = new HashMap<>();

    public void addDocument(int docId, String content){
        if(content == null || content.isEmpty()){
            return;
        }
        //split content into words
        String[] words = content.split("\\P{Alpha}+");
        for(String word: words){
            invertedIndex.computeIfAbsent(word.toLowerCase(), k-> new TreeSet<>()).add(docId);
        }
    }
    public List<Integer> search(String term){
        if(term == null || term.isEmpty()){
            return Collections.emptyList();
        }

        String normalized = term.toLowerCase();
        if(invertedIndex.containsKey(normalized)){
            Set<Integer> docIds = invertedIndex.get(normalized);
            return new ArrayList<>(docIds);

        }else{
            return Collections.emptyList();
        }
    }

}
