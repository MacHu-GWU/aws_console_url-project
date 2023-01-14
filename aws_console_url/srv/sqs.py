# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class SQS(Builder):
    _AWS_SERVICE = "sqs/v2"

    @property
    def queues(self) -> str:
        return f"{self._service_root}/home?#/queues"

    def get_queue(self, name: str) -> str:
        return (
            f"{self._service_root}/home?#/queues"
            f"/https%3A%2F%2Fsqs.{self._region}.amazonaws.com%2F{self._account_id}%2F{name}"
        )

    def get_queue_url(self, name: str) -> str:
        return f"https://sqs.{self._region}.amazonaws.com/{self._account_id}/{name}"

    def get_queue_arn(self, name: str) -> str:
        return f"arn:aws:sqs:{self._region}:{self._account_id}:{name}"
