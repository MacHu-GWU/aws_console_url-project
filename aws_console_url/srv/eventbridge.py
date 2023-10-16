# -*- coding: utf-8 -*-

import typing as T
import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSEventBridge(Service):
    _AWS_SERVICE = "events"

    # --- arn
    def _get_event_bus_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.EventBridgeEventBus.from_arn(name_or_arn)
        else:
            return aws_arns.res.EventBridgeEventBus.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_event_bus_arn(self, name: str) -> str:
        return self._get_event_bus_obj(name).to_arn()

    def _get_event_rule_obj(self, name_or_arn: str, bus_name: T.Optional[str] = None):
        if name_or_arn.startswith("arn:"):
            if name_or_arn.count("/") == 1:
                return aws_arns.res.EventBridgeRuleOnDefaultEventBus.from_arn(
                    name_or_arn
                )
            else:
                return aws_arns.res.EventBridgeRuleOnCustomEventBus.from_arn(
                    name_or_arn
                )
        else:
            if bus_name is None:
                raise ValueError
            if bus_name == "default":
                return aws_arns.res.EventBridgeRuleOnDefaultEventBus.new(
                    self._account_id,
                    self._region,
                    name_or_arn,
                )
            else:
                return aws_arns.res.EventBridgeRuleOnCustomEventBus.new(
                    self._account_id,
                    self._region,
                    event_bus_name=bus_name,
                    rule_name=name_or_arn,
                )

    def get_event_bus_rule_arn(
        self,
        name_or_arn: str,
        bus_name: T.Optional[str] = None,
    ) -> str:
        return self._get_event_rule_obj(name_or_arn, bus_name).to_arn()

    # --- dashboard
    @property
    def event_buses(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/eventbuses"

    @property
    def event_rules(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/rules"

    # --- resource
    def get_event_bus(self, name_or_arn: str) -> str:
        obj = self._get_event_bus_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/eventbus/{obj.resource_id}"
        )

    def get_event_rule(
        self,
        name_or_arn: str,
        bus_name: T.Optional[str] = None,
    ) -> str:
        obj = self._get_event_rule_obj(name_or_arn, bus_name)
        if "/" in obj.resource_id:
            event_bus_name, rule_name = obj.resource_id.split("/")
        else:
            event_bus_name = "default"
            rule_name = obj.resource_id
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/eventbus/{event_bus_name}/rules/{rule_name}"
        )
