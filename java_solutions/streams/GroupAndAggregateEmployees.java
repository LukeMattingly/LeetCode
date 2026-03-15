package streams;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;


public class GroupAndAggregateEmployees {
    // Write a method that returns a Map<String, Double> where:
    // the key is the department name
    // the value is the average salary of employees in that department

    public class Employee {
        String name;
        String department;
        int salary;
        int yearsOfExperience;

        public Employee(String name, String department, int salary, int yearsOfExperience){
            this.name = name;
            this.department = department;
            this.salary = salary;
            this.yearsOfExperience = yearsOfExperience;
        }
    }


    List<Employee> employees = Arrays.asList(
        new Employee("Alice", "Engineering", 120000, 5),
        new Employee("Bob", "Engineering", 135000, 8),
        new Employee("Charlie", "HR", 80000, 6),
        new Employee("Diana", "HR", 85000, 4),
        new Employee("Eve", "Sales", 95000, 7),
        new Employee("Frank", "Sales", 105000, 10)
    );
    
    Map<String, Double> result = employees.stream().collect(Collectors.groupingBy(k->k.department, Collectors.averagingInt(s->s.salary)));

    //Then write a second version that returns the highest-paid employee name per department as:
    //where the key is the department and the value is the employee name.

    Map<String, String> highestPaid = employees.stream()
        .sorted((a,b)-> Integer.compare(b.salary, a.salary))
        .collect(Collectors.toMap(
            emp->emp.department,
            emp->emp.name));

    Map<String, String> highestPaid2 = employees.stream()
    .collect(Collectors.groupingBy(
        emp -> emp.department,
        Collectors.collectingAndThen(
            Collectors.maxBy(Comparator.comparingInt(emp -> emp.salary)),
            opt -> opt.get().name
        )
    ));
}
