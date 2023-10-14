# -*- coding: utf-8 -*-

import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSAthena(Service):
    _AWS_SERVICE = "athena"

    # --- arn
    def _get_capacity_reservation_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.AthenaCapacityReservation.from_arn(name_or_arn)
        else:
            return aws_arns.res.AthenaCapacityReservation.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_capacity_reservation_arn(self, name: str) -> str:
        return self._get_capacity_reservation_obj(name).to_arn()

    def _get_data_catalog_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.AthenaDataCatalog.from_arn(name_or_arn)
        else:
            return aws_arns.res.AthenaDataCatalog.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_data_catalog_arn(self, name: str) -> str:
        return self._get_data_catalog_obj(name).to_arn()

    def _get_workgroup_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.AthenaWorkgroup.from_arn(name_or_arn)
        else:
            return aws_arns.res.AthenaWorkgroup.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_workgroup_arn(self, name: str) -> str:
        return self._get_workgroup_obj(name).to_arn()

    # --- dashboard
    @property
    def capacity_reservations(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/capacity-reservations"

    @property
    def data_catalogs(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/data-sources"

    @property
    def workgroups(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/workgroups"

    # --- resource
    def get_capacity_reservation(self, name_or_arn: str) -> str:
        obj = self._get_capacity_reservation_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/capacity-reservations/details/{obj.resource_id}"
        )

    def get_data_catalog(self, name_or_arn: str) -> str:
        obj = self._get_data_catalog_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/data-sources/details/{obj.resource_id}"
        )

    def get_workgroup(self, name_or_arn: str) -> str:
        obj = self._get_workgroup_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/workgroups/details/{obj.resource_id}"
        )
