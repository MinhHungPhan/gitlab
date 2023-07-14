# Building Your First Static Website with Gatsby 

Welcome to this guide where we'll take you through the steps to start a completely new project with Gatsby, an open-source static website generator. The aim is to build a simple, static website and we'll be using the Gatsby CLI (Command Line Interface) to do so. This guide is suitable for beginners with basic knowledge about the command line and npm.

## Table of Contents

- [Introduction](#Introduction)
- [Installation and Setup](#Installation-and-Setup)
- [Creating a New Gatsby Project](#Creating-a-New-Gatsby-Project)
- [Starting the Development Server](#Starting-the-Development-Server)
- [Hosting on GitLab](#Hosting-on-GitLab)
- [Conclusion](#Conclusion)
- [References](#References)

## Introduction

Gatsby is a free and open-source framework based on React that helps developers build blazing-fast websites and apps. It allows developers to build static websites that can be deployed anywhere, from GitHub Pages to AWS S3.

## Installation and Setup

Before using Gatsby, we need to install it, and this is done via npm (Node Package Manager). Please ensure that Node.js and npm are already installed on your computer. You can check if they are installed by typing `node --version` and `npm --version` into the terminal. If they're installed, the version number of each will be displayed.

Once Node.js and npm are confirmed to be installed, you can proceed with installing Gatsby CLI by entering the following command in your terminal:

```bash
npm install -g gatsby-cli
```
The `-g` flag indicates that the npm dependency is to be installed globally on your computer.

## Creating a New Gatsby Project

To create a new website, use the Gatsby CLI tool with the command `gatsby new`. Here's an example:

```bash
gatsby new static-website
```

This command creates a new folder named "static-website" with the initial Gatsby setup. You can replace "static-website" with the name of your project.

## Starting the Development Server

Navigate into the newly created project's directory using the command `cd static-website`, then start the local development server with `gatsby develop`. This compiles the project and starts a local HTTP server.

```bash
gatsby develop
```

You can then view your website in a web browser at the address `http://localhost:8000`.

## Hosting on GitLab

To make your website accessible to others, you can host it on GitLab. Create a new project on GitLab and name it as per your choice, for instance, "my-static-website". 

If you're happy with your local git repository, you can push the files directly to GitLab. Add GitLab as a remote and push the changes:

```bash
git remote add origin <your-gitlab-repo-url>
git push --set-upstream origin main
```

Refresh your GitLab project page, and you'll find all your committed files present there.

## Conclusion

With these steps, you have successfully set up a Gatsby project, developed a simple static website, and hosted it on GitLab. You can now continue adding more features to your website. Happy coding!

## References

- [Gatsby Quick Start Guide](https://www.gatsbyjs.com/docs/quick-start/#install-the-gatsby-cli)
- [Troubleshooting](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)
