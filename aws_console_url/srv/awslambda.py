# -*- coding: utf-8 -*-

import typing as T
import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSLambda(Service):
    _AWS_SERVICE = "lambda"

    # --- arn
    def get_function_arn(
        self,
        name: str,
        version: T.Optional[T.Union[str, int]] = None,
        alias: T.Optional[str] = None,
    ) -> str:
        return aws_arns.res.LambdaFunction.new(
            self._account_id,
            self._region,
            name,
            version=version,
            alias=alias,
        ).to_arn()

    def get_layer_arn(
        self,
        name: str,
        version: int,
    ) -> str:
        return aws_arns.res.LambdaLayer.new(
            self._account_id,
            self._region,
            name,
            version,
        ).to_arn()

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
    def _get_function_tab(self, name_or_arn: str, tab: str) -> str:
        if name_or_arn.startswith("arn:"):
            name = aws_arns.res.LambdaFunction.from_arn(name_or_arn).name
        else:
            name = name_or_arn
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/functions/{name}?tab={tab}"
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
        name: T.Optional[str] = None,
        version: T.Optional[int] = None,
        arn: T.Optional[str] = None,
    ) -> str:
        if arn is not None:
            lbd_func = aws_arns.res.LambdaFunction.from_arn(arn)
            name = lbd_func.name
            version = lbd_func.version
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/functions/{name}/versions/{version}?tab=code"
        )

    def get_function_alias(
        self,
        name: T.Optional[str] = None,
        alias: T.Optional[str] = None,
        arn: T.Optional[str] = None,
    ) -> str:
        if arn is not None:
            lbd_func = aws_arns.res.LambdaFunction.from_arn(arn)
            name = lbd_func.name
            alias = lbd_func.alias
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/functions/{name}/aliases/{alias}?tab=configure"
        )

    # --- layer
    def get_layer(
        self,
        name: T.Optional[str] = None,
        version: T.Optional[int] = 1,
        arn: T.Optional[str] = None,
    ) -> str:
        if arn is not None:
            layer = aws_arns.res.LambdaLayer.from_arn(arn)
            name = layer.name
            version = layer.version
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/layers/{name}/versions/{version}?tab=versions"
        )
