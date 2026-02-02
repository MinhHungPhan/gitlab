# Setting Up Personal Access Token with GitLab

## Table of Contents

- [Introduction](#introduction)
- [Step-by-Step Guide](#step-by-step-guide)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This tutorial guides you through the process of creating a Personal Access Token (PAT) for your GitLab account. Personal Access Tokens are used to authenticate with GitLab's API and Git operations when SSH keys are not available or when you need programmatic access to GitLab resources.

## Step-by-Step Guide

1. **Log in to GitLab**: Visit [gitlab.com](https://gitlab.com/) and log in to your account.

2. **Access Personal Access Tokens**: Click on your profile picture (top-right corner) and select `Settings`. In the left sidebar, find and click on `Access Tokens`.

3. **Create a New Token**: Click on `Add new token` button.

4. **Configure Token Settings**:
- **Token name**: Give your token a descriptive name (e.g., "My Development Token")
- **Expiration date**: Set an expiration date for security purposes (recommended)
- **Select scopes**: Choose the permissions your token needs:
  - `api` - Full API access
  - `read_repository` - Read access to repositories
  - `write_repository` - Write access to repositories
  - `read_registry` - Read access to container registry
  - `write_registry` - Write access to container registry

5. **Generate the Token**: Click `Create personal access token` button.

6. **Copy the Token**: **Important**: Copy your personal access token immediately. You won't be able to see it again once you leave the page.

7. **Store Securely**: Save the token in a secure location such as a password manager. Never commit tokens to your repository or share them publicly.

## Using Your Personal Access Token

### For Git Operations (HTTPS)

When cloning or pushing to a repository using HTTPS, use your token as the password:

```sh
git clone https://gitlab.com/username/repository.git
Username: your_username/email
Password: your_personal_access_token
```

### For API Requests

Use the token in API requests:

```sh
curl --header "PRIVATE-TOKEN: your_personal_access_token" "https://gitlab.com/api/v4/projects"
```

## Conclusion

Personal Access Tokens provide a secure way to authenticate with GitLab without using your account password. They offer fine-grained access control and can be revoked at any time. Remember to:

- Store tokens securely
- Set appropriate expiration dates
- Only grant necessary permissions
- Revoke tokens when no longer needed

## References

- [GitLab Documentation: Personal Access Tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
- [GitLab API Documentation](https://docs.gitlab.com/ee/api/)
- [GitLab Token Security Best Practices](https://docs.gitlab.com/ee/security/token_overview.html)
