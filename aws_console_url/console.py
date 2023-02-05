# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from boto_session_manager import BotoSesManager

from .compat import cached_property

from .srv.a2i import A2I
from .srv.awslambda import AWSLambda
from .srv.cloudformation import CloudFormation
from .srv.codebuild import CodeBuild
from .srv.codecommit import CodeCommit
from .srv.dynamodb import Dynamodb
from .srv.ec2 import EC2
from .srv.ecr import ECR
from .srv.glue import Glue
from .srv.ground_truth import GroundTruth
from .srv.iam import Iam
from .srv.s3 import S3
from .srv.sagemaker import SageMaker
from .srv.secretmanager import SecretManager
from .srv.sqs import SQS
from .srv.ssm import SSM
from .srv.step_function import StepFunction
from .srv.vpc import VPC


@dataclasses.dataclass
class AWSConsole:
    """
    Public API for AWS Console URL builder.

    :param aws_account_id: optional, explicit AWS account ID.
    :param aws_region: optional, explicit AWS region.
    :param is_us_gov_cloud: default False, is this AWS account in US Gov Cloud?
    :param bsm: optional, the ``boto_session_manager.BotoSesManager`` object.
        Sometimes we need to call AWS API for some information to build the console url.
    """
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    bsm: BotoSesManager = dataclasses.field(default=lambda: BotoSesManager())
    
    @cached_property
    def a2i(self) -> A2I:
        return A2I._from_aws_console(self)
    
    @cached_property
    def awslambda(self) -> AWSLambda:
        return AWSLambda._from_aws_console(self)
    
    @cached_property
    def cloudformation(self) -> CloudFormation:
        return CloudFormation._from_aws_console(self)
    
    @cached_property
    def codebuild(self) -> CodeBuild:
        return CodeBuild._from_aws_console(self)
    
    @cached_property
    def codecommit(self) -> CodeCommit:
        return CodeCommit._from_aws_console(self)
    
    @cached_property
    def dynamodb(self) -> Dynamodb:
        return Dynamodb._from_aws_console(self)
    
    @cached_property
    def ec2(self) -> EC2:
        return EC2._from_aws_console(self)
    
    @cached_property
    def ecr(self) -> ECR:
        return ECR._from_aws_console(self)
    
    @cached_property
    def glue(self) -> Glue:
        return Glue._from_aws_console(self)
    
    @cached_property
    def ground_truth(self) -> GroundTruth:
        return GroundTruth._from_aws_console(self)
    
    @cached_property
    def iam(self) -> Iam:
        return Iam._from_aws_console(self)
    
    @cached_property
    def s3(self) -> S3:
        return S3._from_aws_console(self)
    
    @cached_property
    def sagemaker(self) -> SageMaker:
        return SageMaker._from_aws_console(self)
    
    @cached_property
    def secretmanager(self) -> SecretManager:
        return SecretManager._from_aws_console(self)
    
    @cached_property
    def sqs(self) -> SQS:
        return SQS._from_aws_console(self)
    
    @cached_property
    def ssm(self) -> SSM:
        return SSM._from_aws_console(self)
    
    @cached_property
    def step_function(self) -> StepFunction:
        return StepFunction._from_aws_console(self)
    
    @cached_property
    def vpc(self) -> VPC:
        return VPC._from_aws_console(self)
    