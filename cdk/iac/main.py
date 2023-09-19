# -*- coding: utf-8 -*-

"""
This module is the CloudFormation stack definition.
"""

import aws_cdk as cdk
from constructs import Construct

from .awslambda import LambdaMixin
from .iam import IamMixin
from .s3 import S3Mixin
from .secretmanager import SecretManagerMixin
from .sns import SNSMixin
from .sqs import SQSMixin
from .ssm import SSMMixin


class MainStack(
    cdk.Stack,
    LambdaMixin,
    IamMixin,
    S3Mixin,
    SecretManagerMixin,
    SNSMixin,
    SQSMixin,
    SSMMixin,
):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        prefix: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.prefix_slug = prefix.replace("_", "-")
        self.prefix_snake = prefix.replace("-", "_")

        self.mk_lambda()
        self.mk_iam()
        self.mk_s3()
        self.mk_secretsmanager()
        self.mk_sns()
        self.mk_sqs()
        self.mk_ssm()
