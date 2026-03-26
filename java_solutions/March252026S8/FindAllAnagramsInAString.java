package March252026S8;

import java.util.*;

public class FindAllAnagramsInAString {

    //P anagram in S. (returning starting indicies)
    // sliding window, use a freq map. store starting index when you find first match, 
    // if it isn't a full match, then remove it
    //can have multiple overlapping, so start at first index, check, then move to 2nd index check. O(n^2)
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    Map<Character, Integer> freqMap = new HashMap<>();

    char[] pChars = p.toCharArray();
    for (char c : pChars) {
        freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
    }

    char[] sChars = s.toCharArray();

    for (int i = 0; i < s.length(); i++) {
        Map<Character, Integer> newlyConstructedMap = new HashMap<>();

        for (int j = i; j < s.length(); j++) {
            // window must be exactly p.length()
            if (j - i + 1 > p.length()) {
                break;
            }

            char currentCharacter = sChars[j];

            // invalid char for this anagram window
            if (!freqMap.containsKey(currentCharacter)) {
                break;
            }

            newlyConstructedMap.put(
                currentCharacter,
                newlyConstructedMap.getOrDefault(currentCharacter, 0) + 1
            );

            // too many of this char
            if (newlyConstructedMap.get(currentCharacter) > freqMap.get(currentCharacter)) {
                break;
            }

            // only compare when window size matches p.length()
            if (j - i + 1 == p.length() && freqMap.equals(newlyConstructedMap)) {
                result.add(i);
                break;
            }
        }
    }

    return result;
}
//i=2
//j=2
//freqMap {a :1, b:1} 
// currentChar = a
//startingIndex = 2
// newlyConstructedMap {}