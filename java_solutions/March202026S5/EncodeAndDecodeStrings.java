package March202026S5;

import java.util.ArrayList;
import java.util.List;

public class EncodeAndDecodeStrings {
    //need encoding format Number#Word 5#hello10Worldlessness 
    //loop strings, get sizes, string builder
    public String encode(List<String> strs) {
        StringBuilder encodedBuilder = new StringBuilder();
        for(String str:strs){
            encodedBuilder.append(str.length());
            encodedBuilder.append('#');
            encodedBuilder.append(str);
        }
        return encodedBuilder.toString();
    }

    //decode  Number#Word 5#hello10Worldlessness 
    // could have multiple digits, so need to loop while/until # is hit, then only advance k spaces
    //need to conver number to a Int.Parse(str)
    public List<String> decode(String str) {
        char [] chars = str.toCharArray();
        List<String> result = new ArrayList<>();

        int i =0;
        while(i<str.length()){
            //decode digit
            StringBuilder digitStr = new StringBuilder();
            while(chars[i] != '#'){
                digitStr.append(chars[i]);
                i++;
            }
            int digit = Integer.parseInt(digitStr.toString());

            i++; // skip the #

            //grab the word
            StringBuilder decodedWord = new StringBuilder();
            for(int j =0; j<digit; j++){
                decodedWord.append(chars[i]);
                i++;
            }
            result.add(decodedWord.toString());
        }
        return result;

    }
}
