package streams;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ConvertListofStringsCase {
        List<String> colors = Arrays.asList("RED", "grEEn", "white", "Orange", "pink");
        List<String> upperColors = colors.stream().map(k-> k.toUpperCase()).toList();
        List<String> lowerColors = colors.stream().map(k->k.toLowerCase()).toList();

        //.toList creates unmodifiable list
        //collect(Collectors.toList()); allows modification, older style

        //Modifiable list, alternative mapping option
        List<String> upperColorsAlt = colors.stream().map(String::toUpperCase).collect(Collectors.toList());
        List<String> lowerColorsAlt = colors.stream().map(String::toLowerCase).collect(Collectors.toList());
}
