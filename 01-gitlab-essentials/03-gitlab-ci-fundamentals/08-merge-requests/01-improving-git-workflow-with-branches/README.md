# Improving Git Workflow with Branches

## Table of Contents

- [Introduction](#introduction)
- [Benefits of Using Branches](#benefits-of-using-branches)
- [A Practical Workflow](#a-practical-workflow)
- [Branch Configuration in Pipelines](#branch-configuration-in-pipelines)
- [GitLab Pipeline Example](#gitlab-pipeline-example)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In this tutorial, we will explore the advantages of using branches to enhance your Git workflow. A robust branching strategy ensures a consistent and deployable `main` branch, aiding in continuous deployment and delivery.

## Benefits of Using Branches

A well-structured branch strategy can offer the following benefits:

1. **Safeguarding the main Branch**: By isolating changes in branches, we prevent the `main` branch from becoming undeployable due to mistakes.
   
*Example*: A developer removes an essential import in the `main` branch, rendering the entire branch undeployable. By working in branches, such changes can be tested thoroughly before merging to the `main`.

2. **Continuous Deployment**: To maintain a rhythm of continuous deployment and delivery, ensuring that the main branch remains deployable at all times is crucial.

3. **Flexibility**: There are different branching models available, such as Git flow. The choice depends on what suits an organization's needs best. At the minimum, even having just a development and main branch can help segregate the development work from stable releases.

## A Practical Workflow

While numerous workflows exist, here's a simple one to consider:

1. Create a branch for each feature or bugfix.
2. Test changes in this branch.
3. Once ready, merge the branch into `main`.
4. Deploy from the `main` branch to production.

*Example*: If you wanted to modify the title of a website:

1. Create a branch named `feature/new-title`.
2. Make the changes in this branch.
3. Once tested, merge back to the main branch for deployment.

## Branch Configuration in Pipelines

When using CI/CD pipelines, like those in GitLab, not every pipeline stage might be relevant for feature branches. For instance, while you might want to build and test your changes in a feature branch, deploying them to production directly from this branch might not be desired.

By configuring the pipeline, you can determine which stages run for which branches. 

## GitLab Pipeline Example

Here's an example of a GitLab pipeline configuration:

```yaml
image: node

stages:
  - build
  - test
  - deploy staging
  - deploy production
  - production tests

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/

variables:
  STAGING_DOMAIN: instazone-staging.surge.sh
  PRODUCTION_DOMAIN: instazone.surge.sh

#... [rest of the pipeline details]

deploy staging: 
  stage: deploy staging
  environment:
    name: staging
    url: http://$STAGING_DOMAIN
  only:
    - main  
  #...

deploy production: 
  stage: deploy production
  environment:
    name: production
    url: $PRODUCTION_DOMAIN
  only:
    - main    
  #...

production tests:
  image: alpine
  stage: production tests
  only:
    - main  
  #...
```

In this configuration, the deployment to staging, deployment to production, and production tests will only be executed for the `main` branch.

1. Start by pushing your new changes to GitLab.
2. Navigate to GitLab and go to: Console > Code > Branches.
3. Create a new branch from `main` and name it `feature/new-title`.
4. Once the `feature/new-title` branch is created, the pipeline will automatically initiate.
5. For this branch, the pipeline will be quicker because it only runs the Build and Test stages.

## Conclusion

Employing a structured branching strategy and configuring your pipelines accordingly can significantly improve your Git workflow. This ensures that your `main` branch remains deployable and aligns with best practices for continuous deployment and delivery.

## References

- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/#onlyexcept-basic)
- [Atlassian's Guide on Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)