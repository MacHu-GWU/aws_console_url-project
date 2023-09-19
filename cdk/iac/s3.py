# -*- coding: utf-8 -*-

import typing as T
import os
import aws_cdk as cdk

from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class S3Mixin:
    def mk_s3(self: "MainStack"):
        self.s3_bucket = s3.Bucket(
            self,
            "S3Bucket",
            bucket_name=f"{self.prefix_slug}-test",
        )
        self.s3_object = s3_deployment.BucketDeployment(
            self,
            "S3Object",
            sources=[
                s3_deployment.Source.asset(
                    os.path.join(os.path.dirname(__file__), "artifacts")
                )
            ],
            destination_bucket=self.s3_bucket,
            destination_key_prefix="upload/",
        )
