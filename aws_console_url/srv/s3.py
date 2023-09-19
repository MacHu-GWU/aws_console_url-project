# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


def split_s3_uri(
    s3_uri: str,
) -> T.Tuple[str, str]:
    """
    Split AWS S3 URI, returns bucket and key. If the uri is a bucket,
    then the key is "".

    :param s3_uri: example, ``s3://my-bucket/my-folder/data.json``
    """
    parts = s3_uri.split("/")
    bucket = parts[2]
    key = "/".join(parts[3:])
    return bucket, key


def split_s3_arn(
    s3_arn: str,
) -> T.Tuple[str, str]:
    """
    Split AWS S3 ARN, returns bucket and key. If the arn is a bucket,
    then the key is "".

    :param s3_arn: example, ``arn:aws:s3:::my-bucket/my-folder/data.json``
    """
    parts = s3_arn.split(":", 5)
    return split_s3_uri(f"s3://{parts[5]}")


def split_s3_path(
    s3_path: str,
) -> T.Tuple[str, str]:
    """
    Split AWS S3 path, returns bucket and key. If the path is a bucket,
    then the key is "".

    :param s3_path: example, ``my-bucket/file.txt``, ``/my-bucket/file.txt``
    """
    if s3_path.startswith("/"):
        s3_path = s3_path[1:]
    parts = s3_path.split("/")
    bucket = parts[0]
    key = "/".join(parts[1:])
    return bucket, key


def extract_bucket_key(s3_uri_or_arn_or_path: str) -> T.Tuple[str, str]:
    if s3_uri_or_arn_or_path.startswith("s3:"):
        return split_s3_uri(s3_uri_or_arn_or_path)
    elif s3_uri_or_arn_or_path.startswith("arn:"):
        return split_s3_arn(s3_uri_or_arn_or_path)
    else:
        return split_s3_path(s3_uri_or_arn_or_path)


def normalize_args(
    bucket: T.Optional[str] = None,
    prefix: T.Optional[str] = None,
    uri_liked: T.Optional[str] = None,
):
    """
    Return a normalized bucket and prefix in string.

    :param bucket: example, ``my-bucket``
    :param prefix: example, ``my-folder/data.json``
    :param uri_liked: could be an S3 uri like ``s3://my-bucket/my-folder/data.json``
        could be an S3 arn like ``arn:aws:s3:::my-bucket/my-folder/data.json``
        could be an S3 path like ``my-bucket/my-folder/data.json``
    """
    if uri_liked is None:
        if bucket is None:
            raise ValueError
        if prefix is None:
            prefix = ""
    else:
        if (bucket is not None) or (prefix is not None):
            raise ValueError
        bucket, prefix = extract_bucket_key(uri_liked)
    return bucket, prefix


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
        uri_liked: T.Optional[str] = None,
    ):
        """
        Return an AWS Console url that you can use to open it in your browser.

        :param bucket: example, ``my-bucket``
        :param prefix: example, ``my-folder/data.json``
        :param uri_liked: could be an S3 uri like ``s3://my-bucket/my-folder/data.json``
            could be an S3 arn like ``arn:aws:s3:::my-bucket/my-folder/data.json``
            could be an S3 path like ``my-bucket/my-folder/data.json``
        """
        bucket, prefix = normalize_args(bucket, prefix, uri_liked)

        if len(prefix) == 0:
            return f"{self._service_root}/buckets/{bucket}?region={self._region}&tab=objects"
        elif prefix.endswith("/"):
            s3_type = "buckets"
        else:
            s3_type = "object"
        return f"{self._service_root}/{s3_type}/{bucket}?region={self._region}&prefix={prefix}"

    def get_s3_select_console_url(
        self,
        bucket: T.Optional[str] = None,
        key: T.Optional[str] = None,
        uri_liked: T.Optional[str] = None,
    ):
        """
        Return an AWS Console url that you can use to open it in your browser.

        :param bucket: example, ``"my-bucket"``
        :param key: example, ``"my-folder/data.json"``
        :param uri_liked: could be an S3 uri like ``s3://my-bucket/my-folder/data.json``
            could be an S3 arn like ``arn:aws:s3:::my-bucket/my-folder/data.json``
            could be an S3 path like ``my-bucket/my-folder/data.json``
        """
        bucket, prefix = normalize_args(bucket, key, uri_liked)
        if len(prefix) == 0:
            raise ValueError("key should not be empty")
        if prefix.endswith("/"):
            raise ValueError("key should not end with '/'")
        return f"{self._service_root}/buckets/{bucket}/object/select?region={self._region}&prefix={prefix}"
