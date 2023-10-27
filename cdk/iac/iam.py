# -*- coding: utf-8 -*-

import typing as T

from aws_cdk import (
    aws_iam as iam,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class IamMixin:
    def mk_iam(self: "MainStack"):
        self.iam_managed_policy = iam.ManagedPolicy(
            self,
            "IamManagedPolicy",
            managed_policy_name=f"{self.prefix_snake}_test",
            document=iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.DENY,
                        actions=["*"],
                        resources=["*"],
                    ),
                ],
            ),
        )

        self.iam_inline_policy = iam.Policy(
            self,
            "IamInlinePolicy",
            policy_name=f"{self.prefix_snake}_test_inline_policy",
            document=iam.PolicyDocument(
                statements=[
                    iam.PolicyStatement(
                        effect=iam.Effect.DENY,
                        actions=["*"],
                        resources=["*"],
                    ),
                ],
            ),
        )
        self.iam_role = iam.Role(
            self,
            "IamRole",
            role_name=f"{self.prefix_snake}_test",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[self.iam_managed_policy],
        )
        self.iam_role.attach_inline_policy(self.iam_inline_policy)

        self.iam_group = iam.Group(
            self,
            "IamGroup",
            group_name=f"{self.prefix_snake}_test",
        )

        self.iam_user = iam.User(
            self,
            "IamUser",
            user_name=f"{self.prefix_snake}_test",
            managed_policies=[self.iam_managed_policy],
        )
        self.iam_user.attach_inline_policy(self.iam_inline_policy)
