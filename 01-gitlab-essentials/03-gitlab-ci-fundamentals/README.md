# GitLab CI Fundamentals

Welcome to the GitLab CI Fundamentals course! This course is designed to deepen your understanding of GitLab CI/CD by exploring advanced topics such as environment variables, caching, deployment environments, and more. Through practical exercises, you will learn how to optimize your CI/CD pipelines and make the most out of GitLab’s powerful features.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Sub-directories Overview](#sub-directories-overview)
    - [Using GitLab CI Environment Variables](#using-gitlab-ci-environment-variables)
    - [Pipeline Triggers and Retrying Failed Jobs](#pipeline-triggers-and-retrying-failed-jobs)
    - [Caching in GitLab CI/CD](#caching-in-gitlab-cicd)
    - [Cache vs Artifacts](#cache-vs-artifacts)
    - [Deployment Environments](#deployment-environments)
    - [Defining Variables](#defining-variables)
    - [Manual Deployments](#manual-deployments)
    - [Merge Requests](#merge-requests)
    - [GitLab Environments](#gitlab-environments)
- [Support](#support)
- [Conclusion](#conclusion)

## Introduction

The GitLab CI Fundamentals course covers advanced topics that are essential for optimizing CI/CD pipelines in GitLab. You will learn how to effectively use environment variables, manage caching and artifacts, handle deployment environments, and much more. By the end of this course, you will have a strong grasp of how to build robust and efficient pipelines that can adapt to various workflows and environments.

## Prerequisites

Before starting this course, you should have:

- A basic understanding of GitLab CI/CD
- Familiarity with Git and version control systems
- Experience with writing `.gitlab-ci.yml` files
- Access to a GitLab project with CI/CD enabled
- (Optional) Basic knowledge of Docker and YAML syntax

## Sub-directories Overview

### [Using GitLab CI Environment Variables](01-using-gitlab-ci-environment-variables/README.md)

This module introduces the concept of environment variables in GitLab CI. You will learn how to define and use environment variables to make your pipelines more dynamic and adaptable to different environments.

### [Pipeline Triggers and Retrying Failed Jobs](02-pipeline-triggers-and-retrying-failded-jobs/README.md)

In this module, you will explore how to set up pipeline triggers and manage failed jobs. You will learn how to automatically trigger pipelines based on specific conditions and how to handle job failures effectively by setting up retry strategies.

### [Caching in GitLab CI/CD](03-caching-in-gitlab-cicd/README.md)

Caching is crucial for speeding up your CI/CD pipelines. This module covers how to implement caching in GitLab CI/CD, reducing build times by reusing previously downloaded dependencies and built artifacts.

### [Cache vs Artifacts](04-cache-vs-artifacts/README.md)

Understand the difference between cache and artifacts in GitLab CI/CD. This module will explain when and how to use each, helping you optimize storage and speed up your pipeline execution.

### [Deployment Environments](05-deployment-environments/README.md)

This module focuses on setting up and managing deployment environments in GitLab CI. You will learn how to create multiple environments (e.g., staging, production) and deploy your application to different environments based on your pipeline configuration.

### [Defining Variables](06-defining-variables/README.md)

Learn how to define and manage variables in GitLab CI/CD pipelines. This module will guide you through the process of setting up both global and job-specific variables to control your pipeline's behavior.

### [Manual Deployments](07-manual-deployments/README.md)

In some cases, you may want to deploy your application manually rather than automatically. This module explains how to set up manual deployments in GitLab CI, allowing you to control when and how deployments are executed.

### [Merge Requests](08-merge-requests/README.md)

Merge requests are a critical part of collaborative development. This module covers how to use GitLab CI in conjunction with merge requests to automatically test, review, and merge changes into your main branch.

### [GitLab Environments](09-gitlab-environments/README.md)

This module provides an in-depth look at GitLab environments, explaining how to configure and manage different environments in your CI/CD pipeline. You will learn how to monitor and control deployments across various environments within GitLab.

## Support

If you have any questions or need assistance, you can:
- Open an issue in the GitHub repository
- Contact the course maintainers via email at support@kientree.com
- Join our community Slack channel for real-time help

## Conclusion

We hope that this GitLab CI Fundamentals course equips you with the advanced skills needed to create and manage efficient CI/CD pipelines in GitLab. By consistently applying the concepts and techniques covered in this course, you will be able to optimize your development workflows and deliver high-quality software with confidence. Keep experimenting and refining your pipelines, and enjoy the journey of continuous improvement! 🚀