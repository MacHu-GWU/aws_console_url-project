# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_iam as iam,
    aws_batch as batch,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class BatchMixin:
    def mk_batch(self: "MainStack"):
        self.batch_compute_environment = batch.CfnComputeEnvironment(
            self,
            "BatchComputeEnvironment",
            type="MANAGED",
            compute_environment_name=f"{self.prefix_snake}_test",
            compute_resources=batch.CfnComputeEnvironment.ComputeResourcesProperty(
                type="FARGATE",
                maxv_cpus=16,
                subnets=self.default_subnet_id_list,
                security_group_ids=[self.default_security_group_id],
            ),
        )
        self.batch_compute_environment.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.batch_job_queue = batch.CfnJobQueue(
            self,
            "BatchJobQueue",
            job_queue_name=f"{self.prefix_snake}_test",
            compute_environment_order=[
                batch.CfnJobQueue.ComputeEnvironmentOrderProperty(
                    compute_environment=self.batch_compute_environment.ref,
                    order=1,
                ),
            ],
            priority=1,
            state="ENABLED",
        )

        self.iam_role_for_batch_job_exec = iam.Role(
            self,
            "IamRoleForBatchJobExec",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            role_name=f"{self.prefix_snake}_batch_job_exec",
        )

        self.batch_job_def = batch.CfnJobDefinition(
            self,
            "BatchJobDefinition",
            job_definition_name=f"{self.prefix_snake}_test",
            type="container",
            platform_capabilities=["FARGATE"],
            container_properties=batch.CfnJobDefinition.ContainerPropertiesProperty(
                image="public.ecr.aws/lambda/python:3.8",
                execution_role_arn=self.iam_role_for_batch_job_exec.role_arn,
                resource_requirements=[
                    batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="VCPU",
                        value="0.25",
                    ),
                    batch.CfnJobDefinition.ResourceRequirementProperty(
                        type="MEMORY",
                        value="512",
                    ),
                ],
                network_configuration=batch.CfnJobDefinition.NetworkConfigurationProperty(
                    assign_public_ip="ENABLED",
                ),
            ),
        )
