# -*- coding: utf-8 -*-

import typing as T
import os

import aws_cdk as cdk
from aws_cdk import (
    aws_iam as iam,
    aws_kinesisvideo as kinesisvideo,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class KinesisVideoMixin:
    def mk_kinesis_video(self: "MainStack"):
        self.kinesis_video_stream = kinesisvideo.CfnStream(
            self,
            "KinesisVideoStream",
            name=f"{self.prefix_snake}_test",
        )
        self.kinesis_video_stream.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.kinesis_video_channel = kinesisvideo.CfnSignalingChannel(
            self,
            "KinesisVideoChannel",
            name=f"{self.prefix_snake}_test",
        )
        self.kinesis_video_channel.apply_removal_policy(cdk.RemovalPolicy.DESTROY)
