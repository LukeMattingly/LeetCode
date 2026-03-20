package March192026S4;

import java.util.*;

public class ShortestWordDistanceI {
        // makes 1
        // coding 3 (found both can compute 2)
        // makes 4 (found both can compute 1)
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        int shortestDistance = Integer.MAX_VALUE; //max length of wordDict
        boolean foundWord1 = false;
        boolean foundWord2 = false;
        
        Map<String, Integer> distanceMap = new HashMap<>();

        for(int i=0; i< wordsDict.length; i++){
            if(wordsDict[i].equals(word1)){
                if(foundWord2){
                    //calculate distance
                    int w2Index = distanceMap.get(word2);
                    
                    shortestDistance = Math.min(shortestDistance, i - w2Index);
                }
                distanceMap.put(word1, i);
                foundWord1 = true;
            }else if(wordsDict[i].equals(word2)){
                if(foundWord1){
                    //calculate distance
                    int w1Index = distanceMap.get(word1);
                    
                    shortestDistance = Math.min(shortestDistance, i - w1Index);
                }
                distanceMap.put(word2, i);
                foundWord2 = true;
            }
        }
        return shortestDistance;
    }
}
