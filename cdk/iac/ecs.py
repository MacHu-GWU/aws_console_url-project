# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class ECSMixin:
    def mk_ecs(self: "MainStack"):
        self.ecs_cluster = ecs.Cluster(
            self,
            id="EcsCluster",
            cluster_name=f"{self.prefix_snake}_test",
            vpc=ec2.Vpc.from_lookup(
                self,
                id="ECSClusterDefaultVpc",
                is_default=True,
            ),
        )
        self.ecs_cluster.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.ecs_task_def = ecs.FargateTaskDefinition(
            self,
            id="EcsTaskDef",
            family=f"{self.prefix_snake}_test",
        )
        self.ecs_task_def.add_container(
            "web",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
        )
        self.ecs_task_def.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        # self.ecs_service = ecs.FargateService(
        #     self,
        #     "FargateService",
        #     service_name=f"{self.prefix_snake}_test",
        #     cluster=self.ecs_cluster,
        #     task_definition=self.ecs_task_def,
        #     capacity_provider_strategies=[
        #         ecs.CapacityProviderStrategy(
        #             capacity_provider="FARGATE_SPOT",
        #             weight=2,
        #         ),
        #         ecs.CapacityProviderStrategy(
        #             capacity_provider="FARGATE",
        #             weight=1,
        #         ),
        #     ],
        # )
        # self.ecs_service.apply_removal_policy(cdk.RemovalPolicy.DESTROY)
