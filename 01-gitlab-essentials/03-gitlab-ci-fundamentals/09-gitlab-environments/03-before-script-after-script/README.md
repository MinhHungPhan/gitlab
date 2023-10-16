# Before_Script & After_Script Configuration

## Table of Contents

- [Introduction](#introduction)
- [Before_Script Configuration](#before_script-configuration)
   - [Why Use Before_Script?](#why-use-before_script)
   - [Example](#example)
- [After_Script Configuration](#after_script-configuration)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

Welcome to a concise overview of `before_script` and `after_script` configurations in GitLab CI. These configurations allow for better script organization, ensuring efficient and clean CI/CD processes.

## Before_Script Configuration

The `before_script` configuration in GitLab CI defines a command or set of commands that are executed before the main script runs.

### Why Use Before_Script?

1. **Global vs. Job Level**: `before_script` can be defined at both the global level and the job level. Defining it at the job level can override the global configuration.
2. **Script Separation**: If you have setup-related commands, such as installing dependencies required for your main script, you can separate them using `before_script`. This distinction makes your main script concise and easier to understand.
3. **Enhanced Readability**: Utilizing `before_script` can help clarify your CI configuration, making the pipeline easier to read and comprehend.

### Example

Imagine you have a deployment step and need to install certain tools or dependencies before the main deployment script runs. Here's how you might organize it:

```yaml
deploy production: 
  stage: deploy production
  environment:
    name: production
    url: $PRODUCTION_DOMAIN
  only:
    - main
  before_script:
    - npm install --global surge
  script:
    - surge --project ./public --domain $PRODUCTION_DOMAIN
```

In this example, `before_script` prepares the environment, making it evident what is done for setup and what the main task is.

## After_Script Configuration

The `after_script` is different from `before_script`. It's executed after the main `script`, but the working directory defaults back, and its execution context differs from both `before_script` and the main `script`.

Be aware that:

1. **The local working directory has been set back to default:**

- In computing, the "working directory" refers to the current folder or location in which tasks or commands are being executed. When using `after_script` in GitLab CI, any changes you made to the working directory during the main `script` or `before_script` will not persist. Instead, the working directory will revert to its original state when `after_script` starts executing. 

2. **Commands are executed in a separate context from before_script and script scripts:**

- "Context" here refers to the environment or settings in which commands are executed. This could include available environment variables, system settings, user permissions, and more. 
- This statement means that the conditions or environment under which the `after_script` commands run might be different from the conditions for `before_script` and the main `script`. So, if you set certain conditions or variables in `before_script` or `script`, they might not be available or might behave differently in `after_script`.

To simplify:

When you're using `after_script` in GitLab CI, think of it as a reset space. It goes back to the original folder it started in, and it might not "remember" certain settings or conditions from earlier parts of the CI process.

For more in-depth understanding and usage scenarios, it's advised to consult the official documentation.

## Conclusion

Understanding and using `before_script` and `after_script` configurations can streamline your GitLab CI configurations. Whether or not you choose to use them is up to your specific use-case, but they offer additional structuring options that can improve clarity and maintainability.

## References

- [GitLab CI Documentation: before_script & after_script](https://docs.gitlab.com/ee/ci/yaml/#before_script-and-after_script)