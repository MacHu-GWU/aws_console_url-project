# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class Dynamodb(Service):
    _AWS_SERVICE = "dynamodbv2"

    # --- arn
    def _get_table_obj(self, name_or_arn: str) -> aws_arns.res.DynamodbTable:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.DynamodbTable.from_arn(name_or_arn)
        else:
            return aws_arns.res.DynamodbTable.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_table_arn(self, name: str) -> str:
        """
        Get DynamoDB table ARN.
        """
        return self._get_table_obj(name).to_arn()

    # --- dashboard
    @property
    def tables(self) -> str:
        return f"{self._service_root}/home?region={self._region}#tables"

    # --- table
    def _get_table_tab(
        self,
        table_or_arn: str,
        tab: str,
    ) -> str:
        obj = self._get_table_obj(table_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#table?initialTagKey=&name={obj.table_name}&tab={tab}"
        )

    def get_table(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "overview")

    def get_table_overview(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "overview")

    def get_table_indexes(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "indexes")

    def get_table_monitoring(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "monitoring")

    def get_table_global_tables(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "globalTables")

    def get_table_backups(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "backups")

    def get_table_exports_and_streams(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "streams")

    def get_table_additional_settings(self, table_or_arn: str) -> str:
        return self._get_table_tab(table_or_arn, "settings")

    def get_table_items(self, table_or_arn: str) -> str:
        obj = self._get_table_obj(table_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#item-explorer?initialTagKey=&maximize=true&table={obj.table_name}"
        )

    def get_item_details(
        self,
        table_or_arn: str,
        hash_key: T.Any,
        range_key: T.Optional[T.Any] = None,
    ) -> str:
        obj = self._get_table_obj(table_or_arn)
        if range_key is None:
            range_key_param = "sk"
        else:
            range_key_param = f"sk={range_key}"
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#edit-item?table={obj.table_name}"
            f"&itemMode=2&pk={hash_key}&{range_key_param}&route=ROUTE_ITEM_EXPLORER"
        )
