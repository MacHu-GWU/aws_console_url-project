# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    param_name1 = f"{prefix_snake}_1"
    param_name2 = f"/{prefix_snake}_2"
    param_arn1 = console.ssm.get_parameter_arn(param_name1)
    param_arn2 = console.ssm.get_parameter_arn(param_name2)

    run_command_id = "875f8f80-dc5b-4e68-adb5-54f8fef8eb2e"

    # --- console
    print("-" * 80)
    print(console.ssm.parameters)
    print(console.ssm.run_command_executing_commands)

    print("-" * 80)
    print(console.ssm.filter_parameters(param_name1))
    print(console.ssm.get_parameter(param_name1))
    print(console.ssm.get_parameter(param_arn1))
    assert console.ssm.get_parameter_arn(param_name1).endswith(param_name1)

    print(console.ssm.filter_parameters(param_name2))
    print(console.ssm.get_parameter(param_name2))
    print(console.ssm.get_parameter(param_arn2))
    assert console.ssm.get_parameter_arn(param_name2).endswith(param_name2)

    print(console.ssm.get_run_command_execution(command_id=run_command_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ssm", preview=False)
