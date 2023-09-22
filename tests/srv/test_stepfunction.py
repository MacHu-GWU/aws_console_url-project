# -*- coding: utf-8 -*-

from aws_console_url.tests import console, resource, prefix_snake


def test():
    print("")

    standard_state_machine = f"{prefix_snake}_standard_test"
    express_state_machine = f"{prefix_snake}_express_test"
    # standard_state_machine_arn = "arn:aws:states:us-east-1:669508176277:stateMachine:aws_console_url_test_standard"
    #

    # express_state_machine_arn = "arn:aws:states:us-east-1:669508176277:stateMachine:aws_console_url_test_express"
    #
    # standard_state_machine_execution = (
    #     "aws_console_url_test_standard:fb295259-61a2-b206-8b5a-ae41d06e14ee"
    # )
    # standard_state_machine_execution_arn = "arn:aws:states:us-east-1:669508176277:execution:aws_console_url_test_standard:fb295259-61a2-b206-8b5a-ae41d06e14ee"
    #
    # express_state_machine_execution = "aws_console_url_test_express:569e3b67-85fb-41a5-8743-0a5e0269d57f:5d2d19f7-be1f-41c1-b4a1-f6f37b8997f1"
    # express_state_machine_execution_arn = "arn:aws:states:us-east-1:669508176277:express:aws_console_url_test_express:569e3b67-85fb-41a5-8743-0a5e0269d57f:5d2d19f7-be1f-41c1-b4a1-f6f37b8997f1"
    #
    # # --- arn
    # for name, arn in [
    #     (standard_state_machine, standard_state_machine_arn),
    #     (express_state_machine, express_state_machine_arn),
    # ]:
    #     machine1 = resource.StepFunctionStatemachine.make(
    #         console.aws_account_id,
    #         console.aws_region,
    #         name,
    #     )
    #     assert machine1.arn == arn
    #
    #     machine2 = resource.StepFunctionStatemachine.from_arn(arn)
    #     assert machine2.arn == arn
    #
    #     assert console.step_function.get_state_machine_arn(name) == arn
    #
    #     assert machine1.name == name
    #     assert machine1.arn == arn
    #     assert "None" not in machine1.arn
    #
    # for name, arn, is_standard in [
    #     (standard_state_machine_execution, standard_state_machine_execution_arn, True),
    #     (express_state_machine_execution, express_state_machine_execution_arn, False),
    # ]:
    #     execution1 = resource.StepFunctionStatemachineExecution.make(
    #         console.aws_account_id,
    #         console.aws_region,
    #         name.split(":", 1)[0],
    #         name.split(":", 1)[1],
    #         is_standard,
    #     )
    #     assert execution1.arn == arn
    #
    #     execution2 = resource.StepFunctionStatemachineExecution.from_arn(arn)
    #     assert execution2.arn == arn
    #
    #     assert (
    #         console.step_function.get_state_machine_execution_arn(
    #             name.split(":", 1)[0],
    #             name.split(":", 1)[1],
    #         )
    #         == arn
    #     )
    #
    #     assert execution1.name == name.split(":")[0]
    #     assert execution1.arn == arn
    #     assert "None" not in execution1.arn
    #
    #
    # print(console.step_function.state_machines)
    #
    # print(console.step_function.get_state_machine_view_tab(standard_state_machine))
    # print(console.step_function.get_state_machine_edit_tab(standard_state_machine))
    # print(console.step_function.get_state_machine_visual_editor(standard_state_machine))
    #
    # print(console.step_function.get_state_machine_view_tab(express_state_machine))
    # print(console.step_function.get_state_machine_edit_tab(express_state_machine))
    # print(console.step_function.get_state_machine_visual_editor(express_state_machine))
    #
    # print(console.step_function.get_state_machine_execution(standard_state_machine_execution_arn))
    # print(console.step_function.get_state_machine_execution(express_state_machine_execution_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.step_function", preview=False)
