# Adding Status Script

## Introduction

This document provides a detailed overview of the recent updates made in our project's Git repository, particularly focusing on the latest commit. It aims to shed light on the various improvements and alterations introduced in the codebase.

## Table of Contents

- [Introduction](#introduction)
- [Detailed Comparison](#detailed-comparison)
- [Examples](#examples)
- [Conclusion](#conclusion)
- [References](#references)


## Detailed Comparison

The latest commit has introduced several key changes, especially in the `.gitlab-ci.yml` file:
1. **Build Stage Addition**: A new `composer-build` stage has been added. This stage is dedicated to building composer dependencies.
2. **Transition to Python3 and Pip3**: The script now utilizes Python3 and Pip3, indicating a shift from the older Python versions.
3. **Enhanced Script Security with Sudo**: Key commands in the script are now executed with `sudo`, enhancing the security and robustness of the script.
4. **Optimizations in the Deployment Process**: The deployment script (`deploy_inte`) has been revised for better efficiency, including changes to environment variables and the addition of a new `DEPLOY_ENV` variable.

## Examples

- **Build Stage Addition**:

```yaml
composer-build:
    stage: build
    ...
    script:
        - sh ci/script/get-composer.sh
        - bin/composer self-update 1.10.17
        - composer install -q
```

- **Python3 and Pip3 Usage**:

```yaml
.get_pip:
    - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - python3 get-pip.py
    - pip3 install pipenv
```

- **Enhanced Security with Sudo**:

```yaml
.deploy_provision:
    - sudo apt update -yqq
    - sudo apt install -yqq ssh openssh-client python git curl python-pip libldap2-dev libsasl2-dev bc locales
```

## Conclusion

The latest commit enhances the project's CI/CD pipeline by introducing a new build stage, shifting to more current versions of Python, increasing script security with sudo usage, and optimizing the deployment process. These changes collectively improve the efficiency, security, and maintainability of the project.

## References

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Composer Documentation](https://getcomposer.org/doc/)