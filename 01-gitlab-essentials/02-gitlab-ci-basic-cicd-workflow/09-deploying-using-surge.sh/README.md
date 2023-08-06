# Serverless Deployment using surge.sh

## Table of Contents

- [Introduction](#introduction)
- [What is Surge?](#what-is-surge)
- [Understanding Serverless Deployment](#understanding-serverless-deployment)
- [Getting Started with Surge](#getting-started-with-surge)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Deployment](#deployment)
- [Example: Deploying a Static Website](#example-deploying-a-static-website)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Deploying a static website is a common task that can be made simple and efficient with the right tools. One such tool is Surge, a platform that enables serverless deployment. This document explains what Surge is, how it works, and how to deploy a static website using this service.

## What is Surge?

Surge is a cloud platform designed for serverless deployment of websites. This tutorial provides an example of deploying a static website using `surge.sh`, which is an efficient and straightforward process.

**Key concepts**:

- Cloud platform for serverless deployments
- Easy to use and configure
- Simple deployment process
- Ideal for static websites

## Understanding Serverless Deployment

Serverless deployment means that you don't have to worry about managing the server where your application is running. Instead of taking care of the server's configuration, software, and other aspects, you simply instruct the platform to host your application.

The term "serverless" doesn't mean that there are no servers involved; rather, it signifies that the management of the server infrastructure is handled by the provider. You can focus on your code, and the platform takes care of the rest.

## Getting Started with Surge

### Requirements

To use Surge, you'll need to have Node.js installed on your system. It is a prerequisite for Surge's installation and usage.

### Installation

You can install Surge globally on your system using NPM (Node Package Manager) with the following command:

```bash
npm install --global surge
```

This will install Surge and make it available for use.

### Deployment

To deploy your website with Surge, follow these steps:

1. Open a terminal and run `surge`.
2. Enter your email and password to create an account with Surge. The same procedure is used for login.
3. Inside the public folder (recommended), Surge will automatically detect the path and link it.
4. For the domain name, you can leave whatever domain Surge has selected for you; it can be changed later.
5. Hit enter, and Surge will start to deploy the website. Upon success, it will publish the entire website to the provided address.

## Example: Deploying a Static Website

Here's a quick walkthrough of deploying a static website using Surge:

1. Install Surge using the command provided above.
2. Navigate to your website's public folder.
3. Run `surge` and follow the prompts.
4. Upon successful deployment, you'll receive an address where your site is live.

Within a matter of seconds, your static website is live on the cloud!

## Conclusion

Surge offers a hassle-free solution to deploy static websites without worrying about server configurations and software. It's an excellent choice for small to medium projects, making the deployment process streamlined and straightforward. If you're looking for a quick and efficient way to get your static site online, Surge is a tool worth considering.

## References

- [Surge Official Website](https://surge.sh/)
- [Serverless Architecture Documentation](https://www.serverless.com/learn/quick-start/)
- [Node.js Official Website](https://nodejs.org/)