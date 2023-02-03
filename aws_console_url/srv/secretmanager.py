# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


@dataclasses.dataclass(frozen=True)
class SecretManager(Service):
    _AWS_SERVICE = "secretsmanager"

    # --- arn

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

    def get_secret(self, name: str) -> str:
        return f"{self._service_root}/secret?name={name}&region={self._region}"
