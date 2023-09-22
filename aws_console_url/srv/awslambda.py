# -*- coding: utf-8 -*-

import typing as T
import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSLambda(Service):
    _AWS_SERVICE = "lambda"

    # --- arn
    def _get_function_obj(
        self,
        name_or_arn: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.LambdaFunction.from_arn(name_or_arn)
        else:
            return aws_arns.res.LambdaFunction.new(
                self._account_id,
                self._region,
                name_or_arn,
                version=version,
                alias=alias,
            )

    def get_function_arn(
        self,
        name: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ) -> str:
        return self._get_function_obj(name, version, alias).to_arn()

    def _get_layer_obj(
        self,
        name_or_arn: str,
        version: T.Optional[int] = None,
    ):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.LambdaLayer.from_arn(name_or_arn)
        else:
            if version is None:
                raise ValueError
            return aws_arns.res.LambdaLayer.new(
                self._account_id,
                self._region,
                name_or_arn,
                version=version,
            )

    def get_layer_arn(
        self,
        name: str,
        version: int,
    ) -> str:
        return self._get_layer_obj(name, version).to_arn()

    # --- dashboard
    @property
    def functions(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/functions"

    def filter_functions(
        self,
        facets: T.Union[str, T.List[str]],
    ) -> str:
        if isinstance(facets, str):
            facets = [facets]
        if len(facets) == 0:
            raise ValueError("facets must not be empty")
        query = "&".join([f"&o{i}=%3A&v{i}={token}" for i, token in enumerate(facets)])
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/functions?fo=and&o0=%3A&{query}"
        )

    @property
    def layers(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/layers"

    # --- lambda function
    def _get_function_tab(
        self,
        name_or_arn: str,
        tab: str,
    ) -> str:
        lbd_func = self._get_function_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={lbd_func.aws_region}#"
            f"/functions/{lbd_func.name}?tab={tab}"
        )

    def get_function(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "code")

    def get_function_code_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "code")

    def get_function_test_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "testing")

    def get_function_monitor_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "monitoring")

    def get_function_config_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "configure")

    def get_function_alias_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "aliases")

    def get_function_version_tab(self, name_or_arn: str) -> str:
        return self._get_function_tab(name_or_arn, "versions")

    def get_function_version(
        self,
        name_or_arn: str,
        version: T.Optional[int] = None,
    ) -> str:
        lbd_func = self._get_function_obj(name_or_arn, version=version)
        return (
            f"{self._service_root}/home?region={lbd_func.aws_region}#"
            f"/functions/{lbd_func.name}/versions/{lbd_func.version}?tab=code"
        )

    def get_function_alias(
        self,
        name_or_arn: str,
        alias: T.Optional[str] = None,
    ) -> str:
        lbd_func = self._get_function_obj(name_or_arn, alias=alias)
        return (
            f"{self._service_root}/home?region={lbd_func.aws_region}#"
            f"/functions/{lbd_func.name}/aliases/{lbd_func.alias}?tab=configure"
        )

    # --- layer
    def get_layer(
        self,
        name_or_arn: str,
        version: T.Optional[int] = None,
    ) -> str:
        lbd_layer = self._get_layer_obj(name_or_arn, version=version)
        return (
            f"{self._service_root}/home?region={lbd_layer.aws_region}#"
            f"/layers/{lbd_layer.name}/versions/{lbd_layer.version}?tab=versions"
        )
