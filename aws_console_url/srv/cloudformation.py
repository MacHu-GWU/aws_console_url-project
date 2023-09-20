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
    - long_name: CDKToolkit/b518e0f0-750b-11ed-859b-1208b06dceb3
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
    def long_name(self) -> str:
        return f"{self.name}/{self.short_id}"

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
    permission_model_is_self_managed: bool = dataclasses.field(default=False)
    permission_model_is_service_managed: bool = dataclasses.field(default=False)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        short_id: str,
        permission_model_is_self_managed: bool = False,
        permission_model_is_service_managed: bool = False,
    ) -> "CloudFormationStackSet":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
            permission_model_is_self_managed=permission_model_is_self_managed,
            permission_model_is_service_managed=permission_model_is_service_managed,
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
    def parse_arn(cls, arn: str) -> T.Tuple[str, str, str, str]:
        """
        :return: (aws_account_id, aws_region, name, short_id)
        """
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        chunks = parts[5].split("/")
        name = chunks[1]
        short_id = parts[6]
        return aws_account_id, aws_region, name, short_id

    @classmethod
    def from_arn(cls, arn: str) -> "CloudFormationStackSet":
        aws_account_id, aws_region, name, short_id = cls.parse_arn(arn)
        return cls.make(aws_account_id, aws_region, name, short_id)

    @classmethod
    def from_describe_stack_set_response(cls, data: dict) -> "CloudFormationStackSet":
        """
        Create a "CloudFormationStackSet" object from the response of the
        ``describe_stack_set`` API.

        Reference:

        - describe_stack_set: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation/client/describe_stack_set.html
        """
        aws_account_id, aws_region, name, short_id = cls.parse_arn(data["StackSetARN"])
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            short_id=short_id,
            permission_model_is_self_managed=data["PermissionModel"] == "SELF_MANAGED",
            permission_model_is_service_managed=data["PermissionModel"]
            == "SERVICE_MANAGED",
        )


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
    def _get_stack_object(self, name: str) -> T.Optional[CloudFormationStack]:
        res = self._bsm.cloudformation_client.describe_stacks(StackName=name)
        stack_list = res.get("Stacks", [])
        if len(stack_list) == 0:
            return None
        else:
            return CloudFormationStack.from_stack_id(stack_list[0]["StackId"])

    def _get_stack_object_from_any(
        self,
        name_or_short_name_or_arn: str,
    ) -> T.Optional[CloudFormationStack]:
        if name_or_short_name_or_arn.startswith("arn:"):
            return CloudFormationStack.from_arn(name_or_short_name_or_arn)
        elif "/" in name_or_short_name_or_arn:
            name, short_id = name_or_short_name_or_arn.split("/", 1)
            return CloudFormationStack.make(
                aws_account_id=self._account_id,
                aws_region=self._region,
                name=name,
                short_id=short_id,
            )
        else:
            return self._get_stack_object(name_or_short_name_or_arn)

    def _get_stack_id(self, name_or_short_name_or_arn: str) -> str:
        return self._get_stack_object_from_any(name_or_short_name_or_arn).arn

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

    def _change_set_tab(
        self, stack_name_or_arn: str, change_set_id: str, tab: str
    ) -> str:
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
    ) -> CloudFormationStackSet:
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
        return CloudFormationStackSet.from_describe_stack_set_response(
            response["StackSet"]
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
        if name_or_id_or_arn.startswith("arn:"):
            stack_set_id = CloudFormationStackSet.from_arn(
                name_or_id_or_arn
            ).stack_set_id
            if is_self_managed:  # pragma: no cover
                permissions = "self"
            elif is_service_managed:  # pragma: no cover
                permissions = "service"
            else:  # pragma: no cover
                raise ValueError(
                    "Must specify either is_self_managed or is_service_managed"
                )
        elif ":" in name_or_id_or_arn:
            stack_set_id = name_or_id_or_arn
            if is_self_managed:  # pragma: no cover
                permissions = "self"
            elif is_service_managed:  # pragma: no cover
                permissions = "service"
            else:  # pragma: no cover
                raise ValueError(
                    "Must specify either is_self_managed or is_service_managed"
                )
        else:
            stack_set = self._get_stack_set_object(
                name=name_or_id_or_arn,
                is_self_managed=is_self_managed,
                is_service_managed=is_service_managed,
            )
            stack_set_id = stack_set.stack_set_id
            if stack_set.permission_model_is_self_managed:  # pragma: no cover
                permissions = "self"
            elif stack_set.permission_model_is_service_managed:  # pragma: no cover
                permissions = "service"
            else:  # pragma: no cover
                raise NotImplementedError()
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/stacksets/{stack_set_id}/{tab}?permissions={permissions}"
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
        return stack_set.arn

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
