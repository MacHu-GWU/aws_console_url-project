# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_kinesis as kinesis,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class KinesisMixin:
    def mk_kinesis(self: "MainStack"):
        self.kinesis_data_stream = kinesis.Stream(
            self,
            "KinesisDataStream",
            stream_name=f"{self.prefix_snake}_test",
            stream_mode=kinesis.StreamMode.ON_DEMAND,
        )
        self.kinesis_data_stream.apply_removal_policy(cdk.RemovalPolicy.DESTROY)
