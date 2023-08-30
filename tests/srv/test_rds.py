# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    db_cluster_id = "dbdatamart-powerusers-cluster-cluster-01"
    db_instance_id = "edfred-platformdev-sbx-eu-west-1-pociot-pgdb"
    snapshot_id = "solar-kpi-datamart-snapshot-manual-sbx"
    db_subnet_group_name = "default"
    db_parameter_group_name = "default-postgres-11"

    # --- resource

    # --- console
    print(console.rds.databases)
    print(console.rds.snapshots)
    print(console.rds.db_subnet_groups)
    print(console.rds.db_parameter_groups)
    print(console.rds.get_database_cluster(db_cluster_id))
    print(console.rds.get_database_instance(db_instance_id))
    print(console.rds.get_snapshot(snapshot_id))
    print(console.rds.get_db_subnet_group(db_subnet_group_name))
    print(console.rds.get_db_parameter_group(db_parameter_group_name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.rds", preview=False)
