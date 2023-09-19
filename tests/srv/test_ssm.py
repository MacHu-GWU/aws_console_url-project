# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    param_name1 = f"{prefix_snake}_1"
    param_name2 = f"/{prefix_snake}_2"
    param_arn1 = f"arn:aws:ssm:{console.aws_region}:{console.aws_account_id}:parameter/{param_name1}"
    param_arn2 = f"arn:aws:ssm:{console.aws_region}:{console.aws_account_id}:parameter{param_name2}"
    # --- resource
    assert resource.SSMParameter.from_arn(param_arn1).arn == param_arn1
    assert resource.SSMParameter.from_arn(param_arn2).arn == param_arn2

    # --- console
    print(console.ssm.parameters)

    print(console.ssm.filter_parameters(param_name1))
    print(console.ssm.get_parameter(param_name1))
    print(console.ssm.get_parameter(param_arn1))
    assert console.ssm.get_parameter_arn(param_name1).endswith(param_name1)

    print(console.ssm.filter_parameters(param_name2))
    print(console.ssm.get_parameter(param_name2))
    print(console.ssm.get_parameter(param_arn2))
    assert console.ssm.get_parameter_arn(param_name2).endswith(param_name2)


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ssm", preview=False)
