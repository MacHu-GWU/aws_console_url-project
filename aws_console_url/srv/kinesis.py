# -*- coding: utf-8 -*-

import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSKinesis(Service):
    _AWS_SERVICE = "kinesis"

    # --- arn
    def _get_kinesis_stream_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.KinesisStream.from_arn(name_or_arn)
        else:
            return aws_arns.res.KinesisStream.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_kinesis_stream_arn(self, name: str) -> str:
        return self._get_kinesis_stream_obj(name).to_arn()

    # --- dashboard
    @property
    def data_streams(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/streams/list"

    # --- resource
    def get_stream(self, name_or_arn: str) -> str:
        obj = self._get_kinesis_stream_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/streams/details/{obj.resource_id}/monitoring"
        )
