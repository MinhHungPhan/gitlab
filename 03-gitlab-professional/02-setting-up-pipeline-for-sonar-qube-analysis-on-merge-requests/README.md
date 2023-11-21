# Setting Up GitLab CI for SonarQube Analysis on Merge Requests

This tutorial provides a comprehensive tutorial for configuring your GitLab CI/CD pipeline to perform SonarQube analysis on merge requests, ensuring consistent code quality checks in your project.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Step-by-Step Setup](#step-by-step-setup)
   - [Install and Configure GitLab Runner](#1-install-and-configure-gitlab-runner)
   - [SonarQube Setup](#2-sonarqube-setup)
   - [Configure GitLab CI Variables](#3-configure-gitlab-ci-variables)
   - [Creating the `.gitlab-ci.yml` File](#4-creating-the-gitlab-ci.yml-file)
   - [Commit and Push the `.gitlab-ci.yml` File](#5-commit-and-push-the-gitlab-ci.yml-file)
   - [Triggering the Pipeline](#6-triggering-the-pipeline)
- [Variables in .gitlab-ci.yml](#variables)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Integrating SonarQube analysis into your GitLab CI/CD pipeline for merge requests enhances your project's code quality. This guide will walk you through the necessary steps to set up this process.

## Prerequisites

Before you dive into the configuration of your `.gitlab-ci.yml` file for SonarQube analysis on merge requests, ensure you have the following prerequisites set up and ready:

1. **GitLab Account and Repository**: A GitLab account with a project repository where your source code is hosted. The `.gitlab-ci.yml` file should be placed in the root directory of this repository.

2. **GitLab Runner**: Access to a GitLab Runner, which is essential for executing your CI/CD jobs. You can use shared runners available on GitLab or set up a private runner. For jobs that require Docker, ensure the runner is configured to run Docker containers.

3. **Docker Installation**: Docker needs to be installed on the machine where the GitLab Runner is hosted, as your CI jobs are configured to use Docker images.

4. **SonarQube Server Access**: Availability of a SonarQube server for code quality analysis. In your configuration, this is identified by the URL `https://sonar.pp.cicd.aws.smile.fr`. The server should be accessible from the GitLab Runner.

5. **SonarQube Project Setup**: A project created in SonarQube corresponding to your repository, along with a generated user token for authentication. This token is used in your CI/CD pipeline and should be securely stored as an environment variable in GitLab.

6. **Configured GitLab CI Variables**: Several environment variables are referenced in your `.gitlab-ci.yml` file, such as `$SONAR_LOGIN`, `$CI_COMMIT_SHA`, `$CI_COMMIT_REF_NAME`, `$GITLAB_USER_TOKEN`, and `$CI_PROJECT_ID`. These variables need to be defined in the CI/CD settings of your GitLab project.

7. **Understanding of YAML**: Basic knowledge of YAML syntax is required, as the `.gitlab-ci.yml` file is structured in YAML.

8. **Network Connectivity**: Ensure the GitLab Runner, Docker, and the SonarQube server are properly networked, particularly if they are located on different servers or across cloud services.

Meeting these prerequisites will facilitate a smooth setup and execution of your CI/CD pipeline for SonarQube analysis on merge requests in your GitLab project.

## Step-by-Step Setup

### 1. Install and Configure GitLab Runner

- Install GitLab Runner as per the [official guide](https://docs.gitlab.com/runner/install/).
- Register the runner to your GitLab project using [these instructions](https://docs.gitlab.com/runner/register/).

### 2. SonarQube Setup

- Ensure you have a SonarQube project corresponding to your GitLab repository.
- Generate an access token in SonarQube for secure authentication.

### 3. Configure GitLab CI Variables

- In your GitLab project, navigate to `Settings > CI/CD > Variables`.
- Add the following variables:
  - `SONAR_LOGIN`: SonarQube token.
  - `SONAR_GITLAB_USER_TOKEN`: GitLab user token.
  - `SONAR_HOST_URL`: SonarQube server URL.
  - `SONAR_PROJECT_KEY`: SonarQube project key.
  - `SONAR_SOURCES`: Path to your source code in the repository.

### 4. Creating the `.gitlab-ci.yml` File

In the root of your GitLab project, create or edit the `.gitlab-ci.yml` file. This file will define the CI/CD pipeline configuration.

#### Step 4.1: Configure `sonar-mr` Job

The `sonar-mr` job is designed for running SonarQube analysis in a merge request scenario. Here's how you configure it:

```yaml
variables:
  SONAR_SCANNER_VERSION: 3.3.0.1492

stages:
  - check

sonar-mr:
  image:
    name: newtmitch/sonar-scanner:3.2-alpine
    entrypoint: ['']
  stage: check
  variables:
    SONAR_ANALYSIS_MODE: 'preview'
    SONAR_SCANNER_OPTS: '-Xmx2G'
  tags:
    - docker-accor
  script:
    - "sonar-scanner \
        -Dsonar.projectKey=accor \
        -Dsonar.host.url=$SONAR_HOST_URL \
        -Dsonar.gitlab.api_version=v4 \
        -Dsonar.login=$SONAR_LOGIN \
        -Dsonar.analysis.mode=$SONAR_ANALYSIS_MODE \
        -Dsonar.gitlab.commit_sha=$CI_COMMIT_SHA \
        -Dsonar.gitlab.ref_name=$CI_COMMIT_REF_NAME \
        -Dsonar.gitlab.user_token=$GITLAB_USER_TOKEN \
        -Dsonar.gitlab.project_id=$CI_PROJECT_ID \
        -Dsonar.projectBaseDir=. \
        -Dsonar.profile=magento2 \
        -Dsonar.sources=app/code/Accor/ \
        -Dsonar.gitlab.only_issue_from_commit_line=true \
        -Dsonar.gitlab.max_major_issues_gate=0 \
        -Dsonar.gitlab.max_minor_issues_gate=0 \
        -Dsonar.sourceEncoding=UTF-8"
  only:
    refs:
      - merge_requests
    variables:
      - $CI_PROJECT_PATH == 'Accor/magento'
```

**Note**: Replace `$SONAR_HOST_URL`, `$SONAR_LOGIN`, `$GITLAB_USER_TOKEN`, etc., with actual variable values or references to CI/CD variables set in GitLab.

**Explanation**:
- **Image**: This specifies the Docker image `newtmitch/sonar-scanner:3.2-alpine` to use for the job. The `entrypoint` is overridden to ensure the container does not run any default commands.
- **Stage**: The job is part of the `check` stage.
- **Variables**: Here, `SONAR_ANALYSIS_MODE` is set to 'preview', and Java options for the Sonar Scanner are specified.
- **Tags**: The job uses the `docker-accor` runner tag to select an appropriate runner.
- **Script**: Contains the command to execute the SonarQube scanner, including various SonarQube-specific parameters.
- **Only**: Specifies that this job should only run for merge requests, and only for the specified project path.

#### Step 4.2: Configure `sonar_analyse` Job

The `sonar_analyse` job is set up for a more in-depth SonarQube analysis and is configured to run manually.

```yaml
variables:
  SONAR_SCANNER_VERSION: 3.3.0.1492

stages:
  - check

# ... existing code ...

sonar_analyse:
  image:
    name: newtmitch/sonar-scanner:3.2-alpine
    entrypoint: ['']
  tags:
    - docker-accor
  stage: check
  variables:
    SONAR_ANALYSIS_MODE: 'publish'
  script:
    - "sonar-scanner \
        -Dsonar.projectKey=accor \
        -Dsonar.host.url=$SONAR_HOST_URL \
        -Dsonar.gitlab.api_version=v4 \
        -Dsonar.login=$SONAR_LOGIN \
        -Dsonar.analysis.mode=$SONAR_ANALYSIS_MODE \
        -Dsonar.gitlab.commit_sha=$CI_COMMIT_SHA \
        -Dsonar.gitlab.ref_name=$CI_COMMIT_REF_NAME \
        -Dsonar.gitlab.project_id=$CI_PROJECT_ID \
        -Dsonar.gitlab.user_token=$GITLAB_USER_TOKEN \
        -Dsonar.projectBaseDir=. \
        -Dsonar.profile=magento2 \
        -Dsonar.sources=app/code/Accor/ \
        -Dsonar.sourceEncoding=UTF-8"
  only:
    refs:
      - merge_requests
    variables:
      - $CI_PROJECT_PATH == 'Accor/magento'
  when: manual
```

**Note**: Replace `$SONAR_HOST_URL`, `$SONAR_LOGIN`, `$GITLAB_USER_TOKEN`, etc., with actual variable values or references to CI/CD variables set in GitLab.

**Explanation**:
- Similar to `sonar-mr`, but with key differences in the **Variables** and **When** clauses.
- **Variables**: `SONAR_ANALYSIS_MODE` is set to 'publish', indicating a full analysis as opposed to a preview.
- **When**: This job is set to `manual`, meaning it won’t run automatically but can be triggered manually from the GitLab UI.

### 5. Commit and Push the `.gitlab-ci.yml` File

- Commit the file to your repository and push it to GitLab.

### 6. Triggering the Pipeline

- The pipeline will automatically trigger on creating a merge request in GitLab, executing the SonarQube analysis.

## Variables in .gitlab-ci.yml

- Variables are key components in `.gitlab-ci.yml` that allow you to store values which can be used in your CI/CD pipeline. Sorting out the CI/CD variables used in your `.gitlab-ci.yml` file helps in understanding their purpose and where they are utilized. 
- Here's a breakdown of the variables in the context of the two jobs, `sonar-mr` and `sonar_analyse`:

### Common Variables

These variables are used in both `sonar-mr` and `sonar_analyse` jobs:

1. **`SONAR_HOST_URL`**: The URL of your SonarQube server. This variable is essential for pointing the Sonar Scanner to the correct SonarQube instance.
2. **`SONAR_LOGIN`**: The authentication token or login for SonarQube. This is used by the Sonar Scanner to authenticate with the SonarQube server.
3. **`CI_COMMIT_SHA`**: This is a predefined GitLab CI variable that contains the commit SHA that triggered the CI pipeline.
4. **`CI_COMMIT_REF_NAME`**: Another predefined GitLab CI variable, it holds the name of the branch or tag that triggered the CI pipeline.
5. **`GITLAB_USER_TOKEN`**: Your GitLab user token, used for authentication with GitLab from SonarQube.
6. **`CI_PROJECT_ID`**: A predefined variable in GitLab CI, representing the unique ID of the project.
7. **`SONAR_PROJECT_KEY`**: The key of your project in SonarQube.
8. **`SONAR_SOURCES`**: The path to the source code within your repository that SonarQube will analyze.
9. **`CI_PROJECT_PATH`**: A predefined GitLab CI/CD variable that holds the namespace/project name of the project where the pipeline is running.
10. **`SONAR_SCANNER_VERSION`**: The version of the Sonar Scanner being used. This is particularly important to ensure compatibility and consistent functionality of the Sonar Scanner across different runs.

### Specific Variables for `sonar-mr`

- **`SONAR_ANALYSIS_MODE`**: Set to 'preview' in the `sonar-mr` job. This mode is used for preliminary analysis, often in merge request scenarios.
- **`SONAR_SCANNER_OPTS`**: Java options for the Sonar Scanner, such as memory settings (e.g., `-Xmx2G` for setting the maximum heap size).

### Specific Variables for `sonar_analyse`

- **`SONAR_ANALYSIS_MODE`**: Set to 'publish' in the `sonar_analyse` job. This mode indicates a full analysis and is typically used for deeper, comprehensive analysis.

### Usage in the Jobs

- In the `sonar-mr` job, these variables are used within the script to configure the Sonar Scanner's behavior and to ensure proper authentication and project identification.
- The `sonar_analyse` job uses a similar setup but with the analysis mode set to 'publish' for a complete analysis.
- `SONAR_SCANNER_VERSION` specifies the version of Sonar Scanner to be used, ensuring consistent analysis results.
- The `CI_PROJECT_PATH` variable is particularly used in the `only:variables` condition, making the jobs run only for the specific project path `'Accor/magento'`.

## Conclusion

This setup automates the SonarQube analysis for each merge request, streamlining your CI/CD process and ensuring continuous code quality assessment.

## References

- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
- [GitLab Runner Documentation](https://docs.gitlab.com/runner/)
- [SonarQube Documentation](https://docs.sonarqube.org/latest/)