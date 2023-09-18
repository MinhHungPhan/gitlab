# Optimizing Cache Performance in GitLab CI Pipelines

This guide focuses on enhancing the efficiency of the cache in GitLab CI pipelines. We'll pinpoint jobs that don't require cache, avoid unnecessary cache tasks, and set up a periodic job for cache refresh.

## Table of Contents

- [Introduction](#introduction)
- [Spotting Redundant Cache Usage](#spotting-redundant-cache-usage)
- [Understanding Cache Policies](#understanding-cache-policies)
    - [Pull Policy](#pull-policy)
    - [Push Policy](#push-policy)
- [Scheduling Cache Updates](#scheduling-cache-updates)
- [Setting Up a Scheduled Task in GitLab](#setting-up-a-scheduled-task-in-gitlab)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

GitLab CI's cache feature expedites job execution by reusing previously obtained or generated files. However, using the cache isn't always necessary. Turning it off for certain jobs can boost pipeline speed.

## Spotting Redundant Cache Usage

**Observe:** Analyze the jobs in the pipeline. Note that some jobs might have overhead due to cache operations (like downloading or uploading the `node_modules` folder) even if they don't use the cache.

**Question:** Which jobs don't use project npm dependencies and therefore don't need the cache?

**Answer:** The jobs `test artifact`, `deploy to surge`, and `test deployment` don't require the cache.

**Learn:** GitLab allows the disabling of cache for specific jobs. To do this, you can include the configuration `cache: {}` within the job definition.

## Understanding Cache Policies

By default, GitLab CI jobs fetch cached files at the start and save them again at the end (pull-push cache policy). This ensures the job's changes are available in subsequent runs.

### Pull Policy

The `pull` policy fetches the cache before a job starts. It's turned on for all jobs by default.

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
  policy: pull
```

### Push Policy

Conversely, the `push` policy saves the cache after a job finishes, making it accessible to later jobs.

```yaml
update cache:
  stage: cache
  script:
    - npm install
  cache:
      key: ${CI_COMMIT_REF_SLUG}
      paths:
        - node_modules/
      policy: push
  only:
    - schedules
```

**Note:** In this example, `update cache` renews the cache with `npm install` and only runs for scheduled pipelines.

## Scheduling Cache Updates

**Insight:** Periodically refreshing the cache is crucial, especially for tasks like `npm install` that monitor for dependency changes.

**Implementation:** With GitLab CI, you can create jobs that run under specific conditions. For instance, a job might only activate when a pipeline is initiated by a schedule.

## Understanding `except: schedules`

### Concepts

The `except` directive tells GitLab CI when **not** to run a job. So, if you have a job that you don't want to run during a scheduled pipeline, you would use this directive.

In this specific case:

```yaml
except:
  - schedules
```

This means that the job containing this configuration will run for all pipeline triggers (like manual, push, merge requests, etc.) **except** when the pipeline is triggered by a scheduled run.

### Why would you use this?

There could be jobs that you only want to run when you push changes, or when you merge a pull request, etc., but not when a pipeline is triggered on a schedule (like every night or once a week). 

For example, if you have a nightly scheduled job that updates caches or does some cleanup, you might not want to run certain tests or deployments during that specific run. The `except: schedules` would allow you to skip those jobs for that scheduled pipeline.

### Example

```yaml
build website:
  stage: build
  script:
    - echo $CI_COMMIT_SHORT_SHA
    - npm install
    - npm install -g gatsby-cli
    - gatsby build
    - sed -i "s/%%VERSION%%/$CI_COMMIT_SHORT_SHA/" ./public/index.html
  artifacts:
    paths:
      - ./public
  except:
   - schedules
```

The provided GitLab CI configuration is for a job named `build website`. This job performs several steps to build a website, likely a static site given that it's using `gatsby-cli`.

### What does `except: schedules` mean in this context?

The `except` keyword is used to specify conditions where the job should **not** run. In this case, the condition provided is `schedules`.

So, `except: schedules` means that the `build website` job will run for all pipeline triggers (like manual triggers, push events, merge requests, etc.) **except** when the pipeline is triggered by a scheduled event (like a nightly or weekly scheduled run).

### Why use `except: schedules`?

Imagine you have a scheduled pipeline that runs some maintenance tasks every night or performs regular backups. If the `build website` job is resource-intensive or if there's no need to rebuild the website during these scheduled maintenance tasks, you'd use `except: schedules` to prevent the job from running and consuming resources unnecessarily.

In simpler terms, with this configuration:

- Whenever you push code, the `build website` job will run.
- If you create a merge request, the `build website` job will run.
- However, if you have set up a scheduled task in GitLab to trigger the pipeline, let's say every night at midnight, the `build website` job will **not** run during that scheduled task.

This gives you more control over when specific jobs in your CI/CD pipeline execute.

## Setting up a scheduled task in GitLab

Setting up a scheduled pipeline in GitLab is straightforward. Scheduled pipelines let you run CI/CD jobs at specific intervals, such as nightly builds or weekly deployments. Here's how to set one up:

## Setting up a Scheduled Task in GitLab

1. **Navigate to Your Project**
   
- Open your GitLab instance and navigate to your desired project.

2. **Go to CI/CD Settings**
   
- On the left sidebar, find the "CI/CD" section.
- Click on "Schedules".

3. **Create a New Schedule**

- On the right side of the "Pipeline schedules" page, click on the "New Schedule" button.

4. **Configure the Schedule**

- **Description**: Enter a meaningful description for your scheduled task.
- **Interval Pattern**: Select how often you want the pipeline to run. You can choose from predefined options like "Every hour" or use cron syntax to define custom intervals. For example:
    - `0 * * * *` - Every hour.
    - `0 0 * * *` - Every day at midnight.
    - `0 0 * * 0` - Every Sunday at midnight.
- **Target Branch**: Choose the branch you want this scheduled pipeline to target. This is often `main` or `master` for most projects, but you can specify any branch.

In our case, to periodically trigger the pipeline for cache updates:

- **Description:** `Update Cache`
- **Interval Pattern:** Daily at 4:00 am - `0 4 * * *`

5. **Add Variables (Optional)**

- If your CI/CD tasks need specific variables during the scheduled run, you can define them here. For example, you might have a specific configuration or token that should be used only during scheduled runs.

6. **Save Pipeline Schedule**
   
- Click on the "Save pipeline schedule" button to save and activate your schedule.

7. **Verify the Schedule**

- Once you've saved the schedule, you'll be taken back to the "Pipeline schedules" page. Here, you should see your new schedule listed, along with its next run time. Make sure everything looks correct.

8. **Monitor the Scheduled Pipeline**

- When the schedule triggers, a new pipeline will be started. You can monitor its progress, just as you would with any other pipeline, by going to the "Pipelines" section under "CI/CD" in the left sidebar.

## Conclusion

Boosting cache efficiency in your GitLab CI pipeline can lead to swifter job completions. By discerning the right moments and manners to utilize the cache, you ensure a smooth pipeline flow.

## References

- [GitLab CI Cache Guide](https://docs.gitlab.com/ee/ci/caching/)
- [GitLab CI Schedules Guide](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)
- [GitLab CI YAML Configuration](https://docs.gitlab.com/ee/ci/yaml/)