package March192026S4;

import java.util.*;

public class LongestSubstringWithoutRepeatingCharacters {
    //window
    //set for hte elements in the window, as we move it, remove the previous elements from the set
    //need to track longest
    
    //aab 
    // l=0 a
    // r=1 a
    //window [a]
    public int lengthOfLongestSubstring(String s) {
        //base cases

        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;

        Set<Character> window = new HashSet<>();
        int l = 0;
        int r = 1;

        char[] chars = s.toCharArray();
        window.add(chars[l]);
        int maxLength = 1;

        while (r < s.length()) {
            if (!window.contains(chars[r])) {
                window.add(chars[r]);
                maxLength = Math.max(maxLength,r - l + 1);
                r++;
            } else {
                window.remove(chars[l]);
                l++;
            }
        }
        return maxLength;
    }
}
