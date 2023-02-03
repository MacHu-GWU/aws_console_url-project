# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class CloudFormationStack(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)
    short_id: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        short_id: str,
    ) -> "CloudFormationStack":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
        )

    @property
    def arn(self) -> str:
        return (
            f"arn:aws:cloudformation:{self.aws_region}:{self.aws_account_id}:stack"
            f"/{self.name}/{self.short_id}"
        )

    @property
    def stack_id(self) -> str:
        return self.arn

    @classmethod
    def from_arn(cls, arn: str) -> "CloudFormationStack":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        chunks = parts[5].split("/")
        name = chunks[1]
        short_id = chunks[2]
        return cls.make(aws_account_id, aws_region, name, short_id)

    @classmethod
    def from_stack_id(cls, stack_id: str) -> "CloudFormationStack":
        return cls.from_arn(stack_id)


@dataclasses.dataclass(frozen=True)
class CloudFormation(Service):
    _AWS_SERVICE = "cloudformation"

    @property
    def stacks(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacks"

    @property
    def stacksets(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacksets"

    @property
    def exports(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/exports"

    @lru_cache(maxsize=32)
    def _get_stack_id(self, name: str) -> str:
        response = self._bsm.cloudformation_client.describe_stacks(StackName=name)
        arn = response["Stacks"][0]["StackId"]
        return arn

    def get_stack_arn(self, name: str) -> str:
        return self._get_stack_id(name)

    def _stack_tab(self, name: str, tab: str) -> str:
        stack_id = self._get_stack_id(name)
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks/{tab}?stackId={stack_id}"
        )

    def get_stack(self, name: str) -> str:
        return self.get_stack_info(name)

    def get_stack_info(self, name: str) -> str:
        return self._stack_tab(name, "stackinfo")

    def get_stack_events(self, name: str) -> str:
        return self._stack_tab(name, "events")

    def get_stack_resources(self, name: str) -> str:
        return self._stack_tab(name, "resources")

    def get_stack_outputs(self, name: str) -> str:
        return self._stack_tab(name, "outputs")

    def get_stack_parameters(self, name: str) -> str:
        return self._stack_tab(name, "parameters")

    def get_stack_changesets(self, name: str) -> str:
        return self._stack_tab(name, "changesets")

    def _change_set_tab(self, name: str, change_set_id: str, tab: str) -> str:
        stack_id = self._get_stack_id(name)
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks/changesets/{tab}?stackId={stack_id}&changeSetId={change_set_id}"
        )

    def get_change_set(self, name: str, change_set_id: str) -> str:
        return self.get_change_set_changes(name, change_set_id)

    def get_change_set_changes(self, name: str, change_set_id: str) -> str:
        return self._change_set_tab(name, change_set_id, "changes")

    def get_change_set_inputs(self, name: str, change_set_id: str) -> str:
        return self._change_set_tab(name, change_set_id, "inputs")

    def get_change_set_template(self, name: str, change_set_id: str) -> str:
        return self._change_set_tab(name, change_set_id, "template")

    def get_change_set_json(self, name: str, change_set_id: str) -> str:
        return self._change_set_tab(name, change_set_id, "json")

    def get_change_set_hooks(self, name: str, change_set_id: str) -> str:
        return self._change_set_tab(name, change_set_id, "hooks")
