# Verifying Application Version After Deployment

## Table of Contents

- [Introduction](#introduction)
- [Setup Instructions](#setup-instructions)
- [Deployment and Verification Process](#deployment-and-verification-process)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This document provides a detailed guide on how to verify the version of an application after it has been deployed using a CI/CD pipeline. This process ensures that the deployed application is the intended version and is operating correctly in its environment. By integrating tools like `curl` and `jq` within an Alpine Linux environment, users can automate the verification steps to maintain accuracy and efficiency.

## Setup Instructions

Before beginning the verification process, ensure `curl` and `jq` are installed on your Alpine Linux environment:

```yaml
before_script:
  - apk --no-cache add curl
  - apk --no-cache add jq
```

This step is crucial as `curl` will be used to check application endpoints, and `jq` will parse JSON responses from AWS CLI commands.

## Deployment and Verification Process

### 1. **Deploy the Application**

Deploy your application using AWS CLI to push a build to Elastic Beanstalk:

```bash
aws s3 cp ./build/libs/$ARTIFACT_NAME s3://$S3_BUCKET/$ARTIFACT_NAME
aws elasticbeanstalk create-application-version --application-name $APP_NAME --version-label $CI_PIPELINE_IID --source-bundle S3Bucket=$S3_BUCKET,S3Key=$ARTIFACT_NAME
```

### 2. **Set Domain Name Dynamically**

Extract the domain name using `jq`:

```bash
CNAME=$(aws elasticbeanstalk update-environment --application-name $APP_NAME --environment-name "production" --version-label=$CI_PIPELINE_IID | jq '.CNAME' --raw-output)
```

### 3. **Handling Latency and Environmental Updates**

Wait for 45 seconds to ensure the environment variables are updated correctly:

```bash
sleep 45
```

### 4. **Verify Application Version and Health**

Check the application's version and health status using `curl`:

```bash
curl http://$CNAME/actuator/info | grep $CI_PIPELINE_IID
curl http://$CNAME/actuator/health | grep "UP"
```

## Best Practices

- **Script Automation**: Automate repetitive tasks within scripts to minimize human error.
- **Dynamic Variables**: Use dynamic extraction of environment variables to avoid hard-coding values.
- **Error Handling**: Implement error checking in scripts to handle unexpected failures gracefully.

## Key Takeaways

- Verification of an application's deployment version is critical for maintaining release integrity.
- Using `curl` for endpoint testing and `jq` for JSON parsing provides a robust method for automation.
- Adequate wait times are essential for environmental updates to propagate, ensuring accurate verification.

## Conclusion

By following the steps outlined in this guide, developers can ensure that the version of the application deployed in production is the intended version and is functioning as expected. This process not only reinforces the reliability of the deployment but also enhances the overall security and performance monitoring of the application.

## References

- [curl Official Documentation](https://curl.se/)
- [jq Official Documentation](https://jqlang.github.io/jq/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)