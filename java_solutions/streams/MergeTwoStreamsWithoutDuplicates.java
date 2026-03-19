package streams;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class MergeTwoStreamsWithoutDuplicates {
    List<String> streamOne = Arrays.asList("apple", "banana", "cherry");
    List<String> streamTwo = Arrays.asList("banana", "cherry", "date");

    List<String> mergedStream = Stream.concat(streamOne.stream(), streamTwo.stream())
        .distinct()
        .toList();
        
    class Person{

    String name;
    Integer age;
    
    Person(String name, Integer age){
        this.name = name;
        this.age = age;
    }

    List<Person> listOne = Arrays.asList(
            new Person("John", 30),
            new Person("Jane", 25)
            );
    List<Person> listTwo = Arrays.asList(
        new Person("Jane", 25),
        new Person("Jack", 28)
    );

    List<Person> mergedLists = Stream.concat(listOne.stream(), listTwo.stream()).distinct().toList();
    }
}
