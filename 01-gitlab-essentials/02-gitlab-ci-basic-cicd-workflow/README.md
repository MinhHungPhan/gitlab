# GitLab CI Basic CI/CD Workflow

Welcome to the GitLab CI Basic CI/CD Workflow course! This course is designed to provide you with a solid foundation in GitLab CI/CD, guiding you through the essential concepts and practical implementations needed to build, test, and deploy projects efficiently using GitLab CI.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Sub-directories Overview](#sub-directories-overview)
    - [What is CI/CD?](#what-is-cicd)
    - [Creating a Static Website with Gatsby](#creating-a-static-website-with-gatsby)
    - [Building the Project Locally](#building-the-project-locally)
    - [Docker with GitLab CI](#docker-with-gitlab-ci)
    - [Building the Project Using GitLab CI](#building-the-project-using-gitlab-ci)
    - [Adding a Test Stage](#adding-a-test-stage)
    - [Running Jobs in Parallel](#running-jobs-in-parallel)
    - [Running Jobs in the Background](#running-jobs-in-the-background)
    - [Deploying Using Surge.sh](#deploying-using-surgesh)
    - [Managing Secrets with GitLab CI](#managing-secrets-with-gitlab-ci)
    - [Deploying the Project Using GitLab CI](#deploying-the-project-using-gitlab-ci)
    - [Understanding Environment Variables](#understanding-environment-variables)
- [Support](#support)
- [Conclusion](#conclusion)

## Introduction

The GitLab CI Basic CI/CD Workflow course will guide you through the process of creating a CI/CD pipeline using GitLab CI. Starting from the basics of CI/CD, you'll learn how to set up and deploy a static website, build projects both locally and within Docker containers, add testing stages, and optimize your pipeline by running jobs in parallel and in the background. You'll also learn how to securely manage secrets and deploy your project using GitLab CI.

## Prerequisites

Before starting this course, ensure you have the following:

- Basic understanding of Git and version control systems
- A GitLab account with access to create and manage repositories
- Familiarity with the command line interface (CLI)
- (Optional) Basic knowledge of Docker and YAML syntax
- (Optional) An account on Surge.sh for deployment purposes

## Sub-directories Overview

### [What is CI/CD?](01-what-is-cicd/README.md)

This module introduces the concept of CI/CD (Continuous Integration and Continuous Deployment). You'll learn the importance of CI/CD in modern software development and how GitLab CI can be leveraged to automate these processes.

### [Creating a Static Website with Gatsby](02-creating-static-website-with-gatsby/README.md)

In this module, you will create a simple static website using Gatsby, a popular static site generator. You'll learn how to set up the project and prepare it for CI/CD integration.

### [Building the Project Locally](03-building-the-project-locally/README.md)

This module walks you through the steps of building the Gatsby project locally. You'll understand the build process and the tools required to successfully compile the project on your local machine.

### [Docker with GitLab CI](04-docker-with-gitlab-ci/README.md)

Learn how to integrate Docker into your GitLab CI pipeline. This module covers the basics of Docker, how to create Docker images, and how to use Docker containers to build and test your projects in a consistent environment.

### [Building the Project Using GitLab CI](05-building-the-project-using-gitlab-ci/README.md)

This module demonstrates how to set up a GitLab CI pipeline to build your Gatsby project. You'll configure your `.gitlab-ci.yml` file and learn how to define jobs and stages that automate the build process.

### [Adding a Test Stage](06-adding-test-stage/README.md)

Learn how to add a test stage to your CI/CD pipeline. This module will guide you through writing and running tests as part of your pipeline, ensuring your project is stable and reliable before deployment.

### [Running Jobs in Parallel](07-running-jobs-in-parallel/README.md)

Optimize your CI/CD pipeline by running jobs in parallel. This module explains how to configure your pipeline to execute multiple jobs simultaneously, reducing the overall build time.

### [Running Jobs in the Background](08-running-jobs-in-the-background/README.md)

This module covers running jobs in the background, allowing you to perform long-running tasks without blocking the rest of your pipeline. You'll learn how to manage background jobs and ensure they complete successfully.

### [Deploying Using Surge.sh](09-deploying-using-surge.sh/README.md)

Deploy your static website to the web using Surge.sh, a simple, fast, and free way to publish your site. This module provides a step-by-step guide to deploying your project using GitLab CI and Surge.sh.

### [Managing Secrets with GitLab CI](10-managing-secrets-with-gitlab-ci/README.md)

Learn best practices for managing sensitive information like API keys and credentials within your CI/CD pipeline. This module covers how to securely store and access secrets in GitLab CI.

### [Deploying the Project Using GitLab CI](11-deploying-the-project-using-gitlab-ci/README.md)

In this module, you'll integrate everything you've learned to deploy your project using GitLab CI. You'll configure the pipeline for deployment, ensuring a smooth and automated release process.

### [Understanding Environment Variables](12-understanding-environment-variables/README.md)

Gain a deep understanding of environment variables and how they are used in GitLab CI. This module explains how to define, manage, and use environment variables to make your pipeline more flexible and secure.

## Support

If you have any questions or need assistance, you can:
- Open an issue in the GitHub repository
- Contact the course maintainers via email at support@kientree.com
- Join our community Slack channel for real-time help

## Conclusion

We hope this GitLab CI Basic CI/CD Workflow course empowers you with the skills and knowledge to implement effective CI/CD pipelines in your projects. Continuous practice and exploration of the concepts covered will deepen your understanding and mastery of GitLab CI. Keep experimenting, and happy coding! 🌱