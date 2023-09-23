# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url.api as aws_console_url

    aws = aws_console_url.AWSConsole()

    
    _ = aws.vpc
    _ = aws.rds
    _ = aws.dynamodb
    _ = aws.codecommit
    _ = aws.iam
    _ = aws.sqs
    _ = aws.secretmanager
    _ = aws.cloudformation
    _ = aws.batch
    _ = aws.ground_truth
    _ = aws.codebuild
    _ = aws.glue
    _ = aws.step_function
    _ = aws.a2i
    _ = aws.sagemaker
    _ = aws.cloudwatch
    _ = aws.ec2
    _ = aws.ecr
    _ = aws.codepipeline
    _ = aws.s3
    _ = aws.awslambda
    _ = aws.ssm
    _ = aws.ecs
    _ = aws.sns


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])