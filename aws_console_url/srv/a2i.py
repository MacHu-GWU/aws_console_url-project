# -*- coding: utf-8 -*-

import typing as T
import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class A2I(Service):
    _AWS_SERVICE = "sagemaker/groundtruth"

    # --- Human Review Workflows
    @property
    def human_review_workflows(self) -> str:
        return (
            f"{self._service_root}?region={self._region}#"
            f"/a2i/human-review-workflows"
        )

    def _get_a2i_object(
        self,
        name_or_arn: str,
        class_: T.Type[
            T.Union[
                aws_arns.res.A2IHumanReviewWorkflow,
                aws_arns.res.A2IWorkerTaskTemplate,
                aws_arns.res.A2IHumanLoop,
            ]
        ],
    ):
        if name_or_arn.startswith("arn:"):
            return class_.from_arn(name_or_arn)
        else:
            return class_.new(self._account_id, self._region, name_or_arn)

    def get_human_review_workflow_arn(self, name: str) -> str:
        return self._get_a2i_object(name, aws_arns.res.A2IHumanReviewWorkflow).to_arn()

    def get_human_review_workflow(self, name_or_arn: str) -> str:
        obj = self._get_a2i_object(name_or_arn, aws_arns.res.A2IHumanReviewWorkflow)
        return (
            f"{self._service_root}?region={obj.aws_region}#"
            f"/a2i/human-review-workflows/{obj.name}"
        )

    # --- Worker Task Templates
    @property
    def worker_task_templates(self) -> str:
        return (
            f"{self._service_root}?region={self._region}#" f"/a2i/worker-task-templates"
        )

    def get_worker_task_template_arn(self, name: str) -> str:
        return self._get_a2i_object(name, aws_arns.res.A2IWorkerTaskTemplate).to_arn()

    def get_worker_task_template(self, name_or_arn: str) -> str:
        obj = self._get_a2i_object(name_or_arn, aws_arns.res.A2IWorkerTaskTemplate)
        return (
            f"{self._service_root}?region={obj.aws_region}#"
            f"/a2i/worker-task-templates/{obj.name}"
        )

    # --- Human review workforces
    @property
    def human_review_workforces(self) -> str:
        return (
            f"{self._service_root}?region={self._region}#"
            f"/a2i/human-review-workforces"
        )

    # --- Human Loop
    def get_human_loop_arn(self, name: str) -> str:
        return self._get_a2i_object(name, aws_arns.res.A2IHumanLoop).to_arn()

    def get_human_loop(
        self,
        flow_name_or_arn: str,
        human_loop_name_or_arn: str,
    ) -> str:
        flow_def = self._get_a2i_object(
            flow_name_or_arn, aws_arns.res.A2IHumanReviewWorkflow
        )
        human_loop = self._get_a2i_object(
            human_loop_name_or_arn, aws_arns.res.A2IHumanLoop
        )
        return (
            f"{self._service_root}?region={flow_def.aws_region}#/a2i/human-review-workflows"
            f"/{flow_def.name}/human-loops/{human_loop.name}"
        )
