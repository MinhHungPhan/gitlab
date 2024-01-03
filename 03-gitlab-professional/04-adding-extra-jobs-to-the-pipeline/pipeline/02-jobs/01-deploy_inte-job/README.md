# Overview of `deploy_inte` Job in `gitlab-ci.yml`

## Introduction

The `deploy_inte` job defined in your `gitlab-ci.yml` file is a critical component of the deployment stage in the CI/CD pipeline for the Magento project. It is specifically tailored for deploying to an integration environment.

## Table of Contents

- [Job Configuration](#job-configuration)
- [Scripts and Commands](#scripts-and-commands)
- [Trigger Conditions](#trigger-conditions)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Prerequisites for the Deployment Job

Before diving into the specifics of the `deploy_inte` job, it's essential to understand the prerequisites that set the stage for a successful deployment.

### `.deploy_provision`

The `.deploy_provision` anchor defines a series of commands that prepare the deployment environment:

- Updates the package list and installs essential packages like SSH, Python, Git, and others.
- Sets the system `PATH` to include necessary directories for the deployment process.
- Cleans up any existing distribution builds in the `./build/dist/` directory.

```yaml
.deploy_provision: &deploy_provision
    - apt update -yqq
    - apt install -yqq ssh openssh-client python git curl python-pip libldap2-dev libsasl2-dev bc locales
    - export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin:/usr/games:~/.local/bin
    - rm -rf ./build/dist/*
```

### `.get_pip`

The `.get_pip` anchor is used for setting up Pip, a package manager for Python. This step ensures that Pip is available for installing other Python-based tools necessary for the deployment process.

```yaml
.get_pip: &get_pip
    - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - python get-pip.py
    - pip install pipenv
```

### `.debug_ssh` (For After Script Debugging)

The `.debug_ssh` anchor provides a tool for debugging SSH issues. It's used in the `after_script` section of the job to list the contents of the SSH directory, helping to troubleshoot connection problems.

```yaml
.debug_ssh: &debug_ssh
    - ls -la ~/.ssh/
```

## Job Configuration

- **Image**: Uses `meanbee/magento:7.0-cli`, a Docker image tailored for Magento projects.
- **Tags**: Tagged with `docker-accor` to specify the runner type.
- **Stage**: Allocated to the `deploy` stage of the pipeline.

## Scripts and Commands

1. **Before Script**:

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    before_script:
        - *deploy_provision
        - *get_pip
        - pip install awscli --upgrade --user
        - "export s3_package='aws s3 ls s3://newaccorshop-releases/magento/inte01/ --profile accor-prod | sort | tail -n 2 | grep accor-magento | cut -d \'-\' -f 6- | tail -n 1'"
        - 'git clone https://gitlab-ci-token:${CI_JOB_TOKEN}@git.smile.fr/smile-outsourcing/client-architectures/accor-newaccorshop'
        #- cat /etc/locale.gen
        - export LC_ALL='en_US.UTF-8' && export LANG='en_US.UTF-8' && export LANGUAGE='en_US.UTF-8'
        - pip2 uninstall backports.functools-lru-cache && apt install python-backports.functools-lru-cache
        - *ssh_provision
        - echo '172.18.1.160 astoreshop-corenonprod-bastion1.aws.smile.fr' >> /etc/hosts
        - echo -e "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config
        - cd accor-newaccorshop/ansible/magento2/
        - git checkout in01
        - git pull
        - sed -i 's/ansible-playbook/ansible-playbook -vvvv/g' ./scripts/deploy.sh
    # ... existing code ...
```

- Executes `deploy_provision` and `get_pip` templates.
- Installs and updates the AWS CLI using Pip.
- Sets up an environment variable for S3 package paths.
- Clones a specific Git repository for deployment configurations.
- Sets locale configurations and installs necessary Python packages.
- Implements SSH provisions for secure connections.
- Modifies `/etc/hosts` and SSH configurations for deployment requirements.
- Prepares the Ansible environment by checking out and updating a specific branch and modifying deploy scripts for verbose output.

2. **Script**:

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    # ... existing code ...
    script:
        - './scripts/deploy.sh in01.aws_ec2.yml -p ${s3_package} -s'
    # ... existing code ...
```

- Executes the deployment script (`deploy.sh`) with specific arguments, including the S3 package path and silent mode.

3. **After Script**:

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    # ... existing code ...
    after_script:
        - *debug_ssh
    # ... existing code ...
```

- Executes the `debug_ssh` template to list the contents of the SSH directory, aiding in debugging.

## Trigger Conditions

- **Manual Trigger**: The job requires manual intervention to start.

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    # ... existing code ...
    when: manual
```

- **Tag-Based**: Triggered only for tags matching the pattern `magento-inte-[0-9]{8}-[0-9]{6}`.

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    # ... existing code ...
    only:
        refs:
            - tags
        variables:
            # magento-inte-19901113-010112
            - $CI_COMMIT_TAG =~ /^magento-inte-[0-9]{8}-[0-9]{6}$/
            # ... existing code ...
    when: manual
```

- **Project Path Condition**: Only executes for the `Accor/magento` project path.

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
    # ... existing code ...
    only:
        refs:
            - tags
        variables:
            # ... existing code ...
            - $CI_PROJECT_PATH == 'Accor/magento'    
    when: manual
```

## Pipeline

```yaml
deploy_inte:
    image: meanbee/magento:7.0-cli
    tags:
        - docker-accor
    stage: deploy
#    dependencies:
#        - package
    before_script:
        - *deploy_provision
        - *get_pip
        - pip install awscli --upgrade --user
        - "export s3_package='aws s3 ls s3://newaccorshop-releases/magento/inte01/ --profile accor-prod | sort | tail -n 2 | grep accor-magento | cut -d \'-\' -f 6- | tail -n 1'"
        - 'git clone https://gitlab-ci-token:${CI_JOB_TOKEN}@git.smile.fr/smile-outsourcing/client-architectures/accor-newaccorshop'
        #- cat /etc/locale.gen
        - export LC_ALL='en_US.UTF-8' && export LANG='en_US.UTF-8' && export LANGUAGE='en_US.UTF-8'
        - pip2 uninstall backports.functools-lru-cache && apt install python-backports.functools-lru-cache
        - *ssh_provision
        - echo '172.18.1.160 astoreshop-corenonprod-bastion1.aws.smile.fr' >> /etc/hosts
        - echo -e "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config
        - cd accor-newaccorshop/ansible/magento2/
        - git checkout in01
        - git pull
        - sed -i 's/ansible-playbook/ansible-playbook -vvvv/g' ./scripts/deploy.sh
    script:
        - './scripts/deploy.sh in01.aws_ec2.yml -p ${s3_package} -s'
    after_script:
        - *debug_ssh
    only:
        refs:
            - tags
        variables:
            # magento-inte-19901113-010112
            - $CI_COMMIT_TAG =~ /^magento-inte-[0-9]{8}-[0-9]{6}$/
            - $CI_PROJECT_PATH == 'Accor/magento'
    when: manual
```

This snippet illustrates the deployment script execution within the `deploy_inte` job, highlighting the use of specific parameters for targeted deployment.

## Conclusion

The `deploy_inte` job is a meticulously configured part of the deployment process, tailored for the Magento project's integration environment. It encompasses a series of pre-deployment checks, environment setups, and the execution of a detailed deployment script, ensuring a secure and efficient deployment process. The job's execution is contingent on specific tag patterns and is designed to be manually triggered, providing control and precision in the deployment process.

## References

- [meanbee/docker-magento on Github](https://github.com/meanbee/docker-magento)
- [Gitlab Anchors](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)
- [GitLab CI/CD Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [Magento and Docker Integration](https://devdocs.magento.com/cloud/docker/docker-development.html)
- [Understanding CI/CD Pipeline in GitLab](https://about.gitlab.com/topics/ci-cd/)
- [Ansible Documentation for Deployment Automation](https://docs.ansible.com/ansible/latest/index.html)
- [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)