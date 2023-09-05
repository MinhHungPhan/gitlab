# Manual Deployments

In this tutorial, we'll walk through the process of configuring specific jobs in a GitLab Continuous Deployment (CD) pipeline to require manual intervention. This is useful when you want an extra layer of review before deploying changes to a production environment.

## Table of Contents

- [Introduction](#introduction)
- [Steps to Configure Manual Intervention](#steps-to-configure-manual-intervention)
  - [Revisiting the Deployment Pipeline](#revisiting-the-deployment-pipeline)
  - [Adding the manual directive](#adding-the-manual-directive)
  - [Setting allow_failure to false](#setting-allow_failure-to-false)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

In a typical CD pipeline, changes move through several environments before reaching production. While automation speeds up deployment, there are instances when manual checks are essential, especially when deploying to production.

## Steps to Configure Manual Intervention

### Revisiting the Deployment Pipeline

Recall our pipeline: deployments are automated up to the staging environment. For production, however, we need to pause the automation and manually decide whether the changes in staging should go live.

Currently, GitLab's default behavior is to automatically deploy to production once all preceding stages succeed.

### Adding the manual directive

To introduce manual intervention:

1. **Edit your pipeline**:

Locate the job responsible for deploying to production.

2. **Modify the job configuration**:

Add the `when: manual` directive. This ensures the job only runs when manually triggered via the GitLab interface:

```yaml
deploy production: 
  stage: deploy production
  environment:
    name: production
    url: $PRODUCTION_DOMAIN
  when: manual
```

`when: manual`: This step specifies that the job will not run automatically when the pipeline runs. Instead, someone has to manually trigger this job from the GitLab UI or via an API call. This is especially useful for critical stages like deploying to production, where a human intervention or approval might be desired.

### Setting allow_failure to false

After committing your changes and running the pipeline, you'll notice:

- The `deploy to production` job now requires manual initiation.
- Subsequent stages might execute regardless of the manual job's status, which might not be the desired behavior.

To fix this and make subsequent stages wait for the manual job:

**Edit the job configuration**:

Add `allow_failure: false` directive:

```yaml
deploy production: 
  stage: deploy production
  environment:
    name: production
    url: $PRODUCTION_DOMAIN
  when: manual
  allow_failure: false
```

With this change, the pipeline will be blocked until the manual job is triggered. Any subsequent stages will wait for its completion.

In the context of GitLab CI/CD (Continuous Integration/Continuous Deployment), the `allow_failure` configuration determines how the pipeline should treat a job that has failed.

- When you set `allow_failure: false` for a job in your `.gitlab-ci.yml` configuration, it means that if that particular job fails, the entire pipeline will be marked as failed. 

- Conversely, if `allow_failure` is set to `true`, even if the job fails, the pipeline will not be marked as failed because of that job. The pipeline would continue to run subsequent jobs. This setting can be useful in cases where certain jobs are non-essential or experimental and you don't want their failure to block the entire pipeline.

## Conclusion

Introducing manual intervention in a CD pipeline adds a safety layer before deploying to critical environments like production. While GitLab’s default behavior is geared towards full automation, you can easily configure it to suit scenarios requiring human oversight.

Remember to continually review your pipeline configurations to ensure they meet evolving requirements. In our example, we opted for full automation post-review, but you might find a different setup works best for you.

## References

- [GitLab CI/CD Pipeline Configuration](https://docs.gitlab.com/ee/ci/yaml/)
- [Using Manual Pipelines](https://docs.gitlab.com/ee/ci/pipelines/#manual-pipelines)
- [GitLab reference: when manual](https://docs.gitlab.com/ee/ci/yaml/#whenmanual)
- [GitLab reference: allow_failure](https://docs.gitlab.com/ee/ci/yaml/#allow_failure)