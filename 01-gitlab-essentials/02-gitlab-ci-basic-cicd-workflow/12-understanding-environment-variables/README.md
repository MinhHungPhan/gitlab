# Environment Variables in Deployment Tools

## Table of Contents

- [Introduction](#introduction)
- [Understanding Surge's Behavior](#understanding-surges-behavior)
- [Why Environment Variables?](#why-environment-variables)
- [Naming Conventions & Importance](#naming-conventions--importance)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

When working with deployment tools like Surge, beginners often wonder about the mechanism behind the command execution, especially regarding authentication and configuration. This guide aims to shed light on how Surge and many other tools manage configuration using environment variables.

## Understanding Surge's Behavior

Executing a command for deployment might seem straightforward, but there are underlying processes at work. For instance, when deploying with Surge, even if you only specify the project's location and domain name, Surge magically knows which account to deploy to and obtains the necessary permissions. This raises a question: How does it know?

## Why Environment Variables?

Many Command Network Interface (CNI) tools utilize environment variables to streamline the configuration process. Without them, each command would need to include lengthy authentication details, making it cumbersome for users.

For instance:

```bash
command deploy --project=path/to/project --domain=example.com
```

If we had to append username and token:

```bash
command deploy --project=path/to/project --domain=example.com --user=your_username --token=your_token
```

This not only elongates the command but also complicates the process. With environment variables, the tool can fetch required parameters in a standardized way, making commands concise and clear.

## Naming Conventions & Importance

Not all environment variables are fetched. Tools like Surge look for specific variable names. For Surge, it might be something like `SURGE_LOGIN` for the email and `SURGE_TOKEN` for the authentication token. 

An example of setting these would be:

```bash
export SURGE_LOGIN=your_email@example.com
export SURGE_TOKEN=your_auth_token
```

If these variables aren't named precisely as expected, the tool might not recognize them. Thus, always refer to the documentation to understand the exact naming conventions.

## Conclusion

Tools like Surge utilize environment variables to simplify commands and reduce configuration overhead. For effective usage, it's essential to understand the tool's naming conventions and set environment variables accordingly. This can greatly streamline your deployment processes, especially in continuous integration and deployment pipelines.

## References

- [Surge official documentation](http://surge.sh/help/)
- [Environment Variables in Unix](https://www.tutorialsteacher.com/unix/unix-environment-variables)
- [Integrating with Travis CI](https://surge.sh/help/integrating-with-travis-ci)