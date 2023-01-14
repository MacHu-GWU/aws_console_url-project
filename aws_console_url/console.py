# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from boto_session_manager import BotoSesManager

from .compat import cached_property

from .srv.awslambda import AWSLambda
from .srv.cloudformation import CloudFormation
from .srv.codebuild import CodeBuild
from .srv.codecommit import CodeCommit
from .srv.dynamodb import Dynamodb
from .srv.iam import Iam
from .srv.sqs import SQS


@dataclasses.dataclass
class AWSConsole:
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    bsm: BotoSesManager = dataclasses.field(default=lambda: BotoSesManager())
    
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
    def iam(self) -> Iam:
        return Iam._from_aws_console(self)
    
    @cached_property
    def sqs(self) -> SQS:
        return SQS._from_aws_console(self)
    