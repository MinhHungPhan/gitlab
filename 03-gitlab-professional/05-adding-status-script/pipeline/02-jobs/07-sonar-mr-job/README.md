# Overview of `sonar-mr` Job in `gitlab-ci.yml`

## Introduction

The `sonar-mr` job, as updated in the `gitlab-ci.yml` file, introduces a sophisticated approach to code quality analysis during merge requests. Utilizing SonarQube, this job assesses code quality against defined quality gates and specific rules, enhancing the review process for merge requests.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Execution and Analysis](#execution-and-analysis)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To perform code quality analysis on merge requests using SonarQube.
- **Context**: Triggered when a merge request is submitted, focusing on enforcing quality standards.

## Configuration and Setup

- **Stage**: Assigned to the `test` stage.
- **Image**: Uses `newtmitch/sonar-scanner:3.2-alpine`, a lightweight SonarQube scanner image.
- **Variables**:
  - `SONAR_ANALYSIS_MODE`: Set to `preview` for analysis without affecting the SonarQube dashboard.
  - `SONAR_SCANNER_OPTS`: Configured with `-Xmx2G` to allocate sufficient memory for the scanner.
- **Tags**:
    - `docker-accor`: This tag probably specifies the runner tag that should execute this job, ensuring that the job runs on a specific runner configured with this tag.
    - The job `sonar-mr` has the tag `docker-accor`. This means that this job will be executed by a runner that has been tagged with `docker-accor`.

## Execution and Analysis

### `script`

- Executes `sonar-scanner` with a series of `-D` (define) options to configure the analysis:
    - SonarQube server URL, project key, and base directory.
    - The specific source directory (`app/code/Accor/`) for analysis.
    - Encoding, login credentials, and analysis mode settings.
    - GitLab integration settings, including commit SHA, reference name, user token, project ID.
    - Configuration to only consider issues from the commit line.
    - Limits for major and minor issues, set to `0` (strict quality gate).

### `except`

Defines the conditions under which this job should not run.

- `refs:`: Specifies the type of Git reference.
- `- tags`: This means the job will not run on Git tags, probably to avoid running analysis on version release tags.

## Pipeline

```yaml
sonar-mr:
    image:
        name: newtmitch/sonar-scanner:3.2-alpine
        entrypoint: ['']
    stage: test
    variables:
        SONAR_ANALYSIS_MODE: 'preview'
        SONAR_SCANNER_OPTS: '-Xmx2G'
    tags:
        - docker-accor
    script:
        - "sonar-scanner \
            -Dsonar.host.url=https://sonar.pp.cicd.aws.smile.fr \
            -Dsonar.projectKey=accor \
            -Dsonar.projectBaseDir=. \
            -Dsonar.sources=app/code/Accor/ \
            -Dsonar.sourceEncoding=UTF-8 \
            -Dsonar.login=$SONAR_LOGIN \
            -Dsonar.analysis.mode=$SONAR_ANALYSIS_MODE \
            -Dsonar.gitlab.api_version=v4 \
            -Dsonar.gitlab.commit_sha=$CI_COMMIT_SHA \
            -Dsonar.gitlab.ref_name=$CI_COMMIT_REF_NAME \
            -Dsonar.gitlab.user_token=$GITLAB_USER_TOKEN \
            -Dsonar.gitlab.project_id=$CI_PROJECT_ID \
            -Dsonar.gitlab.only_issue_from_commit_line=true \
            -Dsonar.gitlab.max_major_issues_gate=0 \
            -Dsonar.gitlab.max_minor_issues_gate=0 \
            "
    except:
        refs:
            - tags
```

This example highlights the SonarQube scanner execution, illustrating how it is configured for targeted analysis of the Accor project's codebase within the merge request context.

## Conclusion

The `sonar-mr` job represents a crucial enhancement in the CI/CD pipeline, specifically targeting code quality in merge requests. By integrating SonarQube analysis, this job ensures that new code submissions adhere to the established quality standards, fostering a culture of high code quality and continuous improvement.

## References

- [SonarSource on GitLab Code Quality](https://www.sonarsource.com/products/sonarcloud/features/integrations/gitlab-integration/)
- [SonarSource Documentation on GitLab Integration](https://docs.sonarsource.com/sonarqube/latest/devops-platform-integration/gitlab-integration/)
- [CI Integration Overview by SonarSource](https://docs.sonarsource.com/sonarqube/8.9/analyzing-source-code/ci-integration/overview/)
- [GitLab CI template for SonarQube](https://to-be-continuous.gitlab.io/doc/ref/sonar/)
- [SonarQube Analysis Parameters](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/analysis-parameters/)
- [GitLab documentation for tags](https://docs.gitlab.com/ee/ci/yaml/#tags)