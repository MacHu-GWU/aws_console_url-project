# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class BaseSageMakerResource(BaseServiceResourceV1):
    name: T.Optional[str] = dataclasses.field(default=None)

    _SERVICE_NAME = "sagemaker"
