# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class CodeBuildProject(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ) -> "CodeBuildProject":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:codebuild:{self.aws_region}:{self.aws_account_id}:project/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "CodeBuildProject":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5].split("/")[1]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class CodeBuildRun(Resource):
    """
    For example, if the build arn is:

    "arn:aws:codebuild:us-east-1:111122223333:build/my-project:ae6a271b-609e-4e76-b6bb-3bac681edd05"

    Then:

    - aws_account_id: "111122223333"
    - aws_region: "us-east-1"
    - is_batch: False
    - project_name: "my-project"
    - run_id: "ae6a271b-609e-4e76-b6bb-3bac681edd05"
    - run_uuid: "my-project:ae6a271b-609e-4e76-b6bb-3bac681edd05"
    """

    is_batch: T.Optional[bool] = dataclasses.field(default=False)
    project_name: T.Optional[str] = dataclasses.field(default=None)
    run_id: T.Optional[str] = dataclasses.field(default=None)
    build_number: T.Optional[int] = dataclasses.field(default=None)

    @property
    def run_uuid(self) -> str:
        return f"{self.project_name}:{self.run_id}"

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> "CodeBuildRun":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            is_batch=is_batch,
            project_name=project_name,
            run_id=run_id,
        )

    @property
    def _arn_template(self) -> str:
        return (
            f"arn:aws:codebuild:{self.aws_region}:{self.aws_account_id}:{{type}}/"
            f"{self.project_name}:{self.run_id}"
        )

    @property
    def arn(self) -> str:
        if self.is_batch:
            return self._arn_template.format(type="build-batch")
        else:
            return self._arn_template.format(type="build")

    @classmethod
    def from_arn(cls, arn: str) -> "CodeBuildRun":
        part1, part2 = arn.split("/")
        part1_chunks = part1.split(":")
        part2_chunks = part2.split(":")
        is_batch = part1_chunks[5] == "build-batch"
        return cls(
            aws_account_id=part1_chunks[4],
            aws_region=part1_chunks[3],
            is_batch=is_batch,
            project_name=part2_chunks[0],
            run_id=part2_chunks[1],
        )


@dataclasses.dataclass(frozen=True)
class CodeBuild(Service):
    _AWS_SERVICE = "codesuite/codebuild"

    # arn
    def get_build_project_arn(self, name: str) -> str:
        return CodeBuildProject.make(self._account_id, self._region, name).arn

    def get_build_run_arn(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> str:
        return CodeBuildRun.make(
            self._account_id, self._region, is_batch, project_name, run_id
        ).arn

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

    def get_project(self, project: str) -> str:
        return (
            f"{self._service_root}/{self._account_id}"
            f"/projects/{project}/history?region={self._region}"
        )

    # build run
    def _get_build_run(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
        tab: str,
    ) -> str:
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
        project_name: str,
        run_id: str,
    ) -> str:
        return self._get_build_run(is_batch, project_name, run_id, tab="")

    def get_build_run_phase(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> str:
        return self._get_build_run(is_batch, project_name, run_id, tab="phase")

    def get_build_run_env_var(
        self,
        is_batch: bool,
        project_name: str,
        run_id: str,
    ) -> str:
        return self._get_build_run(is_batch, project_name, run_id, tab="env_var")
