# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class SecretManager(Service):
    _AWS_SERVICE = "secretsmanager"

    @lru_cache(maxsize=32)
    def _get_secret_arn(
        self,
        secret_name: str,
        include_planned_deletion: bool = True,
    ) -> str:
        response = self._bsm.secretsmanager_client.list_secrets(
            IncludePlannedDeletion=include_planned_deletion,
            MaxResults=100,
            Filters=[
                dict(Key="name", Values=[secret_name]),
            ],
        )
        arn = response["SecretList"][0]["ARN"]
        return arn

    def _get_secret_obj(
        self,
        name_or_arn: str,
    ) -> aws_arns.res.SecretManagerSecret:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.SecretManagerSecret.from_arn(name_or_arn)
        else:
            parts = name_or_arn.split("-")
            if len(parts[-1]) == 6:
                return aws_arns.res.SecretManagerSecret.new(
                    self._account_id,
                    self._aws_region,
                    name_or_arn,
                )
            else:
                return aws_arns.res.SecretManagerSecret.from_arn(
                    self._get_secret_arn(name_or_arn),
                )

    # --- arn
    def get_secret_arn(self, name: str) -> str:
        return self._get_secret_arn(name)

    # --- dashboard
    @property
    def secrets(self) -> str:
        return f"{self._service_root}/listsecrets?region={self._region}"

    # --- table
    def filter_secrets(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = "%26".join([f"all%3D{facet}" for facet in facets])
        return (
            f"{self._service_root}/listsecrets?region={self._region}"
            f"&search={search}"
        )

    def get_secret(self, secret_name_or_arn: str) -> str:
        obj = self._get_secret_obj(name_or_arn=secret_name_or_arn)
        return f"{self._service_root}/secret?name={obj.secret_name}&region={obj.aws_region}"
