package leetcode_variations;

public class ValidateParenthesisOptimalSpace {
    public boolean isValid(String s) {
        int balance = 0;

        for(int i=0; i< s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){
                balance++;
            }else if (c == ')'){
                balance--;
                if(balance <=0){
                    return false;
                }
            }
        }
        return balance == 0;
    }
}
