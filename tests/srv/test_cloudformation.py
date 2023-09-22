# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_slug


def test_stack():
    stack_name = "CDKToolkit"
    stack_obj = console.cloudformation._get_stack_object(stack_name)
    stack_arn = stack_obj.to_arn()

    res = console.bsm.cloudformation_client.describe_stacks(
        StackName=stack_name,
    )
    change_set_id = res["Stacks"][0]["ChangeSetId"]

    # --- arn
    assert console.cloudformation.get_stack_arn(stack_name) == stack_arn

    # --- console
    print("-" * 80)
    print(console.cloudformation.stacks)
    print(console.cloudformation.stacksets)
    print(console.cloudformation.stacksets_self_managed)
    print(console.cloudformation.stacksets_service_managed)
    print(console.cloudformation.exports)

    print("-" * 80)
    print(console.cloudformation.filter_stack(stack_name))
    print(console.cloudformation.get_stack(stack_name))
    print(console.cloudformation.get_stack_info(stack_name))
    print(console.cloudformation.get_stack_events(stack_name))
    print(console.cloudformation.get_stack_resources(stack_name))
    print(console.cloudformation.get_stack_outputs(stack_name))
    print(console.cloudformation.get_stack_parameters(stack_name))
    print(console.cloudformation.get_stack_changesets(stack_name))

    print("-" * 80)
    print(console.cloudformation.get_change_set(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_changes(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_inputs(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_template(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_json(stack_name, change_set_id))
    print(console.cloudformation.get_change_set_hooks(stack_name, change_set_id))


def test_stack_set():
    stack_set_self_managed = f"{prefix_slug}-test-self-managed"
    stack_set_service_managed = f"{prefix_slug}-test-service-managed"
    stack_set_self_managed_arn = console.cloudformation.get_stack_set_arn(
        stack_set_self_managed,
        is_self_managed=True,
    )
    stack_set_service_managed_arn = console.cloudformation.get_stack_set_arn(
        stack_set_service_managed,
        is_service_managed=True,
    )

    assert (
        console.cloudformation.get_stack_set_arn(
            stack_set_self_managed, is_self_managed=True
        )
        == stack_set_self_managed_arn
    )
    assert (
        console.cloudformation.get_stack_set_arn(
            stack_set_service_managed, is_service_managed=True
        )
        == stack_set_service_managed_arn
    )

    # --- console
    print("-" * 80)
    print(
        console.cloudformation.get_stack_set_info(
            stack_set_self_managed, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_info(
            stack_set_self_managed_arn, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_info(
            stack_set_service_managed, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_info(
            stack_set_service_managed_arn, is_service_managed=True
        )
    )

    print("-" * 80)
    print(
        console.cloudformation.get_stack_set_instances(
            stack_set_self_managed, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_instances(
            stack_set_self_managed_arn, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_instances(
            stack_set_service_managed, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_instances(
            stack_set_service_managed_arn, is_service_managed=True
        )
    )

    print("-" * 80)
    print(
        console.cloudformation.get_stack_set_operations(
            stack_set_self_managed, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_operations(
            stack_set_self_managed_arn, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_operations(
            stack_set_service_managed, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_operations(
            stack_set_service_managed_arn, is_service_managed=True
        )
    )

    print("-" * 80)
    print(
        console.cloudformation.get_stack_set_parameters(
            stack_set_self_managed, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_parameters(
            stack_set_self_managed_arn, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_parameters(
            stack_set_service_managed, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_parameters(
            stack_set_service_managed_arn, is_service_managed=True
        )
    )

    print("-" * 80)
    print(
        console.cloudformation.get_stack_set_template(
            stack_set_self_managed, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_template(
            stack_set_self_managed_arn, is_self_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_template(
            stack_set_service_managed, is_service_managed=True
        )
    )
    print(
        console.cloudformation.get_stack_set_template(
            stack_set_service_managed_arn, is_service_managed=True
        )
    )


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.cloudformation", preview=False)
