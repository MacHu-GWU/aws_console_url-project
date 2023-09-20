# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_ecr as ecr,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class ECRMixin:
    def mk_ecr(self: "MainStack"):
        self.ecr_repo = ecr.Repository(
            self,
            id="EcrRepository",
            repository_name=f"{self.prefix_snake}_test",
            image_tag_mutability=ecr.TagMutability.MUTABLE,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )