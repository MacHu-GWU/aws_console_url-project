# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class BaseGlueResource(BaseServiceResourceV1):
    name: T.Optional[str] = dataclasses.field(default=None)

    _SERVICE_NAME = "glue"


@dataclasses.dataclass(frozen=True)
class GlueDatabase(BaseGlueResource):
    _RESOURCE_TYPE = "database"


@dataclasses.dataclass(frozen=True)
class GlueTable(Resource):
    database: T.Optional[str] = dataclasses.field(default=None)
    table: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        database: str,
        table: str,
    ) -> "GlueTable":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            database=database,
            table=table,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:glue:{self.aws_region}:{self.aws_account_id}:table/{self.database}/{self.table}"

    @classmethod
    def from_arn(cls, arn: str) -> "GlueTable":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        chunks = parts[5].split("/")
        database = chunks[1]
        table = chunks[2]
        return cls.make(aws_account_id, aws_region, database, table)


@dataclasses.dataclass(frozen=True)
class GlueJob(BaseGlueResource):
    _RESOURCE_TYPE = "job"


@dataclasses.dataclass(frozen=True)
class GlueCrawler(BaseGlueResource):
    _RESOURCE_TYPE = "crawler"


@dataclasses.dataclass(frozen=True)
class GlueRegistry(BaseGlueResource):
    _RESOURCE_TYPE = "registry"


@dataclasses.dataclass(frozen=True)
class GlueSchema(BaseGlueResource):
    _RESOURCE_TYPE = "schema"


@dataclasses.dataclass(frozen=True)
class GlueWorkflow(BaseGlueResource):
    _RESOURCE_TYPE = "workflow"


@dataclasses.dataclass(frozen=True)
class Glue(Service):
    _AWS_SERVICE = "glue"

    # --- arn
    def get_database_arn(self, name: str) -> str:
        return GlueDatabase.make(self._account_id, self._region, name).arn

    def get_table_arn(self, database: str, table: str) -> str:
        return GlueTable.make(self._account_id, self._region, database, table).arn

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
