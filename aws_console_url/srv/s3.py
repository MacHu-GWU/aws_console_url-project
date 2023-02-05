# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


def split_s3_uri(
    s3_uri: str,
) -> T.Tuple[str, str]:
    """
    Split AWS S3 URI, returns bucket and key.

    :param s3_uri: example, ``"s3://my-bucket/my-folder/data.json"``
    """
    parts = s3_uri.split("/")
    bucket = parts[2]
    key = "/".join(parts[3:])
    return bucket, key


@dataclasses.dataclass(frozen=True)
class S3(Service):
    _AWS_SERVICE = "s3"

    # --- dashboard
    @property
    def buckets(self) -> str:
        return f"https://console.aws.amazon.com/s3/buckets"

    def get_console_url(
        self,
        bucket: T.Optional[str] = None,
        prefix: T.Optional[str] = None,
        s3_uri: T.Optional[str] = None,
    ):
        """
        Return an AWS Console url that you can use to open it in your browser.

        :param bucket: example, ``"my-bucket"``
        :param prefix: example, ``"my-folder/data.json"``
        :param s3_uri: example, ``"s3://my-bucket/my-folder/data.json"``
        """
        if s3_uri is None:
            if bucket is None:
                raise ValueError
            if prefix is None:
                prefix = ""
        else:
            if (bucket is not None) or (prefix is not None):
                raise ValueError
            bucket, prefix = split_s3_uri(s3_uri)

        if len(prefix) == 0:
            return f"{self._service_root}/buckets/{bucket}?region={self._region}&tab=objects"
        elif prefix.endswith("/"):
            s3_type = "buckets"
        else:
            s3_type = "object"

        return f"{self._service_root}/{s3_type}/{bucket}?prefix={prefix}"

    def get_s3_select_console_url(
        self,
        bucket: T.Optional[str] = None,
        key: T.Optional[str] = None,
        s3_uri: T.Optional[str] = None,
    ):
        """
        Return an AWS Console url that you can use to open it in your browser.

        :param bucket: example, ``"my-bucket"``
        :param key: example, ``"my-folder/data.json"``
        :param s3_uri: example, ``"s3://my-bucket/my-folder/data.json"``
        """
        if s3_uri is None:
            if not ((bucket is not None) and (key is not None)):
                raise ValueError
        else:
            if (bucket is not None) or (key is not None):
                raise ValueError
            bucket, key = split_s3_uri(s3_uri)

        return f"{self._service_root}/buckets/{bucket}/object/select?region={self._region}&prefix={key}"
