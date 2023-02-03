# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url

    _ = aws_console_url.BotoSesManager

    aws = aws_console_url.AWSConsole()

    _ = aws.a2i
    _ = aws.awslambda
    _ = aws.cloudformation
    _ = aws.codebuild
    _ = aws.codecommit
    _ = aws.dynamodb
    _ = aws.glue
    _ = aws.ground_truth
    _ = aws.iam
    _ = aws.sqs

    aws_res = aws_console_url.resource
    _ = aws_res.LambdaFunction


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
