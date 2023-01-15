# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..builder import ConsoleUrlBuilder


@dataclasses.dataclass(frozen=True)
class Glue(ConsoleUrlBuilder):
    _AWS_SERVICE = "glue"

    @property
    def databases(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/v2/data-catalog/databases"

    @property
    def tables(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog/tables"
        )

    @property
    def crawlers(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog/crawlers"
        )

    @property
    def classifiers(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/v2/data-catalog/classifiers"

    def get_database(
        self,
        database: str,
        catalog_id: T.Optional[str] = None,
    ) -> str:
        catalog_id = catalog_id if catalog_id else self._account_id
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog"
            f"/databases/view/{database}?catalogId={catalog_id}"
        )

    def get_table(
        self,
        database: str,
        table: str,
        catalog_id: T.Optional[str] = None,
    ) -> str:
        catalog_id = catalog_id if catalog_id else self._account_id
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog"
            f"/tables/view/{table}?database={database}&catalogId={catalog_id}&versionId=latest"
        )
