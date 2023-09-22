# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


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
    layer_version = 1
    layer_arn = f"arn:aws:lambda:{console.aws_region}:{console.aws_account_id}:layer:{layer}:{layer_version}"

    # --- arn
    assert console.awslambda.get_function_arn(func) == func_arn
    assert console.awslambda.get_function_arn(func, version=version) == version_arn
    assert console.awslambda.get_function_arn(func, alias=alias) == alias_arn
    assert console.awslambda.get_layer_arn(layer, layer_version) == layer_arn

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
