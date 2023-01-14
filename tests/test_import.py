# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url

    aws = aws_console_url.AWSConsole()

    _ = aws.awslambda
    _ = aws.dynamodb
    _ = aws.iam


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
