# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from .compat import cached_property

from .srv.awslambda import AWSLambda
from .srv.dynamodb import Dynamodb
from .srv.iam import Iam


@dataclasses.dataclass
class AWSConsole:
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)

    @cached_property
    def awslambda(self) -> AWSLambda:
        return AWSLambda._from_aws_console(self)

    @cached_property
    def dynamodb(self) -> Dynamodb:
        return Dynamodb._from_aws_console(self)

    @cached_property
    def iam(self) -> Iam:
        return Iam._from_aws_console(self)
