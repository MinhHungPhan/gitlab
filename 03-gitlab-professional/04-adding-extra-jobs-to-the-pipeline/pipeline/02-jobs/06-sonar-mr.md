# Overview of `sonar-mr` Job in `gitlab-ci.yml`

## Introduction

The `sonar-mr` job, as updated in the `gitlab-ci.yml` file, introduces a sophisticated approach to code quality analysis during merge requests. Utilizing SonarQube, this job assesses code quality against defined quality gates and specific rules, enhancing the review process for merge requests.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Execution and Analysis](#execution-and-analysis)
- [Example](#example)
- [Conclusion](#conclusion)

## Job Description

- **Purpose**: To perform code quality analysis on merge requests using SonarQube.
- **Context**: Triggered when a merge request is submitted, focusing on enforcing quality standards.

## Configuration and Setup

- **Stage**: Assigned to the `test` stage.
- **Image**: Uses `newtmitch/sonar-scanner:3.2-alpine`, a lightweight SonarQube scanner image.
- **Variables**:
  - `SONAR_ANALYSIS_MODE`: Set to `preview` for analysis without affecting the SonarQube dashboard.
  - `SONAR_SCANNER_OPTS`: Configured with `-Xmx2G` to allocate sufficient memory for the scanner.

## Execution and Analysis

- **Script**:
  - Executes `sonar-scanner` with a series of `-D` (define) options to configure the analysis:
    - SonarQube server URL, project key, and base directory.
    - The specific source directory (`app/code/Accor/`) for analysis.
    - Encoding, login credentials, and analysis mode settings.
    - GitLab integration settings, including commit SHA, reference name, user token, project ID.
    - Configuration to only consider issues from the commit line.
    - Limits for major and minor issues, set to `0` (strict quality gate).

## Example

```yaml
sonar-mr:
  ...
  script:
    - "sonar-scanner \
       -Dsonar.projectKey=accor \
       -Dsonar.sources=app/code/Accor/ \
       ..."
  ...
```

This example highlights the SonarQube scanner execution, illustrating how it is configured for targeted analysis of the Accor project's codebase within the merge request context.

## Conclusion

The `sonar-mr` job represents a crucial enhancement in the CI/CD pipeline, specifically targeting code quality in merge requests. By integrating SonarQube analysis, this job ensures that new code submissions adhere to the established quality standards, fostering a culture of high code quality and continuous improvement.