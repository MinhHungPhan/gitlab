# Running Jobs in the Background

## Table of Contents

- [Introduction](#introduction)
- [Setting Up the Test Environment](#setting-up-the-test-environment)
- [Execution and Pipeline Handling](#execution-and-pipeline-handling)
- [Parallel Execution of Pipelines](#parallel-execution-of-pipelines)
- [Solving a Specific Error](#solving-a-specific-error)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This tutorial describes the process of setting up and executing a test website job using Gatsby. It discusses the implementation of an automated testing pipeline and handling potential errors and complexities.

## Setting Up the Test Environment

If you are configuring a test website job, you may have noticed some unexpected behaviors during the process.

When you execute the command `gatsby serve`, you will observe the website running at a specific address, just as expected. However, it may seem that the next command in the pipeline is not being executed.

This is due to the nature of `gatsby serve`, which blocks the entire terminal with its execution. As a result, it does not allow the next command to start. To address this, you will need to make some modifications to the execution process.

```yaml
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby serve &
    - sleep 3
    - curl "http://localhost:9000" | grep -q "Gatsby"
```

The `&` symbol at the end of the command allows it to run in the background, freeing the terminal for the next command. The `sleep` command ensures a pause, providing enough time for the Gatsby server to start.

## Execution and Pipeline Handling

You may observe that the pipeline's duration can run to a pre-configured timeout (e.g., one hour). If the entire job takes longer than this, GitLab will automatically kill it.

If you need to cancel the job, you can simply click on "Cancel" and terminate it.

## Parallel Execution of Pipelines

Multiple pipelines can run in parallel. When a new pipeline starts, it does not automatically cancel the existing ones. You can manually cancel a pipeline or individual stages if necessary.

To stop the entire pipeline, click on "Stop the pipeline." To cancel individual stages, click on the cancel button within the job details.

## Solving a Specific Error

Sometimes you may face specific errors, such as "failed writing body." You can search for the error online and find solutions. Implementing these fixes can help you resolve the problem.

### Example:

Using the `tac` command twice can be a solution for this error:

```yaml
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby serve &
    - sleep 3
    - curl "http://localhost:9000" | tac | tac | grep -q "Gatsby"
```

Test the fix to ensure it works before deploying it.

## Conclusion

The tutorial provides an in-depth guide to setting up a testing environment using Gatsby, including examples and problem-solving strategies. It covers parallel execution of pipelines, handling timeouts, and resolving specific errors.

## References

- [GitLab Jobs](https://docs.gitlab.com/ee/ci/jobs/)
- [Build job running forever](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/2231)
- [Commands (Gatsby CLI)](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
