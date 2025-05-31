# AWS_Boto3_script

This repository contains a collection of Python automation scripts that leverage the boto3 library to interact with various AWS services. These scripts are designed to help you automate common AWS tasks such as listing IAM users, enumerating EC2 instances, and creating new EC2 instances programmatically.

## Features

 - List IAM User Accounts: Retrieve and display all IAM user accounts in your AWS environment.
 - List IAM Users: Enumerate users managed by AWS Identity and Access Management.
 - List EC2 Instances: Fetch details of all EC2 instances running in your AWS account.
 - Create EC2 Instance: Automate the creation of new EC2 instances with customizable parameters.

## Prerequisities

- Python 3.x 
[Download python](https://www.python.org/downloads/)

- pip 
[install pip](https://pip.pypa.io/en/stable/installation/)
Python package manager for installing dependencies.
Make ensure to install latest pip version and matches installation command using with python 

- AWS CLI
[install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
For configuring your AWS credentials and default region. 


## Installation and Execute scripts

1. Install boto3 to local machine

```bash
 pip install boto3

```

2. Install AWS CLI user
```bash 
pip install awscli --upgrade --user
```

3. Configure AWS CLI - Make ensure to provide correct credentials and correct region for CLI.

```bash
aws Configure
```

4. Clone repository - Clone repository that contains boto3 scripts.

```bash
git clone https://github.com/GitAvi001/AWS_Boto3_script
```
5. Select the correct script file and run the python file to see the automated task result.

## Links

Read and Learn more about Boto3 
[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

