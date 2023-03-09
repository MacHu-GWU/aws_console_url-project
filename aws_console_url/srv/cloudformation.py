# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class CloudFormationStack(Resource):
    """
    Example:

    - name: CDKToolkit
    - short_id: b518e0f0-750b-11ed-859b-1208b06dceb3
    - arn: arn:aws:cloudformation:us-east-1:111122223333:stack/CDKToolkit/b518e0f0-750b-11ed-859b-1208b06dceb3
    """

    name: T.Optional[str] = dataclasses.field(default=None)
    short_id: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        short_id: str,
    ) -> "CloudFormationStack":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
        )

    @property
    def arn(self) -> str:
        return (
            f"arn:aws:cloudformation:{self.aws_region}:{self.aws_account_id}:stack"
            f"/{self.name}/{self.short_id}"
        )

    @property
    def stack_id(self) -> str:
        return self.arn

    @classmethod
    def from_arn(cls, arn: str) -> "CloudFormationStack":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        chunks = parts[5].split("/")
        name = chunks[1]
        short_id = chunks[2]
        return cls.make(aws_account_id, aws_region, name, short_id)

    @classmethod
    def from_stack_id(cls, stack_id: str) -> "CloudFormationStack":
        return cls.from_arn(stack_id)


@dataclasses.dataclass(frozen=True)
class CloudFormationStackSet(Resource):
    """
    Example:

    - name: landing-zone-s3
    - short_id: 5bf3c555-6fea-4474-83e7-56f541f8bd39
    - arn: arn:aws:cloudformation:us-east-1:111122223333:stackset/landing-zone-s3:5bf3c555-6fea-4474-83e7-56f541f8bd39
    """

    name: T.Optional[str] = dataclasses.field(default=None)
    short_id: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        short_id: str,
    ) -> "CloudFormationStackSet":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
        )

    @property
    def arn(self) -> str:
        return (
            f"arn:aws:cloudformation:{self.aws_region}:{self.aws_account_id}:stackset"
            f"/{self.name}:{self.short_id}"
        )

    @property
    def stack_set_id(self) -> str:
        return f"{self.name}:{self.short_id}"

    @classmethod
    def from_arn(cls, arn: str) -> "CloudFormationStackSet":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        chunks = parts[5].split("/")
        name = chunks[1]
        short_id = parts[6]
        return cls.make(aws_account_id, aws_region, name, short_id)


@dataclasses.dataclass(frozen=True)
class CloudFormation(Service):
    _AWS_SERVICE = "cloudformation"

    @property
    def stacks(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacks"

    @property
    def stacksets(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacksets"

    @property
    def stacksets_self_managed(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacksets?permissions=self&filteringText="

    @property
    def stacksets_service_managed(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/stacksets?permissions=service&filteringText="

    @property
    def exports(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/exports"

    def filter_stack(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks?filteringText={name}&filteringStatus=active&viewNested=true"
        )

    @lru_cache(maxsize=32)
    def _get_stack_id(self, name: str) -> str:
        response = self._bsm.cloudformation_client.describe_stacks(StackName=name)
        arn = response["Stacks"][0]["StackId"]
        return arn

    def get_stack_arn(self, name: str) -> str:
        return self._get_stack_id(name)

    def ensure_arn(self, name_or_arn: str) -> str:
        return self._ensure_arn(name_or_arn, self._get_stack_id)

    # --------------------------------------------------------------------------
    # specific CloudFormation Stack detail pages
    # --------------------------------------------------------------------------
    def _stack_tab(self, name_or_arn: str, tab: str) -> str:
        stack_id = self.ensure_arn(name_or_arn)
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks/{tab}?stackId={stack_id}"
        )

    def get_stack(self, name_or_arn: str) -> str:
        return self.get_stack_info(name_or_arn)

    def get_stack_info(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "stackinfo")

    def get_stack_events(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "events")

    def get_stack_resources(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "resources")

    def get_stack_outputs(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "outputs")

    def get_stack_parameters(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "parameters")

    def get_stack_changesets(self, name_or_arn: str) -> str:
        return self._stack_tab(name_or_arn, "changesets")

    def _change_set_tab(self, stack_name_or_arn: str, change_set_id: str, tab: str) -> str:
        stack_id = self.ensure_arn(stack_name_or_arn)
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks/changesets/{tab}?stackId={stack_id}&changeSetId={change_set_id}"
        )

    def get_change_set(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self.get_change_set_changes(stack_name_or_arn, change_set_id)

    def get_change_set_changes(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "changes")

    def get_change_set_inputs(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "inputs")

    def get_change_set_template(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "template")

    def get_change_set_json(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "json")

    def get_change_set_hooks(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "hooks")

    def filter_self_managed_stack_set(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets?permissions=self&filteringText={name}"
        )

    def filter_service_managed_stack_set(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets?permissions=service&filteringText={name}"
        )

    @lru_cache(maxsize=32)
    def get_stack_set_arn(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        if is_self_managed:  # pragma: no cover
            call_as = "SELF"
        elif is_service_managed:  # pragma: no cover
            call_as = "DELEGATED_ADMIN"
        else:  # pragma: no cover
            raise ValueError(
                "Must specify either is_self_managed or is_service_managed"
            )
        response = self._bsm.cloudformation_client.describe_stack_set(
            StackSetName=name,
            CallAs=call_as,
        )
        arn = response["StackSet"]["StackSetARN"]
        return arn

    # --------------------------------------------------------------------------
    # specific CloudFormation StackSet detail pages
    # --------------------------------------------------------------------------
    def _get_stack_set(
        self,
        name: str,
        tab: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        stack_set_arn = self.get_stack_set_arn(
            name=name,
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )
        stack_set = CloudFormationStackSet.from_arn(stack_set_arn)
        if is_self_managed:  # pragma: no cover
            permissions = "self"
        elif is_service_managed:  # pragma: no cover
            permissions = "service"
        else:  # pragma: no cover
            raise ValueError(
                "Must specify either is_self_managed or is_service_managed"
            )
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets/{stack_set.stack_set_id}/{tab}?permissions={permissions}"
        )

    def get_stack_set_info(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name=name,
            tab="info",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_instances(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name=name,
            tab="stacks",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_operations(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name=name,
            tab="operations",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_parameters(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name=name,
            tab="parameters",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_template(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name=name,
            tab="template",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )
