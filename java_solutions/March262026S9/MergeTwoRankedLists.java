package March262026S9;

import java.util.*;

public class MergeTwoRankedLists {
    //need a set or a map to store if we've seen a productId before. 
    //need two pointers one per list
    

    class Result {
        String id;
        int rank; // smaller rank means better
    }

    public List<String> mergeRankedLists(
        List<Result> list1,
        List<Result> list2,
        int k
    ){
        Set<String> charactersSeen = new HashSet<>();

        List<String> result = new ArrayList<>();

        int list1Pointer = 0;
        int list2Pointer = 0;

        while(result.size() < k && list1Pointer < list1.size() || list2Pointer < list2.size()){
            Result next;

            if(list1Pointer < list1.size() && list2Pointer < list2.size()){
                if(list1.get(list1Pointer).rank <= list2.get(list2Pointer).rank){
                    next = list1.get(list1Pointer);
                    list1Pointer++;
                }else{
                    next = list2.get(list2Pointer);
                    list2Pointer++;
                }
            }else if(list1Pointer< list1.size()){
                next = list1.get(list1Pointer);
                list1Pointer++;
            }else{
                next = list2.get(list2Pointer);
                list2Pointer++;
            }


            if(!charactersSeen.contains(next.id)){
                result.add(next.id);
                charactersSeen.add(next.id);
            }
        }

        return result;
        // i need to lexigraphically compare ids
        // if the same ids, then list 1 wins
        // i need lower rank to win. 
        // i need to iterate through both lists, but only at one item at a time, and then compare both at each step. 


    }
}
