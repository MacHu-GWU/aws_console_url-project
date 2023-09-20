# -*- coding: utf-8 -*-

"""
This module is the CloudFormation stack definition.
"""

import aws_cdk as cdk
from constructs import Construct

from .helper import HelperMixin

from .awslambda import AWSLambdaMixin
from .batch import BatchMixin
from .cloudformation import CloudFormationMixin
from .codecommit import CodeCommitMixin
from .dynamodb import DynamoDBMixin
from .ecr import ECRMixin
from .iam import IamMixin
from .s3 import S3Mixin
from .secretmanager import SecretManagerMixin
from .sns import SNSMixin
from .sqs import SQSMixin
from .ssm import SSMMixin


class MainStack(
    cdk.Stack,
    HelperMixin,
    AWSLambdaMixin,
    BatchMixin,
    CloudFormationMixin,
    CodeCommitMixin,
    DynamoDBMixin,
    ECRMixin,
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

        # --- bmt_infra account
        def make_bmt_infra():
            # self.mk_awslambda()
            # self.mk_batch()
            self.mk_cloudformation()
            # self.mk_codecommit()
            # self.mk_dynamodb()
            # self.mk_ecr()
            # self.mk_iam()
            # self.mk_s3()
            # self.mk_secretsmanager()
            # self.mk_sns()
            # self.mk_sqs()
            # self.mk_ssm()

        # make_bmt_infra()

        # --- awshsh_app_dev account
        def make_awshsh_app_dev():
            self.mk_awslambda()
            self.mk_batch()
            # self.mk_cloudformation()
            self.mk_codecommit()
            self.mk_dynamodb()
            self.mk_ecr()
            self.mk_iam()
            self.mk_s3()
            self.mk_secretsmanager()
            self.mk_sns()
            self.mk_sqs()
            self.mk_ssm()

        make_awshsh_app_dev()

