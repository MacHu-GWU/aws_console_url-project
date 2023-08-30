# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class SNSTopic(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, aws_account_id: str, aws_region: str, name: str) -> "SNSTopic":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:sns:{self.aws_region}:{self.aws_account_id}:{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "SNSTopic":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class SNSSubscription(Resource):
    topic_name: T.Optional[str] = dataclasses.field(default=None)
    subscription_id: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        topic_name: str,
        subscription_id: str,
    ) -> "SNSSubscription":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            topic_name=topic_name,
            subscription_id=subscription_id,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:sns:{self.aws_region}:{self.aws_account_id}:{self.topic_name}:{self.subscription_id}"

    @classmethod
    def from_arn(cls, arn: str) -> "SNSSubscription":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        topic_name = parts[5]
        subscription_id = parts[6]
        return cls.make(aws_account_id, aws_region, topic_name, subscription_id)


@dataclasses.dataclass(frozen=True)
class SNS(Service):
    _AWS_SERVICE = "sns/v3"

    # --- arn
    def get_topic_arn(self, name: str) -> str:
        return SNSTopic.make(self._account_id, self._region, name).arn

    def get_subscription_arn(self, topic_name: str, subscription_id: str) -> str:
        return SNSSubscription.make(
            self._account_id, self._region, topic_name, subscription_id
        ).arn

    # --- console
    @property
    def topics(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/topics"

    @property
    def subscriptions(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/subscriptions"

    def _topic_arn_to_name(self, arn: str) -> str:
        return arn.split(":")[5]

    def _subscr_arn_to_name(self, arn: str) -> str:
        return arn.split(":")[5]

    def get_topic(self, name_or_arn: str) -> str:
        if name_or_arn.startswith("arn:"):
            arn = name_or_arn
        else:
            arn = SNSTopic.make(
                aws_account_id=self._account_id,
                aws_region=self._region,
                name=name_or_arn,
            ).arn

        return f"{self._service_root}/home?region={self._region}#/topic/{arn}"

    def get_subscription(
        self,
        topic_name_or_subscription_arn: str,
        subscription_id: T.Optional[str] = None,
    ):
        if topic_name_or_subscription_arn.startswith("arn:"):
            arn = topic_name_or_subscription_arn
            if subscription_id is not None:
                raise ValueError(
                    "subscription_id must not be provided if topic_name_or_subscription_arn is an ARN"
                )
        else:
            if subscription_id is None:
                raise ValueError(
                    "subscription_id must be provided if topic_name_or_subscription_arn is not an ARN"
                )
            else:
                arn = SNSSubscription.make(
                    aws_account_id=self._account_id,
                    aws_region=self._region,
                    topic_name=topic_name_or_subscription_arn,
                    subscription_id=subscription_id,
                ).arn

        return f"{self._service_root}/home?region={self._region}#/subscription/{arn}"
