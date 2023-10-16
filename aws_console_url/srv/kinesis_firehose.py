# -*- coding: utf-8 -*-

import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSKinesisFirehose(Service):
    _AWS_SERVICE = "firehose"

    # --- arn
    def _get_kinesis_firehose_delivery_stream_obj(self, name_or_arn: str):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.KinesisFirehoseDeliveryStream.from_arn(name_or_arn)
        else:
            return aws_arns.res.KinesisFirehoseDeliveryStream.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def get_kinesis_firehose_delivery_stream_arn(self, name: str) -> str:
        return self._get_kinesis_firehose_delivery_stream_obj(name).to_arn()

    # --- dashboard
    @property
    def delivery_streams(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/streams"

    # --- resource
    def get_kinesis_firehose_delivery_stream(self, name_or_arn: str) -> str:
        obj = self._get_kinesis_firehose_delivery_stream_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/details/{obj.resource_id}/monitoring"
        )
