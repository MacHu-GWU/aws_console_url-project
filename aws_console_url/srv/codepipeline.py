# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class CodePipelinePipeline(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ) -> "CodePipelinePipeline":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return (
            f"arn:aws:codepipeline:{self.aws_region}:{self.aws_account_id}:{self.name}"
        )

    @classmethod
    def from_arn(cls, arn: str) -> "CodePipelinePipeline":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class CodePipeline(Service):
    _AWS_SERVICE = "codesuite/codepipeline"

    # arn
    def _get_pipeline_object(self, name_or_arn: str) -> CodePipelinePipeline:
        if name_or_arn.startswith("arn:"):
            return CodePipelinePipeline.from_arn(name_or_arn)
        else:
            return CodePipelinePipeline.make(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_pipeline_arn(self, name: str) -> str:
        return CodePipelinePipeline.make(self._account_id, self._region, name).arn

    # build project
    @property
    def pipelines(self) -> str:
        return f"{self._service_root}/pipelines?region={self._region}"

    def get_pipeline(self, name_or_arn: str) -> str:
        pipeline = self._get_pipeline_object(name_or_arn)
        return f"{self._service_root}/pipelines/{pipeline.name}/view?region={pipeline.aws_region}"

    def get_pipeline_execution_history(self, name_or_arn: str) -> str:
        pipeline = self._get_pipeline_object(name_or_arn)
        return f"{self._service_root}/pipelines/{pipeline.name}/executions?region={pipeline.aws_region}"

    def get_pipeline_execution(self, pipeline_name_or_arn: str, execution_id: str) -> str:
        pipeline = self._get_pipeline_object(pipeline_name_or_arn)
        return (
            f"{self._service_root}"
            f"/pipelines/{pipeline.name}"
            f"/executions/{execution_id}"
            f"/timeline?region={pipeline.aws_region}"
        )
