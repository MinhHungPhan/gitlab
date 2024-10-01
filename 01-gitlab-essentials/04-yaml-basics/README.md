# YAML Basics

Welcome to the **YAML Basics** course! This course is designed to introduce you to the fundamental concepts of YAML (YAML Ain't Markup Language) and how it is used in GitLab CI/CD pipelines to structure jobs and configurations. By the end of the course, you will have a solid understanding of YAML syntax and advanced techniques such as anchors, job templates, and disabling jobs.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Sub-directories Overview](#sub-directories-overview)
    - [Understanding YAML](#understanding-yaml)
    - [Disabling Jobs](#disabling-jobs)
    - [YAML Anchors](#yaml-anchors)
    - [Creating Job Templates](#creating-job-templates)
- [Support](#support)
- [Conclusion](#conclusion)

## Introduction

The **YAML Basics** course will cover everything from the basic syntax of YAML to more advanced features like anchors and job templates. You’ll also learn how to disable jobs within GitLab pipelines, which can be useful when managing complex CI/CD configurations.

Throughout the course, you’ll engage with hands-on examples and exercises to build a strong foundation in YAML and its applications in GitLab CI.

## Prerequisites

Before starting this course, ensure you have the following:

- A basic understanding of GitLab CI/CD
- Familiarity with `.gitlab-ci.yml` files and their role in defining CI/CD pipelines
- Access to a GitLab project with CI/CD enabled
- A text editor capable of handling YAML files (e.g., VS Code, Sublime Text)

## Sub-directories Overview

### [Understanding YAML](01-understanding-yaml/README.md)

In this module, you’ll learn the basics of YAML syntax, including how to write key-value pairs, lists, and nested data structures. The focus will be on understanding the structure of YAML files and how to avoid common syntax errors. A sample `test.yml` file will be provided for practice.

- **What you'll learn:**
  - Writing YAML syntax
  - Understanding indentation in YAML
  - Working with lists, dictionaries, and nested elements

### [Disabling Jobs](02-disabling-jobs/README.md)

This module covers how to disable jobs in your `.gitlab-ci.yml` configuration, allowing you to exclude certain jobs from running without having to delete them from your file. This is useful for testing and managing complex pipelines.

- **What you'll learn:**
  - How to disable jobs in YAML
  - Managing complex pipelines with disabled jobs

### [YAML Anchors](03-yaml-anchors/README.md)

YAML anchors are a powerful feature that allows you to reuse and reference pieces of YAML configuration throughout your file. This module will teach you how to use anchors and aliases effectively to simplify and reduce duplication in your `.gitlab-ci.yml` files. A sample `test.yml` file will be provided for practice.

- **What you'll learn:**
  - Using YAML anchors and aliases
  - Reducing redundancy in YAML configurations

### [Creating Job Templates](04-creating-job-templates/README.md)

In this module, you’ll learn how to create reusable job templates in YAML, which can help streamline your GitLab CI configurations by allowing you to define common patterns and reuse them across multiple jobs.

- **What you'll learn:**
  - Creating and using job templates
  - Improving pipeline structure and reusability

## Support

If you have any questions or need assistance, you can:
- Open an issue in the GitHub repository
- Contact the course maintainers via email at support@kientree.com
- Join our community Slack channel for real-time help

## Conclusion

The **YAML Basics** course aims to provide you with a strong understanding of YAML, its syntax, and practical applications in GitLab CI/CD. Practice and experimentation are key to mastering YAML. We encourage you to try out different configurations and dive deeper into advanced YAML features as you progress. Happy learning! 🌱