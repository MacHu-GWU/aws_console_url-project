# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    name = f"{prefix_snake}_test"
    inline_policy_name = f"{name}_inline_policy"

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

    print(console.iam.create_group)
    print(console.iam.create_user)
    print(console.iam.create_role)
    print(console.iam.create_policy)

    print("-" * 80)
    print(console.iam.get_user_group(name))
    print(console.iam.get_user(name))
    print(console.iam.get_role(name))
    print(console.iam.get_policy(name))
    print(console.iam.get_user_inline_policy(name, inline_policy_name))
    print(console.iam.get_role_inline_policy(name, inline_policy_name))

    print("-" * 80)
    print(console.iam.get_user_group(f"arn:aws:iam::{console.aws_account_id}:group/{name}"))
    print(console.iam.get_user(f"arn:aws:iam::{console.aws_account_id}:user/{name}"))
    print(console.iam.get_role(f"arn:aws:iam::{console.aws_account_id}:role/{name}"))
    print(console.iam.get_policy(f"arn:aws:iam::{console.aws_account_id}:policy/{name}"))
    print(console.iam.get_user_inline_policy(f"arn:aws:iam::{console.aws_account_id}:user/{name}", inline_policy_name))
    print(console.iam.get_role_inline_policy(f"arn:aws:iam::{console.aws_account_id}:role/{name}", inline_policy_name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.iam", preview=False)
