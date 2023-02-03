# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    stack_name = "CDKToolkit"
    stack_short_id = "b518e0f0-750b-11ed-859b-1208b06dceb3"
    stack_arn = f"arn:aws:cloudformation:us-east-1:669508176277:stack/{stack_name}/{stack_short_id}"
    change_set_id = "arn:aws:cloudformation:us-east-1:669508176277:changeSet/cdk-deploy-change-set/c78e670d-9563-47ef-a121-df2cf4baf369"

    # --- arn
    print(console.cloudformation.get_stack_arn(stack_name))

    stack = resource.CloudFormationStack.from_arn(
        resource.CloudFormationStack.make(
            console.aws_account_id, console.aws_region, stack_name, stack_short_id
        ).arn
    )
    assert stack.name == stack_name
    assert stack.arn == stack_arn
    assert "None" not in stack.arn

    # --- console
    print(console.cloudformation.stacks)
    print(console.cloudformation.stacksets)
    print(console.cloudformation.exports)

    print(console.cloudformation.get_stack(stack_name))
    print(console.cloudformation.get_stack_info(stack_name))
    print(console.cloudformation.get_stack_events(stack_name))
    print(console.cloudformation.get_stack_resources(stack_name))
    print(console.cloudformation.get_stack_outputs(stack_name))
    print(console.cloudformation.get_stack_parameters(stack_name))
    print(console.cloudformation.get_stack_changesets(stack_name))

    print(console.cloudformation.get_change_set(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_changes(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_inputs(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_template(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_json(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_hooks(stack_name, change_set_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.cloudformation", preview=False)
