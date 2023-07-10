# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    flow_name = "simple-hil-sbx"
    flow_arn = "arn:aws:sagemaker:us-east-1:669508176277:flow-definition/simple-hil-sbx"

    task_template_name = "simple-hil-sbx"
    task_template_arn = (
        "arn:aws:sagemaker:us-east-1:669508176277:human-task-ui/simple-hil-sbx"
    )

    human_loop_name = "cfff6f-91760069b4893543fd97e758f921de6b-84deb8faf352"
    human_loop_arn = "arn:aws:sagemaker:us-east-1:669508176277:human-loop/cfff6f-91760069b4893543fd97e758f921de6b-84deb8faf352"

    # --- arn
    flow_def = resource.A2IFlowDefinition.from_arn(
        resource.A2IFlowDefinition.make(
            console.aws_account_id, console.aws_region, flow_name
        ).arn
    )
    assert flow_def.name == flow_name
    assert flow_def.arn == flow_arn

    task_template = resource.A2IHumanTaskUI.from_arn(
        resource.A2IHumanTaskUI.make(
            console.aws_account_id, console.aws_region, task_template_name
        ).arn
    )
    assert task_template.name == task_template_name
    assert task_template.arn == task_template_arn

    human_loop = resource.A2IHumanLoop.from_arn(
        resource.A2IHumanLoop.make(
            console.aws_account_id, console.aws_region, human_loop_name
        ).arn
    )
    assert human_loop.name == human_loop_name
    assert human_loop.arn == human_loop_arn

    # --- console
    print(console.a2i.human_review_workflows)
    print(console.a2i.get_human_review_workflow(flow_name))
    print(console.a2i.get_human_review_workflow(flow_arn))

    print(console.a2i.worker_task_templates)
    print(console.a2i.get_worker_task_template(task_template_name))
    print(console.a2i.get_worker_task_template(task_template_arn))

    print(console.a2i.get_human_loop(flow_name, human_loop_name))
    print(console.a2i.get_human_loop(flow_name, human_loop_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.a2i", preview=False)
