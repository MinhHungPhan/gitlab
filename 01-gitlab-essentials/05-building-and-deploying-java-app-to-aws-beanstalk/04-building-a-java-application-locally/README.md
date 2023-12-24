# Building a Java Application Locally

## Table of Contents

- [Introduction](#introduction)
- [Understanding the Build Stage](#understanding-the-build-stage)
- [Setting Up Gradle](#setting-up-gradle)
- [Building the Application](#building-the-application)
- [Locating the JAR File](#locating-the-jar-file)
- [Using the Clean Command](#using-the-clean-command)
- [Troubleshooting Build Errors](#troubleshooting-build-errors)
- [Automation with GitLab CI](#automation-with-gitlab-ci)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to the guide on building a Java application locally. This document is designed to help you understand and execute the build stage of a Continuous Integration (CI) pipeline for a Java project. Whether you're a seasoned Java developer or new to the world of programming, this guide will walk you through the essentials of the build process, using Gradle, and preparing your application for deployment.

The goal is to ensure that the artifact we build meets our quality criteria and is ready for release. We will cover the steps to build a Java application locally, focusing on the compilation into Java Byte Code and the creation of a JAR file.

## Understanding the Build Stage

The build stage is a crucial part of the CI pipeline, involving the transformation of source code into an executable format. In Java, this means compiling the code into `Java Byte Code`, which can be run on the `Java Virtual Machine (JVM)`. The outcome of this stage is a `JAR` file, a package containing the compiled byte code.

## Setting Up Gradle

Gradle is a powerful build tool used for Java applications. To set it up:
- Ensure you have Java installed on your machine.
- Download and install Gradle from [Gradle's official website](https://gradle.org/).
- Set up your environment variables (if necessary).

## Building the Application

To build your Java application with Gradle:
- Open your project in your IDE and locate the Gradle panel.
- Select the 'build' option and execute it.
- Wait for the process to complete, resulting in 'build successful'.

Alternatively, use the command line:
- Navigate to your project directory.
- Execute `./gradlew build` (Unix) or `gradlew.bat build` (Windows).
- The build process will start, and a new 'build' folder will appear containing the JAR file.

To build your Java application with Gradle, execute the appropriate command based on your operating system:

### For Unix Systems:

```bash
./gradlew build
```

### For Windows Systems:

```cmd
gradlew.bat build
```

## Locating the JAR File

After building your application, the generated `.jar` file can be found in the `build/libs` directory of your project. The path to this file relative to the root of your project will look like this:

```bash
project-root/build/libs/your-application-name.jar
```

Replace `your-application-name` with the actual name of your application as defined in your Gradle build file.

## Using the Clean Command

Before rebuilding your application, it's good practice to clean the previous builds to avoid conflicts. Use the `./gradlew clean` command to achieve this. It removes the existing 'build' folder, ensuring a fresh start for the next build. After cleaning, you can run the build command again to generate a new artifact.

Use the following commands to clean up previous builds:

### For Unix Systems:

```bash
./gradlew clean
```

### For Windows Systems:

```cmd
gradlew.bat clean
```

After cleaning, you can rebuild your application:

### For Unix Systems:

```bash
./gradlew build
```

### For Windows Systems:

```cmd
gradlew.bat build
```

## Troubleshooting Build Errors

If the build fails, an error will be displayed. Common issues include:
- Syntax errors in the code.
- Dependency conflicts.
- Environmental issues (e.g., wrong Java version).

## Automation with GitLab CI

Automating the build process with GitLab CI involves similar steps but executed within the CI pipeline. This ensures consistency and efficiency in building the application for deployment.

## Conclusion

Building a Java application locally is a straightforward process once you understand the basics of Gradle and the CI pipeline. With this guide, you should be able to build your Java applications successfully and prepare them for the next stages of deployment. Happy coding! 🚀

## References

- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)
- [Gradle Official Website](https://gradle.org/)
- [Java Compilation Process](https://docs.oracle.com/javase/tutorial/getStarted/cupojava/index.html)
- [Java Build Processes](https://docs.oracle.com/javase/tutorial/)