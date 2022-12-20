# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from ..builder import Builder


@dataclasses.dataclass
class Dynamodb(Builder):
    @property
    def tables(self) -> str:
        return f"{self._service_root}/home?#tables"

    def table_overview(self, table: str) -> str:
        return (
            f"{self._service_root}/home?#table?initialTagKey=&name={table}&tab=overview"
        )

    def table_items(self, table: str) -> str:
        return f"{self._service_root}/home?#item-explorer?initialTagKey=&maximize=true&table={table}"

    def item_details(
        self, table: str, hash_key: T.Any, range_key: T.Optional[T.Any] = None
    ) -> str:
        if range_key is None:
            range_key_param = "sk"
        else:
            range_key_param = f"sk={range_key}"
        return (
            f"{self._service_root}/home?#edit-item?table={table}"
            f"&itemMode=2&pk={hash_key}&{range_key_param}&route=ROUTE_ITEM_EXPLORER"
        )


dynamodb = Dynamodb(aws_service="dynamodbv2")
