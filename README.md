## Deploy a manageddevelopment environment for your ETL Pipeline

This repository contains a cloudformation template, sample jupyter notebooks, sample transformation code, and a few supporting scripts to create a managed development sandbox environment for AWS Glue ETL jobs. This repository is part of AWS blog to provide AWS CloudFormation template and necessary scripts to create a managed sandbox environment and a controlled deployment pipeline for AWS Glue ETL jobs. 

## Usage

### Prerequisites

Create an s3 bucket and copy the folders cloudformation, sample and scripts along with all the files. 

### Stack

Use the myCloudFormationTemplate.json file to create a stack in AWS CloudFormation. For the purposes of the demo, all parameters can be left to default except the `sandboxS3Bucket` which should be set to the s3 bucket created in prerequisites. The CloudFormation template will create the following resources. 

Resource ID |   Resource Name   |   Resource Type
----------- |   -------------   |   -------------
CodeCommitRepository    |   ETLDevSandboxCodeCommitRepository   |   AWS::CodeCommit::Repository
getGlueDEP	|   ETLDevSandbox_GlueDevEndPoint   |   AWS::Glue::DevEndpoint
glueDevEndPointRole |   ETLDevSandbox_GlueRole  |   AWS::IAM::Role
glueWrapperJob  |   ETLDevSandbox_GlueJob   |   AWS::Glue::Job
lambdaFunction  |   ETLDevSandbox_LambdaFunction    |   AWS::Lambda::Function
lambdaPermission    |   sandbox-to-etl-stack-lambdaPermission-__________ |   AWS::Lambda::Permission
lambdaRole  |   ETLDevSandbox_LambdaRole    |   AWS::IAM::Role
sageMakerNotebook   |   arn:aws:sagemaker:us-east-1:account-number:notebook-instance/etldevsandbox-sagemakernotebook  |   AWS::SageMaker::NotebookInstance
sageMakerNotebookLifeCycleConfig    |   arn:aws:sagemaker:us-east-1:account-number:notebook-instance-lifecycle-config/sagemakernotebooklifecycleconfig    | AWS::SageMaker::NotebookInstanceLifecycleConfig
sagemakerNotebookRole   |   ETLDevSandbox_SagemakerNotebookRole | AWS::IAM::Role

### Other Contents

1. sample - This folder contains the sample code that you can run on the SageMaker noteboook as well as a sample transformation code to follow along the post.

2. scripts - This folder contains a script for AWS Glue job, a zip file which will work as initial contents of the AWS CodeCommit repository that will be created, and a zip file that includes the source code for the AWS Lambda function within the stack. 

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

