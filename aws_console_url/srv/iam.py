# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass
class Iam(Builder):
    aws_service: str = dataclasses.field(default="iamv2")

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

    def get_group(self, name: str) -> str:
        return f"{self._service_root}/home#/groups/details/{name}?section=users"

    def get_user(self, name: str) -> str:
        return f"{self._sub_domain}/iam/home#/users/{name}"

    def get_role(self, name: str) -> str:
        return f"{self._service_root}/home#/roles/details/{name}?section=permissions"

    def get_policy(self, name: str) -> str:
        return f"{self._sub_domain}/iam/home#/policies/arn:aws:iam::{self.aws_account_id}:policy/{name}$jsonEditor"
