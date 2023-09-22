# -*- coding: utf-8 -*-

import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


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
class CloudWatch(Service):
    _AWS_SERVICE = "cloudwatch"

    # --- arn
    def get_log_group_arn(
        self,
        name: str,
    ) -> str:
        return aws_arns.res.CloudWatchLogGroup.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

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
