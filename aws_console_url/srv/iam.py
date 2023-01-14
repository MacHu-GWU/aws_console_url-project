# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class Iam(Builder):
    _AWS_SERVICE = "iamv2"

    # --- ARN
    def to_group_arn(self, name: str) -> str:
        return f"arn:aws:iam::{self._account_id}:group/{name}"

    def to_group_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    def to_user_arn(self, name: str) -> str:
        return f"arn:aws:iam::{self._account_id}:user/{name}"

    def to_user_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    def to_role_arn(self, name: str) -> str:
        return f"arn:aws:iam::{self._account_id}:role/{name}"

    def to_role_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    def to_policy_arn(self, name: str, is_service_role: bool = False) -> str:
        service_role = "service-role/" if is_service_role else ""
        return f"arn:aws:iam::{self._account_id}:policy/{service_role}{name}"

    def to_policy_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    # --- Console
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

    def get_group(self, name_or_arn: str) -> str:
        name = (
            self.to_group_name(name_or_arn)
            if name_or_arn.startswith("arn:")
            else name_or_arn
        )
        return f"{self._service_root}/home#/groups/details/{name}?section=users"

    def get_user(self, name_or_arn: str) -> str:
        name = (
            self.to_user_name(name_or_arn)
            if name_or_arn.startswith("arn:")
            else name_or_arn
        )
        return f"{self._root_url}/iam/home#/users/{name}"

    def get_role(self, name_or_arn: str) -> str:
        name = (
            self.to_role_name(name_or_arn)
            if name_or_arn.startswith("arn:")
            else name_or_arn
        )
        return f"{self._service_root}/home#/roles/details/{name}?section=permissions"

    "https://us-east-1.console.aws.amazon.com/iam/home#/policies/arn:aws:iam::669508176277:policy/service-role/AmazonKendra-Sanhe-dev-2-experience$jsonEditor"

    def get_policy(self, name_or_arn: str, is_service_role: bool = False) -> str:
        arn = (
            name_or_arn
            if name_or_arn.startswith("arn:")
            else self.to_policy_arn(name_or_arn, is_service_role)
        )
        return f"{self._root_url}/iam/home#/policies/{arn}$jsonEditor"
