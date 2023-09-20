# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_dynamodb as dynamodb,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class DynamoDBMixin:
    def mk_dynamodb(self: "MainStack"):
        self.dynamodb_table_key_only = dynamodb.Table(
            self,
            "DynamoDBTableKeyOnly",
            table_name=f"{self.prefix_snake}_test_key_only",
            partition_key=dynamodb.Attribute(
                name="pk",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        self.dynamodb_table_key_and_range = dynamodb.Table(
            self,
            "DynamoDBTableKeyAndRange",
            table_name=f"{self.prefix_snake}_test_key_and_range",
            partition_key=dynamodb.Attribute(
                name="pk",
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name="sk",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
