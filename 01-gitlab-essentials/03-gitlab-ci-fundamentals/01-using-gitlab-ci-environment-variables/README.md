# Using GitLab CI Pre-defined Environment Variables

Welcome to this tutorial on utilizing GitLab CI's pre-defined environment variables. If you've ever been stumped about which version of your website is deployed on your production server, this guide is for you.

## Table of Contents

- [Introduction](#introduction)
- [Problem Scenario](#problem-scenario)
- [Solution](#solution)
   * [Accessing Pre-defined Variables](#accessing-pre-defined-variables)
   * [Embedding the Commit Hash](#embedding-the-commit-hash)
   * [Displaying the Version in HTML](#displaying-the-version-in-html)
   * [Implementing Changes in the Pipeline](#implementing-changes-in-the-pipeline)
   * [Testing the Implementation](#testing-the-implementation)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

GitLab CI offers a plethora of pre-defined environment variables that can aid in automating and enhancing your continuous integration and deployment tasks. One such use-case is ensuring traceability of your deployed website's version.

## Problem Scenario

Imagine you have a simple, yet elegant website. Periodically, you make changes and deploy them. However, there's a catch. It's not always evident which specific version of the site is live. This can be especially concerning when multiple commits or changes are made in rapid succession.

## Solution

A solution to this challenge is to embed a version or commit identifier directly on the website, ensuring clarity about which commit or version is live at any given time.

### Accessing Pre-defined Variables

GitLab already provides a comprehensive list of environment variables. Among these is the `CI_COMMIT_SHORT_SHA` variable, which retrieves the first eight characters of the commit hash.

Incorporate the `echo $CI_COMMIT_SHORT_SHA` command into the script for the `build website` task as follows:

```yaml
build website:
  stage: build
  script:
    - echo $CI_COMMIT_SHORT_SHA
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
  artifacts:
    paths:
      - ./public
```

This enhancement ensures that the `CI_COMMIT_SHORT_SHA` is echoed within the script of the `build website` task. This unique command allows you to effectively incorporate the specific commit short SHA into your pipeline, enhancing the versioning information within your project.

### Embedding the Commit Hash

Let's go ahead and use this variable to reflect the version on our website:

1. Navigate to your project.
2. Enter the source code pages.
3. Open the `index.js` test page or the main HTML page you're using.
4. Insert a marker, for instance, `VERSION`, where you'd like the version to appear.

```html
<div>Version: %%VERSION%%</div>
```

The marker acts as a placeholder that will be replaced during the build process with the commit hash.

### Displaying the Version in HTML

#### Using `sed` to Transform Text in Files

`sed` stands for "stream editor." It's a powerful command-line tool employed for editing streams of text. With `sed`, you can perform text manipulations, such as insertion, deletion, search, and replace, directly from the terminal.

#### Basic `sed` Syntax

To globally replace occurrences of a text (let's say "word1") with another text (like "word2") in a file, you can use the following command:

```bash
sed -i 's/word1/word2/g' inputfile
```

In this command:
- `-i` allows for in-place editing, i.e., it modifies the original file.
- `s` is the substitute command.
- `word1` is the search pattern.
- `word2` is the replacement.
- `g` stands for "global", which means replacing all occurrences in the file.

#### Applying `sed` for Versioning

When working with version control, especially in CI/CD pipelines, embedding commit identifiers in files can be invaluable for tracking. Let's say we want to replace a placeholder `%%VERSION%%` in an HTML file with an actual commit hash:

```bash
sed -i "s/%%VERSION%%/$CI_COMMIT_SHORT_SHA/" ./public/index.html
```

Here:
- `%%VERSION%%` is the placeholder in the HTML file we intend to replace.
- `$CI_COMMIT_SHORT_SHA` contains the short version of the commit hash, typically provided by CI tools like GitLab.

Executing this command replaces the placeholder `%%VERSION%%` in `./public/index.html` with the actual commit hash.

### Implementing Changes in the Pipeline

After building the website with Gatsby (or your chosen tool), incorporate the aforementioned `sed` command to your pipeline script. The replacement should occur post the build step.

```yaml
build website:
  stage: build
  script:
    - echo $CI_COMMIT_SHORT_SHA
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
    - sed -i "s/%%VERSION%%/$CI_COMMIT_SHORT_SHA/" ./public/index.html
  artifacts:
    paths:
      - ./public
```

### Testing the Implementation

On executing the build step in the pipeline, the actual commit hash should replace the marker. If you refresh your deployed website, the version, derived from the commit hash, should now be visible.

For the assurance that the correct website version gets deployed, it's crucial to compare the displayed version with the expected one. By integrating "deployment tests" into our CI/CD pipeline, we can systematically validate this process.

#### Integrating Deployment Tests in CI/CD Pipeline

1. **Adding the "Deployment Tests" Stage**: Ensure that you include a stage named `deployment tests` in your pipeline configuration. This will be used explicitly for post-deployment validation.

2. **Creating the "Test Deployment" Job**: For this job, you'll be making HTTP requests to your deployed website and checking for specific content. In this case, we're looking for both a generic greeting ("Hi people") and the specific commit hash of the deployment.

```yaml
image: node

stages:
  - build
  - test
  - deploy
  - deployment tests

...

test deployment:
  image: alpine
  stage: deployment tests
  script:
    - apk add --no-cache curl   # Installing curl for making HTTP requests.
    - curl -s "[YOUR_DOMAIN_NAME].surge.sh" | grep -q "$CI_COMMIT_SHORT_SHA"  # Verify if the commit hash is present in the website's content.
```

**Note**: Ensure to replace `[YOUR_DOMAIN_NAME]` with the appropriate domain name of your deployed website.

#### Key Notes

- We're using the `alpine` image for the `test deployment` job as it's lightweight and efficient.
- `curl` is employed to fetch the content of the deployed website.
- The `grep -q` command is used to search within the fetched content. If the specified pattern is found, it exits without producing any output, making it apt for CI scripts.

By incorporating these steps, you can systematically validate the version of your deployed website, thereby ensuring transparency and accuracy in your deployments.

## Conclusion

Leveraging GitLab's pre-defined environment variables is a straightforward and efficient way to embed dynamic content like the commit hash into your website. This ensures that you always know which version of the site is live, fostering better traceability and reliability.

## References

- [GitLab CI Pre-defined Variables Documentation](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)