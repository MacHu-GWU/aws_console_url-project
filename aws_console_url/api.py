# -*- coding: utf-8 -*-

import dataclasses

from .builder import AWSConsole as AWSConsole_

from .srv.awslambda import AWSLambda
from .srv.dynamodb import Dynamodb
from .srv.iam import Iam


@dataclasses.dataclass
class AWSConsole(AWSConsole_):

    @property
    def awslambda(self) -> AWSLambda:
        return self.to_builder(AWSLambda)

    @property
    def dynamodb(self) -> Dynamodb:
        return self.to_builder(Dynamodb)

    @property
    def iam(self) -> Iam:
        return self.to_builder(Iam)
