# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    name = f"{prefix_snake}_test"

    # --- resource
    assert resource.IamRole.make(console.aws_account_id, name).is_service_role is False
    assert (
        resource.IamPolicy.make(console.aws_account_id, name).is_service_role is False
    )

    iam_policy = resource.IamPolicy.from_arn(
        resource.IamPolicy.make(console.aws_account_id, name).arn
    )
    assert iam_policy.name == name

    # --- console
    print("-" * 80)
    print(console.iam.get_user_group_arn(name))
    print(console.iam.get_user_arn(name))
    print(console.iam.get_role_arn(name))
    print(console.iam.get_policy_arn(name))

    print("-" * 80)
    print(console.iam.groups)
    print(console.iam.users)
    print(console.iam.roles)
    print(console.iam.policies)

    print("-" * 80)
    print(console.iam.get_user_group(name))
    print(console.iam.get_user(name))
    print(console.iam.get_role(name))
    print(console.iam.get_policy(name))

    print("-" * 80)
    print(console.iam.get_user_group(f"arn:aws:iam::{console.aws_account_id}:group/{name}"))
    print(console.iam.get_user(f"arn:aws:iam::{console.aws_account_id}:user/{name}"))
    print(console.iam.get_role(f"arn:aws:iam::{console.aws_account_id}:role/{name}"))
    print(console.iam.get_policy(f"arn:aws:iam::{console.aws_account_id}:policy/{name}"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.iam", preview=False)
