# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    cluster = f"{prefix_snake}_test"
    task_def = f"{prefix_snake}_test"
    revision = 1
    service = f"{prefix_snake}_test"

    cluster_arn = console.ecs.get_cluster_arn(cluster)
    task_def_arn = console.ecs.get_task_definition_arn(task_def, revision)
    task_run_arn = console.bsm.ecs_client.list_tasks(
        cluster=cluster,
        family=task_def,
        desiredStatus="STOPPED",  # 'RUNNING'|'PENDING'|'STOPPED'
    )["taskArns"][0]

    # --- arn

    # --- console
    print(console.ecs.clusters)
    print(console.ecs.task_definitions)
    print(console.ecs.get_cluster_services(cluster))
    print(console.ecs.get_cluster_tasks(cluster))
    print(console.ecs.get_task_definition_revisions(task_def))

    print(console.ecs.get_cluster_services(cluster))
    print(console.ecs.get_cluster_services(cluster_arn))
    print(console.ecs.get_task_definition_revision_containers(task_def, revision))
    print(console.ecs.get_task_definition_revision_containers(task_def_arn))
    print(console.ecs.get_task_definition_revision_json(task_def, revision))
    print(console.ecs.get_task_definition_revision_json(task_def_arn))
    print(console.ecs.get_task_run_configuration(task_run_arn))
    print(console.ecs.get_task_run_logs(task_run_arn))
    print(console.ecs.get_task_run_networking(task_run_arn))
    print(console.ecs.get_task_run_tags(task_run_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ecs", preview=False)
