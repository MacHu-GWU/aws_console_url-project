# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_iam as iam,
    aws_logs as logs,
    aws_stepfunctions as sfn,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class StepFunctionMixin:
    def mk_stepfunction(self: "MainStack"):
        # sfn = StepFunction, sm = state machine
        self.iam_role_for_sfn_statemachine = iam.Role(
            self,
            "IamRoleForSFNStatemachine",
            assumed_by=iam.ServicePrincipal("states.amazonaws.com"),
            role_name=f"{self.prefix_snake}_sfn_statemachine",
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess"),
            ]
        )

        self.sfn_standard_sm_log_group = logs.LogGroup(
            self,
            f"SFNStandardStateMachineLogGroup",
            log_group_name=f"/aws/vendedlogs/states/{self.prefix_snake}_standard_test-Logs",
        )
        self.sfn_standard_sm_log_group.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.sfn_standard_sm = sfn.CfnStateMachine(
            self,
            f"SFNStandardStateMachine",
            definition={
                "Comment": "A description of my state machine",
                "StartAt": "Pass",
                "States": {"Pass": {"Type": "Pass", "End": True}},
            },
            state_machine_name=f"{self.prefix_snake}_standard_test",
            state_machine_type="STANDARD",
            role_arn=self.iam_role_for_sfn_statemachine.role_arn,
            logging_configuration=sfn.CfnStateMachine.LoggingConfigurationProperty(
                destinations=[
                    sfn.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=sfn.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn=self.sfn_standard_sm_log_group.log_group_arn,
                        )
                    )
                ],
                include_execution_data=False,
                level="ALL",
            ),
        )

        self.sfn_express_sm_log_group = logs.LogGroup(
            self,
            f"SFNExpressStateMachineLogGroup",
            log_group_name=f"/aws/vendedlogs/states/{self.prefix_snake}_express_test-Logs",
        )
        self.sfn_express_sm_log_group.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.sfn_express_sm = sfn.CfnStateMachine(
            self,
            f"SFNExpressStateMachine",
            definition={
                "Comment": "A description of my state machine",
                "StartAt": "Pass",
                "States": {"Pass": {"Type": "Pass", "End": True}},
            },
            state_machine_name=f"{self.prefix_snake}_express_test",
            state_machine_type="EXPRESS",
            role_arn=self.iam_role_for_sfn_statemachine.role_arn,
            logging_configuration=sfn.CfnStateMachine.LoggingConfigurationProperty(
                destinations=[
                    sfn.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=sfn.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn=self.sfn_express_sm_log_group.log_group_arn,
                        )
                    )
                ],
                include_execution_data=False,
                level="ALL",
            ),
        )
