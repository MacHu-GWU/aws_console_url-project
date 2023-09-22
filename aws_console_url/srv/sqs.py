# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class SQS(Service):
    _AWS_SERVICE = "sqs/v2"

    def _get_queue_obj(self, name_or_arn_or_url: str) -> aws_arns.res.SqsQueue:
        if name_or_arn_or_url.startswith("arn:"):
            return aws_arns.res.SqsQueue.from_arn(name_or_arn_or_url)
        elif name_or_arn_or_url.startswith("http"):
            return aws_arns.res.SqsQueue.from_queue_url(name_or_arn_or_url)
        else:
            return aws_arns.res.SqsQueue.new(
                self._account_id,
                self._region,
                name_or_arn_or_url,
            )

    # --- arn
    def get_queue_arn(self, name_or_url: str) -> str:
        return self._get_queue_obj(name_or_url).to_arn()

    def get_queue_url(self, name_or_arn: str) -> str:
        return self._get_queue_obj(name_or_arn).queue_url

    # --- console
    @property
    def queues(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/queues"

    def get_queue(
        self,
        name_or_arn_or_url: str,
    ) -> str:
        obj = self._get_queue_obj(name_or_arn_or_url)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#/queues"
            f"/https%3A%2F%2Fsqs.{obj.aws_region}.amazonaws.com%2F{obj.aws_account_id}%2F{obj.queue_name}"
        )

    def get_queue_send_and_receive_message(
        self,
        name_or_arn_or_url: str,
    ) -> str:
        base_url = self.get_queue(name_or_arn_or_url)
        return f"{base_url}/send-receive"
