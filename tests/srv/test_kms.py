# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    key_alias = f"{prefix_snake}_test"
    # key_arn = console.kms.get_kms_key_arn(key_alias)
    # --- arn

    # --- console
    print("-" * 80)
    print(console.kms.aws_managed_keys)
    print(console.kms.customer_managed_keys)

    print("-" * 80)
    # print(console.kms.get_kms_key(key_alias))
    # print(console.kms.get_kms_key(key_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.kms", preview=False)
