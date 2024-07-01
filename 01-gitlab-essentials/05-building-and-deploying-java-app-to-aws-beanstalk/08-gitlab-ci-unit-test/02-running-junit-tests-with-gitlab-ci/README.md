# Running JUnit Tests with GitLab CI

Welcome to this comprehensive guide on running JUnit tests with GitLab CI. This document will walk you through the steps required to integrate JUnit testing into your GitLab CI pipeline, ensuring that your Java projects are tested efficiently and effectively. 

## Table of Contents

- [Introduction](#introduction)
- [Java Project Directory Structure](#java-project-directory-structure)
- [Setting Up GitLab CI](#setting-up-gitlab-ci)
- [Configuring the CI Pipeline](#configuring-the-ci-pipeline)
- [Running JUnit Tests](#running-junit-tests)
- [Viewing Test Reports](#viewing-test-reports)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This guide aims to help you set up a GitLab CI pipeline that runs JUnit tests for your Java projects. By following this guide, you'll be able to automate your testing process, ensure code quality, and integrate test reports seamlessly into your GitLab workflow.

## Java Project Directory Structure

Understanding the structure of your Java project is crucial for setting up the CI pipeline correctly. Here’s a typical Java project directory structure, highlighting the path where the test reports are stored:

```tree
.
├── build
│   ├── classes
│   │   └── java
│   ├── generated
│   │   └── sources
│   ├── libs
│   ├── reports          # This is the main directory for reports
│   │   ├── pmd
│   │   └── tests        # Here you will find the HTML test reports
│   ├── resources
│   │   └── main
│   ├── test-results
│   │   └── test         # Here you will find the HTML test results
│   └── tmp
│       ├── bootJar
│       ├── compileJava
│       ├── compileTestJava
│       ├── pmdMain
│       └── test
├── gradle
│   └── wrapper
└── src
    ├── main
    │   ├── java
    │   └── resources
    └── test
        └── java
```

In the `build/reports/tests` directory, you will find the HTML files that contain the test reports. These files are essential for viewing detailed test results and summaries in GitLab CI.

## Configuring the CI Pipeline

### Defining the Unit Test Job

Add a new job called `unit tests` to the `test` stage in your `.gitlab-ci.yml` file. This job will use the OpenJDK image and execute the Gradle wrapper to run your tests.

```yaml
unit tests:
  stage: test
  image: openjdk:12-alpine
  script:
    - ./gradlew test
```

### Specifying Artifacts

Artifacts are files generated during the pipeline run that you want to keep. Define artifacts in your job to store the HTML and JUnit XML test reports.

```yaml
unit tests:
  stage: test
  image: openjdk:12-alpine
  script:
    - ./gradlew test
  artifacts:
    when: always
    paths:
      - build/reports/tests
    reports:
      junit: build/test-results/test/*.xml
```

### Understanding the `reports` Section

The `reports` section in your GitLab CI configuration is used to specify the location of test report files. These reports provide detailed information about the tests that were run during the pipeline and are used by GitLab to display test results in a readable format.

```yaml
reports:
  junit: build/test-results/test/*.xml
```

When you run your tests using Gradle (or another build tool), it generates test result files in a specific directory. For a typical Java project using Gradle, the JUnit test results are stored in the `build/test-results/test/` directory as XML files. By specifying this path in the `reports` section, you tell GitLab CI where to find these test results. 

GitLab CI will then:

1. Look for all XML files in the `build/test-results/test/` directory.
2. Parse these files to extract test results.
3. Display the results in the GitLab pipeline interface under the `Tests` tab.

This setup allows you to easily view and analyze the test results directly from the GitLab interface without having to manually inspect the XML files.

## Running JUnit Tests

The `script` section of your job will run the Gradle `test` task:

```yaml
script:
  - ./gradlew test
```

This command will execute your JUnit tests and generate the necessary reports.

## Viewing Test Reports

### Accessing HTML Reports

After the pipeline runs, you can access the HTML test reports through the GitLab interface. Navigate to the job artifacts and find the HTML reports under `build/reports/tests`.

### Viewing JUnit XML Reports

GitLab CI can also interpret JUnit XML reports and display the results in a structured format. This allows you to view test results directly from the pipeline interface under the `Tests` tab.

## Best Practices

- **Consistent Naming:** Use consistent and descriptive names for your jobs and stages.
- **Dependency Management:** Ensure your project dependencies are correctly configured to avoid issues during the test execution.
- **Fail Fast:** Configure your pipeline to fail early if a test fails, saving time and resources.
- **Artifact Retention:** Manage your artifact retention policies to avoid excessive storage usage.

## Key Takeaways

- Automating JUnit tests with GitLab CI improves code quality and saves time.
- Properly configuring artifacts and reports ensures that test results are easily accessible.
- Following best practices in CI configuration leads to more efficient and maintainable pipelines.

## Conclusion

Integrating JUnit tests with GitLab CI is a powerful way to enhance your development workflow. By automating the testing process and making test reports easily accessible, you can ensure higher code quality and faster feedback loops.

## References

- [GitLab CI/CD artifacts reports types](https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html)
- [GitLab CI/CD artifacts reports - junit](https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsjunit)
- [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)
- [Gradle Documentation](https://docs.gradle.org/current/userguide/userguide.html)