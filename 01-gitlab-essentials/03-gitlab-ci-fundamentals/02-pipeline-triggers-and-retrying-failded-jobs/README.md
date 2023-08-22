# Pipeline triggers, Retrying failed jobs, Pipeline schedules

Welcome to this guide on GitLab CI pipelines! Here, we'll be diving deep into pipeline triggers, retrying failed jobs, and initiating pipelines without making a commit.

## Table of Contents

- [Introduction](#introduction)
- [Retrying Failed Jobs](#retrying-failed-jobs)
- [Starting the Pipeline without Commit](#starting-the-pipeline-without-commit)
- [Scheduling Pipelines](#scheduling-pipelines)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

GitLab's Continuous Integration (CI) provides a platform to automate the deployment process of your projects. One of the powerful features of GitLab CI is pipelines. These pipelines can be triggered in various ways and can be utilized to ensure your project is working seamlessly.

## Retrying Failed Jobs

There might be times when your pipeline fails, and it's especially frustrating if the job that failed is one of the last ones, especially after a long-running job. 

**Example**: Imagine you've got a series of jobs in your pipeline: A, B, C, and D. Job D fails after A, B, and C have taken a combined 3 hours to run. Instead of starting over from A, you can retry just job D.

To retry a failed job:
1. Locate the failed job in the GitLab UI.
2. Click on the `retry` button.
3. If the job runs successfully after retrying, the entire pipeline will be marked as successful.

If the entire pipeline fails, you can similarly retry the whole pipeline.

## Starting the Pipeline without Commit

Sometimes you might want to trigger a pipeline without making changes to your code.

**Example**: Maybe you've updated environment variables or other settings and want to see how they impact your pipeline.

To manually trigger a pipeline:
1. Navigate to your GitLab project's CI/CD settings.
2. Click on `Run Pipeline`.
3. A new interface will appear. Here, you can select the branch you want to run the pipeline for.
4. If there are any variables required, input them.
5. Click on `Run Pipeline` again to start the process.

## Scheduling Pipelines

Running pipelines on a schedule can be helpful in ensuring everything still works even when you're not actively developing.

**Example**: If you want to make sure your project's dependencies are still working properly, you can set up a pipeline to run daily or weekly.

To schedule a pipeline:
1. In GitLab, navigate to the CI/CD settings.
2. Under the `Pipeline schedules` section, click on `New Schedule`.
3. Define when you'd like to run the pipeline, e.g., every day at 4 a.m.
4. Choose a branch, specify any required variables, and save the pipeline schedule.

Once scheduled, GitLab will run your pipeline at the specified intervals. However, if you wish to manually trigger a scheduled pipeline, you can do so from the schedule list.

## Conclusion

Pipelines are a crucial part of GitLab CI, offering flexibility in how and when they're run. Whether you're looking to retry a failed job, manually trigger a pipeline, or set a regular schedule, GitLab provides all the tools necessary. Dive in and explore the myriad of ways you can optimize your CI/CD process with GitLab pipelines.

## References
- [GitLab CI Pipelines Schedules Documentation](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)