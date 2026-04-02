package leetcode_variations;

public class BinarySearchLong {
    

    private static boolean binarySearch(long [] arr, long target){
        int left = 0;
        int right = arr.length-1;

        while(left <=right){

            int mid = left + (right -left) / 2;
            long midValue = arr[mid];

            if(target == midValue){
                return true;
            }else if(target > midValue){
                left += mid+1;
            }else{
                right -=mid-1;
            }
        }
        return false;
    }
}
