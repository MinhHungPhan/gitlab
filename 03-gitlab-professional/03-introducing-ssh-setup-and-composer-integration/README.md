# Introducing SSH Setup and Composer Integration

## Introduction

This tutorial focuses on the significant enhancements in our `gitlab-ci.yml` file, emphasizing the critical role of SSH setup and Composer dependency management in our CI/CD pipeline. The inclusion of these elements marks a progressive step towards a more secure and efficient workflow, particularly in handling dependencies and securing operations in our PHP projects.

## Table of Contents

- [Variables](#variables)
- [Provision and Composer Templates](#provision-and-composer-templates)
- [Workflow Rules in CI/CD Pipeline](#workflow-rules-in-cicd-pipeline)
- [Stages in CI/CD Pipeline](#stages-in-cicd-pipeline)
- [Unit Tests in CI/CD Pipeline](#unit-tests-in-cicd-pipeline)
- [Conclusion](#conclusion)
- [References](#references)

## Provision and Composer Templates

### Concepts

In GitLab CI/CD, `.provision` and `.composer` are examples of YAML anchors and aliases, which are used for reusing sections of the configuration. This technique helps to avoid duplication and makes the CI/CD configuration more maintainable.

### YAML Anchors and Aliases

- **Anchor (`&`)**: Defines a block of configuration that can be reused later.
- **Alias (`*`)**: References an anchor, essentially reusing the anchored block wherever the alias is placed.

### Usage in GitLab CI/CD

- `.provision`: This is likely a set of steps defined for setting up the environment, often involving SSH setup. The `&provision` creates an anchor named `provision`. 
  - Example Steps:
    - Setting up SSH agent.
    - Adding SSH keys.
    - Creating and securing the SSH directory.

- `.composer`: This anchor is probably used for steps involving the Composer tool, which is a dependency manager for PHP. The `&composer` creates an anchor named `composer`.
  - Example Steps:
    - Downloading and verifying Composer.
    - Installing dependencies using Composer.

### Application in CI/CD Jobs

You can reference these anchors in different jobs within your CI/CD pipeline. For instance, if multiple jobs require SSH setup or Composer, you can just use `*provision` or `*composer` in those jobs. This inclusion will copy all the steps from the respective anchors into the job, ensuring consistency and reducing redundancy.

### Example

- **Provision Template (`&provision`)**: 
  - Sets up SSH-agent for secure connections.
  - Ensures the SSH directory exists and has appropriate permissions.

- **Composer Template (`&composer`)**: 
  - Automates the installation of Composer, a PHP dependency manager.
  - Installs project dependencies and generates the autoloader with specific Composer commands.

In a job:

```yaml
unit_test:
    image: php:7.1-cli
    stage: test
    tags:
        - php70
    before_script:
        - *provision # This includes all the steps defined in .provision
        - *composer  # This includes all the steps defined in .composer
```

This approach is beneficial for maintaining complex CI/CD configurations, as it allows you to define common steps in one place and use them across multiple jobs, making updates and changes more manageable.

### Setting Up SSH in CI/CD:

The provision template securely sets up SSH within the CI/CD environment:

```yaml
.provision: &provision
    - 'which ssh-agent'
    - 'eval $(ssh-agent -s)'
    - 'echo "$SSH_ID_RSA" | tr -d "\\r" | ssh-add - > /dev/null'
    - 'mkdir -p ~/.ssh'
    - 'chmod 700 ~/.ssh'
```

### Using Composer for Dependency Management:

The composer template automates the installation and setup of Composer:

```yaml
.composer: &composer
    - php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    - php -r "if (hash_file('sha384', 'composer-setup.php') === 'e0012edf3e80b6978849f5eff0d4b4e4c79ff1609dd1e613307e16318854d24ae64f26d17af3ef0bf7cfb710ca74755a') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
    - mkdir bin
    - php composer-setup.php --filename=composer --install-dir=bin
    - php -r "unlink('composer-setup.php');"
    - 'bin/composer install --prefer-dist --no-interaction --ignore-platform-reqs'
    - 'bin/composer dumpautoload --no-interaction'
```

## Workflow Rules in CI/CD Pipeline

### Overview of Workflow Rules Configuration

The `workflow` section in the `gitlab-ci.yml` file defines the rules that determine when and how the CI/CD pipeline should be triggered. This is crucial for optimizing pipeline execution based on specific conditions, ensuring efficient resource utilization and targeted pipeline runs.

### Detailed Explanation of Workflow Rules

```yml
workflow:
    rules:
        - if: $CI_MERGE_REQUEST_ID
        - if: $CI_PROJECT_PATH == 'Accor/magento'
```

#### Rules:

1. **Merge Request Condition**:

- `if: $CI_MERGE_REQUEST_ID`
- This rule triggers the pipeline whenever there is a merge request. The presence of a merge request ID (`$CI_MERGE_REQUEST_ID`) in the CI/CD environment variables indicates an active merge request, and the pipeline will run in this context.

2. **Project Path Condition**:

- `if: $CI_PROJECT_PATH == 'Accor/magento'`
- This rule specifies that the pipeline should run if the project path matches `'Accor/magento'`. It ensures that the pipeline is executed for specific projects or repositories, in this case, a Magento project under the 'Accor' namespace.

### Example Use Cases

- **Merge Request Scenario**:
  - When a developer creates a merge request, the pipeline will automatically trigger, running all stages and jobs defined in the `gitlab-ci.yml`. This ensures that code changes are automatically tested, built, and reviewed before merging.

- **Project Specific Pipeline Execution**:
  - If the pipeline is part of a larger project with multiple sub-projects or repositories, this rule ensures that it only runs for changes made in the 'Accor/magento' project. This targeted execution prevents unnecessary runs for unrelated changes in other projects.

## Stages in CI/CD Pipeline

### Overview of Stages Configuration

In the `gitlab-ci.yml` file, the `stages` section defines the sequential phases that the pipeline will go through during its execution. Each stage can contain multiple jobs, and the stages are executed in the order they are defined. For your configuration, there are two stages specified: `test` and `full-test`.

### Stages Defined

1. **Test Stage (`test`)**:

- This is the first stage in the pipeline.
- Typically, this stage is used for running initial tests such as unit tests or other lightweight validations that do not require a full environment setup. It's a preliminary check to ensure basic code integrity and functionality.

2. **Full-Test Stage (`full-test`)**:

- This is the second stage in the pipeline.
- The `full-test` stage likely involves more comprehensive testing, possibly including integration tests, end-to-end tests, or other extensive testing procedures that require a complete environment setup or more resources. It's intended to thoroughly validate the application in a scenario that closely mirrors the production environment.

### Code Snippet from `gitlab-ci.yml`

```yaml
stages:
  - test
  - full-test
```

### Example Usage of Stages

1. **In the `test` Stage**:

- Jobs like `unit_test` might be executed. These jobs typically run quickly and provide immediate feedback on the code's integrity.
- `unit_test` job in this stage:

```yaml
# ... existing code ...
unit_test:
    image: php:7.1-cli
    stage: test
```

- `sonar-mr` job in this stage: 

```yaml
  # ... existing code ...
sonar-mr:
  image:
    name: newtmitch/sonar-scanner:3.2-alpine
    entrypoint: ['']
  stage: test
```

2. **In the `full-test` Stage**:

- More comprehensive testing jobs are executed. These jobs are usually more resource-intensive and take longer to complete.
- The jobs in this stage are crucial for ensuring that the application not only works in isolation (as verified in the `test` stage) but also functions correctly in a fully integrated environment.
- `sonar_analyse` job in this stage: 

```yaml
sonar_analyse:
  image:
    name: newtmitch/sonar-scanner:3.2-alpine
    entrypoint: ['']
  tags:
    - docker-accor
  stage: full-test
```

## Unit Tests in CI/CD Pipeline

### Overview of Unit Testing Configuration

The `unit_test` job in the `gitlab-ci.yml` file is pivotal in our continuous integration process. It ensures that code changes do not adversely affect existing functionalities.

#### Key Components of the Unit Test Job

1. **Image**: Utilizes `php:7.1-cli` for PHP applications.
2. **Stage**: Assigned to the `test` stage.
3. **Tags**: Tagged as `php70` for specific runner selection.
4. **Before Script**: Implements SSH setup and Composer for dependencies.
5. **Script**: Executes PHPUnit for unit testing.
6. **After Script**: Adjusts PHPUnit report formatting.
7. **Artifacts**: Generates and retains JUnit logs and reports.
8. **Reports**: JUnit report for easy accessibility in GitLab CI/CD.
9. **Allow Failure**: Temporarily set to `true` due to existing test issues.

#### Example Workflow

```yaml
# ---------------------- Unit tests ----------------------
unit_test:
  image: php:7.1-cli
  stage: test
  tags:
    - php70
  before_script:
    - *provision
    - *composer
  script:
    - './bin/phpunit -c ./dev/tests/unit/phpunit.xml.dist --log-junit junit/log.xml --coverage-xml junit/coverage/'
  after_script:
    # PHPUnit report format fix
    - 'python ci/script/path-phpunit-report.py junit/log.xml'
  artifacts:
    when: always
    expire_in: 1 week
    paths:
      - 'junit/'
    reports:
      junit: 'junit/log.xml'
  # Remove this line as soon as issues from unit tests are solved https://redmine-projets.smile.fr/issues/880097
  allow_failure: true
```

- Initializes SSH.
- Installs PHP dependencies.
- Runs PHPUnit tests.
- Formats and uploads test reports.

### Conclusion

The updated `gitlab-ci.yml` introduces significant improvements, particularly in the areas of secure connections (SSH setup) and dependency management (Composer). These changes facilitate a more robust and secure CI/CD pipeline, particularly beneficial for PHP projects.

### References

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [SSH Configuration in CI/CD](https://docs.gitlab.com/ee/ssh/)
- [Composer Documentation](https://getcomposer.org/doc/)
- [Optimize GitLab CI/CD configuration files: anchors ](https://docs.gitlab.com/ee/ci/yaml/yaml_optimization.html#anchors)