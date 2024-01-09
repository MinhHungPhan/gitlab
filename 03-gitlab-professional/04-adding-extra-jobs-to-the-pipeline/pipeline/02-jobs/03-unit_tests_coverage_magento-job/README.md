# Overview of `unit_tests_coverage_magento` Job in `gitlab-ci.yml`

## Introduction

The `unit_tests_coverage_magento` job is a newly updated component of the `gitlab-ci.yml` file, specifically designed for advanced unit testing of Magento native code, including code coverage generation. This job is essential for ensuring the quality and robustness of Magento's native codebase.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Execution and Reporting](#execution-and-reporting)
- [Scheduling and Failure Policy](#scheduling-and-failure-policy)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To perform advanced unit testing with code coverage on Magento native code.
- **Execution Context**: Launched by a scheduled pipeline in GitLab.

## Prerequisites for the `unit_tests_coverage_magento` Job

Before diving into the specifics of the `unit_tests_coverage_magento` job, it's essential to understand the prerequisites that set the stage for a successful deployment.

### `.ssh_provision` (For Composer Dependencies)

The `.ssh_provision` anchor defines a series of commands primarily used for setting up SSH within the CI/CD pipeline, facilitating secure connections and interactions with other services:

- Checks for and installs `ssh-agent` if not present, ensuring SSH functionalities are available.
- Initializes the SSH agent and securely adds SSH keys to manage connections.
- Sets up the SSH directory with appropriate permissions for secure file handling.
- Executes a custom bash script to integrate GitLab tokens for secure access to private repositories.

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

### `.composer` (For Dependency Management)

The `.composer` anchor is essential for managing PHP dependencies in the project. It ensures that Composer, a PHP dependency manager, is set up and ready for use:

- Downloads and installs Composer, a critical tool for managing PHP packages.
- Locks Composer to a specific version (1.10.17) for consistency and stability across builds.
- Quietly installs necessary PHP dependencies, avoiding verbose output.

```yaml
.composer: &composer
    - sh ci/script/get-composer.sh
    - bin/composer self-update 1.10.17 #Fix composer version to latest 1.x
    - bin/composer install -q
```

## Configuration and Setup

- **Stage**: Allocated to the `test` stage.
- **Image**: Utilizes `meanbee/magento:7.0-cli`, tailored for Magento.
- **Tags**: Uses `docker-accor` for specific runner selection.

## Execution and Reporting

1. **Before Script**:

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget zip unzip
        - docker-php-ext-install bcmath
        - *ssh_provision
        - *composer
    # ... existing code ...
```

- Performs system updates and installs necessary tools (`wget`, `zip`, `unzip`).
- Installs the `bcmath` PHP extension.
- Executes the `ssh_provision` and `composer` templates for secure SSH setup and Composer dependency management.

2. **Script**:

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    script:
        - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_MAGENTO --colors=never
    # ... existing code ...
```

- Runs PHPUnit tests with a memory limit of 2048M, using the Magento-specific PHPUnit configuration (`$PHPUNIT_CONFIG_MAGENTO`).

3. **After Script**:

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    after_script:
        # Used for code coverage parsing see https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-parsing
        - cat $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_MAGENTO
```

- Outputs the code coverage report for parsing, located at `$PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_MAGENTO`.

4. **Artifacts**:

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    artifacts:
        when: always
        expire_in: 1 week
        paths:
            - 'phpunit/coverage/'
    # ... existing code ...
```

- Stores the code coverage reports, with a retention period of one week.

## Scheduling and Failure Policy

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    only:
        - schedules
    allow_failure: true
```

- **Execution Trigger**: Only runs for scheduled pipelines.
- **Allow Failure**: Set to `true`, indicating that pipeline success is not dependent on this job's success.

## Pipeline

```yaml
unit_tests_coverage_magento:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget zip unzip
        - docker-php-ext-install bcmath
        - *ssh_provision
        - *composer
    script:
        - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_MAGENTO --colors=never
    after_script:
        # Used for code coverage parsing see https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-parsing
        - cat $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_MAGENTO
    artifacts:
        when: always
        expire_in: 1 week
        paths:
            - 'phpunit/coverage/'
    only:
        - schedules
    allow_failure: true
```

This example illustrates the execution of PHPUnit with increased memory limits and Magento-specific configurations, highlighting the job's focus on detailed testing and coverage.

## Conclusion

The `unit_tests_coverage_magento` job significantly enhances the testing framework by focusing on in-depth code coverage for Magento native code. Its scheduled execution ensures regular quality checks without overburdening the CI/CD pipeline during routine operations. This job is a strategic addition to the pipeline, striking a balance between thorough testing and efficient resource utilization.

## References

- [PHPUnit Official Website](https://phpunit.de/)
- [PHPUnit Code Coverage Documentation](https://phpunit.readthedocs.io/en/9.5/code-coverage-analysis.html)
- [Docker Hub for Magento Images](https://hub.docker.com/r/meanbee/magento/)
- [GitLab CI/CD Pipeline Documentation](https://docs.gitlab.com/ee/ci/pipelines/)
- [Scheduling Pipelines in GitLab](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)
- [GitLab Test Coverage Parsing Documentation](https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-parsing)
