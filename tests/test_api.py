# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url.api as aws_console_url

    aws = aws_console_url.AWSConsole()

    
    _ = aws.a2i
    _ = aws.apigateway
    _ = aws.athena
    _ = aws.awslambda
    _ = aws.batch
    _ = aws.cloudformation
    _ = aws.cloudwatch
    _ = aws.codebuild
    _ = aws.codecommit
    _ = aws.codepipeline
    _ = aws.dynamodb
    _ = aws.ec2
    _ = aws.ecr
    _ = aws.ecs
    _ = aws.eventbridge
    _ = aws.glue
    _ = aws.ground_truth
    _ = aws.iam
    _ = aws.kinesis
    _ = aws.kinesis_firehose
    _ = aws.kinesis_video
    _ = aws.kms
    _ = aws.rds
    _ = aws.s3
    _ = aws.sagemaker
    _ = aws.secretmanager
    _ = aws.sns
    _ = aws.sqs
    _ = aws.ssm
    _ = aws.step_function
    _ = aws.vpc


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])