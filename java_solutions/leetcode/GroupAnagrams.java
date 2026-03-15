package leetcode;
import java.util.*;

public class GroupAnagrams {

     public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> anagramMap = new HashMap<>();

        for(String str: strs){
            char [] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            anagramMap.computeIfAbsent(sortedStr, k->new ArrayList<String>()).add(str);
        }

        return new ArrayList<>(anagramMap.values());

     }
}
