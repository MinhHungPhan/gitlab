# Overview of `unit_test_all` Job in `gitlab-ci.yml`

## Introduction

The `unit_test_all` job, recently updated in the `gitlab-ci.yml` file, is a critical component of the testing stage in the CI/CD pipeline, specifically designed for running unit tests for both Magento and Accor. This job ensures the reliability and stability of the code during merge requests.

## Table of Contents

- [Job Description](#job-description)
- [External Dependencies for GitLab Pipeline](#external-dependencies-for-gitlab-pipeline)
- [Configuration Details](#configuration-details)
- [Scripts and Execution](#scripts-and-execution)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To run unit tests for Magento and Accor during merge requests.
- **Notable Features**: Deactivates Xdebug and does not generate code coverage, aiming to reduce execution time.

## External Dependencies for GitLab Pipeline

This section outlines the external dependencies required for our GitLab CI/CD pipeline. Ensure these are installed and properly configured in your environment to ensure smooth operation of the pipeline.

### SSH Setup

1. **OpenSSH Client**: Required for handling SSH connections.
2. **SSH Agent**: Used for managing private keys for public key authentication.

### Composer Setup

3. **Composer**: Dependency management tool for PHP. Essential for installing and managing PHP project dependencies.
4. **PHP Extensions**: Specific extensions like BCMath are required (`docker-php-ext-install bcmath`).

### Docker Environment

5. **Docker Image (`meanbee/magento:7.0-cli`)**: Custom Docker image for Magento development with PHP 7.0.

### Testing Tools

6. **PHPUnit**: PHP unit testing framework.

### Utilities

7. **Unix Tools**: Common tools like `wget`, `zip`, `unzip` for file operations.

### Custom Scripts

8. **Project-Specific Scripts**: Includes scripts like `add-gitlab-token.bash` and `get-composer.sh`.

### SonarQube Integration (Optional)

9. **SonarQube**: For code quality and security analysis.

### Magento Specific Tools

10. **Magento Tools**: Any Magento-specific tools or scripts used in the pipeline.

## Prerequisites for the `unit_test_all` Job

Before diving into the specifics of the `unit_test_all` job, it's essential to understand the prerequisites that set the stage for a successful deployment.

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

## Configuration Details

- **Stage**: Allocated to the `test` stage.
- **Image**: Uses `meanbee/magento:7.0-cli`, suitable for Magento projects.
- **Tags**: Tagged with `docker-accor` for specific runner selection.

## Scripts and Execution

1. **Before Script**:

```yaml
unit_test_all:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget zip unzip
        - docker-php-ext-install bcmath
        - *ssh_provision
        - find /usr/local/etc/php/conf.d/ -type f -name '*xdebug*.ini' -exec rm -f {} \;
    # ... existing code ...
```

- Updates and upgrades the system packages.
- Installs necessary tools like `wget`, `zip`, `unzip`.
- Installs PHP extension `bcmath`.
- Executes the `ssh_provision` and `composer` templates for SSH setup and Composer dependency management.
- Removes Xdebug configuration to enhance performance.

2. **Script**:

```yaml
unit_test_all:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    # ... existing code ...
    script:
        - vendor/phpunit/phpunit/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ALL
    # ... existing code ...
```

- Runs PHPUnit tests with a memory limit of 2048M using the `$PHPUNIT_CONFIG_ALL` configuration.

## Pipeline

```yaml
unit_test_all:
    stage: test
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    before_script:
        - apt update && apt upgrade -y
        - apt install -y wget zip unzip
        - docker-php-ext-install bcmath
        - *ssh_provision
        - find /usr/local/etc/php/conf.d/ -type f -name '*xdebug*.ini' -exec rm -f {} \;
    script:
        - vendor/phpunit/phpunit/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_ALL
    needs:
        -   job: composer-build
            artifacts: true
    except:
        refs:
            - tags
```

This example illustrates the PHPUnit execution command within the `unit_test_all` job, highlighting the increased memory limit and the use of a general PHPUnit configuration.

## Conclusion

The `unit_test_all` job significantly streamlines the testing process by focusing on speed and efficiency. By disabling Xdebug and forgoing code coverage, the job is optimized for quicker execution, providing fast feedback during merge requests. This approach is vital in maintaining high-quality code standards while efficiently managing CI/CD resources.

## References

- [meanbee/docker-magento on Github](https://github.com/meanbee/docker-magento)
- [Gitlab Anchors](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)
- [Composer documentation](https://getcomposer.org/doc/)
- [Official Composer Installation Documentation](https://getcomposer.org/download/)
- [PHP Unit official documentation](https://phpunit.de/documentation.html)
- [Using SSH keys with GitLab CI/CD](https://docs.gitlab.com/ee/ci/ssh_keys/)