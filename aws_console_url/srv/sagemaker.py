# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class BaseSageMakerResource(BaseServiceResourceV1):
    name: T.Optional[str] = dataclasses.field(default=None)

    _SERVICE_NAME = "sagemaker"


@dataclasses.dataclass(frozen=True)
class SageMaker(Service):
    _AWS_SERVICE = "sagemaker"

    # --- dashboard
    @property
    def notebooks(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/notebook-instances"

    @property
    def training_jobs(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/jobs"

    @property
    def processing_jobs(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/processing-jobs"

    @property
    def models(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/models"

    @property
    def inference_endpoints(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/endpoints"

    @property
    def batch_transform_jobs(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/transform-jobs"
