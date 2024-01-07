# Adding a Smoke Test

Welcome to the documentation for adding a smoke test to your project. This README aims to guide you through the process of setting up a basic smoke test, ensuring that your application is correctly built and starts as expected. Whether you are a beginner or an experienced developer, this document will help you understand the importance of smoke testing and how to implement it in your workflow.

## Table of Contents

- [Introduction](#introduction)
- [Usage and Examples](#usage-and-examples)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Smoke testing is a preliminary step in software development that ensures the basic functionality of an application. It's like checking if a car starts before testing how well it drives. This README provides a step-by-step guide to implementing a basic smoke test in your CI/CD pipeline, specifically tailored for GitLab CI with a focus on Java applications.

## Usage and Examples

### Smoke Test Script

The smoke test is implemented in the `.gitlab-ci.yml` file of your project. Here’s a basic outline:

```yaml
stages:
  - build
  - test

build:
  stage: build
  image: openjdk:12-alpine
  script:
    - ./gradlew build
  artifacts:
    paths:
      - ./build/libs/

smoke test:
  stage: test
  image: openjdk:12-alpine
  before_script:
    - apk --no-cache add curl
  script:
    - java -jar ./build/libs/cars-api.jar &
    - sleep 30
    - curl http://localhost:5000/actuator/health | grep "UP"
```

This script builds the application and then runs a basic smoke test to check if the application responds to a health check endpoint.

### Command Explanations

1. **Starting the Application:**

- `java -jar ./build/libs/cars-api.jar &`
    - This command starts the application using Java. The `java -jar` part executes the JAR file of the application, located at `./build/libs/cars-api.jar`. 
    - The `&` at the end of the command is crucial; it runs the Java process in the background. This allows the CI pipeline to proceed to the next command without waiting for the Java application to terminate, which is essential for the smoke test.

2. **Waiting for Application Readiness:**

- `sleep 30`
    - After initiating the application, there's a need to wait for it to fully start up and be ready to accept requests. This is where the `sleep 30` command comes in. It pauses the execution of the script for 30 seconds, providing enough time for the server to start running the application. 
    - This duration might need adjustment depending on how long your application typically takes to boot up.

3. **Health Check Verification:**

- `curl http://localhost:5000/actuator/health | grep "UP"`
    - This command is used to verify if the application is up and running. It utilizes `curl` to make a request to the application's health check endpoint (`http://localhost:5000/actuator/health`). 
    - The `| grep "UP"` part filters the response from the health check endpoint, searching for the term "UP". If `grep` finds "UP" in the response, it implies the application is running properly, and the script returns a success code (zero). If "UP" is not found, indicating the application is not running as expected, a non-zero code is returned, and the CI pipeline recognizes this as a failure.

4. **Pre-Script Setup:**

- `before_script: - apk --no-cache add curl`
    - This part of the script is placed in the `before_script` section of the `.gitlab-ci.yml` file. It's used for setting up prerequisites before the main script runs. In this case, `apk --no-cache add curl` is used to install `curl` in the Docker container. Since the container uses Alpine Linux (as indicated by `openjdk:12-alpine`), `apk` is the package manager used for installations. 
    - The `--no-cache` option is included to prevent the cache from being saved, reducing the size of the container.

### Committing and Pushing Changes

- Once you have modified the `.gitlab-ci.yml` file, add it to your Git repository:

```bash
git add .
```

- Commit your changes with a message describing what you have done:

```bash
git commit -m "added test stage and smoke test"
```

- Push the committed changes to your GitLab repository:

```bash
git push
```

### Smoke Test Job Output

When you run the smoke test command in your CI pipeline, you can expect to see output similar to the following in your console:

```bash
$ curl http://localhost:5000/actuator/health | grep "UP"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     02024-01-01 13:08:41.827  INFO 19 --- [nio-5000-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-01-01 13:08:41.828  INFO 19 --- [nio-5000-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-01-01 13:08:41.836  INFO 19 --- [nio-5000-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 8 ms
100    15    0    15    0     0     68      0 --:--:-- --:--:-- --:--:--    68
{"status":"UP"}
```

This output indicates that the smoke test was successful. The `curl` command fetched the health status of the application, and `grep` found the expected "UP" status in the response. This demonstrates that the application has started correctly and is running.

## Best Practices

- **Keep it Simple:** The smoke test should be basic; it's not meant to replace comprehensive tests.
- **Use Appropriate Timeouts:** Adjust the sleep time in the script based on the startup time of your application.
- **Maintain Clean Code:** Separate setup commands in the `before_script` section for clarity.
- **Regularly Update Dependencies:** Ensure your Docker images and dependencies are up to date.

## Key Takeaways

- Smoke tests are basic tests to check if an application starts and runs.
- They are crucial for early detection of major issues in the CI/CD pipeline.
- This guide provides a basic template for adding a smoke test to a Java application using GitLab CI.

## Conclusion

Implementing a smoke test in your CI/CD pipeline is a best practice that can save time and prevent significant issues in software deployment. While simple, it's an effective way to ensure that your application is on the right track from the early stages of development.

## References

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Java Development Documentation](https://docs.oracle.com/en/java/)
- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Docker Documentation](https://docs.docker.com/)