# Building The Project using Gitlab CI

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting Up a CI Pipeline](#setting-up-a-ci-pipeline)
- [Troubleshooting Errors](#troubleshooting-errors)
- [Using Artifacts in GitLab CI/CD](#using-artifacts-in-gitlab-cicd)
- [Optimizing the CI Pipeline](#optimizing-the-ci-pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In this guide, we will be focusing on how to use GitLab CI (Continuous Integration) for building our project. Our objective is to create a pipeline using GitLab CI that can replicate the exact steps we typically perform on our local machine.

## Prerequisites

For this tutorial, we will be working on a project in an IDE. We're using Visual Studio Code, which is free to download and install. However, you can also use the GitLab.com interface to edit files if that's easier for you.

## Setting Up a CI Pipeline

To start building our project, we first need to create a pipeline definition file. Here's a step-by-step guide:

## Step 1: Build the Website:

The first step in our pipeline will be to build our website:

```bash
cd static-website
```

Create a `.gitlab-ci.yml` file at the root of the directory:

```bash
touch .gitlab-ci.yml
```

## Step 2: Define the Scripts

We're working with a JavaScript project that uses NPM. The `package.json` file defines a set of dependencies that need to be installed. The dependencies are installed in a folder called `node_modules`. This isn't something that's checked into the repository as it would be a lot of files. Hence, before GitLab can build our project, it first needs to install all the necessary dependencies using `npm install`.

```yml
build website:
  script:
    - npm install
```

## Step 3: Install Gatsby

We are using Gatsby for generating this website. By default, Gatsby isn't installed so we'll need to install Gatsby and then run the `gatsby build` command:

```yml
build website:
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
```

Here's a simplified explanation of the above script in the `.gitlab-ci.yml` file:

In GitLab CI/CD, a `.gitlab-ci.yml` file is used to define what CI/CD (Continuous Integration / Continuous Deployment) pipelines do. It's a text file that uses the YAML syntax, and it should be placed in the root directory of your repository.

- **build website:** This is the name of the job. In this case, the job is called `build website`. The job name can be anything you want to name it, and it's purely for identification. It's good practice to name your jobs in a way that describes what they do.

- **script:** This keyword is used to define a list of commands that are run in the pipeline job. 

- **- npm install:** This command is used to install all the dependencies of the project. `npm` stands for Node Package Manager, which is used to manage JavaScript packages. When you run `npm install`, it looks at the `package.json` file in the root directory of your project and installs all the dependencies listed there.

- **- npm install -g gatsby-cli:** This command is installing the Gatsby command line interface (CLI) globally (the `-g` flag). Gatsby is a popular static site generator built with React. With the Gatsby CLI installed globally, you can use the `gatsby` command from anywhere on your machine.

- **- gatsby build:** This command is used to create a production build of your Gatsby website. In other words, it takes your website source code and builds all the static pages of your site, so they can be served to your users.

To summarize, this script is setting up a job named `build website` within the GitLab CI/CD pipeline that installs all the necessary dependencies for your project, sets up Gatsby's command line interface globally, and then builds a production-ready version of your Gatsby website.

## Step 4: Git committing the changes

After defining these steps, commit these changes and see how your pipeline works:

```bash
git add .
git commit -m "added pipeline"
git push
```

## Troubleshooting Errors

### npm: command not found

During the execution, you might encounter an error like `npm: command not found`. This happens because the default docker image that comes with GitLab CI does not have Node and NPM installed. To solve this, we need to use a Docker image that already has Node installed. We can find such images from Docker Hub.

Here's how to specify the Docker image in your pipeline:

```yml
build:
  image: node
  stage: build
  script:
    - echo "Installing Gatsby..."
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
```

Let's commit the change:

```bash
git add .
git commit -m "added node image"
git push
```

### Build fails in GitLab CI

If the build fails in GitLab CI, but works locally, make sure that you have same version of Node.js both locally and in your .gitlab-ci.yml

Use the latest LTS Node.js version as you see it on nodejs.org:

```yml
build website:
  image: node:lts
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
```

## Using Artifacts in GitLab CI/CD

Artifacts are files generated by GitLab Runner during a job that are then passed to future stages or jobs. In our context, the artifact is the website we are building.

The main goal is to specify the location of our artifact so it can be saved and retrieved later.

The following configuration illustrates how we define our artifacts in the `.gitlab-ci.yml` file:

```yml
build website:
  image: node:lts
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
  artifacts:
    paths:
      - ./public
```

In this job configuration:

-  `image: node:lts` specifies the Docker image to be used for the job.
-  The `script` section outlines the steps executed in the pipeline job.
-  The `artifacts` section is used to define the files or directories we want to keep as artifacts.
-  `paths` is where we specify the location of our artifacts. 

In this case, our artifact is located inside the `public` folder. We specify this with `./public`. The `./` denotes the current directory, making the path more specific. 

Once the job execution is completed, you'll notice that the artifacts have been generated and uploaded. These artifacts are now accessible for future jobs or stages, or for you to download and inspect manually.

## Optimizing the CI Pipeline

You might notice that GitLab CI can be slower compared to other continuous integration servers like Jenkins. This is primarily because of the ephemeral nature of Docker, where all the generated artifacts are discarded once the job is done. To optimize this, we'll be looking into artifact caching in future sections of this guide.

## Conclusion

In this guide, we've learned how to set up a basic CI pipeline in GitLab, install the necessary dependencies, solve potential errors, and build our project. We've also seen how to specify and use a Docker image that already has Node installed.

## References

- [Docker Hub](https://hub.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)