# Deploying the project using GitLab CI

Welcome to a guide on deploying your website using GitLab CI. We'll walk you through a step-by-step process, ensuring that by the end, even beginners will have a firm grasp of the concept.

## Table of Contents

- [Introduction](#introduction)
- [Setting Up the Deployment Stage](#setting-up-the-deployment-stage)
- [Defining the Node Image](#defining-the-node-image)
- [Installation and Configuration](#installation-and-configuration)
- [Deployment and Viewing Logs](#deployment-and-viewing-logs)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

The deployment process can be significantly streamlined and automated with the right tools. This guide specifically focuses on using GitLab CI, a powerful continuous integration tool, to achieve seamless deployments without the need for manual intervention from your local computer.

## Setting Up the Deployment Stage

Begin by defining a new stage for your deployment. For this guide, we will name this stage `deploy`. 

```yaml
stages:
  - build
  - test
  - deploy
```

You can choose to name your job anything you like, but for demonstration purposes, we'll refer to it as `deploy to surge`

```yaml
deploy to surge: 
  stage: deploy
```

## Defining the Node Image

If you've been using the node image across multiple jobs, it's efficient to set a default image. To do this, move the node image declaration to the top of your configuration. By setting it as a default, every job under GitLab CI will automatically use the node image unless specified otherwise.

```yaml
image: node
```

## Installation and Configuration

Unlike previous setups where tools like Gatsby might have been essential, our focus is now on `surge`. 

To install surge globally, use the command:

```bash
npm install --global surge
```

Once installed, deploy your project with surge using the following syntax:

```bash
surge --project ./public --domain [YOUR_DOMAIN_NAME].surge.sh
```

Here, `./public` points to the path of your project, and you should replace `[YOUR_DOMAIN_NAME]` with the desired domain name. Ensure that the domain you select is unique and not already registered. 

**Tip**: You can utilize domain name generators like Dotomator for creative domain suggestions.

Since your tokens are already set as environment variables, you don't need to specify them; `surge` will automatically access them for authentication.

## Deployment and Viewing Logs

After defining the deployment stage, it's crucial to assign the "Deploy to surge" job to this stage. If not, the job will default to the `test` stage. The correct sequence would be to first run the tests and then, only if they succeed, execute the deployment.

Your pipeline should now comprise:
1. The build stage
2. The test stage (runs in parallel)
3. The deploy stage (only executed if the previous stages are successful)

After a successful pipeline run, inspect the logs. If everything has gone as planned, you'll see that `surge` has been installed, your project has been published, and your chosen domain has been registered. You can now access the website using the provided URL, showcasing a site deployed via `surge` and orchestrated through GitLab CI.

## Conclusion

Congratulations! You have successfully deployed a website using GitLab CI and `surge`. This automated method ensures a streamlined deployment process, eliminating manual steps and potential errors. Thank you for following along, and happy deploying!

## References

- [Dotomator Web 2.0 Name Generator](https://www.dotomator.com/web20.html)