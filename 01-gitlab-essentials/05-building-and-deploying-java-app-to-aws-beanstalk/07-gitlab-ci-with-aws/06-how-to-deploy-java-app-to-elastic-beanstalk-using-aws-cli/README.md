# Deploying a Java Application to AWS Elastic Beanstalk using AWS CLI

Welcome to this comprehensive guide on deploying a Java application to AWS Elastic Beanstalk using the AWS Command Line Interface (CLI). This document is designed to walk you through the entire process, from preparing your application for deployment to executing the deployment using AWS CLI. Whether you're new to AWS or an experienced developer looking to streamline your deployment process, this guide will provide you with the knowledge and tools necessary to successfully deploy your Java applications to Elastic Beanstalk.

## Table of Contents

- [Introduction](#introduction)
- [Understanding the Deployment Process](#understanding-the-deployment-process)
- [Understanding Key Concepts](#understanding-key-concepts)
    - [Application Versions](#application-versions)
    - [Environment Management](#environment-management)
- [Configuring Your CI Pipeline](#configuring-your-ci-pipeline)
    - [Setting Up Variables](#setting-up-variables)
    - [Build Stage](#build-stage)
    - [Deploy Stage](#deploy-stage)
    - [Smoke Test Stage](#smoke-test-stage)
- [Deploying to AWS Elastic Beanstalk](#deploying-to-aws-elastic-beanstalk)
  - [Creating an Application Version](#creating-an-application-version)
  - [Updating the Elastic Beanstalk Environment](#updating-the-elastic-beanstalk-environment)
- [Granting Elastic Beanstalk Admin Access to 'gitlabci' User](#granting-elastic-beanstalk-admin-access-to-gitlabci-user)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Deploying applications can often seem daunting, especially when dealing with complex infrastructures like AWS Elastic Beanstalk. However, with the right tools and understanding, it can be simplified. AWS CLI offers a powerful way to manage your deployments directly from your terminal or within a CI/CD pipeline, providing flexibility and automation capabilities.

## Understanding the Deployment Process

Deploying an application to AWS Elastic Beanstalk involves several steps that must be carefully executed to ensure a successful deployment. Firstly, it's crucial to understand that deploying an application is not as simple as copying files; it involves creating a new application version on AWS Elastic Beanstalk and then updating the environment to use this new version.

## Understanding Key Concepts

### Application Versions

In AWS Elastic Beanstalk, an application version refers to a specific labeled iteration of your application. Managing versions allows you to deploy and rollback easily between different states of your application.

### Environment Management

An environment is a version running within AWS Elastic Beanstalk, associated with a domain and set of resources. Environments allow you to separate your application's stages (e.g., development, testing, production).

## Configuring Your CI Pipeline

### Setting Up Variables

Leveraging variables in your CI pipeline reduces duplication and errors. For instance, using variables like `ARTIFACT_NAME` and `APP_NAME` in your CI pipeline enhances efficiency by reducing redundancy and errors. These variables ensure consistency across your deployment processes.

```yaml
variables:
  ARTIFACT_NAME: cars-api-v$CI_PIPELINE_IID.jar
  APP_NAME: cars-api
```

- `ARTIFACT_NAME`: Dynamically manages artifact versions, improving version control and deployment tracking.
- `APP_NAME`: Ensures consistent application naming throughout the pipeline, streamlining deployments and operations.

#### What is `CI_PIPELINE_IID`?

`CI_PIPELINE_IID` is a predefined environment variable provided by GitLab CI/CD, representing the project-specific, incremental ID for the current pipeline run. This ID is unique within the scope of the project, meaning each pipeline run within a single project receives a sequential integer ID, distinct from pipeline runs in other projects or instances.

#### Why Use `CI_PIPELINE_IID`?

1. **Unique Artifact Identification**: In continuous integration and deployment workflows, especially in projects with frequent builds, it’s crucial to uniquely identify each build and its corresponding artifacts. Using `CI_PIPELINE_IID` as part of the artifact name or version label ensures that each build artifact can be traced back to its pipeline execution, preventing confusion between builds and aiding in version management.

2. **Version Tracking**: Deploying applications to environments like AWS Elastic Beanstalk requires careful version management to allow for controlled rollouts, rollbacks, and historical tracking of what has been deployed. Incorporating `CI_PIPELINE_IID` into the versioning strategy provides a straightforward method to track which version of the code is deployed in an environment, making it easier to manage deployments over time.

3. **Consistency Across Environments**: When deploying across multiple environments (development, staging, production), using an incremental ID like `CI_PIPELINE_IID` helps maintain consistency in artifact naming and versioning across these environments. It simplifies the process of promoting builds from one environment to another by providing a clear, incremental version trail.

4. **Simplification of Rollbacks**: In case a deployment introduces issues, having a clear and easily identifiable versioning system that includes `CI_PIPELINE_IID` allows teams to quickly identify and rollback to a previous version of the application, minimizing downtime and impact on end-users.

5. **Enhanced Traceability**: Integrating `CI_PIPELINE_IID` into the CI/CD pipeline’s artifacts and deployment process enhances traceability. It allows development and operations teams to easily correlate deployed versions of the application with specific pipeline runs, commit history, and changesets. This is particularly useful for auditing, troubleshooting, and understanding the evolution of the application over time.

### Build Stage

In the build stage, after building your application, rename the artifact to match the `ARTIFACT_NAME` variable. This ensures the artifact is uniquely identifiable.

```yaml
build:
  stage: build
  image: openjdk:12-alpine
  script:
    - ./gradlew build
    - mv ./build/libs/cars-api.jar ./build/libs/$ARTIFACT_NAME
  artifacts:
    paths:
      - ./build/libs/
```

### Smoke Test Stage

During the smoke test stage, reference the `ARTIFACT_NAME` when specifying the path to the JAR file you want to test. This ensures the correct, uniquely named artifact is used for testing.

```yaml
smoke test:
  stage: test
  image: openjdk:12-alpine
  before_script:
    - apk --no-cache add curl
  script:
    - java -jar ./build/libs/$ARTIFACT_NAME &
    - sleep 30
    - curl http://localhost:5000/actuator/health | grep "UP"
```

### Deploy Stage

In the deploy stage, when uploading your artifact to AWS S3 and creating a new application version in AWS Elastic Beanstalk, use the `ARTIFACT_NAME` variable to ensure AWS uses the correct, uniquely named artifact.

```yaml
deploy:
  stage: deploy
  image:
    name: amazon/aws-cli
    entrypoint: [""]
  script:
    - aws configure set region us-east-1
    - aws s3 cp ./build/libs/$ARTIFACT_NAME s3://$S3_BUCKET/$ARTIFACT_NAME
    - aws elasticbeanstalk create-application-version --application-name $APP_NAME --version-label $CI_PIPELINE_IID --source-bundle S3Bucket=$S3_BUCKET,S3Key=$ARTIFACT_NAME
    - aws elasticbeanstalk update-environment --application-name $APP_NAME --environment-name "production" --version-label=$CI_PIPELINE_IID
```

## Deploying to AWS Elastic Beanstalk

Deploying your application to AWS Elastic Beanstalk using the AWS CLI involves a series of steps that transition your application from code to a live environment accessible to users. This section will delve into the specifics of deploying to AWS Elastic Beanstalk, focusing on the critical steps of creating an application version and updating the environment with this new version.

### Creating an Application Version

An application version in AWS Elastic Beanstalk represents a specific iteration of your application. Creating a new version is the first step in deploying your changes.

- **Command**: `aws elasticbeanstalk create-application-version`
- **Key Parameters**:
    - `--application-name`: The name of your Elastic Beanstalk application (`APP_NAME`).
    - `--version-label`: A unique identifier for this version, often tied to the build or release ID.
    - `--source-bundle`: Specifies the location of your application code in Amazon S3, consisting of the S3 bucket name and the path to the ZIP file or WAR file in the bucket.

**Example**:

```bash
aws elasticbeanstalk create-application-version --application-name $APP_NAME --version-label $CI_PIPELINE_IID --source-bundle S3Bucket=$S3_BUCKET,S3Key=$ARTIFACT_NAME
```

This command registers a new version of your application with Elastic Beanstalk, using the artifact uploaded to S3 as the source.

### Updating the Elastic Beanstalk Environment

After creating the application version, the next step is to update the Elastic Beanstalk environment to use this new version. This step is what actually starts the deployment process in the environment.

- **Command**: `aws elasticbeanstalk update-environment`
- **Key Parameters**:
  - `--application-name`: The name of your Elastic Beanstalk application (`APP_NAME`).
  - `--environment-name`: The name of the environment you want to update (e.g., "production").
  - `--version-label`: The version label of the application version you want to deploy, ensuring the environment uses the correct version.

**Example**:

```bash
aws elasticbeanstalk update-environment --application-name $APP_NAME --environment-name "production" --version-label=$CI_PIPELINE_IID
```

This command instructs AWS Elastic Beanstalk to deploy the specified application version in the specified environment. It triggers the process of stopping the current application (if any), extracting the new version, and starting the new application version, along with any associated environment configuration changes.

## Granting Elastic Beanstalk Admin Access to 'gitlabci' User

### Step 1: Sign in to AWS Management Console

- Navigate to the AWS Management Console and log in with an account that has administrative access.

### Step 2: Access IAM Service

- In the AWS Management Console, find and click on the "Services" menu, then select "IAM" under the Security, Identity, & Compliance section.

### Step 3: Users List

- Within the IAM dashboard, click on "Users" in the left-hand sidebar to view the list of IAM users.

### Step 4: Find the User

- Search for the user "gitlabci" in the search bar.

### Step 5: Open User Details

- Click on the username "gitlabci" to open the user details page.

### Step 6: Add Permissions

- In the user details page, click on the "Add permissions" button.

### Step 7: Attach Existing Policies Directly

- Choose "Attach existing policies directly" from the options presented.
- In the search box, type "AdministratorAccess-AWSElasticBeanstalk" to find the policy. If you're specifically aiming for broad permissions, you can use "AdministratorAccess". However, be cautious as this grants extensive permissions across your AWS account.

### Step 8: Select the Policy

- Once you find the "AdministratorAccess-AWSElasticBeanstalk" policy (or "AdministratorAccess" if you're using that), check the box next to it to select it.

### Step 9: Review and Confirm

- Review the permissions to ensure that the correct policy is being attached to the user "gitlabci".
- Click the "Next: Review" button, then click "Add permissions" to confirm and apply the policy to the user.

## Best Practices

- Use environment-specific configurations to manage different stages of your application lifecycle efficiently.
- Implement automated testing in your CI pipeline to catch issues early.
- Utilize AWS CLI's capabilities to automate deployment processes, reducing manual errors and saving time.

## Key Takeaways

- AWS CLI is a powerful tool for managing Elastic Beanstalk deployments, offering flexibility and automation.
- Properly configuring your CI pipeline and using variables can significantly streamline the deployment process.
- Understanding the concepts of application versions and environments is crucial for managing deployments in Elastic Beanstalk.

## Conclusion

Deploying your Java application to AWS Elastic Beanstalk using AWS CLI not only simplifies the deployment process but also offers greater control and automation. By following the steps and best practices outlined in this guide, you can efficiently manage your application deployments, allowing you to focus more on development and less on the intricacies of deployment.

## References

- [GitLab CI Variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)
- [AWS CLI Elastic Beanstalk](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/)
- [AWS CLI Create Application Version](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/create-application-version.html)
- [AWS CLI Update Environment](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/update-environment.html)
- [list-available-solution-stacks](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.html)
- [Java SE platform history](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history-javase.html)