# -*- coding: utf-8 -*-

from aws_console_url.tests import console, resource


def test():
    func = "test"
    lbd_func_arn = resource.LambdaFunctionArn.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
    )
    assert lbd_func_arn.is_regular is True
    assert lbd_func_arn.is_version is False
    assert lbd_func_arn.is_alias is False

    lbd_func_arn1 = resource.LambdaFunctionArn.from_arn(lbd_func_arn.arn)
    assert lbd_func_arn == lbd_func_arn1

    lbd_func_arn = resource.LambdaFunctionArn.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
        version=1,
    )
    assert lbd_func_arn.is_regular is False
    assert lbd_func_arn.is_version is True
    assert lbd_func_arn.is_alias is False
    assert lbd_func_arn.arn == "arn:aws:lambda:us-east-1:669508176277:function:test:1"

    lbd_func_arn = resource.LambdaFunctionArn.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
        alias="v1",
    )
    assert lbd_func_arn.is_regular is False
    assert lbd_func_arn.is_version is False
    assert lbd_func_arn.is_alias is True
    assert lbd_func_arn.arn == "arn:aws:lambda:us-east-1:669508176277:function:test:v1"

    print(console.awslambda.functions)
    print(console.awslambda.layers)
    print(console.awslambda.filter_functions(func))
    print(console.awslambda.get_function(func))
    print(console.awslambda.get_function_code_tab(func))
    print(console.awslambda.get_function_test_tab(func))
    print(console.awslambda.get_function_monitor_tab(func))
    print(console.awslambda.get_function_config_tab(func))
    print(console.awslambda.get_function_alias_tab(func))
    print(console.awslambda.get_function_version_tab(func))
    print(console.awslambda.get_function_version(func, 1))
    print(console.awslambda.get_function_alias(func, "v1"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.awslambda", preview=False)
