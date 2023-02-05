# -*- coding: utf-8 -*-
import pytest

from aws_console_url.tests import resource, console


def test():
    print("")

    bucket = "669508176277-us-east-1-artifacts"
    prefix = "cloudformation/upload/"
    key = "cloudformation/upload/10f3db7bcfa62c69e5a71fef595fac84.json"

    # --- resource

    # --- console
    print(console.s3.buckets)
    print(console.s3.get_console_url(bucket=bucket))
    print(console.s3.get_console_url(bucket=bucket, prefix=""))
    print(console.s3.get_console_url(s3_uri=f"s3://{bucket}/"))
    print(console.s3.get_console_url(bucket=bucket, prefix=prefix))
    print(console.s3.get_console_url(s3_uri=f"s3://{bucket}/{prefix}"))
    print(console.s3.get_console_url(bucket=bucket, prefix=key))
    print(console.s3.get_console_url(s3_uri=f"s3://{bucket}/{key}"))

    print(console.s3.get_s3_select_console_url(bucket=bucket, key=key))
    print(console.s3.get_s3_select_console_url(s3_uri=f"s3://{bucket}/{key}"))

    with pytest.raises(Exception):
        print(console.s3.get_console_url())

    with pytest.raises(Exception):
        print(console.s3.get_console_url(bucket=bucket, s3_uri=f"s3://{bucket}/{prefix}"))

    with pytest.raises(Exception):
        print(console.s3.get_s3_select_console_url())

    with pytest.raises(Exception):
        print(console.s3.get_s3_select_console_url(bucket=bucket))

    with pytest.raises(Exception):
        print(console.s3.get_s3_select_console_url(bucket=bucket, s3_uri=f"s3://{bucket}/{prefix}"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.s3", preview=False)
