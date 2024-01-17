# Adding Extra Jobs to the Pipeline

## Introduction

This README provides a detailed overview of the latest updates to the `gitlab-ci.yml` file for our Magento project. These changes are aimed at enhancing the CI/CD pipeline's efficiency, coverage, and reporting mechanisms.

## Table of Contents

- [New Variables](#new-variables)
  - [Example Usage](#example-usage)
- [Infrastructure Enhancements](#infrastructure-enhancements)
  - [SSH Provision for Composer Dependencies](#ssh-provision-for-composer-dependencies)
  - [Deployment Provision Enhancements](#deployment-provision-enhancements)
  - [Pip and Composer Management](#pip-and-composer-management)
  - [Debugging Tools](#debugging-tools)
- [Overview of `deploy_inte` Job](#overview-of-deploy_inte-job)
  - [Job Configuration](#job-configuration)
  - [Scripts and Commands](#scripts-and-commands)
  - [Trigger Conditions](#trigger-conditions)
  - [Example in `deploy_inte` job](#example-in-deploy_inte-job)
- [Overview of `unit_test_all` Job](#overview-of-unit_test_all-job)
  - [Job Description](#job-description)
  - [Configuration Details](#configuration-details)
  - [Scripts and Execution](#scripts-and-execution)
  - [Example in `unit_test_all` job](#example-in-unit_test_all-job)
- [Overview of `unit_tests_coverage_magento` Job](#overview-of-unit_tests_coverage_magento-job)
  - [Job Description](#job-description)
  - [Configuration and Setup](#configuration-and-setup)
  - [Execution and Reporting](#execution-and-reporting)
  - [Scheduling and Failure Policy](#scheduling-and-failure-policy)
  - [Example in `unit_tests_coverage_magento` job](#example-in-unit_tests_coverage_magento-job)
- [Conclusion](#conclusion)
- [References](#references)

## New Variables

The updated `gitlab-ci.yml` introduces several new variables, expanding the pipeline's configurability and functionality:

- **`SONAR_SCANNER_VERSION`**: Set to `3.3.0.1492`, specifies the version of the Sonar Scanner tool.
- **Error Threshold Variables**: 
  - `PHPCS_ALLOWED_ERROR`: Set to `31`, defines the allowed error count for PHP CodeSniffer.
  - `PHPMD_ALLOWED_ERROR`: Set to `6`, specifies the allowed error count for PHP Mess Detector.
  - `SMILEANALYSER_ALLOWED_ERROR`: Set to `119`, indicates the permissible error count for a custom analysis tool.
- **PHPUnit Configuration**: 
  - `PHPUNIT_CONFIG_MAGENTO`: Path to Magento's PHPUnit configuration.
  - `PHPUNIT_CONFIG_ACCOR`: Path to Accor's specific PHPUnit configuration.
  - `PHPUNIT_CONFIG_ALL`: Path to the general PHPUnit configuration.
- **PHPUnit Reporting**:
  - `PHPUNIT_REPORT_FOLDER`, `PHPUNIT_REPORT_TXT_MAGENTO`, `PHPUNIT_REPORT_TXT_ACCOR`, `PHPUNIT_REPORT_FILENAME_ACCOR`, `PHPUNIT_REPORT_CLOVER_ACCOR`: Variables related to PHPUnit reporting, specifying paths and file names for various reports.

### Example Usage

These variables enhance the pipeline's flexibility. For instance:

- **Error Thresholds**: In jobs where code quality tools like PHP CodeSniffer are used, `PHPCS_ALLOWED_ERROR` can be referenced to determine pass/fail criteria.
- **PHPUnit Configuration**: Depending on the test context (Magento or Accor), the appropriate PHPUnit configuration file can be used, as specified by the variables.

## Infrastructure Enhancements

### SSH Provision for Composer Dependencies

- **`.ssh_provision`**:
  - Ensures SSH agent and client are installed and configured.
  - Adds an SSH key for secure interactions with external repositories and services, primarily for Composer dependencies.

### Deployment Provision Enhancements

- **`.deploy_provision`**:
  - Sets up necessary tools and environment for deployment jobs.
  - Installs packages like SSH client, Python, Git, and cleans up the `./build/dist/` directory.

### Pip and Composer Management

- **`.get_pip` and `.composer`**:
  - `.get_pip`: Installs Pip and Pipenv for Python dependency management.
  - `.composer`: Programmatically obtains Composer, setting a specific version for consistency.

### Debugging Tools

- **`.debug_ssh`**:
  - Provides a utility to list contents of the SSH directory (`~/.ssh/`) for debugging purposes.

## Overview of `deploy_inte` Job

The `deploy_inte` job defined in your `gitlab-ci.yml` file is a critical component of the deployment stage in the CI/CD pipeline for the Magento project. It is specifically tailored for deploying to an integration environment.

### Job Configuration

- **Image**: Uses `meanbee/magento:7.0-cli`, a Docker image tailored for Magento projects.
- **Tags**: Tagged with `docker-accor` to specify the runner type.
- **Stage**: Allocated to the `deploy` stage of the pipeline.

### Scripts and Commands

1. **Before Script**:
- Executes `deploy_provision` and `get_pip` templates.
- Installs and updates the AWS CLI using Pip.
- Sets up an environment variable for S3 package paths.
- Clones a specific Git repository for deployment configurations.
- Sets locale configurations and installs necessary Python packages.
- Implements SSH provisions for secure connections.
- Modifies `/etc/hosts` and SSH configurations for deployment requirements.
- Prepares the Ansible environment by checking out and updating a specific branch and modifying deploy scripts for verbose output.

2. **Script**:
- Executes the deployment script (`deploy.sh`) with specific arguments, including the S3 package path and silent mode.

3. **After Script**:
- Executes the `debug_ssh` template to list the contents of the SSH directory, aiding in debugging.

### Trigger Conditions

- **Manual Trigger**: The job requires manual intervention to start.
- **Tag-Based**: Triggered only for tags matching the pattern `magento-inte-[0-9]{8}-[0-9]{6}`.
- **Project Path Condition**: Only executes for the `Accor/magento` project path.

### Example in `deploy_inte` job

```yaml
deploy_inte:
  image: meanbee/magento:7.0-cli
  ...
  script:
    - './scripts/deploy.sh in01.aws_ec2.yml -p ${s3_package} -s'
  ...
```

This snippet illustrates the deployment script execution within the `deploy_inte` job, highlighting the use of specific parameters for targeted deployment.

## Overview of `unit_test_all` Job 

The `unit_test_all` job, recently updated in the `gitlab-ci.yml` file, is a critical component of the testing stage in the CI/CD pipeline, specifically designed for running unit tests for both Magento and Accor. This job ensures the reliability and stability of the code during merge requests.

### Job Description

- **Purpose**: To run unit tests for Magento and Accor during merge requests.
- **Notable Features**: Deactivates Xdebug and does not generate code coverage, aiming to reduce execution time.

### Configuration Details

- **Stage**: Allocated to the `test` stage.
- **Image**: Uses `meanbee/magento:7.0-cli`, suitable for Magento projects.
- **Tags**: Tagged with `docker-accor` for specific runner selection.

### Scripts and Execution

1. **Before Script**:
- Updates and upgrades the system packages.
- Installs necessary tools like `wget`, `zip`, `unzip`.
- Installs PHP extension `bcmath`.
- Executes the `ssh_provision` and `composer` templates for SSH setup and Composer dependency management.
- Removes Xdebug configuration to enhance performance.

2. **Script**:
- Runs PHPUnit tests with a memory limit of 2048M using the `$PHPUNIT_CONFIG_ALL` configuration.

### Example in `unit_test_all` job

```yaml
unit_test_all:
  ...
  script:
    - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ALL
```

This example illustrates the PHPUnit execution command within the `unit_test_all` job, highlighting the increased memory limit and the use of a general PHPUnit configuration.

## Overview of `unit_tests_coverage_magento` Job

The `unit_tests_coverage_magento` job is a newly updated component of the `gitlab-ci.yml` file, specifically designed for advanced unit testing of Magento native code, including code coverage generation. This job is essential for ensuring the quality and robustness of Magento's native codebase.

### Job Description

- **Purpose**: To perform advanced unit testing with code coverage on Magento native code.
- **Execution Context**: Launched by a scheduled pipeline in GitLab.

### Configuration and Setup

- **Stage**: Allocated to the `test` stage.
- **Image**: Utilizes `meanbee/magento:7.0-cli`, tailored for Magento.
- **Tags**: Uses `docker-accor` for specific runner selection.

### Execution and Reporting

1. **Before Script**:
- Performs system updates and installs necessary tools (`wget`, `zip`, `unzip`).
- Installs the `bcmath` PHP extension.
- Executes the `ssh_provision` and `composer` templates for secure SSH setup and Composer dependency management.

2. **Script**:
- Runs PHPUnit tests with a memory limit of 2048M, using the Magento-specific PHPUnit configuration (`$PHPUNIT_CONFIG_MAGENTO`).

3. **After Script**:
- Outputs the code coverage report for parsing, located at `$PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_MAGENTO`.

4. **Artifacts**:
- Stores the code coverage reports, with a retention period of one week.

### Scheduling and Failure Policy

- **Execution Trigger**: Only runs for scheduled pipelines.
- **Allow Failure**: Set to `true`, indicating that pipeline success is not dependent on this job's success.

### Example in `unit_tests_coverage_magento` job

```yaml
unit_tests_coverage_magento:
  ...
  script:
    - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_MAGENTO --colors=never
  ...
```

This example illustrates the execution of PHPUnit with increased memory limits and Magento-specific configurations, highlighting the job's focus on detailed testing and coverage.

## Conclusion

The introduction of these new variables in the `gitlab-ci.yml` file signifies a significant enhancement in the configurability and precision of our CI/CD pipeline. By providing specific thresholds for code quality tools and versatile PHPUnit configurations, we ensure a more tailored and effective CI/CD process tailored to our project's needs.

## References

- [GitLab CI/CD Variables Documentation](https://docs.gitlab.com/ee/ci/variables/)
- [PHPUnit Documentation](https://phpunit.de/documentation.html)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)