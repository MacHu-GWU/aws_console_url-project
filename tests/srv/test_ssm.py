# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    param_name = "test_aws_console_url"
    param_name1 = "/test_aws_console_url"

    # --- resource

    # --- console
    print(console.ssm.parameters)

    print(console.ssm.filter_parameters(param_name))
    print(console.ssm.get_parameter(param_name))
    assert console.ssm.get_parameter_arn(param_name).endswith("parameter/test_aws_console_url")

    print(console.ssm.filter_parameters(param_name1))
    print(console.ssm.get_parameter(param_name1))
    assert console.ssm.get_parameter_arn(param_name1).endswith("parameter/test_aws_console_url")



if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ssm", preview=False)
