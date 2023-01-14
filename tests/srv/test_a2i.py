# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    flow_name = "my-flow"
    flow_arn = (
        "arn:aws:sagemaker:us-east-1:669508176277:flow-definition/my-flow"
    )

    task_template_name = "a2i-playbook"
    task_template_arn = (
        "arn:aws:sagemaker:us-east-1:669508176277:human-task-ui/a2i-playbook"
    )

    human_loop_name = "5e9730e1-da75-4de6-bf29-2ec7b979f10c"
    human_loop_arn = "arn:aws:sagemaker:us-east-1:669508176277:human-loop/5e9730e1-da75-4de6-bf29-2ec7b979f10c"

    print(aws.a2i.human_review_workflows)
    assert aws.a2i.to_human_review_workflow_arn(flow_name) == flow_arn
    assert aws.a2i.to_human_review_workflow_name(flow_arn) == flow_name
    print(aws.a2i.get_human_review_workflow(flow_name))
    print(aws.a2i.get_human_review_workflow(flow_arn))

    print(aws.a2i.worker_task_templates)
    assert aws.a2i.to_worker_task_template_arn(task_template_name) == task_template_arn
    assert aws.a2i.to_worker_task_template_name(task_template_arn) == task_template_name
    print(aws.a2i.get_worker_task_template(task_template_name))
    print(aws.a2i.get_worker_task_template(task_template_arn))

    assert aws.a2i.to_human_loop_arn(human_loop_name) == human_loop_arn
    assert aws.a2i.to_human_loop_name(human_loop_arn) == human_loop_name
    print(aws.a2i.get_human_loop(flow_name, human_loop_name))
    print(aws.a2i.get_human_loop(flow_name, human_loop_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.a2i", preview=False)
