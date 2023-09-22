# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    flow_name = "simple-hil-sbx"
    flow_arn = "arn:aws:sagemaker:us-east-1:807388292768:flow-definition/simple-hil-sbx"

    task_template_name = "simple-hil-sbx"
    task_template_arn = "arn:aws:sagemaker:us-east-1:807388292768:human-task-ui/simple-hil-sbx"

    human_loop_name = "cfff6f-0395060f549acf6a0627d969a98ba34d-6e804b8b23ed"
    human_loop_arn = "arn:aws:sagemaker:us-east-1:807388292768:human-loop/cfff6f-0395060f549acf6a0627d969a98ba34d-6e804b8b23ed"

    # --- arn
    assert console.a2i.get_human_review_workflow_arn(flow_name) == flow_arn
    assert console.a2i.get_worker_task_template_arn(task_template_name) == task_template_arn
    assert console.a2i.get_human_loop_arn(human_loop_name) == human_loop_arn

    # --- console
    print(console.a2i.human_review_workforces)

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
