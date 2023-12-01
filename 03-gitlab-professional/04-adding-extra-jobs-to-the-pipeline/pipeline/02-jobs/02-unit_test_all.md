# Overview of `unit_test_all` Job in `gitlab-ci.yml`

## Introduction

The `unit_test_all` job, recently updated in the `gitlab-ci.yml` file, is a critical component of the testing stage in the CI/CD pipeline, specifically designed for running unit tests for both Magento and Accor. This job ensures the reliability and stability of the code during merge requests.

## Table of Contents

- [Job Description](#job-description)
- [Configuration Details](#configuration-details)
- [Scripts and Execution](#scripts-and-execution)
- [Example](#example)
- [Conclusion](#conclusion)

## Job Description

- **Purpose**: To run unit tests for Magento and Accor during merge requests.
- **Notable Features**: Deactivates Xdebug and does not generate code coverage, aiming to reduce execution time.

## Configuration Details

- **Stage**: Allocated to the `test` stage.
- **Image**: Uses `meanbee/magento:7.0-cli`, suitable for Magento projects.
- **Tags**: Tagged with `docker-accor` for specific runner selection.

## Scripts and Execution

1. **Before Script**:
- Updates and upgrades the system packages.
- Installs necessary tools like `wget`, `zip`, `unzip`.
- Installs PHP extension `bcmath`.
- Executes the `ssh_provision` and `composer` templates for SSH setup and Composer dependency management.
- Removes Xdebug configuration to enhance performance.

2. **Script**:
- Runs PHPUnit tests with a memory limit of 2048M using the `$PHPUNIT_CONFIG_ALL` configuration.

## Example

```yaml
unit_test_all:
  ...
  script:
    - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ALL
```

This example illustrates the PHPUnit execution command within the `unit_test_all` job, highlighting the increased memory limit and the use of a general PHPUnit configuration.

## Conclusion

The `unit_test_all` job significantly streamlines the testing process by focusing on speed and efficiency. By disabling Xdebug and forgoing code coverage, the job is optimized for quicker execution, providing fast feedback during merge requests. This approach is vital in maintaining high-quality code standards while efficiently managing CI/CD resources.