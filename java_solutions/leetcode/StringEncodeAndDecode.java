package leetcode;

import java.util.ArrayList;
import java.util.List;

public class StringEncodeAndDecode {
    public String encode(List<String> strs) {
         StringBuilder encoded = new StringBuilder();
         for(String str: strs){
              encoded.append(str.length());
              encoded.append('#');
              encoded.append(str);
         }
        return encoded.toString();
    }

    public List<String> decode(String str) {
          List<String> result = new ArrayList<>();
          char[] chars = str.toCharArray();
          for(int i=0; i<chars.length;i++){
          StringBuilder digit = new StringBuilder();
           while(chars[i] != '#'){
                digit.append(chars[i]);
                i++;
          }
          int length = Integer.parseInt(digit.toString());
           // skip # 
          i++;
            StringBuilder newStr = new StringBuilder();
            for(int j = i; j<i+length;j++){
                   newStr.append(chars[j]);
            }
            result.add(newStr.toString());
            i = i+length-1;
          }
          return result;
    }
}
