# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class BaseGlueResource(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    _resource_type = ""

    @classmethod
    def make(
        cls, aws_account_id: str, aws_region: str, name: str
    ) -> "BaseGlueResource":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:glue:{self.aws_region}:{self.aws_account_id}:{self._resource_type}/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "BaseGlueResource":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5].split("/")[1]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class GlueDatabase(BaseGlueResource):
    _resource_type = "database"


@dataclasses.dataclass(frozen=True)
class GlueTable(BaseGlueResource):
    _resource_type = "table"


@dataclasses.dataclass(frozen=True)
class GlueJob(BaseGlueResource):
    _resource_type = "job"


@dataclasses.dataclass(frozen=True)
class GlueCrawler(BaseGlueResource):
    _resource_type = "crawler"


@dataclasses.dataclass(frozen=True)
class GlueRegistry(BaseGlueResource):
    _resource_type = "registry"


@dataclasses.dataclass(frozen=True)
class GlueSchema(BaseGlueResource):
    _resource_type = "schema"


@dataclasses.dataclass(frozen=True)
class GlueWorkflow(BaseGlueResource):
    _resource_type = "workflow"


@dataclasses.dataclass(frozen=True)
class Glue(Service):
    _AWS_SERVICE = "glue"

    # --- arn
    def get_database_arn(self, name: str) -> str:
        return GlueDatabase.make(self._account_id, self._region, name).arn

    def get_table_arn(self, name: str) -> str:
        return GlueTable.make(self._account_id, self._region, name).arn

    def get_job_arn(self, name: str) -> str:
        return GlueJob.make(self._account_id, self._region, name).arn

    def get_crawler_arn(self, name: str) -> str:
        return GlueCrawler.make(self._account_id, self._region, name).arn

    # --- dashboard
    @property
    def databases(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/v2/data-catalog/databases"

    @property
    def tables(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog/tables"
        )

    @property
    def jobs(self) -> str:
        return f"{self._root_url}/gluestudio/home?region={self._region}#/jobs"

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

    def get_job(self, name: str) -> str:
        return (
            f"{self._root_url}/gluestudio/home?region={self._region}#/editor/job/{name}"
        )

    def get_crawler(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2/data-catalog"
            f"/crawlers/view/{name}"
        )
