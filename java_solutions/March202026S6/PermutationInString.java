package March202026S6;

import java.util.*;

public class PermutationInString {
    //freqMap for the window
    //s1 will be the freq map
    //loop through s2 until we find a value in the map
    //once we find a value in the map freqMap -=1 to teh value 
    // two maps, one is truth other is temp for removing elements
    // if the key goes to 0, then delete it. 
    // if the map has no values, then we've foudn them all

    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()) return false;

        Map<Character, Integer> freqMap = new HashMap<>();

        char [] s1chars = s1.toCharArray();
        for(char c : s1chars){
            freqMap.put(c,freqMap.getOrDefault(c, 0)+1);
        }

        Map<Character, Integer> tempFreqMap = new HashMap<>(freqMap);
        
        char [] s2chars = s2.toCharArray();
        for(char c2 : s2chars){
            if(tempFreqMap.containsKey(c2)){
                //decrement the current value
                int currentVal = tempFreqMap.get(c2);
                if(currentVal >1){
                    currentVal--;
                    tempFreqMap.put(c2, currentVal);
                }else{
                    tempFreqMap.remove(c2);
                    if(tempFreqMap.values().isEmpty()){
                        return true;
                    }
                }
            }else{
                 tempFreqMap = new HashMap<>(freqMap);
            }
        }
        return false;
    }
}
