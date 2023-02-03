# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class DynamoDBTable(BaseServiceResourceV1):
    _SERVICE_NAME = "dynamodb"
    _RESOURCE_TYPE = "table"


@dataclasses.dataclass(frozen=True)
class Dynamodb(Service):
    _AWS_SERVICE = "dynamodbv2"

    # --- arn
    def get_table_arn(self, name: str) -> str:
        """
        Get DynamoDB table ARN.
        """
        return DynamoDBTable.make(self._account_id, self._region, name).arn

    # --- dashboard
    @property
    def tables(self) -> str:
        return f"{self._service_root}/home?region={self._region}#tables"

    # --- table
    def get_table_overview(self, table: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#table?initialTagKey=&name={table}&tab=overview"
        )

    def get_table_items(self, table: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#item-explorer?initialTagKey=&maximize=true&table={table}"
        )

    def get_item_details(
        self,
        table: str,
        hash_key: T.Any,
        range_key: T.Optional[T.Any] = None,
    ) -> str:
        if range_key is None:
            range_key_param = "sk"
        else:
            range_key_param = f"sk={range_key}"
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#edit-item?table={table}"
            f"&itemMode=2&pk={hash_key}&{range_key_param}&route=ROUTE_ITEM_EXPLORER"
        )
