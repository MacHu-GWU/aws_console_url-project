# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    database = "sampledb"
    table = "elb_logs"
    job = "simple-json-to-parquet"
    crawler = "simple_json_to_parquet"

    # --- arn
    glue_database = resource.GlueDatabase.from_arn(
        resource.GlueDatabase.make(
            console.aws_account_id, console.aws_region, database
        ).arn
    )
    assert glue_database.name == database

    print(console.glue.get_database_arn(database))
    print(console.glue.get_table_arn(database, table))
    print(console.glue.get_job_arn(job))
    print(console.glue.get_crawler_arn(crawler))
    # --- console
    print(console.glue.databases)
    print(console.glue.tables)
    print(console.glue.jobs)
    print(console.glue.crawlers)
    print(console.glue.classifiers)

    print(console.glue.get_database(database))
    print(console.glue.get_table(database, table))
    print(console.glue.get_job(job))
    print(console.glue.get_crawler(crawler))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.glue", preview=False)
