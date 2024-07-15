# Running Postman API Tests in GitLab CI

## Table of Contents

- [Understanding API Testing](#understanding-api-testing)
- [Setting Up Your GitLab CI Pipeline](#setting-up-your-gitlab-ci-pipeline)
- [Creating and Exporting Postman Collections](#creating-and-exporting-postman-collections)
- [Exporting and Adding Collections and Environments to Your Repository](#exporting-and-adding-collections-and-environments-to-your-repository)
- [Running Newman in GitLab CI](#running-newman-in-gitlab-ci)
- [Reviewing API Testing Reports in GitLab](#reviewing-api-testing-reports-in-gitlab)
- [Best Practices](#best-practices)
- [Key Takeaways](#key-takeaways)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to this guide on running Postman API tests in GitLab CI. This document aims to help you integrate API testing into your CI/CD pipeline using Postman and Newman. It provides a step-by-step approach to setting up and running your tests, ensuring that your APIs function correctly throughout the development and deployment process.

## Understanding API Testing

API testing ensures that the API exposed by an application is working correctly. Our application exposes various endpoints, such as retrieving a list of cars, adding a car, getting a single car, deleting a car, and obtaining statistical information. These tests are crucial to verify the application's functionality since it relies solely on API endpoints without a graphical interface.

## Setting Up Your GitLab CI Pipeline

To integrate API testing into your GitLab CI pipeline, you'll need to set up a `.gitlab-ci.yml` file in your repository. This file defines the stages and jobs, specifying how and when your tests should run.

## Creating and Exporting Postman Collections

To begin, create your API tests in Postman. Here's a basic example:

1. **Create a Request**: For example, a GET request to the `/cars` endpoint.

2. **Add a Test**: In the Test tab, add a simple test to check the response status.

```javascript
pm.test("Status is 200", function () {
    pm.response.to.have.status(200);
});
```

3. **Save the Collection**: Save your tests in a collection and export it as a JSON file. Additionally, export any environments used in your tests.

## Exporting and Adding Collections and Environments to Your Repository

Before running Newman in your GitLab CI pipeline, you need to export your Postman collections and environments and add them to your repository. This ensures that Newman can access the necessary configurations to run your API tests.

### Exporting Your Postman Collection and Environment

1. **Export the Postman Collection**:

- Open Postman and go to the 'Collections' tab.
- Find the 'Cars API' collection you created.
- Click on the three dots beside the collection name and select 'Export'.
- Choose the desired format (recommended: Collection v2.1) and click 'Export'.
- Save the file as `Cars-API.postman_collection.json`.

2. **Export the Postman Environment**:

- Go to the 'Environments' tab in Postman.
- Select the 'Production' environment you have configured for your tests.
- Click on the eye icon, then the download button to export the environment settings.
- Save the file as `Production.postman_environment.json`.

### Adding the Exported Files to Your Repository

Once you have exported your collection and environment files, add them to the root of your project's repository:

- Move `Cars-API.postman_collection.json` and `Production.postman_environment.json` to the root directory of the `cars-api` source code repository.
- This setup ensures that when the CI pipeline runs, it has all the necessary files in place to execute the API tests effectively.

## Running Newman in GitLab CI

Newman is a command-line tool to run Postman collections. Below is a sample `.gitlab-ci.yml` configuration to run Postman API tests using Newman:

```yaml
stages:
  - build
  - test
  - deploy
  - post deploy

api testing:
  stage: post deploy
  image:
    name: postman/newman
    entrypoint: [""]
  script:
    - newman --version
    - newman run "Cars-API.postman_collection.json" -e "Production.postman_environment.json" --reporters cli,htmlextra,junit --reporter-htmlextra-export "newman/report.html"
  artifacts:
    when: always
    paths:
      - newman
    reports:
      junit: newman/report.xml
```

### Explanation:

- **Stages**: Define the sequence of steps in the pipeline (`build`, `test`, `deploy`, `post deploy`).
- **API Testing Job**: Specifies the `post deploy` stage and uses the `postman/newman` Docker image.
- **Newman Command**: Runs the Postman collection with specified reporters (`cli`, `htmlextra`, `junit`).
- **Artifacts**: Save the test reports and make them available in GitLab.

## Reviewing API Testing Reports in GitLab

After your API tests have been executed in the GitLab CI pipeline, you can review the generated reports directly in GitLab or download them for detailed analysis. This section guides you on how to access, view, and interpret these reports to monitor the health and performance of your APIs.

### Accessing the Test Reports

1. **Navigate to the Pipeline**:

- Go to your project in GitLab.
- Click on 'CI/CD' in the sidebar to view the pipelines.
- Select the pipeline that ran the API tests.

2. **View Artifacts and Test Results**:

- Within the pipeline details, find the job that executed the Newman tests, typically named `api testing` or similar.
- Click on the job to open its details.
- To see files produced by Newman, under the 'Job Artifacts' section, click on 'Browse'.

3. **Directly Viewing Test Results in GitLab**:

- For immediate review, GitLab may also present test results directly on the pipeline's job page, depending on the configuration of the CI pipeline and the test report format.
- Look for a 'Test' tab next to the 'Job Artifacts' to view the test summary and detailed results within the GitLab interface.

4. **Download and Review Reports**:

- Locate the `newman/report.html` for a detailed HTML report.
- You can also find `newman/report.xml` which is useful for integrating with other reporting tools or for historical comparisons.
  
### Interpreting the Test Reports

- **HTML Report**: Open the `report.html` file in any web browser to see a detailed, user-friendly presentation of each request and response, including passed and failed assertions.
- **JUnit XML Report**: This format is helpful for automated parsing by CI tools and can be viewed directly in GitLab's 'Test' tab for quick insights.

## Best Practices

1. **Fail Fast**: Ensure tests provide quick feedback on failures.
2. **Parallel Execution**: Run independent tests in parallel to save time.
3. **Clear Reporting**: Use multiple reporters to get comprehensive insights into test results.
4. **Environment Variables**: Manage environments effectively to test different configurations.
5. **Version Control**: Specify versions for Docker images to avoid unexpected changes.

## Key Takeaways

- API testing is essential to ensure your application's functionality.
- Postman and Newman provide a robust setup for automating API tests in GitLab CI.
- Clear reporting and artifact management enhance test visibility and debugging.
- Following best practices can optimize your CI/CD pipeline and improve reliability.

## Conclusion

Integrating Postman API tests into your GitLab CI pipeline is a crucial step in ensuring the reliability and functionality of your application. By following the steps outlined in this guide, you can set up and run your tests efficiently, gaining quick feedback and maintaining high code quality.

## References

- [How to Write API Tests with Postman](https://www.youtube.com/watch?v=Qlvbc6kIBOk&ab_channel=ValentinDespa)
- [Introduction to Postman | Installing Postman](https://www.youtube.com/watch?v=Qx0aIoz9Lxw&list=PLL34mf651faNJ6Wm8elGZl5mr9Zf14dWH&ab_channel=SoftwareTestingMentor)
- [postman/newman - Docker Image](https://hub.docker.com/r/postman/newman)