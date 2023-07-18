# Building The Project Locally

## Table of Contents

- [Introduction](#introduction)
- [The Gatsby Build Process](#the-gatsby-build-process)
- [The Role of Minification](#the-role-of-minification)
- [The Build Folder](#the-build-folder)
- [Inspecting the Build Folder](#inspecting-the-build-folder)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to this guide! If you've started using Gatsby and have generated a project and started the local development server, you're off to a great start! However, preparing your website for deployment might require a few additional steps. In this guide, we will walk you through how to create a production-ready build for your Gatsby website. 

## The Gatsby Build Process

While you've been developing locally, the code you have is typically different from what you would deploy in a production environment. Almost every tool comes with a 'build' step that prepares your code for deployment.

This might involve compiling some code. In our case, for a simple Gatsby website, this typically includes generating some JavaScript code. Let's take the example of running `gatsby build` command. Upon running it, Gatsby generates a new folder which will contain the production-ready version of our website that we can deploy somewhere. 

Example:

```bash
gatsby build
```

## The Role of Minification

In addition to generating necessary resources, these resources also need to be minified. Minification reduces the size of your files, making them faster to load in a user's browser. This is a step typically reserved for the build process and is not something you'd do while developing the application, as it can be time-consuming.

## The Build Folder

Gatsby creates a new folder during the build process, but instead of calling it 'build', it names it 'public'. The name 'public' indicates that the files within it are intended to be public-facing, i.e., they're the ones your users will interact with. 

## Inspecting the Build Folder

Inside the 'public' folder, you will find an `index.html` file along with some JavaScript files and other necessary resources. This folder is essentially the 'artifact' of your website, the product of your build process that you want to preserve and deploy on a server.

For instance, let's examine the contents of the 'public' folder:

```bash
cd public
ls
```

At this point, we have completed the build process locally and generated a 'public' folder ready for deployment.

The next logical step would be to automate these steps using continuous integration (CI) tools such as GitLab CI, enabling your build process to execute automatically whenever changes are made to your source code.

## Conclusion

Understanding the build process is a critical step in deploying your Gatsby projects effectively. By following these steps, you can create production-ready builds of your Gatsby websites, and by utilizing CI tools like GitLab CI, you can automate this process to increase productivity and efficiency.

## References

- [Gatsby Official Docs](https://www.gatsbyjs.com/docs/)
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [Introduction to Minification](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/javascript-startup-optimization)