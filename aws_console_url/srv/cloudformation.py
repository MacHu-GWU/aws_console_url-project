# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import lru_cache

import aws_arns.api as aws_arns

from ..model import Service


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
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets?permissions=self&filteringText="
        )

    @property
    def stacksets_service_managed(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets?permissions=service&filteringText="
        )

    @property
    def exports(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/exports"

    def filter_stack(self, name: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacks?filteringText={name}&filteringStatus=active&viewNested=true"
        )

    @lru_cache(maxsize=32)
    def _get_stack_object(
        self,
        stack_name: str,
    ) -> T.Optional[aws_arns.res.CloudFormationStack]:
        res = self._bsm.cloudformation_client.describe_stacks(StackName=stack_name)
        stack_list = res.get("Stacks", [])
        if len(stack_list) == 0:
            return None
        else:
            return aws_arns.res.CloudFormationStack.from_arn(stack_list[0]["StackId"])

    def _get_stack_object_from_any(
        self,
        name_or_short_name_or_arn: str,
    ) -> T.Optional[aws_arns.res.CloudFormationStack]:
        if name_or_short_name_or_arn.startswith("arn:"):
            return aws_arns.res.CloudFormationStack.from_arn(name_or_short_name_or_arn)
        elif "/" in name_or_short_name_or_arn:
            name, short_id = name_or_short_name_or_arn.split("/", 1)
            return aws_arns.res.CloudFormationStack.new(
                aws_account_id=self._account_id,
                aws_region=self._region,
                stack_name=name,
                short_id=short_id,
            )
        else:
            return self._get_stack_object(stack_name=name_or_short_name_or_arn)

    def get_stack_arn(self, name: str) -> str:
        return self._get_stack_object_from_any(name).to_arn()

    # --------------------------------------------------------------------------
    # specific CloudFormation Stack detail pages
    # --------------------------------------------------------------------------
    def _stack_tab(self, name_or_arn: str, tab: str) -> str:
        obj = self._get_stack_object_from_any(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/stacks/{tab}?stackId={obj.to_arn()}"
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

    def _get_change_set_object(
        self,
        name_or_arn: str,
    ) -> aws_arns.res.CloudFormationChangeSet:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.CloudFormationChangeSet.from_arn(name_or_arn)
        else:
            return aws_arns.res.CloudFormationChangeSet.new(
                aws_account_id=self._account_id,
                aws_region=self._region,
                fullname=name_or_arn,
            )

    def _change_set_tab(
        self,
        stack_name_or_arn: str,
        change_set_id: str,
        tab: str,
    ) -> str:
        stack = self._get_stack_object_from_any(stack_name_or_arn)
        return (
            f"{self._service_root}/home?region={stack.aws_region}#"
            f"/stacks/changesets/{tab}?stackId={stack.to_arn()}&changeSetId={change_set_id}"
        )

    def get_change_set(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self.get_change_set_changes(stack_name_or_arn, change_set_id)

    def get_change_set_changes(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "changes")

    def get_change_set_inputs(self, stack_name_or_arn: str, change_set_id: str) -> str:
        return self._change_set_tab(stack_name_or_arn, change_set_id, "inputs")

    def get_change_set_template(
        self, stack_name_or_arn: str, change_set_id: str
    ) -> str:
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

    # --------------------------------------------------------------------------
    # specific CloudFormation StackSet detail pages
    # --------------------------------------------------------------------------
    @lru_cache(maxsize=32)
    def _get_stack_set_object(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> aws_arns.res.CloudFormationStackSet:
        """
        Reference:

        - describe_stack_set: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_set.html
        """
        if is_self_managed:  # pragma: no cover
            call_as = "SELF"
        elif is_service_managed:  # pragma: no cover
            call_as = "DELEGATED_ADMIN"
        else:  # pragma: no cover
            raise ValueError(
                "Must specify either is_self_managed or is_service_managed"
            )
        res = self._bsm.cloudformation_client.describe_stack_set(
            StackSetName=name,
            CallAs=call_as,
        )
        stack_set_arn = res["StackSet"]["StackSetARN"]
        return aws_arns.res.CloudFormationStackSet.from_arn(stack_set_arn)

    def _get_stack_set_object_from_anything(
        self,
        name_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> aws_arns.res.CloudFormationStackSet:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.CloudFormationStackSet.from_arn(name_or_arn)
        else:
            return self._get_stack_set_object(
                name=name_or_arn,
                is_self_managed=is_self_managed,
                is_service_managed=is_service_managed,
            )

    def _get_stack_set(
        self,
        name_or_id_or_arn: str,
        tab: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        """
        Internal method to get the URL for a specific tab of a CloudFormation StackSet
        """
        stack_set = self._get_stack_set_object_from_anything(
            name_or_arn=name_or_id_or_arn,
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )
        if is_self_managed:  # pragma: no cover
            permissions = "self"
        elif is_service_managed:  # pragma: no cover
            permissions = "service"
        else:  # pragma: no cover
            raise ValueError(
                "Must specify either is_self_managed or is_service_managed"
            )
        return (
            f"{self._service_root}/home?region={stack_set.aws_region}#"
            f"/stacksets/{stack_set.to_arn()}/{tab}?permissions={permissions}"
        )

    def get_stack_set_arn(
        self,
        name: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        stack_set = self._get_stack_set_object(
            name,
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )
        return stack_set.to_arn()

    def get_stack_set_info(
        self,
        name_or_id_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name_or_id_or_arn=name_or_id_or_arn,
            tab="info",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_instances(
        self,
        name_or_id_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name_or_id_or_arn=name_or_id_or_arn,
            tab="stacks",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_operations(
        self,
        name_or_id_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name_or_id_or_arn=name_or_id_or_arn,
            tab="operations",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_parameters(
        self,
        name_or_id_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name_or_id_or_arn=name_or_id_or_arn,
            tab="parameters",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )

    def get_stack_set_template(
        self,
        name_or_id_or_arn: str,
        is_self_managed: bool = False,
        is_service_managed: bool = False,
    ) -> str:
        return self._get_stack_set(
            name_or_id_or_arn=name_or_id_or_arn,
            tab="template",
            is_self_managed=is_self_managed,
            is_service_managed=is_service_managed,
        )
