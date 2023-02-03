# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class BaseSSMResource(BaseServiceResourceV1):
    _SERVICE_NAME = "ssm"


@dataclasses.dataclass(frozen=True)
class SSMParameter(BaseSSMResource):
    _RESOURCE_TYPE = "parameter"


@dataclasses.dataclass(frozen=True)
class SSM(Service):
    _AWS_SERVICE = "systems-manager"

    # --- arn
    def get_parameter_arn(self, name: str) -> str:
        return SSMParameter.make(self._account_id, self._region, name).arn

    def _parameter_arn_to_name(self, arn: str) -> str:
        return SSMParameter.from_arn(arn).name

    # --- dashboard
    @property
    def parameters(self) -> str:
        return (
            f"{self._service_root}/parameters/?region={self._region}&tab=Table"
        )

    # --- table
    def filter_parameters(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join([f"Name:Contains:{facet}" for facet in facets])
        return (
            f"{self._service_root}/parameters"
            f"/?region={self._region}&tab=Table#list_parameter_filters={search}"
        )

    def get_parameter(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._parameter_arn_to_name)
        return (
            f"{self._service_root}/parameters"
            f"/{name}/description?region={self._region}&tab=Table"
        )
