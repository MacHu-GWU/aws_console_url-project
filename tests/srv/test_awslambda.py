# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    func = "test"
    print(aws.awslambda.functions)
    print(aws.awslambda.layers)
    print(aws.awslambda.filter_functions(func))
    print(aws.awslambda.get_function(func))
    print(aws.awslambda.get_function_code_tab(func))
    print(aws.awslambda.get_function_test_tab(func))
    print(aws.awslambda.get_function_monitor_tab(func))
    print(aws.awslambda.get_function_config_tab(func))
    print(aws.awslambda.get_function_alias_tab(func))
    print(aws.awslambda.get_function_version_tab(func))
    print(aws.awslambda.get_function_version(func, 1))
    print(aws.awslambda.get_function_alias(func, "v1"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.awslambda", preview=False)
