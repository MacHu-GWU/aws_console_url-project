# -*- coding: utf-8 -*-

"""
This module is the CloudFormation stack definition.
"""

import aws_cdk as cdk
from constructs import Construct

from .iam import IamMixin
from .s3 import S3Mixin


class MainStack(
    cdk.Stack,
    IamMixin,
    S3Mixin,
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
