# Disabling Jobs

## Table of Contents

- [Introduction](#introduction)
- [Understanding Job Disabling](#understanding-job-disabling)
- [Example and Usage](#example-and-usage)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to the new tutorial on optimizing your workflow within a pipeline. In this guide, we'll explore a practical approach to work more efficiently on specific jobs or stages in your project without the need to run the entire pipeline. This can significantly save time, especially when you are making changes or testing parts of your project that are towards the end of your pipeline.

## Understanding Job Disabling

There are times when you may need to focus on specific jobs or stages of your pipeline, and you don’t want to spend time building or running the entire pipeline. This is particularly true for stages that are towards the end of the pipeline. 

If your work on a specific stage does not rely on any dependencies from the previous stages, a handy solution is to temporarily disable the jobs from the previous stages. Disabling jobs ensures that they are not executed, which can lead to a faster run time for your pipeline.

### How to Disable Jobs

Disabling jobs can be achieved with a simple yet effective trick: by adding a dot (.) before the job’s name. This act of commenting out the job ensures that it will not be executed during the pipeline run.

```yaml
.build_website:
  script:
    - echo "Building the website"
```

In the example above, the `build_website` job is disabled and will not be executed when the pipeline runs. This simple modification can lead to a significant reduction in pipeline execution time.

## Example and Usage

Let’s go through a step-by-step example to clarify the concept:

### Step 1: Identify the Job to Work On

First, determine which specific job or stage you want to work on. For instance, let’s say you have a pipeline with the following stages: `build`, `test`, and `deploy`, and you want to focus on the `deploy` stage.

### Step 2: Disable Unnecessary Jobs

Next, disable all jobs in the `build` and `test` stages since you are not working on them. Add a dot before each job in these stages.

```yaml

# ... existing code ...

.build website:
  stage: build
  only:
    - main
    - merge_requests
  script:
    - echo $CI_COMMIT_SHORT_SHA
    - npm install
    - npm install -g gatsby-cli

# ... existing code ...

.test artifact:
  image: alpine
  stage: test
  only:
    - main
    - merge_requests
  script:
    - grep -q "Gatsby" ./public/index.html

# ... existing code ...
```

### Step 3: Run Your Pipeline

Now, run your pipeline. You will notice that it directly jumps to the `deploy` stage, saving time and resources.

## Conclusion

By disabling jobs that are not relevant to the specific part of the pipeline you are working on, you can significantly reduce the execution time and resources used. This trick is particularly useful when working on stages that are towards the end of your pipeline and do not have dependencies on previous stages. It is a simple yet effective way to optimize your workflow, making your development process faster and more efficient.

## References

- [CI/CD Pipeline Documentation: Hide jobs](https://docs.gitlab.com/ee/ci/jobs/index.html#hide-jobs)
