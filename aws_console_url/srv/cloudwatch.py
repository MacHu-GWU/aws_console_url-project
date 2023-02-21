# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service, Resource


_url_escapes = [
    ("$", "$2524"),
    ("/", "$252F"),
    ("[", "$255B"),
    ("]", "$255D"),
]

_pattern_escapes = [
    ('"', "$2522"),
]

def encode_url(name: str) -> str:
    for before, after in _url_escapes:
        name = name.replace(before, after)
    return name

def encode_pattern(pattern: str) -> str:
    for before, after in _pattern_escapes:
        pattern = pattern.replace(before, after)
    return pattern

@dataclasses.dataclass(frozen=True)
class CloudwatchLogGroup(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ) -> "CloudwatchLogGroup":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self):
        return f"arn:aws:logs:{self.aws_region}:{self.aws_account_id}:log-group:{self.name}:*"

    @classmethod
    def from_arn(cls, arn: str) -> "CloudwatchLogGroup":
        parts = arn.split(":")
        return cls(
            aws_account_id=parts[4],
            aws_region=parts[3],
            name=parts[6],
        )


@dataclasses.dataclass(frozen=True)
class CloudwatchLogStream(Resource):
    group_name: T.Optional[str] = dataclasses.field(default=None)
    stream_name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        group_name: str,
        stream_name: str,
    ) -> "CloudwatchLogStream":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            group_name=group_name,
            stream_name=stream_name,
        )


@dataclasses.dataclass(frozen=True)
class CloudWatch(Service):
    _AWS_SERVICE = "cloudwatch"

    # --- arn
    def get_log_group_arn(
        self,
        name: str,
    ) -> str:
        return CloudwatchLogGroup.make(self._account_id, self._region, name).arn

    # --- dashboard
    @property
    def log_groups(self) -> str:
        return f"{self._service_root}/home?region={self._region}#logsV2:log-groups"

    def filter_log_groups(self, pattern: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups$3FlogGroupNameFilter$3D{pattern}"
        )

    def filter_log_streams(self, group_name: str, pattern: str) -> str:
        group_name = encode_url(group_name)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups/log-group/{group_name}$3FlogStreamNameFilter$3D{pattern}"
        )

    def filter_log_event(
        self,
        group_name: str,
        stream_name: str,
        pattern: str,
    ) -> str:
        group_name = encode_url(group_name)
        stream_name = encode_url(stream_name)
        pattern = encode_pattern(pattern)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups/log-group/{group_name}"
            f"/log-events/{stream_name}$3FfilterPattern$3D{pattern}"
        )

    def filter_log_event_by_lambda_request_id(
        self,
        func_name: str,
        request_id: str,
        lookback_seconds: int = 24 * 3600,
    ) -> str:
        group_name = encode_url(f"/aws/lambda/{func_name}")
        pattern = encode_pattern('"' + request_id + '"')
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups/log-group/{group_name}"
            f"/log-events$3FfilterPattern$3D{pattern}$26start$3D-{lookback_seconds * 1000}"
        )

    # --- lambda function
    def _get_log_group_tab(self, name: str, tab: str) -> str:
        name = encode_url(name)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups/log-group/{name}{tab}"
        )

    def get_log_group(self, name: str) -> str:
        return self._get_log_group_tab(name, "")

    def get_log_group_log_streams_tab(self, name: str) -> str:
        return self._get_log_group_tab(name, "")

    def get_log_stream(self, group_name: str, stream_name: str) -> str:
        group_name = encode_url(group_name)
        stream_name = encode_url(stream_name)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#logsV2:log-groups/log-group/{group_name}/log-events/{stream_name}"
        )
