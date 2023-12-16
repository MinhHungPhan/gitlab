# Overview of `spbuilder-analyse` Job in `gitlab-ci.yml`

## Introduction

The `spbuilder-analyse` job has been introduced in the latest update to the `gitlab-ci.yml` file, enhancing the code analysis phase of the CI/CD pipeline. This job leverages the Spbuilder tool along with other analysis tools to ensure code quality and adherence to standards.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Execution](#configuration-and-execution)
- [Scripts and Quality Checks](#scripts-and-quality-checks)
- [Artifact Management](#artifact-management)
- [Example](#example)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To conduct a comprehensive code analysis using the Spbuilder tool, PHP CodeSniffer (PHPCS), PHP Mess Detector (PHPMD), and SmileAnalyser.
- **Configuration Files**: Utilizes `.spbuilder.yml` and `.smileanalyser.yml` for configuration settings.

## Configuration and Execution

- **Stage**: Allocated to the `test` stage.
- **Tags**: Uses `php71` for runner selection.
- **Before Script**:
  - Implements `ssh_provision` for SSH setup.
  - Installs dependencies using Composer within the Software Collections (scl) environment for PHP 7.2.

## Scripts and Quality Checks

- **Script**:
  - Runs Spbuilder analysis, excluding the visualization tool.
  - Performs checks against set thresholds for PHPCS, PHPMD, and SmileAnalyser, using the corresponding allowed error variables (`PHPCS_ALLOWED_ERROR`, `PHPMD_ALLOWED_ERROR`, `SMILEANALYSER_ALLOWED_ERROR`).

- **Quality Gate Checks**:
  - Ensures that the number of errors detected by each tool does not exceed the predefined limits.

## Artifact Management

- **After Script**:
  - Reports the total number of errors detected by each tool for transparency.
- **Artifacts**:
  - Stores logs from the analyses in `build/logs/` with a retention period of one week.

## Example

```yaml
spbuilder-analyse:
  ...
  script:
    - scl enable rh-php72 'bin/spbuilder analyze --ignore-tool=visualization'
  ...
```

This example demonstrates how the Spbuilder analysis is executed within the job, showcasing the integration of quality checks and the use of Software Collections for a specific PHP version.

## Conclusion

The `spbuilder-analyse` job is a crucial addition to the CI/CD pipeline, focusing on maintaining high code quality standards. By integrating multiple code analysis tools and setting specific error thresholds, it ensures that the codebase remains clean, efficient, and adheres to best practices. This job represents a proactive approach to code quality management in the development process.

## References

- [Code Quality | GitLab](https://docs.gitlab.com/ee/ci/testing/code_quality.html)
- [GitHub - micheh/phpcs-gitlab](https://github.com/micheh/phpcs-gitlab)
- [GitLab CI/CD configuration for PHP_CodeSniffer](https://github.com/micheh/phpcs-gitlab)
- [PHPMD - PHP Mess Detector](https://phpmd.org/documentation/ci-integration.html)
- [Spbuilder configuration | GitHub Actions](https://github.com/storefront-bvba/elasticsuite-magento2/blob/master/Resources/spbuilder.yml)