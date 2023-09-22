# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class ECS(Service):
    _AWS_SERVICE = "ecs/v2"

    # --- arn
    def _get_cluster_obj(self, name_or_arn: str) -> aws_arns.res.EcsCluster:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.EcsCluster.from_arn(name_or_arn)
        else:
            return aws_arns.res.EcsCluster.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def _get_task_definition_obj(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> aws_arns.res.EcsTaskDefinition:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.EcsTaskDefinition.from_arn(name_or_arn)
        else:
            return aws_arns.res.EcsTaskDefinition.new(
                self._account_id,
                self._region,
                name_or_arn,
                revision,
            )

    def _get_task_run_obj(
        self,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> aws_arns.res.EcsTaskRun:
        if task_short_id_or_arn.startswith("arn:"):
            return aws_arns.res.EcsTaskRun.from_arn(task_short_id_or_arn)
        else:
            if cluster_name is None: # pragma: no cover
                raise ValueError("cluster_name is required when task_short_id_or_arn is not an ARN")
            return aws_arns.res.EcsTaskRun.new(
                self._account_id,
                self._region,
                f"{cluster_name}/{task_short_id_or_arn}",
            )

    def get_cluster_arn(self, name: str) -> str:
        return self._get_cluster_obj(name).to_arn()

    def get_task_definition_arn(self, name: str, revision: int) -> str:
        return self._get_task_definition_obj(name, revision).to_arn()

    def get_task_run_arn(self, cluster_name: str, task_short_id: str) -> str:
        return self._get_task_run_obj(task_short_id, cluster_name).to_arn()

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
        obj = self._get_cluster_obj(name_or_arn)
        return (
            f"{self._service_root}/clusters/{obj.cluster_name}"
            f"/{tab}?region={obj.aws_region}"
        )

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

    def get_task_definition_revisions(
        self,
        name_or_arn: str,
    ) -> str:
        if name_or_arn.startswith("arn:"):
            obj = self._get_task_definition_obj(name_or_arn)
        else:
            obj = self._get_task_definition_obj(name_or_arn, 1)
        return f"{self._service_root}/task-definitions/{obj.task_name}?region={obj.aws_region}"

    def _get_task_definition_revision_tab(
        self,
        tab: str,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        obj = self._get_task_definition_obj(name_or_arn, revision)
        return (
            f"{self._service_root}/task-definitions"
            f"/{obj.task_name}/{obj.version}/{tab}?region={obj.aws_region}"
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

    def _get_task_run_tab(
        self,
        tab: str,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> str:
        obj = self._get_task_run_obj(task_short_id_or_arn, cluster_name)
        cluster_name, task_short_id = obj.run_id.split("/", 1)
        return (
            f"{self._service_root}/clusters/{cluster_name}/tasks"
            f"/{task_short_id}/{tab}?region={obj.aws_region}"
        )

    def get_task_run_configuration(
        self,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> str:
        return self._get_task_run_tab("configuration", task_short_id_or_arn, cluster_name)

    def get_task_run_logs(
        self,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> str:
        return self._get_task_run_tab("logs", task_short_id_or_arn, cluster_name)

    def get_task_run_networking(
        self,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> str:  # pragma: no cover
        return self._get_task_run_tab("networking", task_short_id_or_arn, cluster_name)

    def get_task_run_tags(
        self,
        task_short_id_or_arn: str,
        cluster_name: T.Optional[str] = None,
    ) -> str:  # pragma: no cover
        return self._get_task_run_tab("tags", task_short_id_or_arn, cluster_name)
