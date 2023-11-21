# Deploying React App on AWS Amplify

This tutorial will guide you through the process of creating a static website using React, pushing the source code to GitLab, and hosting it on AWS Amplify.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

By following this tutorial, you'll learn how to leverage the power of React to create dynamic and interactive user interfaces while harnessing the benefits of a static website. You'll also gain hands-on experience with version control using GitLab and deploy your website on AWS Amplify for easy and scalable hosting.

## Prerequisites

- Node.js and npm installed on your local machine.
- Git installed on your local machine.
- An account on GitLab.
- An account on AWS.

## Step 1: Create a New React App

First, let's create a new React application using Create React App.

```bash
npx create-react-app my-app
cd my-app
```

## Step 2: Build Your Website

Now, you can start building your website. You can modify the `src/App.js` file to start with.

## Step 3: Push Your Code to GitLab

First, initialize a new Git repository in your project folder.

```bash
git init
```

Then, create a new repository on GitLab. After you've done that, link your local repository to the GitLab repository.

```bash
git remote add origin YOUR_GITLAB_REPO_URL
```

**Note**: Remember to replace `YOUR_GITLAB_REPO_URL` with the actual URL of your GitLab repository.

Now, commit your changes and push your code to GitLab.

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Step 4: Host Your Website on AWS Amplify

First, go to the AWS Amplify console and click on "Connect app". Then, select "GitLab" as your repository service.

Next, select the repository and the branch (usually "master" or "main") you want to deploy.

Then, Amplify will automatically detect that you're using React and suggest appropriate build settings. Confirm these settings and click "Next".

Finally, review everything and click "Save and deploy". AWS Amplify will now build and deploy your website.

## Conclusion

Congratulations! You've just created a static website using React, pushed it to GitLab, and hosted it on AWS Amplify.

## References

- [React Documentation](https://reactjs.org/docs)
- [Create React App](https://create-react-app.dev/docs/getting-started/)
- [GitLab Documentation](https://docs.gitlab.com/)
- [AWS Amplify Documentation](https://aws.amazon.com/amplify/getting-started/)
- [Node.js Documentation](https://nodejs.org/en/docs/)
