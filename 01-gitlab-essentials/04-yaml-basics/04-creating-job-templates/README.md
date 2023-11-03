# Creating Job Templates in GitLab CI

Welcome to this guide on how to create job templates in GitLab CI/CD pipelines using the YAML language. This document is structured to be beginner-friendly and includes practical examples to help you grasp the concepts quickly.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Understanding the Basics](#understanding-the-basics)
- [Creating Job Templates](#creating-job-templates)
- [Applying Job Templates](#applying-job-templates)
- [Validation and Testing](#validation-and-testing)
- [Committing and Pushing Changes](#committing-and-pushing-changes)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This guide covers the process of creating reusable job templates in GitLab CI/CD pipelines, utilizing the YAML language. GitLab CI/CD pipelines help automate the stages of your application development, from building and testing to deployment. However, as projects grow, you might find yourself writing similar job definitions multiple times, which can become tedious and prone to errors. By the end of this guide, you should be able to define job templates, apply them to different environments, and streamline your CI/CD pipeline configurations.

## Prerequisites

Before we start, ensure that you have:

1. A GitLab account and a repository with a `.gitlab-ci.yml` file.
2. Basic understanding of Git commands and CI/CD concepts.
3. A text editor of your choice.

## Understanding the Basics

In GitLab CI/CD, jobs are defined in the `.gitlab-ci.yml` file located at the root of your repository. A job defines what to do, under what conditions it should be executed, and on which environment. When defining multiple jobs, you might notice that some parts of the job definitions are similar or even duplicated. 

For example, consider having three jobs for deploying your application to review, staging, and production environments. The deployment steps for staging and production might be very similar, differing only in the domain name used for deployment. Instead of writing the entire job definition for each environment, you can define a template and reuse it across different jobs.

## Creating Job Templates

**Define a Job Template**: A job template is defined in the `.gitlab-ci.yml` file and starts with a dot (.) followed by the template name. For instance, `.deploy_template`. The dot (.) prefix prevents GitLab from executing the template as a job. 

```yaml
.deploy_template: &deploy
  only:
    - master
  script:
    - npm install --global surge
    - surge --project ./public --domain $DOMAIN
  environment:
    url: http://$DOMAIN
```

In this example, the `.deploy_template` defines common settings for deployment jobs, such as the script to run and the environment URL. The `$DOMAIN` variable will be defined in the specific jobs that use this template.

## Applying Job Templates

**Using the Template in Jobs**: To use the template in a job, use the YAML merge key (`<<`) followed by a reference to the template (`*template_name`).

```yaml
deploy staging:
  <<: *deploy
  stage: deploy staging
  variables:
    DOMAIN: $STAGING_DOMAIN
  environment:
    name: staging
```

In this job, we are using the `.deploy_template` template and providing specific values for the `DOMAIN` variable and environment name.

Next, you can use this template in your actual `deploy production` job like so:

```yaml
deploy production:
  <<: *deploy
  stage: deploy production
  variables:
    DOMAIN: $PRODUCTION_DOMAIN
  environment:
    name: production
```

## Validation and Testing

**Validating the CI/CD Configuration**: Before committing your changes, validate your `.gitlab-ci.yml` file using the CI Lint tool in GitLab. Navigate to CI/CD > CI Lint in your project's settings, paste your configuration, and click on Validate.

## Committing and Pushing Changes

**Pushing Your Changes**: After validation, follow these steps to commit and push your changes:

```sh
❯ git pull
❯ code .  # Open the repository in Visual Studio Code (or your preferred text editor)
❯ git checkout -b feature/job-templates  # Create a new branch for your changes
❯ git status  # Check the status of your changes
❯ git add .  # Add all changes to staging
❯ git commit -m "added job templates"  # Commit your changes
❯ git push --set-upstream origin feature/job-templates  # Push your changes and set the upstream branch
```

GitLab will provide a link to create a merge request for your changes after pushing.

Make sure to monitor the pipeline and ensure that all jobs are running as expected. You should see that `deploy staging` and `deploy production` are using the configurations from the template, and they’re successfully deploying to their respective environments.

## Conclusion

You have now learned how to create reusable job templates in GitLab CI/CD, which helps in reducing duplication, making your `.gitlab-ci.yml` file cleaner and easier to maintain. By using templates, you ensure consistency across different jobs and simplify updates since changes to the template automatically apply to all jobs using it.

Remember, practice makes perfect! Don’t hesitate to experiment with job templates and apply them to various parts of your pipeline to see how they can help optimize your CI/CD process. Happy coding! 🚀

## References

- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [YAML Language Specification](https://yaml.org/spec/1.2/spec.html)
- [GitLab CI/CD Variables](https://docs.gitlab.com/ee/ci/variables/)
- [GitLab CI Lint Tool](https://docs.gitlab.com/ee/ci/lint.html)