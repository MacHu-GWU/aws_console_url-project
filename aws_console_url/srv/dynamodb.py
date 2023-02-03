# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class DynamoDBTable(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str
    ) -> "DynamoDBTable":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:dynamodb:{self.aws_region}:{self.aws_account_id}:table/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "DynamoDBTable":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5].split("/")[1]
        return cls.make(aws_account_id, aws_region, name)


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
