# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class Glue(Service):
    _AWS_SERVICE = "glue"

    def _get_glue_table_obj(
        self,
        table_name_or_arn: str,
        database_name: T.Optional[str] = None,
    ) -> aws_arns.res.GlueTable:
        if table_name_or_arn.startswith("arn:"):
            return aws_arns.res.GlueTable.from_arn(table_name_or_arn)
        else:
            if database_name is None:
                raise ValueError(
                    "database_name must be specified if table_name_or_arn is not an ARN"
                )
            return aws_arns.res.GlueTable.new(
                self._account_id, self._region, table_name_or_arn, database_name
            )

    def _get_glue_obj(
        self,
        name_or_arn: str,
        class_: T.Type[
            T.Union[
                aws_arns.res.GlueDatabase,
                aws_arns.res.GlueCrawler,
                aws_arns.res.GlueJob,
                aws_arns.res.GlueTrigger,
                aws_arns.res.GlueMLTransform,
            ]
        ],
    ) -> T.Union[
        aws_arns.res.GlueDatabase,
        aws_arns.res.GlueCrawler,
        aws_arns.res.GlueJob,
        aws_arns.res.GlueTrigger,
        aws_arns.res.GlueMLTransform,
    ]:
        if name_or_arn.startswith("arn:"):
            return class_.from_arn(name_or_arn)
        else:
            return class_.new(self._account_id, self._region, name_or_arn)

    def _get_glue_database_obj(self, name_or_arn: str) -> aws_arns.res.GlueDatabase:
        return self._get_glue_obj(name_or_arn, aws_arns.res.GlueDatabase)

    def _get_glue_crawler_obj(self, name_or_arn: str) -> aws_arns.res.GlueCrawler:
        return self._get_glue_obj(name_or_arn, aws_arns.res.GlueCrawler)

    def _get_glue_job_obj(self, name_or_arn: str) -> aws_arns.res.GlueJob:
        return self._get_glue_obj(name_or_arn, aws_arns.res.GlueJob)

    def _get_glue_trigger_obj(self, name_or_arn: str) -> aws_arns.res.GlueTrigger:
        return self._get_glue_obj(name_or_arn, aws_arns.res.GlueTrigger)

    def _get_glue_ml_transform_obj(
        self,
        name_or_arn: str,
    ) -> aws_arns.res.GlueMLTransform:
        return self._get_glue_obj(name_or_arn, aws_arns.res.GlueMLTransform)

    # --- arn
    def get_table_arn(self, database: str, table: str) -> str:
        return self._get_glue_table_obj(table, database).to_arn()

    def get_database_arn(self, name: str) -> str:
        return self._get_glue_database_obj(name).to_arn()

    def get_crawler_arn(self, name: str) -> str:
        return self._get_glue_crawler_obj(name).to_arn()

    def get_job_arn(self, name: str) -> str:
        return self._get_glue_job_obj(name).to_arn()

    def get_trigger_arn(self, name: str) -> str:
        return self._get_glue_trigger_obj(name).to_arn()

    def get_ml_transform_arn(self, name: str) -> str:
        return self._get_glue_ml_transform_obj(name).to_arn()

    # --- dashboard
    @property
    def databases(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/data-catalog/databases"
        )

    @property
    def tables(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/data-catalog/tables"
        )

    @property
    def jobs(self) -> str:
        return f"{self._service_root}/gluestudio/home?region={self._region}#/jobs"

    @property
    def crawlers(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/data-catalog/crawlers"
        )

    @property
    def classifiers(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/data-catalog/classifiers"
        )

    @property
    def triggers(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/etl-configuration/triggers"
        )

    @property
    def ml_transforms(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/v2"
            f"/etl-configuration/ml-transforms"
        )

    def get_database(
        self,
        database_or_arn: str,
        catalog_id: T.Optional[str] = None,
    ) -> str:
        if database_or_arn.startswith("arn:"):
            obj = self._get_glue_database_obj(database_or_arn)
            return (
                f"{self._service_root}/home?region={obj.aws_region}#/v2/data-catalog"
                f"/databases/view/{obj.database_name}?catalogId={obj.aws_account_id}"
            )
        else:
            catalog_id = catalog_id if catalog_id else self._account_id
            return (
                f"{self._service_root}/home?region={self._region}#/v2/data-catalog"
                f"/databases/view/{database_or_arn}?catalogId={catalog_id}"
            )

    def get_table(
        self,
        table_or_arn: str,
        database: T.Optional[str] = None,
        catalog_id: T.Optional[str] = None,
    ) -> str:
        if table_or_arn.startswith("arn:"):
            obj = self._get_glue_table_obj(table_or_arn)
            return (
                f"{self._service_root}/home?region={obj.aws_region}#/v2/data-catalog"
                f"/tables/view/{obj.table_name}?database={obj.database_name}&catalogId={obj.aws_account_id}&versionId=latest"
            )
        else:
            if database is None:
                raise ValueError("database must be specified if table is not an ARN")
            catalog_id = catalog_id if catalog_id else self._account_id
            return (
                f"{self._service_root}/home?region={self._region}#/v2/data-catalog"
                f"/tables/view/{table_or_arn}?database={database}&catalogId={catalog_id}&versionId=latest"
            )

    def get_job(self, name_or_arn: str) -> str:
        obj = self._get_glue_job_obj(name_or_arn)
        return (
            f"{self._root_url}/gluestudio/home?region={obj.aws_region}#"
            f"/editor/job/{obj.job_name}"
        )

    def get_crawler(self, name_or_arn: str) -> str:
        obj = self._get_glue_crawler_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/v2/data-catalog/crawlers/view/{obj.crawler_name}"
        )

    def get_trigger(self, name_or_arn: str) -> str:
        obj = self._get_glue_trigger_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/v2/etl-configuration/triggers/view/{obj.trigger_name}"
        )

    def get_ml_transform(self, name_or_arn: str) -> str:
        obj = self._get_glue_ml_transform_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/v2/etl-configuration/ml-transforms/view/{obj.ml_transform_name}"
        )

    def get_glue_job_run(
        self,
        job_name_or_arn: str,
        job_run_id: str,
    ) -> str:
        obj = self._get_glue_job_obj(job_name_or_arn)
        return (
            f"{self._root_url}/gluestudio/home?region={self._region}#"
            f"/job/{obj.job_name}/run/{job_run_id}"
        )
