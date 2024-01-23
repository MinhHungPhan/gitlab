# Overview for `composer-build` Job in `gitlab-ci.yml`

## Table of Contents

- [Introduction](#introduction)
- [External Dependencies for GitLab Pipeline](#external-dependencies-for-gitlab-pipeline)
- [Prerequisites for the composer-build Job](#prerequisites-for-the-composer-build-job)
- [Job Configuration](#job-configuration)
- [Scripts and Commands](#scripts-and-commands)
- [Trigger Conditions](#trigger-conditions)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This document outlines the configuration and usage of a Continuous Integration (CI) pipeline, primarily focused on managing composer dependencies within a PHP-based environment.

## External Dependencies for GitLab Pipeline

The pipeline relies on various external dependencies, which are not detailed in this document but are crucial for its functioning. Ensure all dependencies are met before proceeding.

## Prerequisites for the composer-build Job

### .ssh_provision

- **YAML code snippet:**

```yaml
.ssh_provision: &ssh_provision
    - which ssh-agent || ( apt-get update -y && apt-get install openssh-client -y )
    - eval $(ssh-agent -s)
    - echo "$SSH_ID_RSA" | tr -d "\r" | ssh-add -
    - mkdir -p ~/.ssh
    - chmod -R 700 ~/.ssh
    - echo "$SSH_ID_RSA" | tr -d "\r" > ~/.ssh/id_rsa-ci-accor
    - bash ci/script/add-gitlab-token.bash composer.lock deployv2/environments.py .spbuilder.yml
```

- **Explanation:** This configuration sets up SSH for secure communication. It installs SSH if not present, initializes an SSH agent, adds the private key, and configures the necessary directories and permissions. The script also handles GitLab token additions.

## Job Configuration

### YAML code snippet

```yaml
stages:
  - build
  - test
  - sonarqube-analysis
  - deploy
```

- **Explanation:** Defines the stages of the CI/CD pipeline. The `composer-build` job will be part of the build stage, which follows build, test, and sonarqube-analysis stages.

## Scripts and Commands

### Before Script

- **YAML code snippet:**

```yaml
before_script:
    - apt update && apt install -y libzip-dev wget
    - docker-php-ext-install zip
    - *ssh_provision
```

- **Explanation:** Prepares the environment by updating packages, installing dependencies, and setting up SSH.

### Script

- **YAML code snippet:**

```yaml
 script:
    - sh ci/script/get-composer.sh
    - bin/composer self-update 1.10.17 #Fix composer version to lastest 1.x
    - composer install -q
```

- **Explanation:** Executes the core steps of the deployment job, including updating Composer and installing dependencies.

- `get-composer.sh`: Script to retrieve the Composer executable.
- `self-update 1.10.17`: Updates Composer to a specific version for consistency.

### After Script

- **YAML code snippet:**

```yaml
after_script:
    - ls -la
```

- **Explanation:** Provides a log of the directory's state after script execution, useful for debugging.

### Cache

- **Purpose**: The `cache` directive is used to specify files or directories that GitLab CI/CD should preserve between jobs. This can significantly speed up job execution, especially for dependencies that don't change often.

- **Syntax and Usage**: 

```yaml
cache:
  key:
    files:
      - composer.lock
  paths:
    - vendor
    - app/etc
    - generated
    - dev/tests/unit
    - app/autoload.php
    - app/bootstrap.php
    - app/functions.php
    - setup
    - lib
```

- `composer.lock` and directories like `vendor` and `lib` are typically cached to avoid reinstalling dependencies that haven't changed.

### Artifacts

- **Purpose**: The `artifacts` directive is used to specify output files or directories created by jobs that should be attached to the job after it completes. Artifacts can be used in later stages, downloaded, or kept for a specified time.

- **Syntax and Usage**:

```yaml
artifacts:
  paths:
    - vendor
    - app/etc
    - generated
    - dev/tests/unit
    - app/autoload.php
    - app/bootstrap.php
    - app/functions.php
    - setup
    - lib
    - composer.lock
  expire_in: 1 week
```

- This configuration helps in persisting important files like `composer.lock` and project-specific directories beyond the job's execution, available for later stages or for review.

## Trigger Conditions

The `composer-build` job does have a specific trigger condition defined under the `except` keyword. Here's how it works:

- The `except` keyword in GitLab CI/CD is used to specify conditions under which a job should **not** run. In your case, the configuration is as follows:

```yaml
except:
  refs:
    - tags
```

- This means that the `composer-build` job is set to run on all branches and push events, **except** when the event is a tag. In other words, whenever a new tag is created, this particular job will not execute.

## Conclusion

This pipeline is optimized for PHP projects using Composer and is particularly suited for environments that require SSH keys for dependency management.

## References

- [Run your CI/CD jobs in Docker containers | GitLab](https://docs.gitlab.com/ee/ci/docker/using_docker_images.html#run-your-cicd-jobs-in-docker-containers)
- [Gitlab CI Series - Building PHP Containers with Docker and Gitlab | cwd.at GmbH](https://cwd.at/blog/building-php-containers-with-docker-and-gitlab/)
- [Testing PHP projects | GitLab](https://docs.gitlab.com/ee/ci/examples/php.html)
- [Command not found 'docker-php-ext-install' from gitlab ci](https://github.com/mlocati/docker-php-extension-installer/discussions/627)