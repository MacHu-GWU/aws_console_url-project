# -*- coding: utf-8 -*-

from aws_console_url.tests import console, resource


def test():
    cluster = "sennen-main"
    task_def = "poc-storage"
    revision = 1
    task_id = "7c3b3aebf9ca4f2789c217f461fc2379"

    # --- arn
    res_cluster = resource.ECSCluster.from_arn(console.ecs.get_cluster_arn(cluster))
    res_task_def = resource.ECSTaskDefinition.from_arn(
        console.ecs.get_task_definition_arn(task_def, revision)
    )

    assert res_cluster == resource.ECSCluster.from_arn(res_cluster.arn)
    assert res_task_def == resource.ECSTaskDefinition.from_arn(res_task_def.arn)

    # --- console
    print(console.ecs.clusters)
    print(console.ecs.task_definitions)
    print(console.ecs.get_cluster_services(cluster))
    print(console.ecs.get_cluster_tasks(cluster))
    print(console.ecs.get_task_definition_revisions(task_def))
    print(console.ecs.get_task_definition_revision_containers(task_def, revision))
    print(console.ecs.get_task_definition_revision_json(task_def, revision))
    print(console.ecs.get_task_configuration(cluster, task_id))
    print(console.ecs.get_task_logs(cluster, task_id))

    print(console.ecs.get_cluster_services(res_cluster.arn))
    print(console.ecs.get_task_definition_revision_containers(res_task_def.arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ecs", preview=False)
