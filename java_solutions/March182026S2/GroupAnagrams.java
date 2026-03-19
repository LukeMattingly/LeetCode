package March182026S2;

import java.util.*;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        // create a map of sortedStr as index as list of values as the value
        //act -> [act, cat]
        Map<String, List<String>> map = new HashMap<>();

        for(String str : strs){
            char [] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            map.computeIfAbsent(sortedStr,k-> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
