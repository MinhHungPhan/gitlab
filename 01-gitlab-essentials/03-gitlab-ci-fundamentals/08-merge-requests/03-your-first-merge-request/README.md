# Your First Merge Request

Welcome to a simple tutorial on how to utilize GitLab's branching and merging capabilities. The goal of this tutorial is to walk you through the process of creating a new branch, making changes, and merging it back to the `main` branch.

## Table of Contents

- [Introduction](#introduction)
- [Creating a New Branch](#creating-a-new-branch)
- [Making Changes and Committing](#making-changes-and-committing)
- [Merge Requests](#merge-requests)
- [Monitoring Pipelines](#monitoring-pipelines)
- [Using the only Job Policy](#using-the-only-job-policy)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In this tutorial, we'll focus on branching and merging, two fundamental aspects of version control that enable collaborative development.

## Creating a New Branch

1. Navigate to your GitLab repository.
2. Select **Repository** and then **Branches**.
3. Click on **New Branch**.
4. Name your branch. For this tutorial, we'll name our branch `feature/new-title`.
5. Choose the source branch, usually `main`, from which this new branch will be created.
6. Click **Create Branch**.

Upon creating a new branch, the pipeline will immediately begin executing.

## Making Changes and Committing

1. Navigate to the location of the change. For instance, `src > pages > index.js`.
2. Make the desired modifications. In this case, we're adding a new title.

```js
<h1>Welcome to <b>Gatsby!</b></h1>
<h2>This is a new title</h2>
<p className={styles.intro}>
  <b>Example pages:</b> 
  {samplePageLinks.map((link, i) => (
    <React.Fragment key={link.url}>
      <Link to={link.url}>{link.text}</Link>
      {i !== samplePageLinks.length - 1 && <> · </>}
    </React.Fragment>
  ))}
  <br />
  Edit <code>src/pages/index.js</code> to update this page.
</p>
```

3. Once done, **Commit** your changes with an appropriate commit message.

## Merge Requests

1. Navigate back to your GitLab repository.
2. Click **New Merge Request**.
3. If desired, add a description detailing the reason for the changes.
4. Opt to delete the branch post-merge to keep your repository clean.
5. Click **Submit merge Request**.
6. Click **Set to Auto-merge**.

## Monitoring Pipelines

After initiating the merge request, you'll observe a pipeline starts running, indicating the stages your changes go through:
1. Building the website.
2. Testing.
3. Deployment to staging.
4. Deployment to production.
5. Production tests.

Once all stages are successful, GitLab will automatically merge the changes, and if chosen, delete the source branch.

## Using the only Job Policy

You can decide when certain tasks (like building or testing your website) should happen using something called an `only` job policy. Think of it as a set of rules for when certain tasks should run.

Here's an example:

```yaml
build website:
  stage: build
  only:
    - main
    - merge_requests
  script:
    - echo $CI_COMMIT_SHORT_SHA
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
    - sed -i "s/%%VERSION%%/$CI_COMMIT_SHORT_SHA/" ./public/index.html
  artifacts:
    paths:
      - ./public

test artifact:
  image: alpine
  stage: test
  only:
    - main
    - merge_requests
  script:
    - grep -q "Gatsby" ./public/index.html

test website:
  stage: test
  only:
    - main
    - merge_requests
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby serve &
    - sleep 3
    - curl "http://localhost:9000" | tac | tac | grep -q "Gatsby"
```

Here's a breakdown of what's happening:

1. The `only` section tells the system on which branches or cases the task should run. In our example, tasks are set to run on the `main` branch and any `merge_requests`.
2. Each task has a `script` section that lists out the commands to run for that task.

It's worth noting that although it's technically possible to reuse some parts that were built in one branch (to avoid doing the same thing multiple times, like building and testing on the `main` branch), for now, we'll just make a new one when running the main process.

## Conclusion

Utilizing GitLab's branching and merging capabilities is an efficient way to manage your codebase. By following this workflow, you ensure that the main branch remains stable and every change undergoes a thorough review process. 

## References

- [GitLab CI/CD Pipeline Configuration](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab CI/CD Pipeline: only / except](https://docs.gitlab.com/ee/ci/yaml/#only--except)