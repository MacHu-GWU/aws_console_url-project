# -*- coding: utf-8 -*-

import typing as T
import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSKinesisVideo(Service):
    _AWS_SERVICE = "kinesisvideo"

    # --- arn
    def _get_kinesis_video_stream_obj(self, name_or_arn: str, creation_time: T.Optional[str]=None):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.KinesisVideoStream.from_arn(name_or_arn)
        else:
            return aws_arns.res.KinesisVideoStream.new(
                self._account_id,
                self._region,
                stream_name=name_or_arn,
                creation_time=creation_time,
            )

    def get_kinesis_video_stream_arn(self, name: str, creation_time: str) -> str:
        return self._get_kinesis_video_stream_obj(name, creation_time).to_arn()

    def _get_kinesis_video_channel_obj(self, name_or_arn: str, creation_time: T.Optional[str]=None):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.KinesisVideoChannel.from_arn(name_or_arn)
        else:
            return aws_arns.res.KinesisVideoChannel.new(
                self._account_id,
                self._region,
                channel_name=name_or_arn,
                creation_time=creation_time,
            )

    def get_kinesis_video_channel_arn(self, name: str, creation_time: str) -> str:
        return self._get_kinesis_video_channel_obj(name, creation_time).to_arn()

    # --- dashboard
    @property
    def streams(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/streams"

    @property
    def channels(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/signalingChannels"

    # --- resource
    def get_stream(self, name_or_arn: str) -> str:
        obj = self._get_kinesis_video_stream_obj(name_or_arn, creation_time="")
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"streams/streamName/{obj.stream_name}"
        )

    def get_channel(self, name_or_arn: str) -> str:
        obj = self._get_kinesis_video_channel_obj(name_or_arn, creation_time="")
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"signalingChannels/signalingChannelName/{obj.channel_name}"
        )
