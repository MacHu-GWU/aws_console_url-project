# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class SQSQueue(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, aws_account_id: str, aws_region: str, name: str) -> "SQSQueue":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:sqs:{self.aws_region}:{self.aws_account_id}:{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "SQSQueue":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class SQS(Service):
    _AWS_SERVICE = "sqs/v2"

    # --- arn
    def get_queue_arn(self, name: str) -> str:
        return SQSQueue.make(self._account_id, self._region, name).arn

    # --- console
    @property
    def queues(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/queues"

    def get_queue(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/queues"
            f"/https%3A%2F%2Fsqs.{self._region}.amazonaws.com%2F{self._account_id}%2F{name}"
        )

    def get_queue_url(self, name: str) -> str:
        return f"https://sqs.{self._region}.amazonaws.com/{self._account_id}/{name}"

    def get_queue_send_and_receive_message(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#/queues"
            f"/https%3A%2F%2Fsqs.{self._region}.amazonaws.com%2F{self._account_id}%2F{name}"
            f"/send-receive"
        )
