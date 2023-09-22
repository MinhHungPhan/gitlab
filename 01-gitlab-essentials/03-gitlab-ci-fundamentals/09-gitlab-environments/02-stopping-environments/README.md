# Stopping Environments in GitLab CI

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Stopping Environments](#stopping-environments)
    - [Technical Background](#technical-background)
    - [Command to Tear Down](#command-to-tear-down)
    - [Configuring GitLab](#configuring-gitlab)
- [Implementation](#implementation)
    - [Deploy Review](#deploy-review)
    - [Stop Review](#stop-review)
- [Review and Testing](#review-and-testing)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Dynamic environments bring immense flexibility to the world of development, allowing for instantaneous testing in isolated environments. However, with this innovation comes new challenges. This guide aims to address one such issue, ensuring environments aren't left running unnecessarily, thereby optimizing resource use.

## Problem Statement

Dynamically created environments, especially those spawned during feature development, often outlive their utility. Once the feature branch merges, these environments aren't needed. Yet, they continue running by default, leading to potential resource wastage. Stopping them manually isn't a scalable solution.

## Stopping Environments

In this section, we'll explore how to automatically stop environments post-merge using GitLab.

### Technical Background

The technical crux of the issue is instructing our deployment tool, `surge`, to shut down a domain where files have been deployed. Fortunately, `surge` provides documentation detailing the tear-down process.

### Command to Tear Down

`surge` simplifies this task. The command is:

```bash
surge teardown [YOUR_DOMAIN_NAME].surge.sh
```

**Note**: `[YOUR_DOMAIN_NAME]` represents the address of the deployed environment.

### Configuring GitLab

#### Initial Configuration:

To achieve our goal, the configuration starts with creating a job named `stop review` within the `deployed review` stage.

#### Git Strategy:

Since the branch may have been merged and possibly deleted by the time we want to run the `stop review` job, we need a special Git strategy. Specifically, we set the `GIT_STRATEGY` variable to `none`, ensuring GitLab doesn’t clone the repository for this task.

```yaml
GIT_STRATEGY: none
```

#### Scripting:

The script for this task involves two main actions:
1. Installing `surge` globally.
2. Executing the `surge teardown` command with the appropriate domain name.

To associate the `deployed review` with the `stop review`, we utilize GitLab's `environment` setting. This involves setting the `on_stop` attribute to `stop review`.

#### Job Execution:

The `stop review` job doesn't run by default during a pipeline execution. Instead, it’s triggered under specific conditions, like when a branch merges. Therefore, the manual execution isn’t strictly "by hand" but rather condition-based. If there’s a naming mismatch in environments or if the `action` isn’t set to `stop`, the process won’t work.

## Implementation

### Deploy Review

#### Configuration

```yaml
deploy review:
  stage: deploy review
  only:
    - merge_requests
  environment:
      name: review/$CI_COMMIT_REF_NAME
      url: https://[YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
      on_stop: stop review
  script:
    - npm install --global surge
    - surge --project ./public --domain [YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
```

#### Explanation

**Purpose**: Automatically deploy a review instance for every merge request. It's especially useful for QA and stakeholder reviews before changes are merged into the main branch.

1. **Stage**: This job belongs to the `deploy review` stage.
2. **Only on merge_requests**: This job runs only for merge requests.
3. **Environment**: 
    - `name`: Names the environment dynamically based on the commit.
    - `url`: Provides a dynamic URL using the `CI_ENVIRONMENT_SLUG` variable, which converts the environment name to a URL-safe string.
    - `on_stop`: Refers to the `stop review` job, which will be triggered when the environment needs to be stopped.
4. **Script**: 
    - Installs the `surge` deployment tool.
    - Deploys the `./public` directory to the specified domain using `surge`.

### Stop Review

#### Configuration

```yaml
stop review:
  stage: deploy review
  only:
    - merge_requests
  variables:
    GIT_STRATEGY: none
  script:
    - npm install --global surge
    - surge teardown [YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
  when: manual
  environment:
    name: review/$CI_COMMIT_REF_NAME
    action: stop
```

#### Explanation

**Purpose**: Allow manual termination of the review environment once it's no longer needed, ensuring optimal resource utilization.

1. **Stage**: This job belongs to the same `deploy review` stage.
2. **Only on merge_requests**: This job runs only for merge requests.
3. **Variables**: 
    - `GIT_STRATEGY`: Set to `none` to ensure the repository isn’t cloned for this task, since the branch might have been merged or deleted.
4. **Script**: 
    - Installs the `surge` deployment tool.
    - Tears down the deployed site using the `surge teardown` command.
5. **When**: Set to `manual` indicating the job can be manually triggered, but also can be invoked automatically by GitLab under certain conditions.
6. **Environment**: 
    - `name`: Names the environment dynamically based on the commit.
    - `action`: Specifies that this job's purpose is to stop the environment.

## Review and Testing

After setting up the configuration:

1. Create a new branch and observe its pipeline execution.
2. Once the `deployed review` environment is up and the feature branch is merged, GitLab should automatically trigger the `stop review` job.
3. After successful execution, visiting the environment URL should return a "project not found" message, confirming the environment's termination.

## Conclusion

Dynamic environments are powerful tools in a developer's arsenal, but like all tools, they require management. With the above configuration, we've ensured that GitLab efficiently manages the lifecycle of these environments, spinning them up when needed and tearing them down post-merge. This automatic management optimizes resources, streamlining the development process, and ensuring a greener, more eco-friendly approach.

## References

- [Tearing down a published project](https://surge.sh/help/tearing-down-a-project)
- [Stopping an environment](https://docs.gitlab.com/ee/ci/environments/#stopping-an-environment)