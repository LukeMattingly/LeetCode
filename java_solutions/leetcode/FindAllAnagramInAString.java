package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FindAllAnagramInAString {
    public List<Integer> findAnagrams(String s, String p) {
    List<Integer> result = new ArrayList<>();
    if (s.length() < p.length()) return result;

    Map<Character, Integer> pCount = new HashMap<>();
    Map<Character, Integer> windowCount = new HashMap<>();

    // Build frequency map for p
    for (char c : p.toCharArray()) {
        pCount.put(c, pCount.getOrDefault(c, 0) + 1);
    }

    int windowSize = p.length();

    // Build first window
    for (int i = 0; i < windowSize; i++) {
        char c = s.charAt(i);
        windowCount.put(c, windowCount.getOrDefault(c, 0) + 1);
    }

    // Check first window
    if (windowCount.equals(pCount)) {
        result.add(0);
    }

    // Slide the window
    for (int right = windowSize; right < s.length(); right++) {
        char addChar = s.charAt(right);
        char removeChar = s.charAt(right - windowSize);

        // Add new char
        windowCount.put(addChar, windowCount.getOrDefault(addChar, 0) + 1);

        // Remove old char
        windowCount.put(removeChar, windowCount.get(removeChar) - 1);
        if (windowCount.get(removeChar) == 0) {
            windowCount.remove(removeChar);
        }

        // Compare maps
        if (windowCount.equals(pCount)) {
            result.add(right - windowSize + 1);
        }
    }

    return result;
}
}
