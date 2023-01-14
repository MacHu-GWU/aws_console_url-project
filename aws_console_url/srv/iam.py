# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class Iam(Builder):
    _AWS_SERVICE = "iamv2"

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
        return f"{self._root_url}/iam/home#/users/{name}"

    def get_role(self, name: str) -> str:
        return f"{self._service_root}/home#/roles/details/{name}?section=permissions"

    def get_policy(self, name: str) -> str:
        return f"{self._root_url}/iam/home#/policies/arn:aws:iam::{self._account_id}:policy/{name}$jsonEditor"
