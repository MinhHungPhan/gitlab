# Dynamic Environments in GitLab CI

Welcome to this tutorial on how to leverage GitLab CI to create dynamic environments for each merge request. With this approach, developers, testers, product owners, and any stakeholders can view the changes in a real system without having to locally compile or start servers.

## Table of Contents

- [Introduction](#introduction)
- [Dynamic Environments](#dynamic-environments)
- [Setting Up Dynamic Environments](#setting-up-dynamic-environments)
- [Creating a New Environment](#creating-a-new-environment)
- [Benefits of Dynamic Environments](#benefits-of-dynamic-environments)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Currently, many teams operate with only two environments: staging and production. However, for larger teams working on numerous features, there's a clear advantage in having an environment for each feature branch. This allows stakeholders to visualize changes without the technical hassles.

## Dynamic Environments

- As each Merge Request / Branch is deployed to an environment, we can easily review the changes made.
- Sometimes it makes sense to run additional tests on a system that was deployed.
- Changes can be reviewed by non-developers as well (Tester, Product Owners/Project Managers, Domain Experts and so on).

## Setting Up Dynamic Environments

GitLab CI offers the capability to automatically spin up a dynamic environment for each merge request:

1. **System Review Stage**: This is where we aim to review the changes made. We can name this as `deploy review`.

2. **Jobs**: Here, we add a new job under the `deploy review` stage. The goal is to deploy our changes similar to how we deploy to production. 

3. **Environment Specification**: For each merge request, we specify the environment. Using GitLab's provided environment variable, we can generate a unique name for each environment like so:

```yaml
review/<branch-name> 
```

4. **URL Specification**: We also specify a dynamic URL for this environment. With GitLab's variables, we can ensure each branch has its own unique URL.

By implementing the above, every time we create a new branch, GitLab CI will automatically set up a new environment for that branch.

### Implementation

To give you a practical example, here's a configuration that accomplishes the above:

```yaml
deploy review:
  stage: deploy review
  only:
    - merge_requests
  environment:
      name: review/$CI_COMMIT_REF_NAME
      url: https://[YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
  script:
    - npm install --global surge
    - surge --project ./public --domain [YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
```
---

**Note**: Replace `[YOUR_DOMAIN_NAME]` with your domain name to ensure the correct URL is generated for each branch.

### Explanation

Alright! Let's break this GitLab job down step-by-step:

1. **Environment**:

```yaml
name: review/$CI_COMMIT_REF_NAME
```

- The environment's name is dynamically set based on the branch or tag name related to the commit using the variable `$CI_COMMIT_REF_NAME`.

- If you're working on a new feature and you push code to a branch named `feature-1`:
    - `$CI_COMMIT_REF_NAME` will automatically be set to `feature-1`.
    - Consequently, the environment's name becomes `review/feature-1`.

```yaml
url: https://[YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
```

- This defines the URL for the environment. The `$CI_ENVIRONMENT_SLUG` variable transforms the environment's name into a URL-friendly string, ensuring any special characters are safely translated.

- Assume your project domain is `[YOUR_DOMAIN_NAME]`. If your branch is named `feature-1`:
    - The environment's name, as discussed above, might be `review/feature-1`.
    - Translating this to a URL-friendly format using `$CI_ENVIRONMENT_SLUG` could result in `review-feature-1`.
    - Thus, the environment's URL becomes `https://[YOUR_DOMAIN_NAME]-review-feature-1.surge.sh`.

2. **Script**:

```yaml
script:
- npm install --global surge
- surge --project ./public --domain $STAGING_DOMAIN
```

- `npm install --global surge`: This command installs the "surge" package globally. Surge is a simple tool for deploying static websites.

- `surge --project ./public --domain [YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh`: This command deploys the content of the "./public" directory to the specified domain. The domain is dynamically set based on the environment slug (similar to the URL above).

In simpler terms, this job, when triggered by a merge request, will deploy a review version of your site using Surge to a unique URL based on the branch name.

## Creating a New Environment

Let's walk through the process of creating a new environment:

1. **Branch Creation**:

- Create a new branch and name it `feature/dynamic-environments`:

```bash
git checkout -b feature/dynamic-environments
```

- Make your modifications to the .gitlab-ci.yml file within this new branch:

```yaml
deploy review:
  stage: deploy review
  only:
    - merge_requests
  environment:
      name: review/$CI_COMMIT_REF_NAME
      url: https://[YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
  script:
    - npm install --global surge
    - surge --project ./public --domain [YOUR_DOMAIN_NAME]-$CI_ENVIRONMENT_SLUG.surge.sh
```

2. **Pipeline Extension**: 

Extend the pipeline to include the new branch.

In GitLab's `.gitlab-ci.yml` configuration, you can define which branches a job or a stage should run for. It's done using the `only` or `except` keywords. 

The above code already has an `only` keyword specifying `merge_requests`, which means the job will run only for merge requests. If you want the pipeline to run for the `feature/dynamic-environments` branch specifically (outside the context of a merge request), you'd adjust the configuration accordingly.

However, based on the provided information, you don't need to do anything extra, since the pipeline is set up to run for merge requests, and when you create a merge request from your new branch, the pipeline will be triggered.

3. **Dynamic Environment**: 

After pushing changes to the branch, you'll notice that a dynamic environment named `review/feature/dynamic-environments` gets created.

4. **Viewing the App**: 

The deployed app can now be accessed through a unique URL in the format `[YOUR_DOMAIN_NAME]-review-feature-dynamic-environments`.

Remember, all of this is automated. The use of variables ensures that the environment and its associated URL are dynamically generated based on the branch name.

## Benefits of Dynamic Environments

- **Accessibility**: Stakeholders can view changes without technical hurdles.
  
- **Feedback Loop**: Faster feedback on changes, allowing for quick iterations.

- **Simplicity**: While the deployment process remains simple, the ability to dynamically generate environments adds significant value.

## Conclusion

Leveraging dynamic environments streamlines the development and review process. This GitLab CI feature ensures every branch gets its unique environment, simplifying reviews and testing. While the configuration might seem overwhelming initially, once set up, it's relatively straightforward and offers considerable benefits.

## References

- [Environments and deployments](https://docs.gitlab.com/ee/ci/environments/#create-a-dynamic-environment)