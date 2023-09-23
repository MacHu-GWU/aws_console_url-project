# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class RDS(Service):
    _AWS_SERVICE = "rds"

    def _get_rds_obj(
        self,
        id_or_arn: str,
        class_,
    ) -> aws_arns.res.RdsDBCluster:
        if id_or_arn.startswith("arn:"):
            return class_.from_arn(id_or_arn)
        else:
            return class_.new(
                self._account_id,
                self._region,
                id_or_arn,
            )

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

    def get_database_cluster(self, id_or_arn: str) -> str:
        obj = self._get_rds_obj(id_or_arn, aws_arns.res.RdsDBCluster)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#database:id={obj.resource_id};is-cluster=true"
        )

    def get_database_instance(self, id_or_arn: str) -> str:
        obj = self._get_rds_obj(id_or_arn, aws_arns.res.RdsDBInstance)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#database:id={obj.resource_id};is-cluster=false"
        )

    def get_snapshot(self, name_or_arn: str) -> str:
        # it's ok to use instance snapshot class here, we only need the resource id
        obj = self._get_rds_obj(name_or_arn, aws_arns.res.RdsDBInstanceSnapshot)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#db-snapshot:id={obj.resource_id}"
        )

    def get_db_subnet_group(self, name_or_arn: str) -> str:
        obj = self._get_rds_obj(name_or_arn, aws_arns.res.RdsDBSubnetGroup)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#db-subnet-group:id={obj.resource_id}"
        )

    def get_db_parameter_group(self, name_or_arn: str) -> str:
        obj = self._get_rds_obj(name_or_arn, aws_arns.res.RdsDBParameterGroup)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#parameter-group-details:parameter-group-name={obj.resource_id}"
        )
