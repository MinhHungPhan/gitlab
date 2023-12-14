# Overview of `unit_tests_coverage_magento` Job in `gitlab-ci.yml`

## Introduction

The `unit_tests_coverage_magento` job is a newly updated component of the `gitlab-ci.yml` file, specifically designed for advanced unit testing of Magento native code, including code coverage generation. This job is essential for ensuring the quality and robustness of Magento's native codebase.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Execution and Reporting](#execution-and-reporting)
- [Scheduling and Failure Policy](#scheduling-and-failure-policy)
- [Example](#example)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To perform advanced unit testing with code coverage on Magento native code.
- **Execution Context**: Launched by a scheduled pipeline in GitLab.

## Configuration and Setup

- **Stage**: Allocated to the `test` stage.
- **Image**: Utilizes `meanbee/magento:7.0-cli`, tailored for Magento.
- **Tags**: Uses `docker-accor` for specific runner selection.

## Execution and Reporting

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

## Scheduling and Failure Policy

- **Execution Trigger**: Only runs for scheduled pipelines.
- **Allow Failure**: Set to `true`, indicating that pipeline success is not dependent on this job's success.

## Example

```yaml
unit_tests_coverage_magento:
  ...
  script:
    - ./bin/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_MAGENTO --colors=never
  ...
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
