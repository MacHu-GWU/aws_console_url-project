# -*- coding: utf-8 -*-

from aws_console_url.utils import (
    encode_arn_in_url,
)


def test_encode_arn_in_url():
    arn = "arn:aws:dynamodb:us-east-1:111122223333:table/my-table"
    res = encode_arn_in_url(arn)
    assert res == "arn%3Aaws%3Adynamodb%3Aus-east-1%3A111122223333%3Atable%2Fmy-table"


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.utils", preview=False)
