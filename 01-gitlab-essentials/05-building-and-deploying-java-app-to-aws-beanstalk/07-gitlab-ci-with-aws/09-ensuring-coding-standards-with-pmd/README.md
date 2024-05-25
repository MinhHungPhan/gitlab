# Ensuring Coding Standards with PMD

## Table of Contents

- [Introduction](#introduction)
- [What is PMD?](#what-is-pmd)
- [Setting Up PMD](#setting-up-pmd)
- [Running PMD](#running-pmd)
- [Using PMD in a Java Project](#using-pmd-in-a-java-project)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Programming efficiency and maintenance are heavily influenced by consistent code styles and adherence to industry best practices. PMD is a powerful static code analysis tool used primarily for Java projects, helping developers identify unused variables, problematic code blocks, and enforce generally accepted best practices. This document serves as a comprehensive guide to integrating and utilizing PMD in your Java projects, making your code cleaner and more maintainable. We will cover the basic setup, execution, and customization of PMD rules to fit your coding standards.

## What is PMD?

PMD stands for Programming Mistake Detector, a tool that performs static code analysis to check Java source code against a set of predefined rules. Static analysis involves examining the code without actually executing it, which differs from dynamic analysis that requires running the program. PMD helps ensure that code adheres to a set of standards which promotes code readability, maintainability, and error reduction.

## Setting Up PMD

PMD is integrated into Java projects through build automation tools like Maven and Gradle. Here's how you can set it up using Gradle:

1. **Add PMD Plugin to `build.gradle`:**

```gradle
plugins {
	id 'org.springframework.boot' version '2.2.4.RELEASE'
	id 'io.spring.dependency-management' version '1.0.9.RELEASE'
	id 'java'
	id 'pmd'
}
```

2. **Configure PMD plugin settings:**

```gradle
pmd {
	sourceSets = [] // this disables pmd from the build & check tasks
	ruleSetFiles = files("pmd-ruleset.xml")
	ruleSets = []
}
```

3. **Create a `pmd-ruleset.xml` file in the project root:**
   
- This file will contain all the custom rules and configurations for PMD.

- For example:

```xml
<?xml version="1.0"?>

<ruleset name="Custom Rules"
         xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0 https://pmd.sourceforge.io/ruleset_2_0_0.xsd">

    <description>
        My custom rules
    </description>


    <rule ref="category/java/errorprone.xml/BeanMembersShouldSerialize" >
        <properties>
            <property name="ignoredAnnotations" value="Autowired|GetMapping|Mock|InjectMocks" />
            <property name="prefix" value="" />
        </properties>
    </rule>

</ruleset>
```

## Running PMD

To execute PMD through the terminal using Gradle, use the following commands:

- **PMD for main source code:**

```bash
./gradlew pmdMain
```

- **PMD for test code:**

```bash
./gradlew pmdTest
```

These commands will generate reports in XML format that provide details on any code issues or rule violations.

## Using PMD in a Java Project

This practical exercise will guide you through the process of using PMD to analyze and improve the code quality of a Java application. We will modify the code to introduce a common best practices violation and then use PMD to detect this issue.

### Step 1: Set Up Your Java Project

To effectively use PMD for analyzing and improving code quality, start by setting up a Java project with Gradle. Below is an example of a simple Spring Boot application configured for this purpose. We will modify this application by introducing a `System.out.println` statement, which is commonly used for debugging but is generally advised against in production code for performance reasons.

#### Original `CarsApplication.java`
Here is the initial version of the `CarsApplication.java` file in a typical Spring Boot project:

```java
@SpringBootApplication
public class CarsApplication {

    public static void main(String[] args) {
        SpringApplication.run(CarsApplication.class, args);
    }

}
```

#### Modified `CarsApplication.java` for PMD Testing
To test the PMD rule setup, add a `System.out.println` statement to the `main` method. This modification serves as a deliberate introduction of a best practices violation to demonstrate PMD's capability to detect it:

```java
@SpringBootApplication
public class CarsApplication {

    public static void main(String[] args) {
        System.out.println("Entering test"); // This line is added for PMD testing
        SpringApplication.run(CarsApplication.class, args);
    }

}
```

This updated application now includes a print statement that PMD, with the appropriate rule configuration, will identify as a breach of best practices. This setup allows you to verify that PMD is correctly integrated and configured in your development environment.

### Step 2: Configure PMD Rules

Proper configuration of PMD rules is crucial to ensure that the tool effectively identifies issues according to your project's specific guidelines. Here is a step-by-step guide to setting up your PMD rules:

#### 1. Modify the `pmd-ruleset.xml` File

Update the `pmd-ruleset.xml` file in your project's root directory to include custom rules. Here’s an example configuration that incorporates rules for error-prone code and best practices:

```xml
<?xml version="1.0"?>
<ruleset name="Custom Rules"
         xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0 https://pmd.sourceforge.io/ruleset_2_0_0.xsd">
    <description>
        My custom rules to enhance code quality and enforce best practices.
    </description>
    <rule ref="category/java/errorprone.xml/BeanMembersShouldSerialize">
        <properties>
            <property name="ignoredAnnotations" value="Autowired|GetMapping|Mock|InjectMocks" />
            <property name="prefix" value="" />
        </properties>
    </rule>
</ruleset>
```

#### 2. Extend the Rule Set

To further enhance the rule set, add additional rules as necessary. For instance, to prevent the use of `System.out.println` in production code, add the following rule:

```xml
<rule ref="category/java/bestpractices.xml/SystemPrintln" />
```

Incorporating this rule ensures that PMD checks for instances of `System.out.println`, helping you avoid common debugging practices in production environments.

#### 3. Final `pmd-ruleset.xml` Configuration

With the additional rule, your final `pmd-ruleset.xml` should look like this:

```xml
<?xml version="1.0"?>
<ruleset name="Custom Rules"
         xmlns="http://pmd.sourceforge.net/ruleset/2.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://pmd.sourceforge.net/ruleset/2.0.0 https://pmd.sourceforge.io/ruleset_2_0_0.xsd">
    <description>
        My custom rules to enhance code quality and enforce best practices.
    </description>

    <rule ref="category/java/errorprone.xml/BeanMembersShouldSerialize">
        <properties>
            <property name="ignoredAnnotations" value="Autowired|GetMapping|Mock|InjectMocks" />
            <property name="prefix" value="" />
        </properties>
    </rule>

    <rule ref="category/java/bestpractices.xml/SystemPrintln" />
</ruleset>
```

This configuration not only enforces good coding practices but also customizes the analysis to align with specific needs of your Java project, ensuring high-quality, maintainable code.

### Step 3: Run PMD Analysis

After configuring the PMD rules as described in Step 2, you are now ready to run the analysis to identify violations of these rules in your Java code.

Run PMD using the Gradle wrapper commands:

```bash
./gradlew pmdMain pmdTest
```

#### Expected Output

Given the rules specified in the `pmd-ruleset.xml` from Step 2, including the rule against using `System.out.println`, the output from PMD will specifically highlight if such a violation is found:

```plaintext
> Task :pmdMain FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':pmdMain'.
> 1 PMD rule violations were found. See the report at: build/reports/pmd/main.html

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 1s
3 actionable tasks: 2 executed, 1 up-to-date
```

#### Explanation of the output message

1. **Rule Configuration:** In Step 2, the `SystemPrintln` rule was added to your `pmd-ruleset.xml`. This rule is designed to detect and report instances where `System.out.println` is used in the code.

2. **Running PMD Analysis:** When you execute PMD as outlined in Step 3, it scans the code for any matches to the rules defined in the `pmd-ruleset.xml`. If the newly added `System.println` exists in the code, PMD identifies it as a violation.

3. **Reviewing the Report:** The path `build/reports/pmd/main.html` provides a detailed report that lists each violation, helping developers to easily locate and understand the issues PMD found. The inclusion of this specific rule in the PMD configuration directly influences what appears in this report.

## Best Practices

- **Regularly Update Rules:** As best practices evolve, update your `pmd-ruleset.xml` to reflect these changes.
- **Integrate with CI/CD:** Automate PMD checks in your continuous integration/continuous deployment pipeline to catch issues early.
- **Review PMD Reports Regularly:** Regular reviews of PMD output help maintain code quality and adherence to standards.

## Key Takeaways

- PMD is a valuable tool for maintaining high code quality in Java projects.
- Setting up and customizing PMD can significantly reduce the occurrence of common coding errors.
- Regular use of PMD encourages adherence to coding standards and best practices.

## Conclusion

PMD is an essential tool for any team looking to enforce coding standards and best practices within their Java projects. By integrating PMD into your development workflow, you can ensure higher code quality, easier maintenance, and better performance. We encourage all developers to leverage PMD to its fullest potential to maintain a healthy codebase.

## References

- [PMD Official Website](https://pmd.github.io/)
- [PMD Making rulesets](https://pmd.github.io/pmd/pmd_userdocs_making_rulesets.html)
- [PMD Rule Sets](https://docs.pmd-code.org/latest/pmd_rules_java_bestpractices.html#systemprintln)