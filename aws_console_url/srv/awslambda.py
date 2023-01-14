# -*- coding: utf-8 -*-

import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class AWSLambda(Builder):
    _AWS_SERVICE = "lambda"

    @property
    def functions(self) -> str:
        return f"{self._service_root}/home?#/functions"

    @property
    def layers(self) -> str:
        return f"{self._service_root}/home?#/layers"

    def filter_functions(self, name: str) -> str:
        return f"{self._service_root}/home?#/functions?fo=and&o0=%3A&v0={name}"

    def _function_tab(self, name: str, tab: str) -> str:
        return f"{self._service_root}/home?#/functions/{name}?tab={tab}"

    def get_function(self, name: str) -> str:
        return self._function_tab(name, "code")

    def get_function_code_tab(self, name: str) -> str:
        return self._function_tab(name, "code")

    def get_function_test_tab(self, name: str) -> str:
        return self._function_tab(name, "testing")

    def get_function_monitor_tab(self, name: str) -> str:
        return self._function_tab(name, "monitoring")

    def get_function_config_tab(self, name: str) -> str:
        return self._function_tab(name, "configure")

    def get_function_alias_tab(self, name: str) -> str:
        return self._function_tab(name, "aliases")

    def get_function_version_tab(self, name: str) -> str:
        return self._function_tab(name, "versions")

    def get_function_version(self, name: str, version: int) -> str:
        return (
            f"{self._service_root}/home?#/functions/{name}/versions/{version}?tab=code"
        )

    def get_function_alias(self, name: str, alias: str) -> str:
        return (
            f"{self._service_root}/home?#/functions/{name}/aliases/{alias}?tab=configure"
        )
