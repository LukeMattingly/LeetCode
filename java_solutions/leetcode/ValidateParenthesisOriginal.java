package leetcode;

import java.util.*;

public class ValidateParenthesisOriginal {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closeToOpenMap = new HashMap<>();
        closeToOpenMap.put(')','(');
        closeToOpenMap.put(']','[');
        closeToOpenMap.put('}', '{');

        char[] chars = s.toCharArray();
        for(char c: chars){
            // if the character is a closing one check to see if we can pop
            if(closeToOpenMap.containsKey(c)){
                if(stack.isEmpty() || stack.peek() != (closeToOpenMap.get(c))){
                    return false;
                }else{
                    stack.pop();
                }
            }else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
