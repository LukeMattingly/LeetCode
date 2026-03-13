import java.util.*;

public class GroupAnagrams {
        public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String,List<String>> anagramMap = new HashMap<>();

        for(int i=0;i< strs.length; i++){
            char [] strsCharArray = strs[i].toCharArray();
            Arrays.sort(strsCharArray);
            String key = new String(strsCharArray);
            anagramMap.computeIfAbsent(key, k-> new ArrayList<>()).add(strs[i]);
        }
        
        for(List<String> anagram: anagramMap.values()){
            result.add(anagram);
        }
        return result;
    }
}
