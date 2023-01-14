# -*- coding: utf-8 -*-

import pytest
from aws_console_url.tests import aws


def test():
    _ = aws.iam._account_id
    _ = aws.iam._region


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
