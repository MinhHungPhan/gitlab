# GitLab Architecture

This document aims to introduce GitLab's architecture, offering a detailed understanding of how the GitLab server, pipeline, and runners operate together. We will also delve into how to configure and optimize runners according to your project's needs.

## Table of Contents

- [Introduction](#introduction)
- [GitLab Server](#gitlab-server)
- [GitLab Runner](#gitlab-runner)
- [GitLab Pipeline](#gitlab-pipeline)
- [Configuring Runners](#configuring-runners)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

[GitLab](https://about.gitlab.com/) is a widely used platform that enables teams to collaborate on software development projects. It provides a seamless interface for managing repositories, pipelines, and everything related to your project. To understand GitLab more effectively, it's necessary to comprehend its architecture. Let's dive into the primary components: GitLab server and GitLab runners.

## GitLab Server

The GitLab server is the heart of GitLab's architecture. It offers an interface to create repositories, manage your project, and save your operations in a database. In other words, the GitLab server coordinates everything. 

Here's an example to illustrate its function:

Suppose you create a pipeline - a sequence of actions performed to achieve continuous integration and deployment. The GitLab server manages this pipeline, but the actual execution is delegated to a 'GitLab runner'.

## GitLab Runner

A GitLab runner is an agent that executes the steps within your pipeline. Think of the GitLab server as a director instructing the GitLab runner, "Here's what you need to do next: download this image, execute these steps, and save any artifacts produced." The GitLab server ensures that the runner picks up this job and that the output from the runner is stored safely. 

A critical point to note is that while the server oversees the entire process, it doesn't perform the heavy lifting - the runner does.

To function, a GitLab server must have at least one runner to execute the pipelines. However, if your requirements are higher, you can add as many GitLab runners as needed, illustrating the scalability of GitLab's architecture.

```plaintext
┌───────────────────────────────────────────────────────────────────────────────────────┐
│GitLab Architecture                                                                    │
│                                                                                       │
│                                        ┌───────────────┐          ┌───────────────┐   │
│                                        │               │          │               │   │
│                                 ┌─────▶│ GitLab Runner │─────────▶│   Artifacts   │   │
│                                 │      │               │          │               │   │
│                                 │      └───────────────┘          └───────────────┘   │
│                                 │                                                     │
│                                 │                                                     │
│    ┌──────────────────────┐     │                                                     │
│    │                      │     │                                                     │
│    │                      │     │      ┌───────────────┐                              │
│    │                      │     │      │               │                              │
│    │    GitLab Server     ├─────┼─────▶│ GitLab Runner │                              │
│    │                      │     │      │               │                              │
│    │                      │     │      └───────────────┘                              │
│    │                      │     │                                                     │
│    └──────────────────────┘     │                                                     │
│                                 │                                                     │
│                                 │                                                     │
│                                 │      ┌───────────────┐                              │
│                                 └─────▶│               │                              │
│                                        │ GitLab Runner │                              │
│                                        │               │                              │
│                                        └───────────────┘                              │
│                                                                                       │
│                                                                                       │
└───────────────────────────────────────────────────────────────────────────────────────┘

                                © Minh Hung Phan
```

In summary, the GitLab Runner serves as the essential tool responsible for running the commands defined within a job.

## GitLab Pipeline

To better grasp these concepts, consider a real-world example of a job, such as 'building a car,' executed by a GitLab runner. This job uses a Docker image, such as Ruby version 3.1. 

The runner begins by cloning the repository, then executing the steps found in the script. After generating the artifacts, it uploads them to the GitLab server (referred to as the 'coordinator'), which then knows about these artifacts. Once the job is successful, the runner stops the task, and the image used is destroyed, leaving behind only the logs and the job artifacts, which can be downloaded and inspected later.

## Configuring Runners

To see how the runners are configured, navigate to your project settings in GitLab. Here you will find settings related to runners. By default, your project will run on shared runners provided by GitLab, but you can specify your own runners if needed. 

For instance, if your tasks require intensive GPU work and the shared runners are insufficient, you can define specific runners with characteristics tailored for your jobs. This demonstrates the flexibility and adaptability of GitLab's architecture.

## Conclusion

In conclusion, GitLab's architecture offers flexibility and scalability for managing and executing software development tasks. Understanding how GitLab server and runners function can make navigating and leveraging GitLab more effective. We hope that this guide has clarified the fundamental workings of GitLab, making your journey in using GitLab.com much clearer.

## References

- [GitLab Basics](https://docs.gitlab.com/ee/gitlab-basics/)
- [GitLab Runner](https://docs.gitlab.com/runner/)
- [GitLab CI/CD Pipeline](https://docs.gitlab.com/ee/ci/pipelines/)
- [Configure GitLab Runner](https://docs.gitlab.com/runner/configuration/)