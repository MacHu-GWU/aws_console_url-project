# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_events as events,
)

if T.TYPE_CHECKING:
    from .main import MainStack


class EventBridgeMixin:
    def mk_eventbridge(self: "MainStack"):
        self.eventbridge_bus = events.EventBus(
            self,
            id="EventBridgeBus",
            event_bus_name=f"{self.prefix_snake}_test",
        )

        self.eventbridge_rule_on_default = events.Rule(
            self,
            id="EventBridgeRuleOnDefault",
            rule_name=f"{self.prefix_snake}_default_test",
            schedule=events.Schedule.rate(cdk.Duration.days(30)),
        )

        self.eventbridge_rule_on_custom = events.Rule(
            self,
            id="EventBridgeRuleOnCustom",
            rule_name=f"{self.prefix_snake}_custom_test",
            event_pattern=events.EventPattern(
                source=["aws.codecommit"],
                detail_type=["CodeCommit Repository State Change"],
                resources=[
                    f"arn:aws:codecommit:{cdk.Aws.REGION}:{cdk.Aws.ACCOUNT_ID}:{self.prefix_snake}_test"
                ],
                detail={
                    "event": ["referenceCreated", "referenceUpdated"],
                    "referenceName": [{"prefix": "release/"}],
                },
            ),
            event_bus=self.eventbridge_bus,
        )
