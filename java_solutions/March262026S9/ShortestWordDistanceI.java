package March262026S9;

public class ShortestWordDistanceI {
    //minDistance var
    //first instance of word1
    //first instance of word2. 
    // if we haven't seen 2nd word but we have one word, and we find a 2nd instance of the other word, then update it
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        
        int minDistance =wordsDict.length;
        //will track both index and if we have found the word
        int w1Index = -1;
        int w2Index = -1;
        for(int i=0; i< wordsDict.length; i++){
            if(wordsDict[i].equals(word1)){
                if(w2Index != -1){
                    minDistance = Math.min(minDistance, i - w2Index);
                }
                w1Index = i;
            }else if(wordsDict[i].equals(word2)){
                if(w1Index != -1){
                    minDistance = Math.min(minDistance, i - w1Index);
                }
                w2Index = i;
            }
        }
        return minDistance;
    }
}

//minD = 2
//w1 = 4
//w2= 3
//4-3 = 1