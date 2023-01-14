# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class CodeBuild(Builder):
    _AWS_SERVICE = "codesuite/codebuild"

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
        return f"{self._service_root}/{self._account_id}/projects/{project}/history?region={self._region}"

    def get_build_run(self, project: str, build_id: int) -> str:
        return (
            f"{self._service_root}/{self._account_id}/projects/{project}/build"
            f"/{build_id}"
        )
