# Managing Secrets with GitLab CI

## Table of Contents

- [Introduction](#introduction)
- [Understanding Secrets](#understanding-secrets)
- [Generating Tokens](#generating-tokens)
- [Managing Secrets in GitLab](#managing-secrets-in-gitlab)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to our tutorial! Today, we'll explore how to manage secrets using GitLab. While working on projects, it's crucial to secure any sensitive data such as credentials, tokens, and passwords. We will discuss how GitLab CI helps us store such secrets and deploy a website to a platform (we'll use 'search' as a placeholder name for our example). Remember, this is a beginner-friendly guide and our objective is to keep things simple and understandable.

## Understanding Secrets

Secrets refer to sensitive data like usernames, passwords, tokens, etc., that you wouldn't want exposed in your project files or pipelines. In general, anything committed inside Git shouldn't contain such sensitive data. GitLab CI, fortunately, provides us with a convenient method to store such secrets.

## Generating Tokens

Let's start with generating a token from `surge`. Tokens serve as an alternative to using your username and password for deployments. This approach increases security as tokens can be revoked if you think they've been compromised without changing your username and password. 

Follow these steps:
1. Navigate to your website's public folder and type in `surge token`. 
2. Assuming you're logged in, `surge` will generate a token for you.

## Managing Secrets in GitLab

Now, let's transition over to GitLab to see how we can manage secrets. 

1. **Navigating to Settings**: On your project sidebar, navigate to the bottom and find 'settings'. Hover over it and select 'secrecy'.

2. **Adding Variables**: Expand the 'variables' section and click on 'Add variable'.

3. **Adding Search Login Variable**: For the variable key, input `SURGE_LOGIN`, which corresponds to your email address. Notice a flag called 'protect variable' is enabled by default. This means this variable will only be available on protected branches and tags, such as the main or master branch. If you want this information to be available on other branches, disable this flag.

4. **Adding Search Token Variable**: Add another variable named `SURGE_TOKEN` and paste the token you generated from `surge`. As before, disable 'protect variable', but this time enable 'mask variable'. This masks the variable in logs, adding an extra layer of security.

Now, you have successfully stored your secrets in GitLab. These secrets can now be used across your projects without revealing sensitive information.

## Conclusion

Managing secrets in GitLab is crucial for the security of your project. Remember to never commit sensitive data in your pipelines or project files. Use tokens instead of usernames and passwords for deployments. Take advantage of GitLab's features to secure your secrets effectively. We hope this guide made these processes more understandable and accessible for beginners!

## References

- [GitLab Documentation](https://docs.gitlab.com/ee/ci/variables/)
- [GitLab Secrets Management](https://about.gitlab.com/blog/2020/12/07/gitlab-secrets-management/)