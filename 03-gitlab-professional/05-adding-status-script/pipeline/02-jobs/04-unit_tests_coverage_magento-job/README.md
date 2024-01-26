# Overview of `unit_test_coverage_magento` Job in `gitlab-ci.yml`

## Introduction

This README outlines the configuration and usage of key jobs in the `gitlab-ci.yml` file for a Magento project. These jobs are crucial for managing dependencies, running unit tests, and ensuring code quality in the continuous integration pipeline.

## Table of Contents

- [SSH Provisioning for Composer Dependencies](#ssh-provisioning-for-composer-dependencies)
- [Stages](#stages)
- [Unit Tests Coverage for Magento Native Code](#unit-tests-coverage-for-magento-native-code)
- [Conclusion](#conclusion)
- [References](#references)

## SSH Provisioning for Composer Dependencies

The `.ssh_provision` job is crucial for setting up SSH in the CI/CD pipeline, facilitating secure interactions with other services for Composer dependencies.

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

## Stages

Defines the order of stages in the CI/CD pipeline:

```yaml
stages:
  - build
  - test
  - sonarqube-analysis
  - deploy
```

## Unit Tests Coverage for Magento Native Code

The `unit_tests_coverage_magento` job is designed for advanced unit testing with code coverage generation, specifically for Magento native code. It's triggered by scheduled pipelines in GitLab.

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
    script:
        - vendor/phpunit/phpunit/phpunit -d memory_limit=2048M -c $PHPUNIT_CONFIG_MAGENTO --colors=never
    after_script:
        # Used for code coverage parsing
        - cat $PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_TXT_MAGENTO
    artifacts:
        when: always
        expire_in: 1 week
        paths:
            - 'phpunit/coverage/'
    only:
        - schedules
    allow_failure: true
    needs:
        -   job: composer-build
            artifacts: true
```

## Conclusion

This README provides an overview of the key jobs in the `gitlab-ci.yml` file for a Magento project, focusing on SSH provisioning, Composer dependency management, and unit test coverage. These configurations are integral to maintaining code quality and efficiency in the CI/CD pipeline.

## References

- [meanbee/docker-magento on Github](https://github.com/meanbee/docker-magento)
- [Gitlab Anchors](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)
- [GitLab CI/CD Pipeline Documentation](https://docs.gitlab.com/ee/ci/)
- [Magento Official Documentation](https://devdocs.magento.com/)
- [Composer Official Documentation](https://getcomposer.org/doc/)
- [PHPUnit Official Website](https://phpunit.de/)