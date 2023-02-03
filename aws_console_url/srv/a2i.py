# -*- coding: utf-8 -*-

import dataclasses

from ..model import Service
from .sagemaker import BaseSageMakerResource


@dataclasses.dataclass(frozen=True)
class A2IFlowDefinition(BaseSageMakerResource):
    _RESOURCE_TYPE = "flow-definition"


@dataclasses.dataclass(frozen=True)
class A2IHumanTaskUI(BaseSageMakerResource):
    _RESOURCE_TYPE = "human-task-ui"


@dataclasses.dataclass(frozen=True)
class A2IHumanLoop(BaseSageMakerResource):
    _RESOURCE_TYPE = "human-loop"


@dataclasses.dataclass(frozen=True)
class A2I(Service):
    _AWS_SERVICE = "a2i"

    # --- Human Review Workflows
    @property
    def human_review_workflows(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/human-review-workflows"
        )

    def get_human_review_workflow_arn(self, name: str) -> str:
        return A2IFlowDefinition.make(self._account_id, self._region, name=name).arn

    def _human_review_workflow_arn_to_name(self, arn: str) -> str:
        return A2IFlowDefinition.from_arn(arn).name

    def get_human_review_workflow(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._human_review_workflow_arn_to_name)
        return f"{self._service_root}/home?region={self._region}#/human-review-workflows/{name}"

    # --- Worker Task Templates
    @property
    def worker_task_templates(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/worker-task-templates"

    def get_worker_task_template_arn(self, name: str) -> str:
        return A2IHumanTaskUI.make(self._account_id, self._region, name=name).arn

    def _worker_task_template_arn_to_name(self, arn: str) -> str:
        return A2IHumanTaskUI.from_arn(arn).name

    def get_worker_task_template(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._worker_task_template_arn_to_name)
        return f"{self._service_root}/home?region={self._region}#/worker-task-templates/{name}"

    # --- Human Loop
    def get_human_loop_arn(self, name: str) -> str:
        return A2IHumanLoop.make(self._account_id, self._region, name=name).arn

    def _human_loop_arn_to_name(self, arn: str) -> str:
        return A2IHumanTaskUI.from_arn(arn).name

    def get_human_loop(
        self,
        flow_name_or_arn: str,
        human_loop_name_or_arn: str,
    ) -> str:
        flow_name = self._ensure_name(
            flow_name_or_arn, self._human_review_workflow_arn_to_name
        )
        human_loop_name = self._ensure_name(
            human_loop_name_or_arn, self._human_loop_arn_to_name
        )
        return (
            f"{self._service_root}/home?region={self._region}#/human-review-workflows"
            f"/{flow_name}/human-loops/{human_loop_name}"
        )
