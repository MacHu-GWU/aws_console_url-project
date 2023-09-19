# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_secretsmanager as secretsmanager,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class SecretManagerMixin:
    def mk_secretsmanager(self: "MainStack"):
        self.sm_secret = secretsmanager.Secret(
            self,
            "SecretManagerSecret",
            secret_name=f"{self.prefix_slug}-test", # we have to use prefix_slug to test something
            description="Test",
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )