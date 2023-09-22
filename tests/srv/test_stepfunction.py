# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    print("")

    standard_state_machine = f"{prefix_snake}_standard_test"
    express_state_machine = f"{prefix_snake}_express_test"
    standard_state_machine_arn = console.step_function.get_state_machine_arn(standard_state_machine)
    express_state_machine_arn = console.step_function.get_state_machine_arn(express_state_machine)

    standard_state_machine_execution_arn = console.bsm.sfn_client.list_executions(
        stateMachineArn=standard_state_machine_arn,
        maxResults=1,
    )["executions"][0]["executionArn"]
    express_state_machine_execution_arn = (
        f"arn:aws:states:{console.aws_region}:{console.aws_account_id}:express:{express_state_machine}"
        f":7f101ca8-5ff9-428b-b48a-aa7f6f83dd40:25f705b3-9633-4c55-9dd7-82818e3be403"
    )

    # --- arn
    print(console.step_function.state_machines)

    print(console.step_function.get_state_machine_view_tab(standard_state_machine))
    print(console.step_function.get_state_machine_view_tab(standard_state_machine_arn))
    print(console.step_function.get_state_machine_edit_tab(standard_state_machine))
    print(console.step_function.get_state_machine_edit_tab(standard_state_machine_arn))
    print(console.step_function.get_state_machine_visual_editor(standard_state_machine))
    print(console.step_function.get_state_machine_visual_editor(standard_state_machine_arn))

    print(console.step_function.get_state_machine_view_tab(express_state_machine))
    print(console.step_function.get_state_machine_view_tab(express_state_machine_arn))
    print(console.step_function.get_state_machine_edit_tab(express_state_machine))
    print(console.step_function.get_state_machine_edit_tab(express_state_machine_arn))
    print(console.step_function.get_state_machine_visual_editor(express_state_machine))
    print(console.step_function.get_state_machine_visual_editor(express_state_machine_arn))

    print(console.step_function.get_state_machine_execution(standard_state_machine_execution_arn))
    print(console.step_function.get_state_machine_execution(express_state_machine_execution_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.step_function", preview=False)
