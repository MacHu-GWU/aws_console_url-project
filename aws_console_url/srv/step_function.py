# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

import aws_arns.api as aws_arns

from ..model import Service

T_SM_EXEC = T.Union[
    aws_arns.res.SfnStandardStateMachineExecution,
    aws_arns.res.SfnExpressStateMachineExecution,
]


@dataclasses.dataclass(frozen=True)
class StepFunction(Service):
    _AWS_SERVICE = "states"

    def _get_state_machine_obj(
        self,
        name_or_arn: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ) -> aws_arns.res.SfnStateMachine:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.SfnStateMachine.from_arn(name_or_arn)
        else:
            return aws_arns.res.SfnStateMachine.new(
                self._account_id,
                self._region,
                name_or_arn,
                version,
                alias,
            )

    def _get_state_machine_execution_obj(
        self,
        exec_id_or_arn: str,
        state_machine: T.Optional[str] = None,
        is_standard: T.Optional[bool] = None,
    ) -> T_SM_EXEC:
        if exec_id_or_arn.startswith("arn:"):
            arn = aws_arns.Arn.from_arn(exec_id_or_arn)
            if arn.resource_type == "execution":
                return aws_arns.res.SfnStandardStateMachineExecution.from_arn(
                    exec_id_or_arn
                )
            elif arn.resource_type == "express":
                return aws_arns.res.SfnExpressStateMachineExecution.from_arn(
                    exec_id_or_arn
                )
            else:  # pragma: no cover
                raise NotImplementedError(f"Unknown resource type: {arn.resource_type}")
        else:
            if state_machine is None or is_standard is None:
                raise ValueError(
                    "state_machine and is_standard must be specified if exec_id_or_arn is not an ARN"
                )
            if is_standard:
                return aws_arns.res.SfnStandardStateMachineExecution.new(
                    self._account_id,
                    self._region,
                    state_machine,
                    exec_id_or_arn,
                )
            else:
                return aws_arns.res.SfnExpressStateMachineExecution.new(
                    self._account_id,
                    self._region,
                    state_machine,
                    exec_id_or_arn,
                )

    @lru_cache(maxsize=32)
    def _get_state_machine_details(self, name_or_arn: str) -> dict:
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine
        """
        obj = self._get_state_machine_obj(name_or_arn)
        return self._bsm.sfn_client.describe_state_machine(
            stateMachineArn=obj.to_arn(),
        )

    def _is_state_machine_type_standard(self, name_or_arn: str) -> bool:
        return self._get_state_machine_details(name_or_arn)["type"] == "STANDARD"

    # --- arn
    def get_state_machine_arn(
        self,
        name: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ) -> str:
        return self._get_state_machine_obj(name, version, alias).to_arn()

    def get_state_machine_execution_arn(
        self,
        exec_id_or_arn: str,
        state_machine: T.Optional[str] = None,
        is_standard: T.Optional[bool] = None,
    ) -> str:
        return self._get_state_machine_execution_obj(
            exec_id_or_arn,
            state_machine,
            is_standard,
        ).to_arn()

    # --- dashboard
    @property
    def state_machines(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/statemachines"

    # --- state machine
    def _get_state_machine_tab(self, name_or_arn: str, tab: str) -> str:
        obj = self._get_state_machine_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/statemachines/{tab}/{obj.to_arn()}"
        )

    def get_state_machine_view_tab(self, name_or_arn: str) -> str:
        return self._get_state_machine_tab(name_or_arn, "view")

    def get_state_machine_edit_tab(self, name_or_arn: str) -> str:
        return self._get_state_machine_tab(name_or_arn, "edit")

    def get_state_machine_visual_editor(self, name_or_arn: str) -> str:
        obj = self._get_state_machine_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/visual-editor?stateMachineArn={obj.to_arn()}"
        )

    # --- execution
    def get_state_machine_execution(
        self,
        exec_id_or_arn: str,
        state_machine: T.Optional[str] = None,
        is_standard: T.Optional[bool] = None,
    ) -> str:
        obj = self._get_state_machine_execution_obj(
            exec_id_or_arn,
            state_machine,
            is_standard,
        )
        is_standard = obj.resource_type == "execution"
        if is_standard:
            href = "executions"
        else:
            href = "express-executions"
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/{href}/details/{obj.to_arn()}"
        )
