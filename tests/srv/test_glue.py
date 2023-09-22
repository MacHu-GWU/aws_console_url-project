# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    database = f"{prefix_snake}_test"
    table = f"{prefix_snake}_table1"
    crawler = f"{prefix_snake}_test"
    job = f"{prefix_snake}_test"
    job_run_id = console.bsm.glue_client.get_job_runs(JobName=job)["JobRuns"][0]["Id"]

    database_arn = console.glue.get_database_arn(database)
    table_arn = console.glue.get_table_arn(database, table)
    crawler_arn = console.glue.get_crawler_arn(crawler)
    job_arn = console.glue.get_job_arn(job)

    # --- console
    print(console.glue.databases)
    print(console.glue.tables)
    print(console.glue.jobs)
    print(console.glue.crawlers)
    print(console.glue.classifiers)
    print(console.glue.triggers)
    print(console.glue.ml_transforms)

    print(console.glue.get_database(database))
    print(console.glue.get_database(database_arn))
    print(console.glue.get_table(table, database))
    print(console.glue.get_table(table_arn))
    print(console.glue.get_job(job))
    print(console.glue.get_job(job_arn))
    print(console.glue.get_glue_job_run(job, job_run_id))
    print(console.glue.get_glue_job_run(job_arn, job_run_id))
    print(console.glue.get_crawler(crawler))
    print(console.glue.get_crawler(crawler_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.glue", preview=False)
