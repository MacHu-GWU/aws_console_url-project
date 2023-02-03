# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class StepFunctionStatemachine(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ) -> "StepFunctionStatemachine":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:states:{self.aws_region}:{self.aws_account_id}:stateMachine:{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "StepFunctionStatemachine":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[6]
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )


@dataclasses.dataclass(frozen=True)
class StepFunctionStatemachineExecution(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)
    short_id: T.Optional[str] = dataclasses.field(default=None)
    is_standard: T.Optional[bool] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        short_id: str,
        is_standard: bool,
    ) -> "StepFunctionStatemachineExecution":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
            is_standard=is_standard,
        )

    @property
    def _type(self) -> str:
        if self.is_standard:
            return "execution"
        else:
            return "express"

    @property
    def arn(self) -> str:
        return f"arn:aws:states:{self.aws_region}:{self.aws_account_id}:{self._type}:{self.name}:{self.short_id}"

    @classmethod
    def from_arn(cls, arn: str) -> "StepFunctionStatemachineExecution":
        parts = arn.split(":", 7)
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[6]
        short_id = parts[7]
        is_standard = parts[5] == "execution"
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
            is_standard=is_standard,
        )


@dataclasses.dataclass(frozen=True)
class StepFunction(Service):
    _AWS_SERVICE = "states"

    @lru_cache(maxsize=32)
    def _get_state_machine_details(self, name_or_arn: str) -> dict:
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine
        """
        arn = self._ensure_arn(name_or_arn, self.get_state_machine_arn)
        return self._bsm.stepfunctions_client.describe_state_machine(
            stateMachineArn=arn,
        )

    def _is_state_machine_type_standard(self, name_or_arn: str) -> bool:
        return self._get_state_machine_details(name_or_arn)["type"] == "STANDARD"

    # --- arn
    def get_state_machine_arn(self, name: str) -> str:
        return StepFunctionStatemachine.make(self._account_id, self._region, name).arn

    def get_state_machine_execution_arn(self, name: str, short_id: str) -> str:
        return StepFunctionStatemachineExecution.make(
            self._account_id,
            self._region,
            name,
            short_id,
            self._is_state_machine_type_standard(name),
        ).arn

    # --- dashboard
    @property
    def state_machines(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/statemachines"

    # --- state machine
    def _get_state_machine_tab(self, name_or_arn: str, tab: str) -> str:
        arn = self._ensure_arn(name_or_arn, self.get_state_machine_arn)
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/statemachines/{tab}/{arn}"
        )

    def get_state_machine_view_tab(self, name_or_arn: str) -> str:
        return self._get_state_machine_tab(name_or_arn, "view")

    def get_state_machine_edit_tab(self, name_or_arn: str) -> str:
        return self._get_state_machine_tab(name_or_arn, "edit")

    def get_state_machine_visual_editor(self, name_or_arn: str) -> str:
        state_machine_arn = StepFunctionStatemachine.make(
            aws_account_id=self._account_id,
            aws_region=self._region,
            name=name_or_arn,
        )
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/visual-editor?stateMachineArn={state_machine_arn.arn}"
        )

    # --- execution
    def get_state_machine_execution(
        self,
        name_or_arn: str,
        short_id: T.Optional[str] = None,
    ) -> str:
        if name_or_arn.startswith("arn:"):
            arn = name_or_arn
        elif short_id is None:
            raise ValueError
        else:
            arn = self.get_state_machine_execution_arn(name_or_arn, short_id)
        execution = StepFunctionStatemachineExecution.from_arn(arn)
        state_machine_name = execution.name
        if self._is_state_machine_type_standard(state_machine_name):
            href = "executions"
        else:
            href = "express-executions"
        return (
            f"{self._service_root}/home?region={self._region}#" f"/{href}/details/{arn}"
        )