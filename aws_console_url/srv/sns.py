# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class SNS(Service):
    _AWS_SERVICE = "sns/v3"

    def _get_topic_obj(self, name_or_arn: str) -> aws_arns.res.SnsTopic:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.SnsTopic.from_arn(name_or_arn)
        else:
            return aws_arns.res.SnsTopic.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def _get_subscription_obj(
        self,
        subscription_id_or_arn: str,
        topic_name: T.Optional[str] = None,
    ) -> aws_arns.res.SnsSubscription:
        if subscription_id_or_arn.startswith("arn:"):
            return aws_arns.res.SnsSubscription.from_arn(subscription_id_or_arn)
        else:
            if topic_name is None:
                raise ValueError("topic_name must be specified")
            return aws_arns.res.SnsSubscription.new(
                self._account_id,
                self._region,
                topic_name,
                subscription_id_or_arn,
            )

    # --- arn
    def get_topic_arn(self, name: str) -> str:
        return self._get_topic_obj(name).to_arn()

    def get_subscription_arn(self, topic_name: str, subscription_id: str) -> str:
        return self._get_subscription_obj(subscription_id, topic_name).to_arn()

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
        obj = self._get_topic_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#/topic/{obj.to_arn()}"
        )

    def get_subscription(
        self,
        subscription_id_or_arn: str,
        topic_name: T.Optional[str] = None,
    ):
        obj = self._get_subscription_obj(subscription_id_or_arn, topic_name)
        return f"{self._service_root}/home?region={obj.aws_region}#/subscription/{obj.to_arn()}"
