# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    stack = "CDKToolkit"
    change_set_id = "arn:aws:cloudformation:us-east-1:669508176277:changeSet/cdk-deploy-change-set/c78e670d-9563-47ef-a121-df2cf4baf369"

    # --- arn
    print(console.cloudformation.get_stack_arn(stack))

    # --- console
    print(console.cloudformation.stacks)
    print(console.cloudformation.stacksets)
    print(console.cloudformation.exports)

    print(console.cloudformation.get_stack(stack))
    print(console.cloudformation.get_stack_info(stack))
    print(console.cloudformation.get_stack_events(stack))
    print(console.cloudformation.get_stack_resources(stack))
    print(console.cloudformation.get_stack_outputs(stack))
    print(console.cloudformation.get_stack_parameters(stack))
    print(console.cloudformation.get_stack_changesets(stack))

    print(console.cloudformation.get_change_set(stack, change_set_id))
    print(console.cloudformation.get_change_set_changes(stack, change_set_id))
    print(console.cloudformation.get_change_set_inputs(stack, change_set_id))
    print(console.cloudformation.get_change_set_template(stack, change_set_id))
    print(console.cloudformation.get_change_set_json(stack, change_set_id))
    print(console.cloudformation.get_change_set_hooks(stack, change_set_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.cloudformation", preview=False)
