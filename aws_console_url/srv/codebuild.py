# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class CodeBuild(Service):
    _AWS_SERVICE = "codesuite/codebuild"

    # arn
    def _get_build_project_obj(self, name_or_arn: str) -> aws_arns.res.CodeBuildProject:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.CodeBuildProject.from_arn(name_or_arn)
        else:
            return aws_arns.res.CodeBuildProject.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_build_project_arn(self, name: str) -> str:
        return self._get_build_project_obj(name).to_arn()

    def _get_build_run_obj(
        self,
        run_id_or_arn: str,
        project_name: T.Optional[str] = None,
        is_batch: T.Optional[bool] = None,
    ) -> T.Union[
         aws_arns.res.CodeBuildRun,
         aws_arns.res.CodeBuildBatchRun,
    ]:
        if run_id_or_arn.startswith("arn:"):
            return aws_arns.parse_arn(run_id_or_arn)
        else:
            if is_batch:
                return aws_arns.res.CodeBuildBatchRun.new(
                    self._account_id,
                    self._region,
                    f"{project_name}:{run_id_or_arn}",
                )
            else:
                return aws_arns.res.CodeBuildRun.new(
                    self._account_id,
                    self._region,
                    f"{project_name}:{run_id_or_arn}",
                )

    def get_build_run_arn(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> str:
        return self._get_build_run_obj(
            run_id_or_arn=run_id,
            project_name=project_name,
            is_batch=is_batch,
        ).to_arn()

    # build project
    @property
    def build_projects(self) -> str:
        return f"{self._service_root}/projects?region={self._region}"

    @property
    def build_history(self) -> str:
        return f"{self._service_root}/builds/build-history?region={self._region}"

    @property
    def report_groups(self) -> str:
        return f"{self._service_root}/testReports/reportGroups?region={self._region}"

    @property
    def report_history(self) -> str:
        return f"{self._service_root}/testReports/reports?region={self._region}"

    @property
    def metrics(self) -> str:
        return f"{self._service_root}/metrics?region={self._region}"

    def get_project(self, project_or_arn: str) -> str:
        obj = self._get_build_project_obj(project_or_arn)
        return (
            f"{self._service_root}/{obj.aws_account_id}"
            f"/projects/{obj.codebuild_project_name}/history?region={obj.aws_region}"
        )

    # build run
    def _get_build_run(
        self,
        tab: str,
        run_id_or_arn: str,
        project_name: T.Optional[str] = None,
        is_batch: T.Optional[bool] = None,
    ) -> str:
        obj = self._get_build_run_obj(
            run_id_or_arn=run_id_or_arn,
            project_name=project_name,
            is_batch=is_batch,
        )
        if obj.resource_type == "build-batch":
            type = "batch"
        else:
            type = "build"
        return (
            f"{self._service_root}/{obj.aws_account_id}"
            f"/projects/{obj.codebuild_project_name}/{type}/"
            f"{obj.codebuild_project_name}:{obj.codebuild_run_id}/{tab}?region={obj.aws_region}"
        )

    def get_build_run(
        self,
        run_id_or_arn: str,
        project_name: T.Optional[str] = None,
        is_batch: T.Optional[bool] = None,
    ) -> str:
        return self._get_build_run(
            tab="",
            run_id_or_arn=run_id_or_arn,
            project_name=project_name,
            is_batch=is_batch,
        )

    def get_build_run_phase(
        self,
        run_id_or_arn: str,
        project_name: T.Optional[str] = None,
        is_batch: T.Optional[bool] = None,
    ) -> str:
        return self._get_build_run(
            tab="phase",
            run_id_or_arn=run_id_or_arn,
            project_name=project_name,
            is_batch=is_batch,
        )

    def get_build_run_env_var(
        self,
        run_id_or_arn: str,
        project_name: T.Optional[str] = None,
        is_batch: T.Optional[bool] = None,
    ) -> str:
        return self._get_build_run(
            tab="env_var",
            run_id_or_arn=run_id_or_arn,
            project_name=project_name,
            is_batch=is_batch,
        )
