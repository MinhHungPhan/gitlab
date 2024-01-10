# Overview of `unit_tests_coverage_accor` Job in `gitlab-ci.yml`

## Introduction

The `unit_tests_coverage_accor` job, as part of the latest update to the `gitlab-ci.yml` file, focuses on advanced unit testing with code coverage generation for ACCOR specific code. This job is an essential component in ensuring the quality and performance of the ACCOR-specific customizations within the Magento project.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Scripts and Execution](#scripts-and-execution)
- [Artifacts and Reporting](#artifacts-and-reporting)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To perform advanced unit testing with code coverage for ACCOR-specific code.
- **Context**: Executed by scheduled pipelines in GitLab for focused quality checks.

## Configuration and Setup

- **Stage**: Assigned to the `test` stage.
- **Image**: Utilizes `meanbee/magento:7.0-cli`, optimized for Magento environments.
- **Tags**: Tagged with `docker-accor` for specific runner deployment.

## Scripts and Execution

1. **Before Script**:

```yaml
unit_tests_coverage_accor:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget
        - docker-php-ext-install bcmath
        - *ssh_provision
        - *composer
    # ... existing code ...
```

- Updates system packages and installs necessary tools.
- Installs the `bcmath` PHP extension for PHP-related operations.
- Executes `ssh_provision` and `composer` templates for secure operations and dependency management.

2. **Script**:

```yaml
unit_tests_coverage_accor:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    script:
        - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ACCOR --colors=never
        - python ci/script/path-phpunit-report.py $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_FILENAME_ACCOR # Fixes the php unit report file format
    # ... existing code ...
```

- Executes PHPUnit tests, specifying a memory limit of 2048M and using the ACCOR-specific PHPUnit configuration (`$PHPUNIT_CONFIG_ACCOR`).
- Runs a Python script to fix the format of the PHPUnit report file.

## Artifacts and Reporting

```yaml
unit_tests_coverage_accor:
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
```

- **Artifact Storage**: Code coverage reports are stored as artifacts, with a retention period of one week.
- **After Script**:
  - Outputs the code coverage report for GitLab parsing, located at `$PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_ACCOR`.

## Pipeline

```yaml
unit_tests_coverage_accor:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget
        - docker-php-ext-install bcmath
        - *ssh_provision
        - *composer
    script:
        - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ACCOR --colors=never
        - python ci/script/path-phpunit-report.py $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_FILENAME_ACCOR # Fixes the php unit report file format
    after_script:
        # Used for code coverage parsing see https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-parsing
        - cat $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_ACCOR
    artifacts:
        when: always
        expire_in: 1 week
        paths:
            - 'phpunit/coverage/'
```

This snippet illustrates the PHPUnit execution within the `unit_tests_coverage_accor` job, demonstrating the use of specific memory limits and configurations tailored to ACCOR's code.

## Conclusion

The `unit_tests_coverage_accor` job is a strategic enhancement to the Magento project's CI/CD pipeline, focusing on the thorough testing of ACCOR-specific code. It ensures that customizations made for ACCOR maintain high quality and performance standards. This job's scheduled execution allows for regular, in-depth quality checks without overburdening the pipeline during routine operations.

## References

- [CI/CD YAML syntax reference | GitLab - GitLab Documentation](https://docs.gitlab.com/ee/ci/yaml/)
- [GitHub - meanbee/docker-magento](https://github.com/meanbee/docker-magento)
- [Adding PHPUnit Test Log and Coverage to GitLab CI/CD Pipeline](https://dev.to/muhamadhhassan/adding-phpunit-test-log-and-coverage-to-gitlab-cicd-33b5)
- [Job artifacts | GitLab - GitLab Documentation](https://docs.gitlab.com/ee/ci/jobs/job_artifacts.html)