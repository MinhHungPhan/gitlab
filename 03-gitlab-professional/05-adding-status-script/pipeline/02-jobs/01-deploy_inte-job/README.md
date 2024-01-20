# Overview of `deploy_inte` Job in `gitlab-ci.yml`

This README outlines the configuration for the `deploy_inte` job within the `gitlab-ci.yml` file, focusing on a deployment process tailored for a Magento-based project.

## Table of Contents

- [Prerequisites for the Deployment Job](#prerequisites-for-the-deployment-job)
- [Job Configuration](#job-configuration)
- [Pipeline Stages](#pipeline-stages)
- [Scripts and Commands](#scripts-and-commands)
- [Trigger Conditions and Execution](#trigger-conditions-and-execution)
- [Conclusion](#conclusion)
- [References](#references)

## Prerequisites for the Deployment Job

The `.deploy_provision` anchor defines a series of commands that prepare the deployment environment by updating package lists, installing essential packages, setting the system `PATH`, and cleaning up distribution builds.

```yaml
.deploy_provision: &deploy_provision
    - apt update -yqq
    - apt install -yqq ssh openssh-client python git curl python-pip libldap2-dev libsasl2-dev bc locales
    - export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin:/usr/games:~/.local/bin
    - rm -rf ./build/dist/*
```

The `.get_pip` anchor sets up Pip for Python package management, ensuring necessary tools are installed.

```yaml
.get_pip: &get_pip
    - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - python get-pip.py
    - pip install pipenv
```

The `.debug_ssh` anchor is used for SSH debugging in the `after_script` section, aiding in troubleshooting connection problems.

```yaml
.debug_ssh: &debug_ssh
    - ls -la ~/.ssh/
```

## Job Configuration

The `deploy_inte` job is configured with specific tags for the runner, allocated to the `deploy` stage in the pipeline. It includes environment variables for deployment settings and uses anchors for pre-deployment setup.

## Pipeline Stages

The job is part of a pipeline with the following stages:

1. Test
2. SonarQube Analysis
3. Deploy

```yaml
stages:
  - test
  - sonarqube-analysis
  - deploy
```

## Scripts and Commands

### Before Script

The `before_script` section includes:

- Executing `.deploy_provision` and `.get_pip` templates.
- Installing and updating the AWS CLI.
- Cloning a specific Git repository for deployment configurations.
- Preparing the Ansible environment for deployment.

```yaml
before_script:
    - *deploy_provision
    - *get_pip
    # ... additional commands ...
```

### Script

The main script executes deployment steps, including echoing the deployment plan and running cache clean-up scripts.

```yaml
script:
    - echo "We are about to deliver ${S3_PACKAGE} on ${DEPLOY_ENV}"
    - ./scripts/cache-clean.sh ${DEPLOY_ENV}.aws_ec2.yml
```

### After Script

Post-deployment, a PHP script is run for continuous delivery notifications.

```yaml
after_script:
    - php ci/script/continuous-delivery-notification.php
```

## Trigger Conditions and Execution

The deployment job is manually triggered and subject to conditions like specific tag patterns and branch names. The job allows failures, indicating its non-critical nature in the pipeline.

```yaml
only:
    refs:
        - tags
        - inte
    variables:
        - $CI_COMMIT_TAG =~ /magento-inte-[0-9]{8}-[0-9]{6}/
when: manual
allow_failure: true
```

## Conclusion

The `deploy_inte` job in the `gitlab-ci.yml` file is a crucial part of the deployment process, focusing on a Magento project. It is designed for flexibility and debugging ease, with a manual trigger option for controlled execution. This README serves as a guide for understanding and managing the deployment job in the project's CI/CD pipeline.

## References

- [Gitlab Anchors](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)
- [GitLab CI/CD Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [Magento and Docker Integration](https://devdocs.magento.com/cloud/docker/docker-development.html)
- [Understanding CI/CD Pipeline in GitLab](https://about.gitlab.com/topics/ci-cd/)
- [Ansible Documentation for Deployment Automation](https://docs.ansible.com/ansible/latest/index.html)
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)