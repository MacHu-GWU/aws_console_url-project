# -*- coding: utf-8 -*-

from aws_console_url.tests import console, resource, prefix_snake


def test():
    func = f"{prefix_snake}_test"
    func_arn = (
        f"arn:aws:lambda:{console.aws_region}:{console.aws_account_id}:function:{func}"
    )
    version = "1"
    alias = "LIVE"
    version_arn = f"arn:aws:lambda:{console.aws_region}:{console.aws_account_id}:function:{func}:{version}"
    alias_arn = f"arn:aws:lambda:{console.aws_region}:{console.aws_account_id}:function:{func}:{alias}"
    layer = f"{prefix_snake}_test"
    layer_arn = (
        f"arn:aws:lambda:{console.aws_region}:{console.aws_account_id}:layer:{layer}:1"
    )

    # --- arn
    lbd_func_arn = resource.LambdaFunction.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
    )
    assert lbd_func_arn.is_regular is True
    assert lbd_func_arn.is_version is False
    assert lbd_func_arn.is_alias is False

    lbd_func_arn1 = resource.LambdaFunction.from_arn(lbd_func_arn.arn)
    assert lbd_func_arn == lbd_func_arn1

    lbd_func_arn = resource.LambdaFunction.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
        version=1,
    )
    assert lbd_func_arn.is_regular is False
    assert lbd_func_arn.is_version is True
    assert lbd_func_arn.is_alias is False
    assert lbd_func_arn.arn == version_arn

    lbd_func_arn1 = resource.LambdaFunction.from_arn(lbd_func_arn.arn)
    assert lbd_func_arn == lbd_func_arn1

    lbd_func_arn = resource.LambdaFunction.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=func,
        alias="LIVE",
    )
    assert lbd_func_arn.is_regular is False
    assert lbd_func_arn.is_version is False
    assert lbd_func_arn.is_alias is True
    assert lbd_func_arn.arn == alias_arn

    lbd_func_arn1 = resource.LambdaFunction.from_arn(lbd_func_arn.arn)
    assert lbd_func_arn == lbd_func_arn1

    lbd_layer = resource.LambdaLayer.from_arn(
        resource.LambdaLayer.make(
            aws_account_id=console.aws_account_id,
            aws_region=console.aws_region,
            name=layer,
            version=1,
        ).arn
    )
    assert lbd_layer.name == layer
    lbd_layer1 = resource.LambdaLayer.from_arn(lbd_layer.arn)
    assert lbd_layer == lbd_layer1

    # --- console
    print(console.awslambda.functions)
    print(console.awslambda.layers)
    print(console.awslambda.filter_functions(func))
    print(console.awslambda.filter_functions([prefix_snake, "test"]))

    print(console.awslambda.get_function(func))
    print(console.awslambda.get_function_code_tab(func))
    print(console.awslambda.get_function_test_tab(func))
    print(console.awslambda.get_function_monitor_tab(func))
    print(console.awslambda.get_function_config_tab(func_arn))
    print(console.awslambda.get_function_alias_tab(func_arn))
    print(console.awslambda.get_function_version_tab(func_arn))

    print(console.awslambda.get_function_version(func, version))
    print(console.awslambda.get_function_version(arn=version_arn))
    print(console.awslambda.get_function_alias(func, alias))
    print(console.awslambda.get_function_alias(arn=alias_arn))

    print(console.awslambda.get_layer(layer))
    print(console.awslambda.get_layer(arn=layer_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.awslambda", preview=False)
