package streams;

import java.util.Arrays;
import java.util.List;


//use filter to only apply operation to certain values
//use mapTo Int to convert to an IntStream
//Sum to finish
public class SumEvenAndOdd {
       List < Integer > numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

       Integer evenSum = numbers.stream().filter(k->k%2==0).mapToInt(Integer::intValue).sum();

       Integer oddSum = numbers.stream().filter(k->k%2!=0).mapToInt(Integer::intValue).sum();
}
