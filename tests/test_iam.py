# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    print(aws.iam.groups)
    print(aws.iam.users)
    print(aws.iam.roles)
    print(aws.iam.policies)
    print(aws.iam.get_group("Admin"))
    print(aws.iam.get_user("sanhe"))
    print(aws.iam.get_role("Admin"))
    print(aws.iam.get_policy("ge-dev"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.iam", preview=False)
