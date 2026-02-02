# Setting Up SSH Authentication with GitLab

## Table of Contents

- [Introduction](#introduction)
- [Step-by-Step Guide](#step-by-step-guide)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

This lesson guides you through the process of setting up SSH authentication with your GitLab account. If you already have a GitLab account and have set up SSH authentication, feel free to skip this lesson and proceed to the next one.

## Step-by-Step Guide

1. **Create a GitLab account**: Visit [gitlab.com](https://gitlab.com/) to sign up and log in.

2. **Access SSH settings**: Once logged in, click on your profile picture (top-right corner) and select `Settings`. In the settings menu, find and click on `SSH Keys`.

3. **Understand SSH authentication**: SSH authentication works with a pair of keys – a public key and a private key. The public key is shared with services (like GitLab) that you wish to authenticate with, while the private key acts as a secret password stored on your machine.

4. **Generate SSH Key**: To generate a new SSH key, open your terminal (Bash for Windows users), and enter the following command:

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This command requests an RSA key with a size of 4096 bits. Replace `"your_email@example.com"` with your GitLab email address.

5. **Store the SSH Key**: When prompted to "Enter a file in which to save the key," press `Enter` to accept the default location. 

6. **Secure the SSH Key**: It is recommended to secure the key with a passphrase for an added layer of security. If your key is stolen, the thief would still need the passphrase to use it. Follow the prompts to enter and confirm your passphrase.

7. **Export the Public Key**: After creating the SSH key, you need to share your public key with GitLab. Run the following command to display your public key:

```sh
cat ~/.ssh/id_rsa.pub
```

**Important**: Ensure you include `.pub` at the end. Without this, you will display your private key, which should remain secret.

8. **Copy the Public Key**: The output will be a long string of text, which is your public key. Copy this entire string.

9. **Add the Public Key to GitLab**: Return to the SSH keys settings in GitLab. Click on `Add SSH Key`, paste your public key into the `Key` field, give it a suitable title, and click `Add Key`.

**Note**: Remember to keep your private key secure by storing it in a safe location and protecting it with a strong passphrase. Additionally, never share your private key with anyone and ensure that only the public key is added to GitLab.

## Conclusion

Setting up SSH authentication with your GitLab account is a crucial step to ensure secure and convenient access to your repositories. By following the step-by-step guide provided above, you have learned how to create a GitLab account, generate an SSH key pair, and add the public key to your GitLab account. SSH authentication provides an additional layer of security by using a pair of keys – a public key and a private key – for authentication purposes.

With SSH authentication set up, you can now securely interact with your GitLab repositories, clone repositories, and perform other Git operations without the need to provide your username and password repeatedly.

## References

The following references provide additional information and resources related to SSH authentication and GitLab:

- GitLab Documentation: [SSH key](https://docs.gitlab.com/ee/ssh/)
- GitLab Documentation: [Adding an SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/#adding-an-ssh-key-to-your-gitlab-account)
- GitLab Documentation: [SSH keys in Git](https://docs.gitlab.com/ee/ssh/#ssh-keys-in-git)
- OpenSSH Documentation: [SSH key management](https://www.openssh.com/manual.html#public-key-management)
- GitHub Help: [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- GitHub Help: [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)