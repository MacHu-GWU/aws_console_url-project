# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service, Resource


@dataclasses.dataclass(frozen=True)
class LambdaFunction(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)
    version: T.Optional[int] = dataclasses.field(default=None)
    alias: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        version: T.Optional[int] = None,
        alias: T.Optional[str] = None,
    ) -> "LambdaFunction":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            version=version,
            alias=alias,
        )

    @property
    def is_regular(self) -> bool:
        return not bool(self.version or self.alias)

    @property
    def is_version(self) -> bool:
        return bool(self.version)

    @property
    def is_alias(self) -> bool:
        return bool(self.alias)

    @property
    def arn(self):
        arn = f"arn:aws:lambda:{self.aws_region}:{self.aws_account_id}:function:{self.name}"
        if self.version:
            return f"{arn}:{self.version}"
        if self.alias:
            return f"{arn}:{self.alias}"
        return arn

    @classmethod
    def from_arn(cls, arn: str) -> "LambdaFunction":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[6]
        if len(parts) == 8:
            last_part = parts[7]
            if last_part.isdigit():
                version = int(last_part)
                return cls(
                    aws_account_id=aws_account_id,
                    aws_region=aws_region,
                    name=name,
                    version=version,
                )
            else:
                alias = last_part
                return cls(
                    aws_account_id=aws_account_id,
                    aws_region=aws_region,
                    name=name,
                    alias=alias,
                )
        else:
            return cls(
                aws_account_id=aws_account_id,
                aws_region=aws_region,
                name=name,
            )


@dataclasses.dataclass(frozen=True)
class LambdaLayer(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)
    version: T.Optional[int] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
        version: int,
    ) -> "LambdaLayer":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            version=version,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:lambda:{self.aws_region}:{self.aws_account_id}:layer:{self.name}:{self.version}"

    @classmethod
    def from_arn(cls, arn: str) -> "LambdaLayer":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[6]
        version = parts[7]
        return cls.make(aws_account_id, aws_region, name, int(version))


@dataclasses.dataclass(frozen=True)
class AWSLambda(Service):
    _AWS_SERVICE = "lambda"

    # --- arn
    def get_function_arn(
        self,
        name: str,
        version: T.Optional[int] = None,
        alias: T.Optional[str] = None,
    ) -> str:
        return LambdaFunction.make(
            self._account_id, self._region, name, version, alias
        ).arn

    def get_layer_arn(
        self,
        name: str,
        version: int,
    ) -> str:
        return LambdaLayer.make(self._account_id, self._region, name, version).arn

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
        return f"{self._service_root}/home?region={self._region}#/functions?fo=and&o0=%3A&{query}"

    @property
    def layers(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/layers"

    # --- lambda function
    def _get_function_tab(self, name_or_arn: str, tab: str) -> str:
        if name_or_arn.startswith("arn:"):
            name = LambdaFunction.from_arn(name_or_arn).name
        else:
            name = name_or_arn
        return f"{self._service_root}/home?region={self._region}#/functions/{name}?tab={tab}"

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
            lbd_func = LambdaFunction.from_arn(arn)
            name = lbd_func.name
            version = lbd_func.version
        return f"{self._service_root}/home?region={self._region}#/functions/{name}/versions/{version}?tab=code"

    def get_function_alias(
        self,
        name: T.Optional[str] = None,
        alias: T.Optional[str] = None,
        arn: T.Optional[str] = None,
    ) -> str:
        if arn is not None:
            lbd_func = LambdaFunction.from_arn(arn)
            name = lbd_func.name
            alias = lbd_func.alias
        return f"{self._service_root}/home?region={self._region}#/functions/{name}/aliases/{alias}?tab=configure"

    # --- layer
    def get_layer(
        self,
        name: T.Optional[str] = None,
        version: T.Optional[int] = 1,
        arn: T.Optional[str] = None,
    ) -> str:
        if arn is not None:
            layer = LambdaLayer.from_arn(arn)
            name = layer.name
            version = layer.version
        return (
            f"{self._service_root}/home?region={self._region}#"
            f"/layers/{name}/versions/{version}?tab=versions"
        )
