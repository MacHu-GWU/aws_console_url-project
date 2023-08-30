# -*- coding: utf-8 -*-

import dataclasses

from ..model import Service


@dataclasses.dataclass(frozen=True)
class CodePipeline(Service):
    _AWS_SERVICE = "codesuite/codepipeline"

    # arn
    def _arn_to_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    # build project
    @property
    def pipelines(self) -> str:
        return f"{self._service_root}/pipelines?region={self._region}"

    def get_pipeline(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/pipelines/{name}/view?region={self._region}"
        )

    def get_pipeline_execution_history(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/pipelines/{name}/executions?region={self._region}"
        )

    def get_pipeline_execution(self, pipeline_name: str, execution_id: str) -> str:
        return (
            f"{self._service_root}"
            f"/pipelines/{pipeline_name}"
            f"/executions/{execution_id}"
            f"/timeline?region={self._region}"
        )
