# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

from ..model import BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class BaseSecretManagerResource(BaseServiceResourceV1):
    _SERVICE_NAME = "secretsmanager"


@dataclasses.dataclass(frozen=True)
class SecretManagerSecret(BaseSecretManagerResource):
    _RESOURCE_TYPE = "secret"

    @property
    def secret_name(self) -> str:
        return "-".join(self.name.split("-")[:-1])


@dataclasses.dataclass(frozen=True)
class SecretManager(Service):
    _AWS_SERVICE = "secretsmanager"

    # --- arn
    def get_secret_arn(self, name: str) -> str:
        return SecretManagerSecret.make(self._account_id, self._region, name).arn

    def secret_arn_to_secret_name(self, arn: str) -> str:
        """
        :return: secret name is the name you used to create the secret,
            it is not the long name with random characters ``${secret_name}-ABCDEF``.
        """
        return SecretManagerSecret.from_arn(arn).secret_name

    @lru_cache(maxsize=32)
    def _get_secret_arn(
        self,
        secret_name: str,
        include_planned_deletion: bool = False,
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
        name = self._ensure_name(secret_name_or_arn, self.secret_arn_to_secret_name)
        return f"{self._service_root}/secret?name={name}&region={self._region}"
