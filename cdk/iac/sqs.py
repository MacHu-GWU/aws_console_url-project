# -*- coding: utf-8 -*-

import typing as T

from aws_cdk import (
    aws_sqs as sqs,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class SQSMixin:
    def mk_sqs(self: "MainStack"):
        self.sqs_queue = sqs.Queue(
            self,
            "SQSQueue",
            queue_name=f"{self.prefix_snake}_test",
        )
