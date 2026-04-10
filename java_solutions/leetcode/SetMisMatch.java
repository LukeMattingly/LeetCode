public class SetMisMatch {

    public int[] findErrorNums(int[] nums) {
        int [] buckets = new int[nums.length +1];

        int missing = -1;
        int duplicate = -1;

        for(int i=0; i< nums.length; i++){
            buckets[nums[i]]++;
        }

        for(int i =1; i< buckets.length; i++){
            if(buckets[i] == 2){
                duplicate = i;
            }
            if(buckets[i] == 0){
                missing = i;
            }
        }
        return new int[]{duplicate, missing};
    }
}