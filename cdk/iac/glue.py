# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_iam as iam,
    aws_glue as glue,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class GlueMixin:
    def mk_glue(self: "MainStack"):
        database_name = f"{self.prefix_snake}_test"
        self.glue_database = glue.CfnDatabase(
            self,
            id="GlueDatabase",
            catalog_id=cdk.Aws.ACCOUNT_ID,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name=database_name,
            ),
        )

        self.glue_table_1 = glue.CfnTable(
            self,
            id="GlueTable1",
            catalog_id=cdk.Aws.ACCOUNT_ID,
            database_name=database_name,
            table_input=glue.CfnTable.TableInputProperty(
                name=f"{self.prefix_snake}_table1",
                description="test table1",
                storage_descriptor=glue.CfnTable.StorageDescriptorProperty(
                    location="s3://bucket/folder/",
                    columns=[
                        glue.CfnTable.ColumnProperty(
                            name="col1",
                            type="string",
                        ),
                    ],
                ),
            ),
        )
        self.glue_table_1.add_dependency(self.glue_database)

        self.iam_role_for_glue_job_run = iam.Role(
            self,
            "IamRoleForGlueJobRun",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            role_name=f"{self.prefix_snake}_glue_job_run",
        )

        self.glue_crawler = glue.CfnCrawler(
            self,
            id="GlueCrawler",
            name=f"{self.prefix_snake}_test",
            role=self.iam_role_for_glue_job_run.role_arn,
            database_name=database_name,
            targets=glue.CfnCrawler.TargetsProperty(
                s3_targets=[
                    glue.CfnCrawler.S3TargetProperty(
                        path="s3://bucket/folder/",
                    ),
                ],
            ),
        )

        self.glue_job = glue.CfnJob(
            self,
            id="GlueJob",
            name=f"{self.prefix_snake}_test",
            role=self.iam_role_for_glue_job_run.role_arn,
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                script_location=f"{self.prefix_slug}-test/upload/__init__.py",
            ),
            glue_version="4.0",
            max_retries=0,
            worker_type="Standard",
            number_of_workers=2,
        )
