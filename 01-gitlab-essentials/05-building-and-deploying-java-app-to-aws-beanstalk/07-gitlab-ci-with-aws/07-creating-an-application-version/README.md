# Creating an Application Version

Welcome to our guide on managing application versions effectively within a deployment pipeline. This document is designed for software developers and DevOps engineers looking to automate and streamline their deployment processes. Here, you'll learn how to ensure the correct application version is running in production without manual checks, utilizing automation tools like Postman and GitLab CI.

## Table of Contents

- [Introduction](#introduction)
- [Understanding the Deployment Process](#understanding-the-deployment-process)
- [Automating Version Verification](#automating-version-verification)
- [Modifying Application Configurations](#modifying-application-configurations)
- [Hands-On Lab](#hands-on-lab)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In the lifecycle of software development, deploying a new version to production is a critical step. It's essential not only to deploy but also to verify that the correct version is active. This document explores methods to automate this verification, reducing the dependency on manual checks and enhancing reliability in your deployment process.

## Understanding the Deployment Process

Deploying an application typically involves several steps, from code commits to building artifacts and finally, deployment. However, ensuring that a specific version is running in production can be challenging without continuous monitoring and verification systems.

## Automating Version Verification

To verify which version of an application is running, you can use the health and information endpoints:
- **Health Check**: Ensures the application is running smoothly.
- **Info Endpoint**: Provides specific version details.

For instance, querying an application’s `/actuator/info` endpoint might return:

```json
{
  "app": {
    "version": "current_version",
    "commit": "current_commit_hash",
    "branch": "current_branch"
  }
}
```

## Modifying Application Configurations

During the build process in a GitLab CI pipeline, placeholders in the `application.yml` are replaced with actual data like version ID, commit SHA, and branch name using the `sed` command. This is done before the build to ensure the application configuration carries accurate version information post-deployment.

Example `sed` command to replace placeholders:

```bash
sed -i "s/PIPELINE_IID/$CI_PIPELINE_IID/" ./src/main/resources/application.yml
```

## Hands-On Lab

### Step 1: Check from Postman

**Send a GET request to `{{baseURL}}/actuator/info`.**

**Expected Output:**

```json
{
  "app": {
    "version": "CI_PIPELINE_IID",
    "commit": "CI_COMMIT_SHORT_SHA",
    "branch": "CI_COMMIT_BRANCH"
  }
}
```

### Step 2: Modify `application.yml`

Update the `application.yml` file to include the pipeline-specific variables:

```yml
info:
  app:
    version: CI_PIPELINE_IID
    commit: CI_COMMIT_SHORT_SHA
    branch: CI_COMMIT_BRANCH
```

### Step 3: Configure the build job

Set up the build job in your GitLab CI configuration file:

```yml
build:
  stage: build
  image: openjdk:12-alpine
  script:
    - sed -i "s/CI_PIPELINE_IID/$CI_PIPELINE_IID/" ./src/main/resources/application.yml
    - sed -i "s/CI_COMMIT_SHORT_SHA/$CI_COMMIT_SHORT_SHA/" ./src/main/resources/application.yml
    - sed -i "s/CI_COMMIT_BRANCH/$CI_COMMIT_BRANCH/" ./src/main/resources/application.yml
    - ./gradlew build
    - mv ./build/libs/cars-api.jar ./build/libs/$ARTIFACT_NAME
  artifacts:
    paths:
      - ./build/libs/
```

#### What is sed command on Linux?

The term `sed` stands for **Stream Editor**. It is a powerful and versatile text-processing utility in Unix and Unix-like operating systems, designed for filtering and transforming text in a stream. `sed` is typically used for extracting portions of text from files, making modifications directly within text files, or transforming text as it is processed.

#### General Syntax of sed

The syntax used here is:

```bash
sed -i "s/find/replace/" file
```

- `sed`: Stream editor for filtering and transforming text.
- `-i`: Option that instructs `sed` to edit files in-place. This means `sed` will directly modify the file if it finds a match, without needing to output to a new file.
- `"s/find/replace/"`: The substitution command (`s`) followed by the pattern to find (`find`) and the text to replace it with (`replace`), separated by slashes. This is enclosed in quotes to handle potential special characters gracefully.
- `file`: The path to the file where the replacements will be made.

#### Specific Commands

1. **Pipeline ID Replacement**

```bash
sed -i "s/CI_PIPELINE_IID/$CI_PIPELINE_IID/" ./src/main/resources/application.yml
```

- This command replaces the placeholder `CI_PIPELINE_IID` in `application.yml` with the value of the `$CI_PIPELINE_IID` environment variable.
- `$CI_PIPELINE_IID`: Typically holds a unique identifier for the current pipeline run in GitLab CI, which can be useful for tracking which pipeline build was deployed.

2. **Commit SHA Replacement**

```bash
sed -i "s/CI_COMMIT_SHORT_SHA/$CI_COMMIT_SHORT_SHA/" ./src/main/resources/application.yml
```

- Replaces `CI_COMMIT_SHORT_SHA` with the value of the `$CI_COMMIT_SHORT_SHA` environment variable.
- `$CI_COMMIT_SHORT_SHA`: Contains the short SHA of the commit that triggered the CI pipeline, providing a concise identifier of the specific commit.

3. **Branch Name Replacement**

```bash
sed -i "s/CI_COMMIT_BRANCH/$CI_COMMIT_BRANCH/" ./src/main/resources/application.yml
```

- Substitutes `CI_COMMIT_BRANCH` with the value of the `$CI_COMMIT_BRANCH` environment variable.
- `$CI_COMMIT_BRANCH`: Indicates the name of the branch from which the pipeline was triggered, which is useful for conditional behaviors in multi-branch pipelines.

### Step 4: Check the result in Postman

After the deployment, verify the version, commit, and branch information through Postman.

**Expected Output:**

```json
{
  "app": {
    "version": 27,
    "commit": "bd2cd25a",
    "branch": "main"
  }
}
```

## Best Practices

- **Automate Everything**: Automation minimizes human error and enhances efficiency.
- **Consistent Placeholders**: Use consistent naming for placeholders in your configurations to avoid confusion.
- **Regularly Update Documentation**: Keep your documentation aligned with changes in your CI/CD processes.

## Key Takeaways

- Automation tools are crucial for verifying deployed versions without manual intervention.
- Modifying application configurations during the build process ensures that the running application reflects the correct version information.

## Conclusion

By automating the verification of deployed application versions, teams can achieve more reliable and efficient deployment workflows. The techniques and examples provided here should empower you to implement similar practices in your projects.

## References

- [Predefined CI/CD variables reference](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)
- [What is sed command on Linux?](https://www.ionos.com/digitalguide/server/configuration/linux-sed-command/)
- [GNU `sed` Manual](https://www.gnu.org/software/sed/manual/sed.html)