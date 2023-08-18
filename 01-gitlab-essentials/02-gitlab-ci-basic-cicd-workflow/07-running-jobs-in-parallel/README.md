# Running Jobs in Parallel

Welcome to this detailed tutorial on enhancing your testing strategy, in this case, using GitLab CI/CD pipelines. Here, you'll learn how to execute parallel jobs, use Docker images for testing, and how to streamline your CI/CD pipeline. This guide is beginner-friendly with clear explanations and practical examples.

## Table of Contents

- [Introduction](#introduction)
- [Optimizing GitLab CI/CD Pipelines](#optimizing-gitlab-cicd-pipelines)
- [Creating Jobs in Parallel](#creating-jobs-in-parallel)
- [Differences between test artifact and test website](#differences-between-test-artifact-and-test-website)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In software development, continuous testing is crucial to ensure the reliability and robustness of your code. As your project grows, testing strategy optimization becomes vital. In this guide, we'll explore how to refine our testing strategies using GitLab's CI/CD pipelines, Docker images, and other tools.

## Optimizing GitLab CI/CD Pipelines

### Using Minimal Docker Images

To start, we want our tests to succeed rather than fail. We want to reduce the volume of data logs from our test outputs. Here, Docker images come into play. We can use the default Docker image or specify our own.

Consider using a very minimal Linux distribution, like Alpine, which is only 5 megabytes in size. It's lightweight and fast, making it ideal for our purposes. It's important to note that for testing this artifact, we don't need anything else installed, not even Node.js. However, ensure that the utility `grep` is installed because that's the only tool we need in this instance.

Add `image: alpine` to our `test artifact` job:

```yaml
stages:
  - build
  - test

build website:
  stage: build
  image: node
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
  artifacts:
    paths:
      - ./public

test artifact:
  image: alpine
  stage: test
  script:
    - grep -q "Gatsby" ./public/index.html
```

### Adding Additional Jobs

Gatsby gives us the option of starting a server that we can access using HTTP to visualize the website. We will label this job 'test website'. It will be added to the 'test' stage.

1. To run Gatsby, we need to execute a couple of steps:
- We need to install NPM using `npm install`
- We need to install Gatsby using `npm install -g gatsby-cli`
- We need to start a local HTML server for testing the Gatsby site using `gatsby serve`

2. After this, we will need to use `curl` to fetch resources. We will fetch the local website that Gatsby serves, usually at localhost port 9000:

```bash
curl "http://localhost:9000"
```

**Note**: `curl` is a command line tool and library for transferring data with URLs. It supports many protocols including HTTP.

3. We can also use `grep` for the string we want. The `pipe` operator will pass the output from the website download to the `grep` command, eliminating the need to specify the file for the string search:

```bash
curl "http://localhost:9000" | grep -q "Gatsby"
```

**Note**: Pipes (`|`) let you use the output of a program as the input of another program. The standard syntax for pipes is to list multiple commands, separated by vertical bars. Example: tool1 | tool2 | tool3

4. However, we need to specify the Docker image (`image: node`)since we still need Node.js for this job.

```yaml
stages:
  - build
  - test

build website:
  stage: build
  image: node
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
  artifacts:
    paths:
      - ./public

test artifact:
  image: alpine
  stage: test
  script:
    - grep -q "Gatsby" ./public/index.html

test website:
  image: node
  stage: test
  script:
    - npm install
    - npm install -g gatsby-cli
    - gatsby serve
    - curl "http://localhost:9000" | grep -q "Gatsby"
```

Expected Output for `test website` job:

```plaintext
You can now view gatsby-starter-default in the browser.
⠀
  http://localhost:9000/
```

When we run a `test website` job, you might notice something unusual. We've started a process called `Gatsby serve`. This tells us the website is running at a specific address, which is what we expected. However, the problem is the next command isn't starting.

This happens because `Gatsby serve` takes up the whole terminal with its process. It doesn't allow the next command to begin because it's still busy. As a result, it doesn't give a chance for the rest of the job to proceed.

This isn't what we wanted to happen. If we let it stay like this, it would keep running indefinitely. In this situation, we can resolve it by clicking `Cancel` to terminate the job. Rest assured, we'll address this issue comprehensively in the upcoming tutorial.

## Creating Jobs in Parallel

Running jobs in parallel can make the process faster, reducing the time it takes for the pipeline to complete. However, we can only parallelize jobs that don't have dependencies. For example, we can't run the `build` and `test` steps in parallel because we need to build the artifact before testing it.

In our case, we are creating two jobs: `test artifact` and `test website`. They both fall under the `test` stage, so GitLab will run them in parallel. 

Running jobs in parallel is an excellent idea for optimizing processes, especially when the job execution is lengthy. However, it might not make the job run faster because of the overhead of downloading the Docker image. 

Remember, not every job can be parallelized. If there are dependencies between jobs, parallelization is not possible.

## Differences between test artifact and test website

The provided GitLab pipeline code defines two jobs under the "test" stage: `test artifact` and `test website`. Let's understand the differences between them:

1. **Base Image**:

- **test artifact**: Uses the `alpine` image. This is a minimalistic lightweight Linux distribution, mostly used when a small footprint is required.
- **test website**: Uses the `node` image, which is likely a Node.js environment. This is needed for running applications that depend on Node.js.

2. **Purpose**:

- **test artifact**: Checks if the built website (specifically, the `index.html` file) contains the word "Gatsby". It's a very basic validation to ensure that the built content (artifact) has specific content.
- **test website**: Installs necessary packages, starts the Gatsby development server, and then uses `curl` to fetch the website's homepage from `localhost` on port `9000`. It then checks if the fetched content contains the word "Gatsby". This test validates that the website can be served and responds correctly.

3. **Commands**:

- **test artifact**: It simply uses the `grep` command to check for the existence of the word "Gatsby" in the `index.html` file. This is a straightforward check against the artifact.
- **test website**: It installs dependencies, starts the website using Gatsby's serve command, and then checks the served website for the existence of the word "Gatsby" using a combination of `curl` and `grep`.

4. **Interactions**:

- **test artifact**: This job doesn't actively run the website. It only checks the static files that were generated in the build process.
- **test website**: This job actively serves the website and tests it by accessing the website using `curl`.

5. **Resource Intensity**:

- **test artifact**: Typically less resource-intensive because it's merely checking static content without starting any server or application.
- **test website**: More resource-intensive compared to `test artifact` because it's running a server, serving the website, and making an HTTP request.

In summary:
- `test artifact` is a simple validation to ensure that the built artifact (here, the `index.html` file) contains the word "Gatsby".
- `test website` is a more involved test to ensure not only that the built website contains "Gatsby" but also that the site is served correctly using Gatsby's server.

## Conclusion

Optimizing your testing strategy is a key part of the development process, and tools like GitLab and Docker make this process efficient and manageable. Using minimal Docker images, creating jobs in parallel, and structuring your pipeline correctly can significantly improve your development and testing processes. 

## References

- [GitLab CI/CD Pipeline Documentation](https://docs.gitlab.com/ee/ci/pipelines/)
- [Docker Documentation](https://docs.docker.com/)
- [Alpine Linux Distribution](https://alpinelinux.org/)
- [Gatsby Documentation](https://www.gatsbyjs.com/docs/)
