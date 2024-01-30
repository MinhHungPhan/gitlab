# Overview of `spbuilder-analyse` Job in `gitlab-ci.yml`

## Introduction

The `spbuilder-analyse` job has been introduced in the latest update to the `gitlab-ci.yml` file, enhancing the code analysis phase of the CI/CD pipeline. This job leverages the Spbuilder tool along with other analysis tools to ensure code quality and adherence to standards.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Execution](#configuration-and-execution)
- [Scripts and Quality Checks](#scripts-and-quality-checks)
- [Artifact Management](#artifact-management)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To conduct a comprehensive code analysis using the Spbuilder tool, PHP CodeSniffer (PHPCS), PHP Mess Detector (PHPMD), and SmileAnalyser.
- **Configuration Files**: Utilizes `.spbuilder.yml` and `.smileanalyser.yml` for configuration settings.

## Configuration and Execution

```yaml
spbuilder-analyse:
    tags: [php71]
    stage: test
    before_script:
        - *ssh_provision
    # ... existing code ...
```

- **Stage**: Allocated to the `test` stage.
- **Tags**: Uses `php71` for runner selection.
- **Before Script**:
  - Implements `ssh_provision` for SSH setup.
  - Installs dependencies using Composer within the Software Collections (scl) environment for PHP 7.2.

## Scripts and Execution

```yaml
spbuilder-analyse:
    # ... existing code ...
    script:
        - scl enable rh-php72 'vendor/smile/spbuilder/bin/spbuilder analyze --ignore-tool=visualization'
        - test $(grep '<error ' build/logs/checkstyle.xml | wc -l) -le "$PHPCS_ALLOWED_ERROR" || (echo "Checking PHPCS failed, $(grep '<error ' build/logs/checkstyle.xml | wc -l) exceed $PHPCS_ALLOWED_ERROR errors" && false)
        - test $(grep '<violation ' build/logs/pmd.xml | wc -l) -le "$PHPMD_ALLOWED_ERROR" || (echo "Checking PHPMD failed, $(grep '<violation ' build/logs/pmd.xml | wc -l) exceed $PHPMD_ALLOWED_ERROR errors" && false)
        - test $(grep '<error ' build/logs/smileanalyser.xml | wc -l) -le "$SMILEANALYSER_ALLOWED_ERROR" || (echo "Checking SmileAnalyser failed, $(grep '<error ' build/logs/smileanalyser.xml | wc -l) exceed $SMILEANALYSER_ALLOWED_ERROR errors" && false)
    after_script:
        - 'curl --output checkstyle-valid.xml --header "PRIVATE-TOKEN: $GITLAB_USER_TOKEN" "https://git.smile.fr/api/v4/projects/6095/jobs/artifacts/develop/raw/build/logs/checkstyle.xml?job=spbuilder-analyse"'
        - 'curl --output pmd-valid.xml --header "PRIVATE-TOKEN: $GITLAB_USER_TOKEN" "https://git.smile.fr/api/v4/projects/6095/jobs/artifacts/develop/raw/build/logs/pmd.xml?job=spbuilder-analyse"'
        - 'curl --output smileanalyser-valid.xml --header "PRIVATE-TOKEN: $GITLAB_USER_TOKEN" "https://git.smile.fr/api/v4/projects/6095/jobs/artifacts/develop/raw/build/logs/smileanalyser.xml?job=spbuilder-analyse"'
        - diff -uB pmd-valid.xml build/logs/pmd.xml || true
        - diff -uB smileanalyser-valid.xml build/logs/smileanalyser.xml || true
        - diff -uB checkstyle-valid.xml build/logs/checkstyle.xml || true
    # ... existing code ...
```

### `script` Section

This section defines a series of commands that are executed as part of the job.

1. **SCL Enable Command**: 

- `scl enable rh-php72 '...'`: This command is used to enable a software collection (SCL), specifically `rh-php72`, which is likely a Red Hat Software Collection for PHP 7.2. This ensures that the specified version of PHP is used for the following commands.
- `'vendor/smile/spbuilder/bin/spbuilder analyze --ignore-tool=visualization'`: This seems to be a command to run an analysis tool (`spbuilder`) from the `vendor/smile/spbuilder/bin/` directory, ignoring the 'visualization' tool.

2. **Error Checks**: 

- The following commands check for errors in different logs (`checkstyle.xml`, `pmd.xml`, and `smileanalyser.xml`). They count the number of errors and compare them with predefined thresholds (`PHPCS_ALLOWED_ERROR`, `PHPMD_ALLOWED_ERROR`, `SMILEANALYSER_ALLOWED_ERROR`). If the number of errors exceeds the allowed threshold, the script prints a failure message and returns a non-zero exit status (`false`), indicating failure.

### `after_script` Section

These are commands executed after the main script commands.

1. **Fetching Artifacts**:

- Uses `curl` to download various XML files from a specified URL. These files are named `checkstyle-valid.xml`, `pmd-valid.xml`, and `smileanalyser-valid.xml`. The URLs include a private token for authentication.

2. **Comparing Reports**:

- The `diff -uB` command is used to compare the downloaded "valid" XML files with the ones generated in the `build/logs` directory. The `-uB` flags are for unified diff format and ignoring blank lines. The `|| true` at the end ensures that this command doesn't cause the script to fail even if differences are found.

## Artifact Management

```yaml
spbuilder-analyse:
    # ... existing code ...
    artifacts:
        paths:
            - build/logs/
        expire_in: 1 week
```

- **Artifacts**:
  - Stores logs from the analyses in `build/logs/` with a retention period of one week.

## Pipeline

```yaml
spbuilder-analyse:
    tags: [php71]
    stage: test
    before_script:
        - *ssh_provision
        - scl enable rh-php72 'composer install -q'
    script:
        - scl enable rh-php72 'bin/spbuilder analyze --ignore-tool=visualization'
        - test $(grep '<error ' build/logs/checkstyle.xml | wc -l) -le "$PHPCS_ALLOWED_ERROR" || (echo "Checking PHPCS failed, $(grep '<error ' build/logs/checkstyle.xml | wc -l) exceed $PHPCS_ALLOWED_ERROR errors" && false)
        - test $(grep '<violation ' build/logs/pmd.xml | wc -l) -le "$PHPMD_ALLOWED_ERROR" || (echo "Checking PHPMD failed, $(grep '<violation ' build/logs/pmd.xml | wc -l) exceed $PHPMD_ALLOWED_ERROR errors" && false)
        - test $(grep '<error ' build/logs/smileanalyser.xml | wc -l) -le "$SMILEANALYSER_ALLOWED_ERROR" || (echo "Checking SmileAnalyser failed, $(grep '<error ' build/logs/smileanalyser.xml | wc -l) exceed $SMILEANALYSER_ALLOWED_ERROR errors" && false)
    after_script:
        - grep '<error ' build/logs/checkstyle.xml | wc -l && grep '<violation ' build/logs/pmd.xml | wc -l && grep '<error ' build/logs/smileanalyser.xml | wc -l
    artifacts:
        paths:
            - build/logs/
        expire_in: 1 week
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