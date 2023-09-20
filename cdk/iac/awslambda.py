# -*- coding: utf-8 -*-

import typing as T
import os
import textwrap

from aws_cdk import (
    aws_lambda as lambda_,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class AWSLambdaMixin:
    def mk_awslambda(self: "MainStack"):
        self.lbd_func = lambda_.Function(
            self,
            "LambdaFunction",
            function_name=f"{self.prefix_snake}_test",
            handler="lambda_function.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.from_inline(
                textwrap.dedent(
                    """
                def lambda_handler(event, context):
                    return {"status": 200}
                """
                )
            ),
        )
        self.lbd_alias = lambda_.Alias(
            self,
            "LambdaAlias",
            alias_name="LIVE",
            version=self.lbd_func.current_version,
        )

        self.lbd_layer = lambda_.LayerVersion(
            self,
            "LambdaLayer",
            layer_version_name=f"{self.prefix_snake}_test",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "artifacts")
            ),
        )
