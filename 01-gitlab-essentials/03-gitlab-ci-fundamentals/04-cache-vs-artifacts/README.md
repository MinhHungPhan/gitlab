# Cache vs Artifacts

Understanding the distinction between cache and artifacts is crucial when working with continuous integration and delivery (CI/CD) tools. This guide will take you through their differences, purposes, and some examples to solidify your understanding.

## Table of Contents

- [Introduction](#introduction)
- [Understanding Cache](#understanding-cache)
- [Understanding Artifacts](#understanding-artifacts)
- [Key Differences](#key-differences)
- [Example Scenario](#example-scenario)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Both cache and artifacts are terms that you will encounter in the world of CI/CD. Though they may seem alike, they serve distinct roles. Dive into the sections below to grasp these differences thoroughly.

## Understanding Cache

A cache primarily aids in speeding up processes by storing resources that can be reused in subsequent runs. This means, if a process has some dependencies or files that don't change frequently, they can be cached to avoid redundant downloads or builds.

**Key Point**: Caching is not meant for storing build results or the outputs of your CI/CD jobs.

## Understanding Artifacts

Artifacts are the outputs or results produced after a build job. They can be binary files, libraries, or any other file needed for deployment. 

More than just storing outputs, artifacts can act as a bridge between different jobs or stages in a CI/CD pipeline. For instance, one job might compile the code, creating an artifact, which can then be used by a subsequent job for deployment.

## Key Differences

- **Purpose**: 
  - Cache: Speeds up CI/CD processes by reusing stored resources.
  - Artifacts: Stores outputs of jobs and can transfer data between CI/CD stages.
  
- **Usage**:
  - Cache should not replace artifacts for storing build results.
  - Artifacts can be used to pass data between different jobs or stages.

## Example Scenario

Imagine a CI/CD pipeline for a software application. The first job fetches dependencies. Instead of downloading these dependencies every time, they can be cached after the first download, reducing future fetch times.

The second job compiles the application code. The compiled binary is an artifact. This artifact can be passed to the next job, which might be for testing or deployment. Thus, artifacts act as a chain, connecting different jobs in the pipeline.

## Conclusion

Cache and artifacts, though seemingly similar, cater to different needs in a CI/CD process. Remember to use caching for speeding up repetitive tasks and artifacts for storing and transferring build results or data between jobs. Always refer to official documentation or resources to ensure best practices in your CI/CD pipelines.

## References

- [GitLab Cache vs Artifacts](https://docs.gitlab.com/ee/ci/caching/#cache-vs-artifacts).