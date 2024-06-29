# Introduction to Unit Testing in CI Pipeline

## Table of Contents

- [What is a Unit Test?](#what-is-a-unit-test)
- [Understanding the Testing Pyramid](#understanding-the-testing-pyramid)
- [Service Introduction: FleetStatisticsService](#service-introduction-fleetstatisticsservice)
- [Unit Testing Examples for FleetStatisticsService](#unit-testing-examples-for-fleetstatisticsservice)
- [Executing Unit Tests](#executing-unit-tests)
- [Best Practices for Unit Testing](#best-practices-for-unit-testing)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to the "Introduction to Unit Testing in CI Pipeline" guide! This document is designed to help newcomers understand the fundamental concepts of unit testing within Continuous Integration (CI) pipelines. Unit testing is a critical stage in software development that ensures individual units of code function as intended. This guide outlines what unit tests are, why they are important, how they fit into the CI pipeline, and provides practical examples to illustrate these concepts. By the end of this guide, you will have a solid understanding of unit testing basics and how to implement them effectively in your CI processes.

## What is a Unit Test?

A unit test is designed to verify the smallest testable parts of an application, usually individual functions or methods in classes. These tests are quick to run, providing immediate feedback on the functionality of your code. Unlike integration or system tests, unit tests do not require the entire application to be up and running, thus reducing the complexity and cost associated with the test environment.

## Understanding the Testing Pyramid

The testing pyramid is a concept used to describe the optimal distribution of different types of automated tests in software development. At the base of this pyramid are unit tests, which are abundant due to their speed and low cost. As we move up the pyramid, tests become fewer and more complex, encompassing integration and UI tests. This structure emphasizes the importance of unit tests in providing a solid foundation for higher-level tests.

## Service Introduction: FleetStatisticsService

Before diving into unit tests, it's important to understand the service being tested. The `FleetStatisticsService` class is a core component of our application, tasked with calculating the average age of a fleet of cars. Below is a brief overview of the service:

**Java Service Code:**

```java
@Service
public class FleetStatisticsService {
    @SuppressWarnings("PMD.BeanMembersShouldSerialize")
    @Autowired
    private CarsRepository repository;

    public FleetAge getAverageFleetAge() {
        List<Car> cars = repository.findAll();  // Retrieves all cars from the repository

        OptionalDouble average = cars
            .stream()  // Streams the list of cars
            .mapToDouble(a -> (2020 - a.getBuild()))  // Converts each car's build year into its age
            .average();  // Calculates the average age

        return new FleetAge(cars.size(), average.getAsDouble());  // Returns the average age and count of cars
    }
}
```

This service utilizes Spring's `@Service` annotation to denote a business service facade and `@Autowired` to inject the `CarsRepository` dependency. It calculates the average age of the fleet by subtracting the build year from a fixed year (2020), then computes the average. This method will be the target of our unit tests to ensure its accuracy and reliability.

## Unit Testing Examples for FleetStatisticsService

Here's an example to demonstrate how unit testing works:

**Existing Java Code:**

```java
@Test
public void twoCars() {
    List<Car> myList = new ArrayList<>();
    myList.add(new Car(1L, "Dacia", "Duster", 2000));
    myList.add(new Car(2L, "Dacia", "Logan", 2010));

    when(repo.findAll()).thenReturn(myList);

    assertEquals(service.getAverageFleetAge().getAge(), 15, 0);
}
```

**Modified Code to Introduce a Fail:**

```java
@Test
public void twoCars() {
    List<Car> myList = new ArrayList<>();
    myList.add(new Car(1L, "Dacia", "Duster", 2000));
    myList.add(new Car(2L, "Dacia", "Logan", 2010));

    when(repo.findAll()).thenReturn(myList);

    assertEquals(service.getAverageFleetAge().getAge(), 16, 0); // This assertion is intentionally wrong to simulate a test failure.
}
```

This simple example illustrates how a unit test checks the functionality of a method by asserting expected outcomes.

## Executing Unit Tests

To ensure that the `FleetStatisticsService` functions as expected, we can execute unit tests in two main ways:

### Using Gradle from the IDE Console

- To run unit tests directly from the Integrated Development Environment (IDE), you can use the built-in Gradle support. Navigate to the Gradle tasks panel and locate the `test` task under the `/tasks/verification/test` directory. 

- Running this task will execute all unit tests and display results directly in your IDE console. This method provides an interactive way to run tests and instantly view the output, which is ideal for development and debugging.

### Using Gradle Wrapper in GitLab CI

- For continuous integration, the Gradle Wrapper is an ideal choice. It ensures that everyone, including the CI server, uses the same Gradle version to execute tests, maintaining consistency across environments. 

- Here's how you can run the tests using Gradle Wrapper:

```bash
./gradlew test
```

- This command will execute all unit tests in the project and provide a detailed report of the test results in the console.

## Best Practices for Unit Testing

- **Write Clear and Concise Tests**: Each test should focus on one specific functionality.
- **Maintain Independence**: Tests should not rely on each other's success to pass.
- **Use Mocks and Stubs**: These tools help isolate the unit of code being tested, ensuring that tests are not affected by external dependencies.
- **Run Tests Frequently**: Integrate tests into your CI pipeline to run automatically with every code change.
- **Keep Tests Fast**: Optimize test execution to maintain a quick feedback loop.

## Key Takeaways

- Unit tests are essential for ensuring individual components of an application function correctly.
- They are fast, inexpensive, and critical for maintaining code quality in a CI pipeline.
- A robust testing strategy begins with a solid foundation of unit tests.

## Conclusion

Unit testing is a powerful tool in software development, especially within CI pipelines, where it ensures that every component functions correctly before integration. By embracing the best practices outlined in this guide and understanding the role of unit tests, developers can improve the quality and reliability of their software.

## References

- [What is Unit Testing?](https://aws.amazon.com/what-is/unit-testing/#:~:text=Unit%20testing%20is%20the%20process,test%20for%20each%20code%20unit.)
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)