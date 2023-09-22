# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class CodePipeline(Service):
    _AWS_SERVICE = "codesuite/codepipeline"

    # arn
    def _get_pipeline_object(
        self, name_or_arn: str
    ) -> aws_arns.res.CodePipelinePipeline:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.CodePipelinePipeline.from_arn(name_or_arn)
        else:
            return aws_arns.res.CodePipelinePipeline.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_pipeline_arn(self, name: str) -> str:
        return aws_arns.res.CodePipelinePipeline.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

    # build project
    @property
    def pipelines(self) -> str:
        return f"{self._service_root}/pipelines?region={self._region}"

    def get_pipeline(self, name_or_arn: str) -> str:
        pipeline = self._get_pipeline_object(name_or_arn)
        return (
            f"{self._service_root}/pipelines"
            f"/{pipeline.pipeline_name}/view?region={pipeline.aws_region}"
        )

    def get_pipeline_execution_history(self, name_or_arn: str) -> str:
        pipeline = self._get_pipeline_object(name_or_arn)
        return (
            f"{self._service_root}/pipelines"
            f"/{pipeline.pipeline_name}/executions?region={pipeline.aws_region}"
        )

    def get_pipeline_execution(
        self, pipeline_name_or_arn: str, execution_id: str
    ) -> str:
        pipeline = self._get_pipeline_object(pipeline_name_or_arn)
        return (
            f"{self._service_root}"
            f"/pipelines/{pipeline.pipeline_name}"
            f"/executions/{execution_id}"
            f"/timeline?region={pipeline.aws_region}"
        )
