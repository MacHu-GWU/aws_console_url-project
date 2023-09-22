# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class CodeBuild(Service):
    _AWS_SERVICE = "codesuite/codebuild"

    # arn
    def get_build_project_arn(self, name: str) -> str:
        return aws_arns.res.CodeBuildProject.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

    def get_build_run_arn(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> str:
        if is_batch:
            return aws_arns.res.CodeBuildBatchRun.new(
                self._account_id,
                self._region,
                f"{project_name}:{run_id}",
            ).to_arn()
        else:
            return aws_arns.res.CodeBuildRun.new(
                self._account_id,
                self._region,
                f"{project_name}:{run_id}",
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

    def _project_arn_to_name(self, arn: str) -> str:
        return aws_arns.res.CodeBuildProject.from_arn(arn).codebuild_project_name

    def get_project(self, project_or_arn: str) -> str:
        project = self._ensure_name(project_or_arn, self._project_arn_to_name)
        return (
            f"{self._service_root}/{self._account_id}"
            f"/projects/{project}/history?region={self._region}"
        )

    # build run
    def _get_build_run(
        self,
        is_batch: bool,
        tab: str,
        project_name: T.Optional[str],
        run_id: T.Optional[str],
        run_arn: T.Optional[str] = None,
    ) -> str:
        if run_arn is not None:
            if is_batch:
                run = aws_arns.res.CodeBuildBatchRun.from_arn(run_arn)
            else:
                run = aws_arns.res.CodeBuildRun.from_arn(run_arn)
            project_name = run.codebuild_project_name
            run_id = run.codebuild_run_id
        if is_batch:
            type = "batch"
        else:
            type = "build"
        return (
            f"{self._service_root}/{self._account_id}"
            f"/projects/{project_name}/{type}/"
            f"{project_name}:{run_id}/{tab}?region={self._region}"
        )

    def get_build_run(
        self,
        is_batch: bool,
        project_name: T.Optional[str] = None,
        run_id: T.Optional[str] = None,
        run_arn: T.Optional[str] = None,
    ) -> str:
        return self._get_build_run(
            is_batch,
            tab="",
            project_name=project_name,
            run_id=run_id,
            run_arn=run_arn,
        )

    def get_build_run_phase(
        self,
        is_batch: bool,
        project_name: T.Optional[str] = None,
        run_id: T.Optional[str] = None,
        run_arn: T.Optional[str] = None,
    ) -> str:
        return self._get_build_run(
            is_batch,
            tab="phase",
            project_name=project_name,
            run_id=run_id,
            run_arn=run_arn,
        )

    def get_build_run_env_var(
        self,
        is_batch: bool,
        project_name: T.Optional[str] = None,
        run_id: T.Optional[str] = None,
        run_arn: T.Optional[str] = None,
    ) -> str:
        return self._get_build_run(
            is_batch,
            tab="env_var",
            project_name=project_name,
            run_id=run_id,
            run_arn=run_arn,
        )
