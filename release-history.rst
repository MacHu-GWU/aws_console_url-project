.. _release_history:

Release and Version History
==============================================================================
NOTE: version < 1.0.0 should be considered as unstable


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.1.1 (2023-10-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add support for:
    - event bridge.
    - kinesis stream.
    - kinesis firehose delivery stream.
    - kinesis video stream and channel.


1.0.1 (2023-09-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- 💥 First API stable release.
- 💥 Removed the AWS resources object. The functionality is replaced by the `aws_arns <https://github.com/MacHu-GWU/aws_arns-project>`_ project.
- Reworked the API,
    - the main entry point is now ``import aws_console_url.api as aws_console_url``.
    - most of get_xxx_resource() console url method takes both resource id or arn.


0.8.1 (2023-08-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add aws batch service
- add aws ecs service
- add codepipeline service
- add rds service
- add sns service


0.7.6 (2023-07-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- AWS updates the augmented ai related url, so we fixed ``a2i`` related URL.


0.7.5 (2023-05-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- add support to those resource name may have slash (SSM parameter)


0.7.4 (2023-05-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that when SSM parameter has a prefix "/", the console url is not correct.


0.7.3 (2023-03-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- cloudformation ``get_stack_set_xxx`` method now take name, stack_set_id or arn.


0.7.2 (2023-03-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- cloudformation ``get_stack`` method now take name or arn.


0.7.1 (2023-03-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add cloudformation stacksets support


0.6.1 (2023-02-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add cloudwatch service


0.5.1 (2023-02-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add s3 service
- add vpc service


0.4.1 (2023-02-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ec2 service
- add ssm service
- add secret manager service
- add ecr service
- add sagemaker service


0.3.1 (2023-02-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- refactor the public API
- add step function service
- add a list of public API


0.2.1 (2023-01-15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add support for the following AWS Services:
    - a2i
    - ground_truthın
    - glue


0.1.1 (2023-01-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add support for the following AWS Services:
    - awslambda
    - cloudformation
    - codebuild
    - codecommit
    - dynamodb
    - iam
    - sqs
