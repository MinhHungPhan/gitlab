# Defining and Using Variables

In this tutorial, we'll discuss how to effectively define and utilize variables within GitLab CI, making your CI/CD pipeline more maintainable and modular.

## Table of Contents

- [Introduction](#introduction)
- [Why Use Variables?](#why-use-variables)
- [Setting Up Variables](#setting-up-variables)
- [Examples: Implementing Variables](#examples-implementing-variables)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

GitLab CI/CD is a robust tool to automate the deployment pipeline. While working on it, you might find repetitive tasks or values that can be better managed. One effective way is through variables. 

## Why Use Variables?

Ever noticed repetitive values or strings like domain names spread throughout your configuration file? Redundancy can lead to mistakes, especially if you need to update that value later. This is where variables come in handy. They ensure:

- **Reduced Duplication:** Avoid having the same value repeated in numerous places.
- **Flexibility:** Change the variable once, and the updated value gets reflected everywhere it's referenced.
- **Clarity:** Make your scripts more readable and maintainable.

## Setting Up Variables

Variables are not just for secrets, although they're great for that too. To set up a variable in GitLab CI:

1. Navigate to your project in GitLab.
2. Go to `Settings > CI/CD`.
3. Under the `Variables` section, you can define your variable.

## Examples: Implementing Variables

Imagine you have multiple instances where you need to mention staging and production domains. Instead of writing the domain directly, you can define them as variables:

```yaml
variables:
  STAGING_DOMAIN: [YOUR_DOMAIN_NAME]-staging.surge.sh
  PRODUCTION_DOMAIN: [YOUR_DOMAIN_NAME].surge.sh
```

Now, wherever you need to mention these domains in your script, just reference the variables:

```yaml
deploy staging: 
  stage: deploy staging
  environment:
    name: staging
    url: http://$STAGING_DOMAIN
  script:
    - npm install --global surge
    - surge --project ./public --domain $STAGING_DOMAIN

deploy production: 
  stage: deploy production
  environment:
    name: production
    url: $PRODUCTION_DOMAIN
  script:
    - npm install --global surge
    - surge --project ./public --domain $PRODUCTION_DOMAIN

production tests:
  image: alpine
  stage: production tests
  script:
    - apk add --no-cache curl
    - curl -s "https://$PRODUCTION_DOMAIN" | grep -q "$CI_COMMIT_SHORT_SHA"
```

By doing this, if ever there's a need to change the domain, you only have to modify the variable's value, making the process more efficient.

## Conclusion

Using variables in GitLab CI not only enhances the readability of your scripts but also adds a layer of abstraction, making modifications smoother. Whether it's domain names or other frequently used values, always consider variables as a tool in your GitLab CI arsenal to avoid repetition and maintain clarity.

I hope this tutorial helps you understand the importance and usage of variables in GitLab CI. Happy coding! 🌱

## References

- [GitLab CI/CD Variables Documentation](https://docs.gitlab.com/ee/ci/variables/)