# -*- coding: utf-8 -*-

import typing as T

from aws_cdk import (
    aws_sns as sns,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class SNSMixin:
    def mk_sns(self: "MainStack"):
        self.sns_topic = sns.Topic(
            self,
            "SNSTopic",
            topic_name=f"{self.prefix_snake}_test",
        )

        self.sns_topic_subscription = sns.Subscription(
            self,
            "SNSTopicSubscription",
            topic=self.sns_topic,
            endpoint="qibaishang@gmail.com",
            protocol=sns.SubscriptionProtocol.EMAIL,
        )
