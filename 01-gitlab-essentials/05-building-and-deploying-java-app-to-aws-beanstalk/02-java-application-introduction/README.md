# Car Fleet Management Java Project Setup

## Table of Contents

- [Introduction](#introduction)
- [Forking the Repository](#forking-the-repository)
- [Setting Up IntelliJ IDEA](#setting-up-intellij-idea)
- [Cloning and Opening the Project](#cloning-and-opening-the-project)
- [Understanding the Project](#understanding-the-project)
- [Running the Application](#running-the-application)
- [Using Postman with the API](#using-postman-with-the-api)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to the Car Fleet Management Java project setup guide! This tutorial is designed to help beginners set up and understand a Java project for car fleet management. We'll guide you through each step, from forking the repository to running the application.

## Forking the Repository

1. **Start Point**: We have a public repository without a GitLab CI pipeline, which we will set up together.
2. **Forking**: Go to the top of the repository page and click 'Fork'. Choose to fork into a group or under your profile.

## Setting Up IntelliJ IDEA

1. **About IntelliJ**: IntelliJ IDEA is an Integrated Development Environment (IDE) for Java and JVM projects.
2. **Downloading IntelliJ**: If you haven't, download IntelliJ IDEA [here](https://www.jetbrains.com/idea/download/). It's free and straightforward to install.

## Cloning and Opening the Project

1. **Creating a New Project**: In `IntelliJ`, select 'Create Project from Version Control'.
2. **Repository URL**: Go back to the GitLab repository, click 'Clone', and copy the URL. Use SSH if you have set up SSH credentials.
3. **Cloning in IntelliJ**: Paste the repository URL in IntelliJ and click 'Clone'.

## Understanding the Project

1. **Project Overview**: This is a simple Java application for managing a car fleet.
2. **Gradle Build Tool**: We use Gradle to build and start the project. Gradle handles dependencies and project tasks.

## Running the Application

1. **Starting the App**: In `IntelliJ`, navigate to 'Gradle' > 'Tasks' > 'application' > 'bootRun'. This will start the application with all necessary dependencies.
2. **Local Installation**: Installing and running the project locally is beneficial but not required for building the pipeline.

## Using Postman with the API

1. **Understanding APIs**: The application exposes an API to interact with car data but doesn't have a GUI.
2. **Using Postman**: Download Postman [here](https://www.postman.com/downloads/) for interacting with the API. It's a free tool for API testing.

**Note**: `Gradle` is a powerful build automation tool that's used to manage the dependencies and build process of the project.

## Conclusion

This guide aims to help you set up and understand the Java project for car fleet management. Although having the project run locally is ideal, it's not crucial for the pipeline's construction. Check the resources for additional tutorials and assistance.

## References

- [Download IntelliJ IDEA](https://www.jetbrains.com/idea/download/)
- [Download Postman](https://www.postman.com/downloads/)
- [Gradle Documentation](https://gradle.org/docs/)
- [Understanding APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)