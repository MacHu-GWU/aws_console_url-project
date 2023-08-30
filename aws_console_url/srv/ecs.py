# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import BaseServiceResourceV1, BaseServiceResourceV2, Service


@dataclasses.dataclass(frozen=True)
class ECSCluster(BaseServiceResourceV1):
    _SERVICE_NAME = "ecs"
    _RESOURCE_TYPE = "cluster"


@dataclasses.dataclass(frozen=True)
class ECSTaskDefinition(BaseServiceResourceV2):
    _SERVICE_NAME = "ecs"
    _RESOURCE_TYPE = "task-definition"


@dataclasses.dataclass(frozen=True)
class ECS(Service):
    _AWS_SERVICE = "ecs/v2"

    # --- arn
    def get_cluster_arn(self, name: str) -> str:
        return ECSCluster.make(self._account_id, self._region, name).arn

    def get_task_definition_arn(self, name: str, revision: int) -> str:
        return ECSTaskDefinition.make(
            self._account_id,
            self._region,
            name,
            str(revision),
        ).arn

    # --- dashboard
    @property
    def clusters(self) -> str:
        return f"{self._service_root}/clusters?region={self._region}"

    @property
    def task_definitions(self) -> str:
        return f"{self._service_root}/task-definitions?region={self._region}"

    def _arn_to_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    def _get_cluster_tab(self, name_or_arn: str, tab: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return f"{self._service_root}/clusters/{name}/{tab}?region={self._region}"

    def get_cluster_services(self, name_or_arn: str) -> str:
        return self._get_cluster_tab(name_or_arn, "services")

    def get_cluster_tasks(self, name_or_arn: str) -> str:
        return self._get_cluster_tab(name_or_arn, "tasks")

    def get_cluster_infrastructure(self, name_or_arn: str) -> str:  # pragma: no cover
        return self._get_cluster_tab(name_or_arn, "infrastructure")

    def get_cluster_cluster_metrics(self, name_or_arn: str) -> str:  # pragma: no cover
        return self._get_cluster_tab(name_or_arn, "clusterMetrics")

    def get_cluster_scheduled_tasks(self, name_or_arn: str) -> str:  # pragma: no cover
        return self._get_cluster_tab(name_or_arn, "scheduled-tasks")

    def get_cluster_tags(self, name_or_arn: str) -> str:  # pragma: no cover
        return self._get_cluster_tab(name_or_arn, "tags")

    def get_task_definition_revisions(self, name_or_arn: str) -> str:
        if name_or_arn.startswith("arn:"):
            name_and_revision = self._arn_to_name(name_or_arn)
            name = name_and_revision.split(":")[0]
        else:
            name = name_or_arn
        return f"{self._service_root}/task-definitions/" f"{name}?region={self._region}"

    def _get_task_definition_revision_tab(
        self,
        tab: str,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        if name_or_arn.startswith("arn:"):
            if revision is not None:  # pragma: no cover
                raise ValueError("revision must be None if name_or_arn is an ARN")
            else:
                name_and_revision = self._arn_to_name(name_or_arn)
                name, revision = name_and_revision.split(":")
        else:
            if revision is None:  # pragma: no cover
                raise ValueError("revision must be specified if name_or_arn is a name")
            else:
                name = name_or_arn
        return (
            f"{self._service_root}/task-definitions"
            f"/{name}/{revision}/{tab}?region={self._region}"
        )

    def get_task_definition_revision_containers(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        return self._get_task_definition_revision_tab(
            "containers", name_or_arn, revision
        )

    def get_task_definition_revision_json(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        return self._get_task_definition_revision_tab("json", name_or_arn, revision)

    def get_task_definition_revision_storage(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:  # pragma: no cover
        return self._get_task_definition_revision_tab("storage", name_or_arn, revision)

    def get_task_definition_revision_tags(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:  # pragma: no cover
        return self._get_task_definition_revision_tab("tags", name_or_arn, revision)

    def _get_task_tab(
        self,
        cluster_name_or_arn: str,
        task_id: str,
        tab: str,
    ) -> str:
        cluster_name = self._ensure_name(cluster_name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/clusters/{cluster_name}/tasks"
            f"/{task_id}/{tab}?region={self._region}"
        )

    def get_task_configuration(
        self,
        cluster_name_or_arn: str,
        task_id: str,
    ) -> str:
        return self._get_task_tab(cluster_name_or_arn, task_id, "configuration")

    def get_task_logs(
        self,
        cluster_name_or_arn: str,
        task_id: str,
    ) -> str:
        return self._get_task_tab(cluster_name_or_arn, task_id, "logs")

    def get_task_networking(
        self,
        cluster_name_or_arn: str,
        task_id: str,
    ) -> str:  # pragma: no cover
        return self._get_task_tab(cluster_name_or_arn, task_id, "networking")

    def get_task_tags(
        self,
        cluster_name_or_arn: str,
        task_id: str,
    ) -> str:  # pragma: no cover
        return self._get_task_tab(cluster_name_or_arn, task_id, "tags")
