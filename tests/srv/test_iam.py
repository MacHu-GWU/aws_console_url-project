# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    print(console.iam.groups)
    print(console.iam.users)
    print(console.iam.roles)
    print(console.iam.policies)

    print(console.iam.get_group("Admin"))
    print(console.iam.get_user("sanhe"))
    print(console.iam.get_role("Admin"))
    print(console.iam.get_policy("test"))

    print(console.iam.get_group("arn:aws:iam::669508176277:group/Admin"))
    print(console.iam.get_user("arn:aws:iam::669508176277:user/sanhe"))
    print(console.iam.get_role("arn:aws:iam::669508176277:role/Admin"))
    print(console.iam.get_policy("arn:aws:iam::669508176277:policy/test"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.iam", preview=False)
