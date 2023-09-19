# -*- coding: utf-8 -*-

import typing as T

from aws_cdk import (
    aws_ssm as ssm,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class SSMMixin:
    def mk_ssm(self: "MainStack"):
        self.ssm_parameter_1 = ssm.StringParameter(
            self,
            "SSMParameter1",
            parameter_name=f"{self.prefix_snake}_test_1",
            string_value="a dummy ssm parameter content",
        )

        self.ssm_parameter_2 = ssm.StringParameter(
            self,
            "SSMParameter2",
            parameter_name=f"/{self.prefix_snake}_test_2",
            string_value="a dummy ssm parameter content",
        )
