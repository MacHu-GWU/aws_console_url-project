# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test_stack():
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

    assert stack.stack_id == stack_arn
    stack = resource.CloudFormationStack.from_stack_id(stack.stack_id)
    assert stack.arn == stack_arn

    # --- console
    print(console.cloudformation.stacks)
    print(console.cloudformation.stacksets)
    print(console.cloudformation.stacksets_self_managed)
    print(console.cloudformation.stacksets_service_managed)
    print(console.cloudformation.exports)

    print(console.cloudformation.filter_stack(stack_name))
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


def test_stack_set():
    aws_account_id = "111122223333"
    aws_region = "us-east-1"
    stack_set_name = "org-infra-common-tier"
    stack_set_short_id = "28fbd0a2-aced-40bf-9361-ef1c74d56e51"
    stack_set_arn = f"arn:aws:cloudformation:{aws_region}:{aws_account_id}:stackset/{stack_set_name}:{stack_set_short_id}"

    stack_set = resource.CloudFormationStackSet.from_arn(
        resource.CloudFormationStackSet.make(
            aws_account_id, aws_region, stack_set_name, stack_set_short_id
        ).arn
    )
    assert stack_set.name == stack_set_name
    assert stack_set.arn == stack_set_arn
    assert "None" not in stack_set.arn
    assert stack_set.stack_set_id == f"{stack_set_name}:{stack_set_short_id}"

    # --- console
    from boto_session_manager import BotoSesManager
    from aws_console_url import AWSConsole

    bsm = BotoSesManager(profile_name="awshsh_infra_us_east_1")

    console = AWSConsole(
        aws_account_id=bsm.aws_account_id,
        aws_region=bsm.aws_region,
        bsm=bsm,
    )
    print(
        console.cloudformation.get_stack_set_info(
            stack_set_name, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_instances(
            stack_set_name, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_operations(
            stack_set_name, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_parameters(
            stack_set_name, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_template(
            stack_set_name, is_service_managed=True
        )
    )


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.cloudformation", preview=False)
