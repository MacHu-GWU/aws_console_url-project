# -*- coding: utf-8 -*-

import pytest

from aws_console_url.tests import console, prefix_slug


def test():
    bucket = f"{prefix_slug}-test"
    prefix = "upload/"
    key = "upload/__init__.py"

    # --- resource

    # --- console
    print(console.s3.buckets)
    print(console.s3.get_console_url(bucket=bucket))
    print(console.s3.get_console_url(bucket=bucket, prefix=""))
    print(console.s3.get_console_url(uri_liked=f"s3://{bucket}/"))
    print(console.s3.get_console_url(uri_liked=f"arn:aws:s3:::{bucket}"))
    print(console.s3.get_console_url(uri_liked=f"{bucket}"))
    print(console.s3.get_console_url(uri_liked=f"/{bucket}"))
    print(console.s3.get_console_url(uri_liked=f"/{bucket}/"))

    print(console.s3.get_console_url(bucket=bucket, prefix=prefix))
    print(console.s3.get_console_url(uri_liked=f"s3://{bucket}/{prefix}"))
    print(console.s3.get_console_url(uri_liked=f"arn:aws:s3:::{bucket}/{prefix}"))
    print(console.s3.get_console_url(uri_liked=f"{bucket}/{prefix}"))
    print(console.s3.get_console_url(uri_liked=f"/{bucket}/{prefix}"))

    print(console.s3.get_console_url(bucket=bucket, prefix=key))
    print(console.s3.get_console_url(uri_liked=f"s3://{bucket}/{key}"))
    print(console.s3.get_console_url(uri_liked=f"arn:aws:s3:::{bucket}/{key}"))
    print(console.s3.get_console_url(uri_liked=f"{bucket}/{key}"))
    print(console.s3.get_console_url(uri_liked=f"/{bucket}/{key}"))

    print(console.s3.get_s3_select_console_url(bucket=bucket, key=key))
    print(console.s3.get_s3_select_console_url(uri_liked=f"s3://{bucket}/{key}"))
    print(
        console.s3.get_s3_select_console_url(uri_liked=f"arn:aws:s3:::{bucket}/{key}")
    )

    with pytest.raises(Exception):
        print(console.s3.get_console_url())

    with pytest.raises(Exception):
        print(
            console.s3.get_console_url(bucket=bucket, s3_uri=f"s3://{bucket}/{prefix}")
        )

    with pytest.raises(Exception):
        print(console.s3.get_s3_select_console_url())

    with pytest.raises(Exception):
        print(console.s3.get_s3_select_console_url(bucket=bucket))

    with pytest.raises(Exception):
        print(
            console.s3.get_s3_select_console_url(
                bucket=bucket, s3_uri=f"s3://{bucket}/{prefix}"
            )
        )


#

if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.s3", preview=False)
