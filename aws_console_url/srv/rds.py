# -*- coding: utf-8 -*-

import dataclasses

from ..model import Service


@dataclasses.dataclass(frozen=True)
class RDS(Service):
    _AWS_SERVICE = "rds"

    # --- arn
    def _arn_to_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    # --- dashboard
    @property
    def databases(self) -> str:
        return f"{self._service_root}/home?region={self._region}#databases:"

    @property
    def snapshots(self) -> str:
        return f"{self._service_root}/home?region={self._region}#snapshots-list:"

    @property
    def db_subnet_groups(self) -> str:
        return f"{self._service_root}/home?region={self._region}#db-subnet-groups-list:"

    @property
    def db_parameter_groups(self) -> str:
        return f"{self._service_root}/home?region={self._region}#parameter-group-list:"

    def get_database_cluster(self, identifier: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#database:id={identifier};is-cluster=true"
        )

    def get_database_instance(self, identifier: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#database:id={identifier};is-cluster=false"
        )

    def get_snapshot(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#db-snapshot:id={name}"
        )

    def get_db_subnet_group(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#db-subnet-group:id={name}"
        )

    def get_db_parameter_group(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#parameter-group-details:parameter-group-name={name}"
        )
