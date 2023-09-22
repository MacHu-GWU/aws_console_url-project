# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class SSM(Service):
    _AWS_SERVICE = "systems-manager"

    def _get_parameter_obj(self, name_or_arn: str) -> aws_arns.res.SSMParameter:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.SSMParameter.from_arn(name_or_arn)
        else:
            return aws_arns.res.SSMParameter.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    # --- arn
    def get_parameter_arn(self, name: str) -> str:
        return self._get_parameter_obj(name).to_arn()

    # --- dashboard
    @property
    def parameters(self) -> str:
        return f"{self._service_root}/parameters/?region={self._region}&tab=Table"

    # --- table
    def filter_parameters(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        new_facets = []
        for facet in facets:
            if facet.startswith("/"):
                facet = facet[1:]
            new_facets.append(facet)
        search = ",".join([f"Name:Contains:{facet}" for facet in new_facets])
        return (
            f"{self._service_root}/parameters"
            f"/?region={self._region}&tab=Table#list_parameter_filters={search}"
        )

    def get_parameter(self, name_or_arn: str) -> str:
        obj = self._get_parameter_obj(name_or_arn)
        if obj.parameter_name.startswith("/"):
            name = obj.parameter_name[1:]
        else:
            name = obj.parameter_name
        return (
            f"{self._service_root}/parameters"
            f"/{name}/description?region={self._region}&tab=Table"
        )
