# Deployment Environments

In this guide, we will discuss enhancing our continuous deployment pipeline by introducing a staging environment. This additional environment serves as a bridge between development and production, providing a testing ground that closely mimics the production system.

## Table of Contents

- [Introduction](#introduction)
- [Need for a Staging Environment](#need-for-a-staging-environment)
- [Modifying the Pipeline](#modifying-the-pipeline)
- [Using GitLab Environments](#using-gitlab-environments)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Continuous integration and continuous deployment (CI/CD) have become the backbone of modern software development. With CI, the focus is on integrating code from different sources, building it, and ensuring it passes unit tests. On the other hand, CD focuses on the delivery or deployment of the integrated code.

## Need for a Staging Environment

A continuous deployment pipeline without a staging environment poses two significant challenges:

1. **Direct Deployment to Production**: Deploying changes directly to the production system can be risky. Mistakes that aren't caught in CI tests can lead to outages or other issues for end-users.
2. **Lack of Change Review**: Without a staging system similar to production, there's no way to review and test the changes in a realistic environment.

Thus, a staging environment lets developers test their code changes in a system that closely resembles the production environment, ensuring that what works in staging will likely work in production.

## Modifying the Pipeline

Let's start by making a few adjustments to our existing pipeline:
- Change "deploy" to "deploy production".
- Rename "deployment tests" to "production tests".
  
The new pipeline structure is as follows:
1. build
2. test
3. deploy staging
4. deploy production
5. production tests

```yaml
image: node

stages:
  - build
  - test
  - deploy staging
  - deploy production
  - production tests
```

## Using GitLab Environments

- GitLab provides a feature known as "environments" which helps track deployments across different stages. You can tag your jobs, allowing GitLab to monitor your deployment progress.

- Environments allow you to control the continuous delivery / deployment process

- Easily track deployments

- You will know exactly what was deployed and on which environment

- You will have a full history of your deployments

### Configuration

1. For the staging deployment job:

```yaml
deploy staging: 
  stage: deploy staging
  environment:
    name: staging
    url: http://[YOUR_DOMAIN_NAME]-staging.surge.sh
  script:
    - npm install --global surge
    - surge --project ./public --domain [YOUR_DOMAIN_NAME]-staging.surge.sh
```

2. For the production deployment job:

```yaml
deploy production: 
  stage: deploy production
  environment:
    name: production
    url: http://[YOUR_DOMAIN_NAME].surge.sh
  script:
    - npm install --global surge
    - surge --project ./public --domain [YOUR_DOMAIN_NAME].surge.sh
```

Now, within GitLab, you can navigate to **Operations** -> **Environment** to view the status of each environment, including the latest deployed commit and a direct link to the environment.

## Conclusion

A staging environment is a crucial addition to any continuous deployment pipeline. It offers an intermediate testing ground, ensuring smoother and safer deployments to the production system. By utilizing GitLab's environment feature, developers can keep track of their deployment status across different stages.

## References

- [GitLab Environments Documentation](https://docs.gitlab.com/ee/ci/environments/)