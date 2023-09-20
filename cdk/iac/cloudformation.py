# -*- coding: utf-8 -*-

import typing as T
import json

from aws_cdk import (
    aws_cloudformation as cf,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class CloudFormationMixin:
    def mk_cloudformation(self: "MainStack"):
        self.cf_stack_set_self_managed = cf.CfnStackSet(
            self,
            "CloudFormationStackSetSelfManaged",
            stack_set_name=f"{self.prefix_slug}-test-self-managed",
            permission_model="SELF_MANAGED",
            template_body=json.dumps(
                {
                    "AWSTemplateFormatVersion": "2010-09-09",
                    "Resources": {
                        "S3Bucket": {
                            "Type": "AWS::S3::Bucket",
                            "Properties": {
                                "BucketName": f"{self.prefix_slug}-cf-test-self-managed-bucket",
                            },
                        }
                    },
                },
                indent=4,
            )
        )

        self.cf_stack_set_service_managed = cf.CfnStackSet(
            self,
            "CloudFormationStackSetServiceManaged",
            stack_set_name=f"{self.prefix_slug}-test-service-managed",
            permission_model="SERVICE_MANAGED",
            template_body=json.dumps(
                {
                    "AWSTemplateFormatVersion": "2010-09-09",
                    "Resources": {
                        "S3Bucket": {
                            "Type": "AWS::S3::Bucket",
                            "Properties": {
                                "BucketName": f"{self.prefix_slug}-cf-test-service-managed-bucket",
                            },
                        }
                    },
                },
                indent=4,
            ),
            call_as="DELEGATED_ADMIN",
            auto_deployment=cf.CfnStackSet.AutoDeploymentProperty(
                enabled=False,
            ),
        )
