# Adding a Test Stage

## Table of Contents

- [Introduction](#introduction)
- [Understanding the Importance of Testing](#understanding-the-importance-of-testing)
- [What Makes GitLab CI Jobs Fail?](#what-makes-gitlab-ci-jobs-fail)
- [Implementing a Simple Test Stage](#implementing-a-simple-test-stage)
- [Example: Testing for a Specific String](#example-testing-for-a-specific-string)
- [Debugging Return Codes](#debugging-return-codes)
- [Adding a Test Stage to GitLab CI](#adding-a-test-stage-to-gitlab-ci)
- [Viewing the Test Results](#viewing-the-test-results)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to this guide on adding a test stage to your pipeline using GitLab CI. This guide will walk you through why testing is crucial for your development workflow, how to implement a simple test stage, and how to interpret and handle failure cases in GitLab CI jobs. This guide is designed for beginners and aims to provide an understanding of testing in continuous integration pipelines, accompanied by practical examples.

## Understanding the Importance of Testing

When building software, it's vital to ensure that your code functions as expected. Testing can help confirm that the features you've built align with what you intend to deploy later. As part of this guide, we will demonstrate how to integrate very basic tests into your GitLab CI pipeline.

## What Makes GitLab CI Jobs Fail?

GitLab CI jobs typically fail when a command executed within a job does not return a success status. In conventional terms, a command returns zero on success and an integer ranging from 1 to 255 on error. If GitLab CI receives a status that isn't zero (indicating success), it interprets this as a job failure. This may occur due to improper function calls, missing parameters, or assertions not behaving as expected.

## Implementing a Simple Test Stage

A test stage in your pipeline could involve various checks, such as testing whether files have been properly generated or if specific strings exist within these files. As an example, let's consider a scenario where we test an HTML file for the presence of a specific string.

## Example: Testing for a Specific String

Suppose you wish to test if an `index.html` file contains a particular string, say "Gatsby". To achieve this, we'll use the `grep` command-line utility:

```bash
grep "Gatsby" index.html
```

The `grep` command will return the entire line where the string "Gatsby" is found, indicating a successful match.

## Debugging Return Codes

At times, especially when using `grep` in quiet mode (which provides no output), it might be unclear what the return status of the command is:

```bash
grep -q "Gatsby" index.html
```

For debugging purposes, use the following command to check the last return code:

```bash
echo $?
```

If the previous command was successful, you would see a return code of `0`. If it failed, you would receive a `1`.

## Adding a Test Stage to GitLab CI

In GitLab CI, you can add a job to test if your build was successful. For instance, you can create a job named `test artifact` to check for the presence of the string "Gatsby" in `index.html` within the public folder. 

```yaml
stages:
  - build
  - test

build website:
  stage: build
  image: node:lts
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
  artifacts:
    paths:
      - ./public

test artifact:
  stage: test
  script:
    - grep "Gatsby" ./public/index.html
    - grep "XXXXXXXX" ./public/index.html
```

In the example above, `test artifact` is a job that belongs to the `test` stage. If the `grep` command fails (i.e., "Gatsby" is not found in `index.html`), the job and hence the pipeline fails.

## Viewing the Test Results

Once you've committed your changes and run the pipeline, you'll observe two stages - the build stage and the test stage. If your build stage succeeds, the pipeline will progress to the test stage. The test stage's output will confirm whether the command executed successfully or failed.

Expected Output for Build Stage:

```js
Cleaning up project directory and file based variables
Job succeeded
```

Expected Output for Test Stage:

```js
$ grep "XXXXXXXX" ./public/index.html
Cleaning up project directory and file based variables
ERROR: Job failed: exit code 1
```

## Conclusion

Adding a test stage to your GitLab CI pipeline can significantly improve the reliability of your code and ensure your built artefacts meet your expectations. By following this guide, you've taken a step towards a robust development process that incorporates essential testing practices.

## References

- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [Understanding Exit Codes and how to use them in bash scripts](https://bash.cyberciti.biz/guide/The_exit_status)
- [How to use grep command in UNIX / Linux](https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/)
