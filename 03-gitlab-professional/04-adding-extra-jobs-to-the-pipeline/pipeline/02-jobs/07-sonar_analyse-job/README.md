# Overview of `sonar_analyse` Job in `gitlab-ci.yml`

## Introduction

The `sonar_analyse` job, as introduced in the latest `gitlab-ci.yml` update, is designed for a comprehensive SonarQube analysis of the project, with a focus on code coverage integration. This analysis is pivotal for maintaining high code quality standards and is scheduled to run periodically.

## Table of Contents

- [Job Description](#job-description)
- [Configuration and Setup](#configuration-and-setup)
- [Execution and Analysis](#execution-and-analysis)
- [Scheduling and Dependencies](#scheduling-and-dependencies)
- [Pipeline](#pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Job Description

- **Purpose**: To perform a full SonarQube analysis of the project, including code coverage, specifically focusing on Accor dedicated code coverage.
- **Context**: Executed as part of a scheduled pipeline in GitLab.

## Configuration and Setup

- **Stage**: Allocated to the `sonarqube-analysis` stage.
- **Image**: Uses `newtmitch/sonar-scanner:3.2-alpine`, a lightweight image suitable for SonarQube scanning.
- **Variables**:
  - `GIT_DEPTH`: Set to `0` to avoid shallow clone issues in analysis.
  - `SONAR_ANALYSIS_MODE`: Set to `publish` for results to be reflected in SonarQube.

## Execution and Analysis

- **Before Script**:
  - Lists the contents of the PHPUnit report folder for verification.
- **Script**:
  - Executes `sonar-scanner` with multiple configuration options:
    - SonarQube server URL and project key.
    - Paths to PHPUnit test reports and coverage reports.
    - Project base directory, source encoding, and other GitLab integration settings.

## Scheduling and Dependencies

- **Dependency Management**:
  - Depends on the `unit_tests_coverage_accor` job for code coverage data.
- **Execution Trigger**:
  - Runs only for scheduled pipelines, ensuring regular, comprehensive analysis without overloading the CI/CD pipeline.

## Pipeline

```yaml
sonar_analyse:
    image:
        name: newtmitch/sonar-scanner:3.2-alpine
        entrypoint: ['']
    tags:
        - docker-accor
    stage: sonarqube-analysis
    dependencies:
        - unit_tests_coverage_accor
    needs:
        - unit_tests_coverage_accor
    variables:
        # To Avoid Shallow clone and analysis error from Sonar
        GIT_DEPTH: 0
        SONAR_ANALYSIS_MODE: 'publish'
    before_script:
        - ls -la $PHPUNIT_REPORT_FOLDER
    script:
        - "sonar-scanner \
            -Dsonar.host.url=https://sonar.pp.cicd.aws.smile.fr \
            -Dsonar.php.tests.reportPath=$PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_FILENAME_ACCOR \
            -Dsonar.php.coverage.reportPaths=$PHPUNIT_REPORT_FOLDER/$PHPUNIT_REPORT_CLOVER_ACCOR \
            -Dsonar.projectBaseDir=. \
            -Dsonar.sources=app/code/Accor/ \
            -Dsonar.projectKey=accor \
            -Dsonar.login=$SONAR_LOGIN \
            -Dsonar.sourceEncoding=UTF-8 \
            -Dsonar.analysis.mode=$SONAR_ANALYSIS_MODE \
            -Dsonar.gitlab.commit_sha=$CI_COMMIT_SHA \
            -Dsonar.gitlab.ref_name=$CI_COMMIT_SHORT_SHA \
            -Dsonar.gitlab.project_id=$CI_PROJECT_ID \
            -Dsonar.gitlab.user_token=$GITLAB_USER_TOKEN \
            -Dsonar.gitlab.api_version=v4"
    only:
        - schedules
```

This snippet illustrates how the SonarQube scanner is configured to analyze the project, including the integration of code coverage reports, emphasizing the job's role in quality assurance.

## Conclusion

The `sonar_analyse` job is a crucial addition to the CI/CD pipeline, offering an in-depth analysis of the project's code quality and coverage. By scheduling this job, the pipeline ensures ongoing monitoring and maintenance of high coding standards, crucial for the project's integrity and reliability.

## References

- [SonarSource on GitLab Code Quality](https://www.sonarsource.com/products/sonarcloud/features/integrations/gitlab-integration/)
- [SonarSource Documentation on GitLab Integration](https://docs.sonarsource.com/sonarqube/latest/devops-platform-integration/gitlab-integration/)
- [GitLab CI template for SonarQube](https://to-be-continuous.gitlab.io/doc/ref/sonar/)
- [Configuring SonarScanner](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/)
- [SonarQube Analysis Parameters](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/analysis-parameters/)