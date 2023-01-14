# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class A2I(Builder):
    _AWS_SERVICE = "a2i"

    # --- Human Review Workflows
    @property
    def human_review_workflows(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/human-review-workflows"
        )

    def to_human_review_workflow_arn(self, name) -> str:
        return f"arn:aws:sagemaker:{self._region}:{self._account_id}:flow-definition/{name}"

    def to_human_review_workflow_name(self, arn) -> str:
        return arn.split("/")[-1]

    def get_human_review_workflow(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self.to_human_review_workflow_name)
        "https://us-east-1.console.aws.amazon.com/a2i/home?region=us-east-1#/human-review-workflows/verisk-deduplicate"
        return f"{self._service_root}/home?region={self._region}#/human-review-workflows/{name}"

    # --- Worker Task Templates
    @property
    def worker_task_templates(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/worker-task-templates"

    def to_worker_task_template_arn(self, name) -> str:
        return (
            f"arn:aws:sagemaker:{self._region}:{self._account_id}:human-task-ui/{name}"
        )

    def to_worker_task_template_name(self, arn) -> str:
        return arn.split("/")[-1]

    def get_worker_task_template(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self.to_worker_task_template_name)
        return f"{self._service_root}/home?region={self._region}#/worker-task-templates/{name}"

    # --- Human Loop
    def to_human_loop_arn(self, name) -> str:
        return f"arn:aws:sagemaker:{self._region}:{self._account_id}:human-loop/{name}"

    def to_human_loop_name(self, arn) -> str:
        return arn.split("/")[-1]

    def get_human_loop(
        self,
        flow_name_or_arn: str,
        human_loop_name_or_arn: str,
    ) -> str:
        flow_name = self._ensure_name(
            flow_name_or_arn, self.to_human_review_workflow_name
        )
        human_loop_name = self._ensure_name(
            human_loop_name_or_arn, self.to_human_loop_name
        )
        return (
            f"{self._service_root}/home?region={self._region}#/human-review-workflows"
            f"/{flow_name}/human-loops/{human_loop_name}"
        )
