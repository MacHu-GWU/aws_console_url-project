# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from .srv.awslambda import AWSLambda
from .srv.dynamodb import Dynamodb


@dataclasses.dataclass
class AWSConsole:
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)

    @property
    def awslambda(self) -> AWSLambda:
        return AWSLambda(aws_service="lambda")

    @property
    def dynamodb(self) -> Dynamodb:
        return Dynamodb(aws_service="dynamodbv2")
