package leetcode_variations;

public class ValidateParenthesisQuoted {
    boolean isBalancedOutsideQuotes(String text) {
        int parenOpenClosed = 0;
        boolean inQuotes = false;

        for(int i=0; i<text.length(); i++){
            char c = text.charAt(i);

            if(c == '"' && (i==0|| text.charAt(i-1) != '\\')){
                inQuotes =!inQuotes;
            }else if(!inQuotes){
                if(c=='('){
                    parenOpenClosed ++;
                }else if(c == ')'){
                    parenOpenClosed--;
                    if(parenOpenClosed<0){
                        return false;
                    }
                }
            }
        }
        return !inQuotes && parenOpenClosed == 0;
    }
}
