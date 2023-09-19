# -*- coding: utf-8 -*-

"""
This module is the CloudFormation stack definition.
"""

import aws_cdk as cdk
from constructs import Construct

from .iam import IamMixin
from .s3 import S3Mixin
from .sns import SNSMixin
from .sqs import SQSMixin


class MainStack(
    cdk.Stack,
    IamMixin,
    S3Mixin,
    SNSMixin,
    SQSMixin,
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

        self.mk_iam()
        self.mk_s3()
        self.mk_sns()
        self.mk_sqs()
