# -*- coding: utf-8 -*-

import dataclasses
from functools import lru_cache

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class CloudFormation(Builder):
    _AWS_SERVICE = "cloudformation"

    @property
    def stacks(self) -> str:
        return f"{self._service_root}/home?#/stacks"

    @property
    def stacksets(self) -> str:
        return f"{self._service_root}/home?#/stacksets"

    @property
    def exports(self) -> str:
        return f"{self._service_root}/home?#/exports"

    @lru_cache(maxsize=32)
    def _get_stack_id(self, name: str) -> str:
        response = self.bsm.cloudformation_client.describe_stacks(StackName=name)
        arn = response["Stacks"][0]["StackId"]
        return arn

    def _stack_tab(self, name: str, tab: str) -> str:
        stack_id = self._get_stack_id(name)
        return f"{self._service_root}/home?#/stacks/{tab}?stackId={stack_id}"

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
        return f"{self._service_root}/home?#/stacks/changesets/{tab}?stackId={stack_id}&changeSetId={change_set_id}"

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
