package March182026S1;

import java.util.*;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        //if not the same length can't be anagrams
        if(s.length()!= t.length()){
            return false;
        }

        Map<Character, Integer> sFreqMap = new HashMap<>();
        Map<Character, Integer> tFreqMap = new HashMap<>();

        for(int i=0; i< s.length(); i++){
            char [] sChars = s.toCharArray();
            char [] tChars = t.toCharArray();
            sFreqMap.put(sChars[i], sFreqMap.getOrDefault(sChars[i], 0)+1);
            tFreqMap.put(tChars[i], tFreqMap.getOrDefault(tChars[i], 0)+1);
        }

        return sFreqMap.equals(tFreqMap);
    }
}
