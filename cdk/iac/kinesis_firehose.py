# -*- coding: utf-8 -*-

import typing as T
import os

import aws_cdk as cdk
from aws_cdk import (
    aws_iam as iam,
    aws_kinesisfirehose as kinesisfirehose,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class KinesisFirehoseMixin:
    def mk_kinesis_firehose(self: "MainStack"):
        self.iam_role_for_kinesis_firehose_delivery_stream_exec = iam.Role(
            self,
            "IamRoleForKinesisFirehoseDeliveryStreamExec",
            assumed_by=iam.ServicePrincipal("firehose.amazonaws.com"),
            role_name=f"{self.prefix_snake}_kinesis_firehose_delivery_stream_exec",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("PowerUserAccess")
            ]
        )

        self.kinesis_firehose_delivery_stream = kinesisfirehose.CfnDeliveryStream(
            self,
            "KinesisFirehoseDeliveryStream",
            delivery_stream_name=f"{self.prefix_snake}_test",
            delivery_stream_type="KinesisStreamAsSource",
            kinesis_stream_source_configuration=kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                kinesis_stream_arn=self.kinesis_data_stream.stream_arn,
                role_arn=self.iam_role_for_kinesis_firehose_delivery_stream_exec.role_arn,
            ),
            s3_destination_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                bucket_arn=self.s3_bucket.bucket_arn,
                role_arn=self.iam_role_for_kinesis_firehose_delivery_stream_exec.role_arn,
            )
        )
        self.kinesis_firehose_delivery_stream.apply_removal_policy(cdk.RemovalPolicy.DESTROY)
