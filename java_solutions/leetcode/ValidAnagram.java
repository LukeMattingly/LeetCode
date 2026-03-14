package leetcode;
import java.util.*;

public class ValidAnagram {
        public boolean isAnagram(String s, String t) {
            Map<Character, Integer> sMap = new HashMap<>();
            Map<Character, Integer> tMap = new HashMap<>();

            for(int i=0; i< s.length(); i++){
                sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0)+1);
                tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0)+1 );
            }

            return sMap.equals(tMap);
    }
}
