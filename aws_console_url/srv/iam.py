# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class IamUserGroup(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, aws_account_id: str, name: str) -> "IamUserGroup":
        return cls(
            aws_account_id=aws_account_id,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:iam::{self.aws_account_id}:group/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "IamUserGroup":
        parts = arn.split(":")
        aws_account_id = parts[4]
        name = parts[5].split("/")[1]
        return cls.make(aws_account_id, name)


@dataclasses.dataclass(frozen=True)
class IamUser(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, aws_account_id: str, name: str) -> "IamUser":
        return cls(
            aws_account_id=aws_account_id,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:iam::{self.aws_account_id}:user/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "IamUser":
        parts = arn.split(":")
        aws_account_id = parts[4]
        name = parts[5].split("/")[1]
        return cls.make(aws_account_id, name)


@dataclasses.dataclass(frozen=True)
class IamRole(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamRole":
        return cls(
            aws_account_id=aws_account_id,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:iam::{self.aws_account_id}:role/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "IamRole":
        parts = arn.split(":")
        aws_account_id = parts[4]
        name = parts[5].split("/", 1)[1]
        return cls.make(aws_account_id, name)

    @property
    def is_service_role(self) -> bool:
        return self.name.startswith("service-role/")


@dataclasses.dataclass(frozen=True)
class IamPolicy(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        name: str,
    ) -> "IamPolicy":
        return cls(
            aws_account_id=aws_account_id,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:iam::{self.aws_account_id}:policy/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "IamPolicy":
        parts = arn.split(":")
        aws_account_id = parts[4]
        name = parts[5].split("/", 1)[1]
        return cls.make(aws_account_id, name)

    @property
    def is_service_role(self) -> bool:
        return self.name.startswith("service-role/")


@dataclasses.dataclass(frozen=True)
class Iam(Service):
    _AWS_SERVICE = "iamv2"

    # --- arn
    def get_user_group_arn(self, name: str) -> str:
        return IamUserGroup.make(self._account_id, name).arn

    def get_user_arn(self, name: str) -> str:
        return IamUser.make(self._account_id, name).arn

    def get_role_arn(self, name: str) -> str:
        return IamRole.make(self._account_id, name).arn

    def get_policy_arn(self, name: str) -> str:
        return IamPolicy.make(self._account_id, name).arn

    def _user_group_arn_to_name(self, arn: str) -> str:
        return IamUserGroup.from_arn(arn).name

    def _user_arn_to_name(self, arn: str) -> str:
        return IamUser.from_arn(arn).name

    def _role_arn_to_name(self, arn: str) -> str:
        return IamRole.from_arn(arn).name

    # --- dashboard
    @property
    def groups(self) -> str:
        return f"{self._service_root}/home?#/groups"

    @property
    def users(self) -> str:
        return f"{self._service_root}/home?#/users"

    @property
    def roles(self) -> str:
        return f"{self._service_root}/home?#/roles"

    @property
    def policies(self) -> str:
        return f"{self._service_root}/home?#/policies"

    def get_user_group(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._user_group_arn_to_name)
        return f"{self._service_root}/home#/groups/details/{name}?section=users"

    def get_user(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._user_arn_to_name)
        return f"{self._root_url}/iam/home#/users/{name}"

    def get_role(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._role_arn_to_name)
        return f"{self._service_root}/home#/roles/details/{name}?section=permissions"

    def get_policy(self, name_or_arn: str) -> str:
        arn = self._ensure_arn(name_or_arn, self.get_policy_arn)
        return f"{self._root_url}/iam/home#/policies/{arn}$jsonEditor"
