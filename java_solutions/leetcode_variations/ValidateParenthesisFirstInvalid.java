package leetcode_variations;

import java.util.Stack;

/*
Return the first invalid position

Variation:
Instead of returning true/false, return the index of the first character that makes the string invalid, or -1 if valid.

*/


public class ValidateParenthesisFirstInvalid {
        public int isValid(String s) {
            Stack<Integer> stack = new Stack<>();

            for(int i=0;i<s.length();i++){
                char c = s.charAt(i);
                if(c=='('){
                    stack.push(i);
                }else if( c== ')'){
                    if(stack.isEmpty()){
                        return i;
                    }
                    stack.pop();
                }
            }
            if(stack.isEmpty()){
                return -1;
            }

            int indexOfFirstUnmatchedopen = -1;
            while(!stack.isEmpty()){
                indexOfFirstUnmatchedopen = stack.pop();
            }
            return indexOfFirstUnmatchedopen;

        }

}
